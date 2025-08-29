# Log Analyzer - Unusual Activity Detection
# PowerShell Script

Write-Host "Log Analyzer - Unusual Activity Detection" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

# Function to test Python installation
function Test-PythonInstallation {
    $pythonCommands = @("py -3", "python", "python3", "py")
    
    foreach ($cmd in $pythonCommands) {
        try {
            if ($cmd -eq "py -3") {
                $result = & py -3 --version 2>$null
                if ($LASTEXITCODE -eq 0) {
                    Write-Host "Found Python: $result" -ForegroundColor Green
                    return $cmd
                }
            } else {
                $result = Get-Command $cmd -ErrorAction Stop
                Write-Host "Found Python at: $($result.Source)" -ForegroundColor Green
                return $cmd
            }
        }
        catch {
            continue
        }
    }
    return $null
}

# Check if Python is installed
$pythonCmd = Test-PythonInstallation

if (-not $pythonCmd) {
    Write-Host "ERROR: Python not found!" -ForegroundColor Red
    Write-Host ""
    Write-Host "Please install Python from https://www.python.org/downloads/" -ForegroundColor Yellow
    Write-Host "Make sure to check 'Add Python to PATH' during installation." -ForegroundColor Yellow
    Write-Host ""
    Write-Host "After installing Python, run:" -ForegroundColor Cyan
    Write-Host "  py -3 -m pip install -r requirements.txt" -ForegroundColor White
    Write-Host "  py -3 log_analyzer.py --file sample_logs.txt" -ForegroundColor White
    Write-Host ""
    Read-Host "Press Enter to exit"
    exit 1
}

# Check if requirements are installed
Write-Host "Checking dependencies..." -ForegroundColor Yellow
try {
    & $pythonCmd -c "import colorama, geopy, pandas" 2>$null
    Write-Host "Dependencies found!" -ForegroundColor Green
}
catch {
    Write-Host "Installing dependencies..." -ForegroundColor Yellow
    & $pythonCmd -m pip install -r requirements.txt
    if ($LASTEXITCODE -ne 0) {
        Write-Host "Failed to install dependencies!" -ForegroundColor Red
        Read-Host "Press Enter to exit"
        exit 1
    }
}

# Run the analyzer
Write-Host ""
Write-Host "Running log analysis..." -ForegroundColor Yellow
& $pythonCmd log_analyzer.py --file clean_sample_logs.txt

if ($LASTEXITCODE -eq 0) {
    Write-Host ""
    Write-Host "Analysis completed successfully!" -ForegroundColor Green
} else {
    Write-Host ""
    Write-Host "Analysis failed!" -ForegroundColor Red
}

Write-Host ""
Write-Host "Available commands:" -ForegroundColor Cyan
Write-Host "  $pythonCmd log_analyzer.py --file clean_sample_logs.txt" -ForegroundColor White
Write-Host "  $pythonCmd log_analyzer.py --file clean_sample_logs.txt --threshold 5" -ForegroundColor White
Write-Host "  $pythonCmd log_analyzer.py --file clean_sample_logs.txt --time-window 48" -ForegroundColor White
Write-Host "  $pythonCmd demo.py" -ForegroundColor White

Read-Host "Press Enter to exit"
