param(
    [Parameter(Mandatory=$true)][ValidateSet('setup','doctor','status','run','revise','history','verify','audit-git')][string]$Action,
    [string]$RunDirectory,
    [ValidateRange(-1,16)][int]$GpuId = -1,
    [string]$Storyboard,
    [ValidateRange(1,10000)][int]$Limit = 20,
    [switch]$Json
)
$ErrorActionPreference = 'Stop'
$projectRoot = Split-Path -Parent $PSScriptRoot
$localRoot = Join-Path $PSScriptRoot '.local'
$logsRoot = Join-Path $localRoot 'launcher-logs'
New-Item -ItemType Directory -Force -Path $logsRoot | Out-Null
$pythonCommand = if ($Action -in @('run','revise','verify')) {
    Join-Path $localRoot 'venv\Scripts\python.exe'
} else { (Get-Command python.exe -ErrorAction Stop).Source }
if (-not (Test-Path -LiteralPath $pythonCommand)) { throw 'Run setup first.' }
$processArgs = @('-u', '-m', 'pc_demo', $Action)
if ($Action -eq 'run') { $processArgs += @('--gpu-id', $GpuId.ToString()) }
if ($RunDirectory -and $Action -notin @('verify','revise')) { throw '-RunDirectory is only valid with verify or revise.' }
if ($RunDirectory) {
    if ($RunDirectory.Contains('"')) { throw 'Invalid path.' }
    $resolvedRun = (Resolve-Path -LiteralPath $RunDirectory -ErrorAction Stop).Path.TrimEnd('\')
    $processArgs += @('--run', ('"' + $resolvedRun + '"'))
}
if ($Storyboard) {
    if ($Action -notin @('run','revise')) { throw '-Storyboard is only valid with run or revise.' }
    if ($Storyboard.Contains('"')) { throw 'Invalid storyboard path.' }
    $resolvedStory = (Resolve-Path -LiteralPath $Storyboard -ErrorAction Stop).Path
    $processArgs += @('--storyboard', ('"' + $resolvedStory + '"'))
}
if ($Action -eq 'history') {
    $processArgs += @('--limit', $Limit.ToString())
    if ($Json) { $processArgs += '--json' }
} elseif ($Json -or $PSBoundParameters.ContainsKey('Limit')) { throw '-Limit and -Json are only valid with history.' }
if ($Action -ne 'run' -and $PSBoundParameters.ContainsKey('GpuId')) { throw '-GpuId is only valid with run; revise preserves the original inference.' }
$logPrefix = Join-Path $logsRoot ($Action + '-' + [DateTime]::UtcNow.ToString('yyyyMMddTHHmmssfff'))
$process = Start-Process -FilePath $pythonCommand -ArgumentList $processArgs -WorkingDirectory $projectRoot -WindowStyle Hidden -Wait -PassThru -RedirectStandardOutput ($logPrefix + '.stdout.log') -RedirectStandardError ($logPrefix + '.stderr.log')
Get-Content -LiteralPath ($logPrefix + '.stdout.log')
Get-Content -LiteralPath ($logPrefix + '.stderr.log')
if ($process.ExitCode -ne 0) { throw "Demo command failed ($($process.ExitCode)). Logs: $logPrefix" }
