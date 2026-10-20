param(
    [Parameter(Mandatory=$true)][ValidateSet('setup','doctor','status','run','revise','history','verify','package','review','audit-git')][string]$Action,
    [string]$RunDirectory,
    [ValidateRange(-1,16)][int]$GpuId = -1,
    [string]$Storyboard,
    [string]$InputImage,
    [string]$LibraryFile,
    [string]$ReviewFile,
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
if ($InputImage) {
    if ($Action -ne 'run') { throw '-InputImage is only valid with run; revise reuses saved inputs.' }
    if ($InputImage.Contains('"')) { throw 'Invalid image path.' }
    $resolvedImage = (Resolve-Path -LiteralPath $InputImage -ErrorAction Stop).Path
    $processArgs += @('--input', ('"' + $resolvedImage + '"'))
}
if ($LibraryFile) {
    if ($Action -ne 'run') { throw '-LibraryFile is only valid with run; revise preserves its original evidence.' }
    if ($LibraryFile.Contains('"')) { throw 'Invalid library path.' }
    $resolvedLibrary = (Resolve-Path -LiteralPath $LibraryFile -ErrorAction Stop).Path
    $processArgs += @('--library-file', ('"' + $resolvedLibrary + '"'))
}
if ($RunDirectory -and $Action -notin @('verify','revise','package','review')) { throw '-RunDirectory is only valid with verify, revise, package or review.' }
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
if ($Action -eq 'review' -and -not $ReviewFile) { throw 'review requires -ReviewFile with the downloaded review.json.' }
if ($ReviewFile) {
    if ($Action -ne 'review') { throw '-ReviewFile is only valid with review.' }
    if ($ReviewFile.Contains('"')) { throw 'Invalid review file path.' }
    $resolvedReview = (Resolve-Path -LiteralPath $ReviewFile -ErrorAction Stop).Path
    $processArgs += @('--review-file', ('"' + $resolvedReview + '"'))
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
