#  Log Analyzer - Unusual Activity Detection

[![Python](https://img.shields.io/badge/Python-3.7+-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Status](https://img.shields.io/badge/Status-Production%20Ready-brightgreen.svg)]()

> **A beginner-friendly Python application that analyzes log files to detect unusual activities and potential security threats in real-time.**

##  What is this project?

This Log Analyzer is a cybersecurity tool designed to help you identify suspicious activities in your system logs. Think of it as a digital security guard that monitors login attempts and flags anything that looks unusual or potentially dangerous.

###  What does it detect?

- ** Failed Login Attacks**: Multiple wrong password attempts (brute force attacks)
- ** Geographic Anomalies**: Users logging in from unexpected locations
- ** Time-based Anomalies**: Logins at unusual hours (like 3 AM)
- ** Frequency Anomalies**: Unusual login patterns (too many logins too quickly)

##  Perfect for Learning

This project is specifically designed for **beginners** who want to learn:
- **Python programming** fundamentals
- **Cybersecurity concepts** and threat detection
- **Data analysis** and pattern recognition
- **File I/O operations** and log parsing
- **Regular expressions** for text processing
- **Command-line tools** development

##  Quick Start

### Prerequisites
- **Python 3.7 or higher** ([Download here](https://www.python.org/downloads/))
- Basic understanding of command line/terminal

### Installation

1. **Clone or download this repository**
   ```bash
   git clone https://github.com/yourusername/log-analyzer.git
   cd log-analyzer
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the analyzer**
   ```bash
   python log_analyzer.py --file clean_sample_logs.txt
   ```

### 🎮 Try the Interactive Demo
```bash
python demo.py
```

## 📊 How it Works (Simple Explanation)

### 1. **Reading Log Files**
The analyzer reads log files line by line, just like you would read a book. Each line contains information about a login attempt:
```
2024-01-15 10:30:45 - User john.doe logged in from 192.168.1.100 (New York, US)
```

### 2. **Extracting Information**
It extracts key details from each line:
- **When**: 2024-01-15 10:30:45 (timestamp)
- **Who**: john.doe (username)
- **Where**: 192.168.1.100 (IP address)
- **Location**: New York, US (geographic location)
- **Success/Failure**: logged in (successful) or failed login attempt

### 3. **Detecting Patterns**
The analyzer looks for suspicious patterns:

####  **Failed Login Detection**
- **What it looks for**: Multiple failed attempts by the same user
- **Example**: User tries wrong password 5 times in 1 hour
- **Why it's suspicious**: Could be a hacker trying to guess passwords

####  **Geographic Anomalies**
- **What it looks for**: Users logging in from unexpected locations
- **Example**: User normally logs in from New York, suddenly logs in from Tokyo
- **Why it's suspicious**: Could be account theft or unauthorized access

####  **Time-based Anomalies**
- **What it looks for**: Logins at unusual hours
- **Example**: User logs in at 3 AM when they normally work 9-5
- **Why it's suspicious**: Could be unauthorized access or account compromise

####  **Frequency Anomalies**
- **What it looks for**: Unusual login patterns
- **Example**: User logs in 3 times within 5 minutes
- **Why it's suspicious**: Could be automated attacks or account sharing

### 4. **Risk Assessment**
The analyzer assigns risk levels:
- **🔴 HIGH RISK**: Immediate attention required (failed logins, geographic changes)
- **🟡 MEDIUM RISK**: Worth investigating (unusual times, rapid logins)
- **🟢 LOW RISK**: Minor anomalies (less concerning patterns)

## 📁 Project Structure

```
log-analyzer/
├── 📄 log_analyzer.py      # Main application (the brain)
├── ⚙️ config.py            # Settings and configuration
├── 📊 sample_logs.txt      # Example log data
├── 🎮 demo.py              # Interactive demo script
├── 📋 requirements.txt     # Python packages needed
├── 📖 README.md           # This file
├── 📚 TUTORIAL.md         # Detailed tutorial
├── 🔧 INSTALL.md          # Installation guide
├── 🖥️ run_analyzer.bat    # Windows batch file
└── 💻 run_analyzer.ps1    # PowerShell script
```

## 🎯 Real-World Examples

### Example 1: Brute Force Attack
```
2024-01-16 03:15:22 - User hacker123 failed login attempt from 45.67.89.123 (Moscow, RU)
2024-01-16 03:16:45 - User hacker123 failed login attempt from 45.67.89.123 (Moscow, RU)
2024-01-16 03:18:12 - User hacker123 failed login attempt from 45.67.89.123 (Moscow, RU)
2024-01-16 03:20:33 - User hacker123 failed login attempt from 45.67.89.123 (Moscow, RU)
2024-01-16 03:22:15 - User hacker123 failed login attempt from 45.67.89.123 (Moscow, RU)
```
**🔴 Result**: HIGH RISK - 5 failed attempts from Moscow (potential brute force attack)

### Example 2: Geographic Anomaly
```
2024-01-15 09:00:00 - User john.doe logged in from 192.168.1.100 (New York, US)
2024-01-15 14:00:00 - User john.doe logged in from 203.45.67.89 (Tokyo, JP)
2024-01-15 19:00:00 - User john.doe logged in from 172.16.0.50 (London, UK)
```
**🔴 Result**: HIGH RISK - User logged in from 3 different countries in one day

### Example 3: Time Anomaly
```
2024-01-16 02:15:00 - User admin logged in from 192.168.1.50 (New York, US)
```
**🟡 Result**: MEDIUM RISK - Admin logged in at 2:15 AM (unusual hour)

## 🛠️ Usage Examples

### Basic Analysis
```bash
python log_analyzer.py --file your_logs.txt
```

### Custom Settings
```bash
# Flag users with 5+ failed attempts (instead of default 3)
python log_analyzer.py --file your_logs.txt --threshold 5

# Analyze logs from the last 48 hours (instead of default 24)
python log_analyzer.py --file your_logs.txt --time-window 48

# Save results to a JSON file
python log_analyzer.py --file your_logs.txt --output results.json
```

### Interactive Demo
```bash
python demo.py
```
This will show you different types of anomalies with explanations.

## 📚 Learning Path

### For Complete Beginners:
1. **Start with the demo**: `python demo.py`
2. **Read the tutorial**: Check `TUTORIAL.md`
3. **Try with sample data**: `python log_analyzer.py --file clean_sample_logs.txt`
4. **Create your own logs**: Make a test log file and analyze it

### For Intermediate Users:
1. **Customize settings**: Edit `config.py` to adjust detection rules
2. **Add new features**: Extend the analyzer with your own detection methods
3. **Integrate with real systems**: Connect to actual log sources

## 🔧 Customization

### Changing Detection Rules
Edit `config.py` to modify:
- **Failed login threshold**: How many failed attempts before flagging
- **Unusual hours**: What times are considered suspicious
- **Log patterns**: How to parse different log formats

### Adding New Anomaly Types
You can extend the analyzer to detect:
- **Port scanning attempts**
- **Unusual file access patterns**
- **Database query anomalies**
- **Network traffic spikes**

## 🤝 Contributing

This project welcomes contributions! Here's how you can help:

1. **Report bugs**: Create an issue with detailed information
2. **Suggest features**: Propose new anomaly detection methods
3. **Improve documentation**: Help make the tutorial clearer
4. **Add examples**: Share real-world log analysis scenarios

### For Contributors:
- Fork the repository
- Create a feature branch
- Make your changes
- Add tests if applicable
- Submit a pull request

## 📖 Documentation

- **[TUTORIAL.md](TUTORIAL.md)**: Detailed tutorial and extension guide
- **[INSTALL.md](INSTALL.md)**: Step-by-step installation instructions
- **[Code Comments](log_analyzer.py)**: Inline documentation in the code

## 🎓 Educational Value

This project teaches:

### **Programming Concepts:**
- **Object-Oriented Programming**: Classes and methods
- **File I/O**: Reading and parsing text files
- **Regular Expressions**: Pattern matching in text
- **Data Structures**: Lists, dictionaries, sets
- **Error Handling**: Try-catch blocks and validation

### **Cybersecurity Concepts:**
- **Threat Detection**: Identifying malicious activities
- **Risk Assessment**: Evaluating security threats
- **Log Analysis**: Understanding system logs
- **Anomaly Detection**: Finding unusual patterns
- **Security Monitoring**: Continuous surveillance

### **Data Analysis:**
- **Pattern Recognition**: Identifying trends and anomalies
- **Statistical Analysis**: Counting and categorizing events
- **Time Series Analysis**: Analyzing events over time
- **Geographic Analysis**: Location-based threat detection

## 🔒 Security Considerations

### What this tool does:
- ✅ Analyzes log files for suspicious patterns
- ✅ Provides risk assessments and alerts
- ✅ Helps identify potential security threats
- ✅ Generates reports for security teams

### What this tool does NOT do:
- ❌ Prevent attacks (it's detection, not prevention)
- ❌ Access your systems directly
- ❌ Store or transmit your data
- ❌ Replace professional security tools

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **Python Community**: For the amazing programming language
- **Open Source Contributors**: For the libraries that make this possible
- **Cybersecurity Community**: For sharing knowledge and best practices
- **Students and Learners**: For inspiring this educational project

## 📞 Support

If you need help:
1. **Check the documentation**: Start with `TUTORIAL.md`
2. **Run the demo**: `python demo.py` to see examples
3. **Create an issue**: Report bugs or ask questions
4. **Read the code**: Well-commented for learning

## 🚀 Future Enhancements

Planned features:
- **Web Interface**: Browser-based analysis
- **Real-time Monitoring**: Live log analysis
- **Machine Learning**: Advanced anomaly detection
- **Database Integration**: Store and query historical data
- **Alert System**: Email/SMS notifications
- **Dashboard**: Visual analytics and charts

---

**⭐ Star this repository if you found it helpful!**

**🔗 Share with fellow students and cybersecurity enthusiasts!**

**📚 Happy learning and stay secure! 🔒**
