# Installation Guide

## Prerequisites

### 1. Python Installation

**Windows:**
1. Download Python from [python.org](https://www.python.org/downloads/)
2. During installation, **make sure to check "Add Python to PATH"**
3. Verify installation by opening Command Prompt and typing: `python --version`

**macOS:**
```bash
# Using Homebrew
brew install python

# Or download from python.org
```

**Linux (Ubuntu/Debian):**
```bash
sudo apt update
sudo apt install python3 python3-pip
```

### 2. Verify Python Installation

Open a terminal/command prompt and run:
```bash
python --version
# or
python3 --version
```

You should see something like: `Python 3.8.0` or higher.

## Installation Steps

### 1. Download the Project

If you haven't already, download or clone this project to your computer.

### 2. Navigate to Project Directory

Open a terminal/command prompt and navigate to the project folder:
```bash
cd path/to/Project2_loganalyser
```

### 3. Install Dependencies

**Windows:**
```bash
# Using the provided script (recommended)
.\run_analyzer.ps1

# Or manually:
pip install -r requirements.txt
```

**macOS/Linux:**
```bash
pip3 install -r requirements.txt
```

### 4. Test Installation

Run the analyzer with sample data:
```bash
python log_analyzer.py --file sample_logs.txt
```

You should see colorful output with analysis results.

## Quick Start

### Option 1: Use the Provided Scripts

**Windows:**
- Double-click `run_analyzer.bat` or
- Right-click `run_analyzer.ps1` → "Run with PowerShell"

**macOS/Linux:**
```bash
chmod +x run_analyzer.ps1
./run_analyzer.ps1
```

### Option 2: Manual Commands

```bash
# Basic analysis
python log_analyzer.py --file sample_logs.txt

# With custom thresholds
python log_analyzer.py --file sample_logs.txt --threshold 5 --time-window 48

# Run demo
python demo.py
```

## Troubleshooting

### Python Not Found

**Error:** `Python was not found`

**Solution:**
1. Reinstall Python and check "Add Python to PATH"
2. Restart your terminal/command prompt
3. Try: `python3` instead of `python`

### Module Not Found

**Error:** `ModuleNotFoundError: No module named 'colorama'`

**Solution:**
```bash
pip install -r requirements.txt
```

### Permission Errors

**Windows:**
- Run PowerShell as Administrator
- Or use: `pip install --user -r requirements.txt`

**macOS/Linux:**
```bash
sudo pip3 install -r requirements.txt
```

### File Not Found

**Error:** `File 'sample_logs.txt' not found`

**Solution:**
- Make sure you're in the correct directory
- Check that all files are present: `dir` (Windows) or `ls` (macOS/Linux)

## Project Structure

After installation, you should have these files:
```
Project2_loganalyser/
├── log_analyzer.py      # Main application
├── config.py            # Configuration settings
├── sample_logs.txt      # Sample log data
├── demo.py              # Demo script
├── requirements.txt     # Python dependencies
├── README.md           # Project documentation
├── TUTORIAL.md         # Tutorial guide
├── INSTALL.md          # This file
├── run_analyzer.bat    # Windows batch file
└── run_analyzer.ps1    # PowerShell script
```

## Next Steps

1. **Read the README.md** for project overview
2. **Run the demo:** `python demo.py`
3. **Try with your own logs:** Create a log file and analyze it
4. **Read TUTORIAL.md** to learn how to extend the analyzer

## Getting Help

If you encounter issues:

1. Check this installation guide
2. Read the troubleshooting section
3. Verify Python installation: `python --version`
4. Check dependencies: `pip list`
5. Try the demo script: `python demo.py`

## System Requirements

- **Python:** 3.7 or higher
- **RAM:** 512 MB minimum
- **Storage:** 50 MB free space
- **OS:** Windows 10+, macOS 10.14+, or Linux

## Dependencies

The project uses these Python packages:
- `requests` - HTTP requests
- `geopy` - Geographic calculations
- `pandas` - Data analysis
- `python-dateutil` - Date parsing
- `colorama` - Colored terminal output
