$ErrorActionPreference = 'Stop'
$osInfo = Get-CimInstance Win32_OperatingSystem
$systemInfo = Get-CimInstance Win32_ComputerSystem
$cpuInfo = Get-CimInstance Win32_Processor
$nvidia = if (Get-Command nvidia-smi -ErrorAction SilentlyContinue) {
    (& nvidia-smi --query-gpu=name,memory.total,driver_version --format=csv,noheader) -join "`n"
} else { 'nvidia-smi unavailable; VRAM unverified' }
[ordered]@{
    captured_utc = [DateTime]::UtcNow.ToString('o')
    os = $osInfo.Caption
    os_version = $osInfo.Version
    architecture = $osInfo.OSArchitecture
    cpu = $cpuInfo.Name
    ram_gib = [math]::Round($systemInfo.TotalPhysicalMemory / 1GB, 2)
    gpus = @(Get-CimInstance Win32_VideoController | Select-Object Name, DriverVersion)
    nvidia_vram = $nvidia
    disks = @(Get-CimInstance Win32_LogicalDisk -Filter 'DriveType=3' | ForEach-Object {
        @{ drive = $_.DeviceID; size_gib = [math]::Round($_.Size / 1GB, 2); free_gib = [math]::Round($_.FreeSpace / 1GB, 2) }
    })
} | ConvertTo-Json -Depth 5
