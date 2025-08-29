# Log Analyzer Tutorial

This tutorial will help you understand how the log analyzer works and how you can extend it for your own needs.

## How It Works

### 1. Log Parsing
The analyzer reads log files line by line and uses regular expressions to extract:
- **Timestamp**: When the event occurred
- **User**: Who performed the action
- **IP Address**: Where the action came from
- **Location**: Geographic location (City, Country)
- **Success/Failure**: Whether the login was successful

### 2. Anomaly Detection Types

#### A. Failed Login Attempts
- **What it detects**: Multiple failed login attempts by the same user
- **Risk level**: HIGH
- **How it works**: Counts failed attempts within a time window
- **Example**: User tries wrong password 5 times in 1 hour

#### B. Geographic Anomalies
- **What it detects**: Users logging in from unexpected locations
- **Risk level**: HIGH
- **How it works**: Compares login locations for each user
- **Example**: User normally logs in from New York, suddenly logs in from Tokyo

#### C. Time-based Anomalies
- **What it detects**: Logins at unusual hours
- **Risk level**: MEDIUM
- **How it works**: Flags logins between 11 PM and 6 AM
- **Example**: User logs in at 3 AM when they normally work 9-5

#### D. Frequency Anomalies
- **What it detects**: Unusual login patterns
- **Risk level**: MEDIUM
- **How it works**: Identifies rapid successive logins
- **Example**: User logs in 3 times within 5 minutes

## Code Structure

### Main Classes

#### LogEntry
```python
class LogEntry:
    def __init__(self, timestamp, user, ip, location, success):
        self.timestamp = datetime.strptime(timestamp, '%Y-%m-%d %H:%M:%S')
        self.user = user
        self.ip = ip
        self.location = location
        self.success = success
```

#### LogAnalyzer
```python
class LogAnalyzer:
    def __init__(self, failed_threshold=3, time_window=24):
        # Initialize analyzer with configurable thresholds
    
    def parse_log_file(self, filename):
        # Read and parse log file
    
    def detect_failed_login_anomalies(self):
        # Find multiple failed attempts
    
    def detect_geographic_anomalies(self):
        # Find location changes
    
    def detect_time_anomalies(self):
        # Find unusual hours
    
    def detect_frequency_anomalies(self):
        # Find rapid logins
```

## How to Extend the Analyzer

### 1. Add New Anomaly Types

To add a new type of anomaly detection:

1. **Create a new detection method**:
```python
def detect_your_anomaly(self) -> List[Dict]:
    anomalies = []
    # Your detection logic here
    return anomalies
```

2. **Add it to the analyze method**:
```python
def analyze(self) -> Dict:
    # ... existing code ...
    your_anomalies = self.detect_your_anomaly()
    all_anomalies = (failed_login_anomalies + geographic_anomalies + 
                    time_anomalies + frequency_anomalies + your_anomalies)
    # ... rest of method ...
```

### 2. Modify Detection Rules

#### Change Failed Login Threshold
```python
# In config.py
DEFAULT_FAILED_LOGIN_THRESHOLD = 5  # Change from 3 to 5
```

#### Change Unusual Hours
```python
# In config.py
UNUSUAL_HOURS_START = 22  # Change from 23 to 22 (10 PM)
UNUSUAL_HOURS_END = 7     # Change from 6 to 7 (7 AM)
```

#### Add New Log Patterns
```python
# In config.py
LOG_PATTERNS = {
    'successful_login': r'your_pattern_here',
    'failed_login': r'your_pattern_here',
    'new_event_type': r'your_new_pattern'
}
```

### 3. Add New Data Sources

To analyze different log formats:

1. **Modify the parse_log_file method** to handle your format
2. **Update the LogEntry class** if you need different fields
3. **Adjust the regular expressions** in config.py

### 4. Add Machine Learning

For more advanced detection:

```python
def detect_ml_anomalies(self):
    # Import your ML library
    import numpy as np
    from sklearn.ensemble import IsolationForest
    
    # Extract features
    features = self.extract_features()
    
    # Train model
    model = IsolationForest()
    model.fit(features)
    
    # Detect anomalies
    predictions = model.predict(features)
    
    # Convert to your anomaly format
    return self.convert_predictions_to_anomalies(predictions)
```

## Common Use Cases

### 1. Web Server Logs
```bash
# Apache/Nginx access logs
python log_analyzer.py --file access.log --threshold 10
```

### 2. SSH Logs
```bash
# SSH authentication logs
python log_analyzer.py --file auth.log --threshold 3
```

### 3. Application Logs
```bash
# Custom application logs
python log_analyzer.py --file app.log --time-window 48
```

## Best Practices

### 1. Log Format
- Use consistent timestamp format
- Include all necessary information (user, IP, location)
- Make logs machine-readable

### 2. Configuration
- Start with conservative thresholds
- Adjust based on your environment
- Document your changes

### 3. Monitoring
- Run analysis regularly (cron jobs)
- Set up alerts for high-risk anomalies
- Keep historical data for trend analysis

### 4. Security
- Don't log sensitive information
- Secure your log files
- Use encryption for transmission

## Troubleshooting

### Common Issues

1. **No anomalies detected**
   - Check if log format matches expected pattern
   - Verify thresholds are appropriate
   - Ensure log file has recent data

2. **Too many false positives**
   - Increase thresholds
   - Adjust time windows
   - Review detection logic

3. **Performance issues**
   - Use smaller time windows
   - Process logs in chunks
   - Optimize detection algorithms

### Debug Mode
Add debug output to see what's happening:
```python
def parse_log_file(self, filename: str) -> bool:
    # ... existing code ...
    print(f"DEBUG: Parsed {len(self.log_entries)} entries")
    for entry in self.log_entries[:5]:  # Show first 5
        print(f"DEBUG: {entry}")
```

## Next Steps

1. **Run the demo**: `python demo.py`
2. **Try with sample data**: `python log_analyzer.py --file sample_logs.txt`
3. **Test with your own logs**: Create a test log file
4. **Customize detection rules**: Modify config.py
5. **Add new features**: Extend the analyzer

## Resources

- [Regular Expressions Tutorial](https://docs.python.org/3/howto/regex.html)
- [Python datetime](https://docs.python.org/3/library/datetime.html)
- [Security Log Analysis](https://owasp.org/www-project-web-security-testing-guide/)
- [Log Management Best Practices](https://www.sans.org/white-papers/36942/)
