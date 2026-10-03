param(
    [Parameter(Mandatory=$true)][ValidateSet('setup','doctor','status','run','verify','audit-git')][string]$Action,
    [string]$RunDirectory,
    [ValidateRange(-1,16)][int]$GpuId = -1
)
$ErrorActionPreference = 'Stop'
$projectRoot = Split-Path -Parent $PSScriptRoot
$localRoot = Join-Path $PSScriptRoot '.local'
$logsRoot = Join-Path $localRoot 'launcher-logs'
New-Item -ItemType Directory -Force -Path $logsRoot | Out-Null
$pythonCommand = if ($Action -in @('run','verify')) {
    Join-Path $localRoot 'venv\Scripts\python.exe'
} else { (Get-Command python.exe -ErrorAction Stop).Source }
if (-not (Test-Path -LiteralPath $pythonCommand)) { throw 'Run setup first.' }
$processArgs = @('-u', '-m', 'pc_demo', $Action)
if ($Action -eq 'run') { $processArgs += @('--gpu-id', $GpuId.ToString()) }
if ($RunDirectory -and $Action -ne 'verify') { throw '-RunDirectory is only valid with verify.' }
if ($Action -eq 'verify' -and $RunDirectory) {
    if ($RunDirectory.Contains('"')) { throw 'Invalid path.' }
    $resolvedRun = (Resolve-Path -LiteralPath $RunDirectory -ErrorAction Stop).Path.TrimEnd('\')
    $processArgs += @('--run', ('"' + $resolvedRun + '"'))
}
$logPrefix = Join-Path $logsRoot ($Action + '-' + [DateTime]::UtcNow.ToString('yyyyMMddTHHmmssfff'))
$process = Start-Process -FilePath $pythonCommand -ArgumentList $processArgs -WorkingDirectory $projectRoot -WindowStyle Hidden -Wait -PassThru -RedirectStandardOutput ($logPrefix + '.stdout.log') -RedirectStandardError ($logPrefix + '.stderr.log')
Get-Content -LiteralPath ($logPrefix + '.stdout.log')
Get-Content -LiteralPath ($logPrefix + '.stderr.log')
if ($process.ExitCode -ne 0) { throw "Demo command failed ($($process.ExitCode)). Logs: $logPrefix" }
