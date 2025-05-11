@REM Windows
@REM Run as Batch file
for /R %%A in (*.wav) do (ffmpeg -i "%%A" -c:a pcm_s16le -ar 16000 -ac 1 "%%~dpnA_.wav") && (echo del /f "%%A") && (del /f "%%A") && (echo ren "%%~dpnA_.wav" "%%~nA.wav") && (ren "%%~dpnA_.wav" "%%~nA.wav")

@REM Run in cmd
@REM for /R %A in (*.wav) do (ffmpeg -i "%A" -c:a pcm_s16le -ar 16000 -ac 1 "%~dpnA_.wav") && (echo del /f "%A") && (del /f "%A") && (echo ren "%~dpnA_.wav" "%~nA.wav") && (ren "%~dpnA_.wav" "%~nA.wav")