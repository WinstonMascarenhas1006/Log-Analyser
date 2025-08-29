@echo off
echo Log Analyzer - Unusual Activity Detection
echo ========================================

REM Try different Python commands
python log_analyzer.py --file sample_logs.txt
if %errorlevel% equ 0 goto :end

python3 log_analyzer.py --file sample_logs.txt
if %errorlevel% equ 0 goto :end

py log_analyzer.py --file sample_logs.txt
if %errorlevel% equ 0 goto :end

echo.
echo ERROR: Python not found!
echo Please install Python from https://www.python.org/downloads/
echo Make sure to check "Add Python to PATH" during installation.
echo.
echo After installing Python, run:
echo   pip install -r requirements.txt
echo   python log_analyzer.py --file sample_logs.txt
echo.
pause

:end
echo.
echo Analysis complete!
pause
