param([Parameter(Mandatory=$true)][string]$RunDirectory)
$ErrorActionPreference = 'Stop'
Add-Type -AssemblyName System.Speech
$story = Get-Content -LiteralPath (Join-Path $RunDirectory 'storyboard.json') -Raw -Encoding UTF8 | ConvertFrom-Json
$speech = New-Object System.Speech.Synthesis.SpeechSynthesizer
try {
    $english = @($speech.GetInstalledVoices() | Where-Object { $_.Enabled -and $_.VoiceInfo.Culture.Name -eq 'en-US' })
    if (-not $english.Count) { throw 'No English US Windows speech voice is installed.' }
    $preferred = @($english | Where-Object { $_.VoiceInfo.Name -match 'Zira' })
    $voice = if ($preferred.Count) { $preferred[0].VoiceInfo.Name } else { $english[0].VoiceInfo.Name }
    $speech.SelectVoice($voice)
    $speech.Rate = 0
    $speech.Volume = 100
    $audioRoot = Join-Path $RunDirectory 'audio'
    New-Item -ItemType Directory -Force -Path $audioRoot | Out-Null
    $index = 0
    foreach ($segment in $story.segments) {
        $path = Join-Path $audioRoot ('voice-{0:00}.wav' -f $index)
        $speech.SetOutputToWaveFile($path)
        $speech.Speak([string]$segment.narration)
        $speech.SetOutputToNull()
        $index++
    }
    @{ engine = 'Windows System.Speech'; voice = $voice; rate = 0; synthetic_narration = $true; app_generated_audio = $false } | ConvertTo-Json | Set-Content -LiteralPath (Join-Path $audioRoot 'voice.json') -Encoding UTF8
} finally { $speech.Dispose() }
