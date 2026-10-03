param(
    [Parameter(Mandatory=$true)][ValidateSet('setup','doctor','run','verify')][string]$Action,
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
if ($Action -eq 'verify') {
    if (-not $RunDirectory) { throw 'Verify requires -RunDirectory.' }
    if ($RunDirectory.Contains('"')) { throw 'Invalid path.' }
    $processArgs += @('--run', ('"' + $RunDirectory + '"'))
}
$logPrefix = Join-Path $logsRoot ($Action + '-' + [DateTime]::UtcNow.ToString('yyyyMMddTHHmmssfff'))
$process = Start-Process -FilePath $pythonCommand -ArgumentList $processArgs -WorkingDirectory $projectRoot -WindowStyle Hidden -Wait -PassThru -RedirectStandardOutput ($logPrefix + '.stdout.log') -RedirectStandardError ($logPrefix + '.stderr.log')
Get-Content -LiteralPath ($logPrefix + '.stdout.log')
Get-Content -LiteralPath ($logPrefix + '.stderr.log')
if ($process.ExitCode -ne 0) { throw "Demo command failed ($($process.ExitCode)). Logs: $logPrefix" }
