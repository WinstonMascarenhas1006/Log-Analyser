#!/usr/bin/env python3
"""
Log Analyzer - Unusual Activity Detection
A beginner-friendly tool to detect security anomalies in log files.
"""

import re
import argparse
import json
from datetime import datetime, timedelta
from collections import defaultdict, Counter
from typing import Dict, List, Tuple, Optional
import math

# Import configuration
from config import *

# For colored output
try:
    from colorama import init, Fore, Style
    init(autoreset=True)
    COLORS_AVAILABLE = True
except ImportError:
    COLORS_AVAILABLE = False
    # Fallback colors
    class Fore:
        RED = ''
        YELLOW = ''
        GREEN = ''
        BLUE = ''
        MAGENTA = ''
        CYAN = ''
        WHITE = ''
    class Style:
        BRIGHT = ''
        RESET_ALL = ''


class LogEntry:
    """Represents a single log entry with parsed information."""
    
    def __init__(self, timestamp: str, user: str, ip: str, location: str, success: bool):
        self.timestamp = datetime.strptime(timestamp, '%Y-%m-%d %H:%M:%S')
        self.user = user
        self.ip = ip
        self.location = location
        self.success = success
        
    def __str__(self):
        status = "logged in" if self.success else "failed login attempt"
        return f"{self.timestamp} - User {self.user} {status} from {self.ip} ({self.location})"


class LogAnalyzer:
    """Main class for analyzing log files and detecting anomalies."""
    
    def __init__(self, failed_threshold: int = DEFAULT_FAILED_LOGIN_THRESHOLD, 
                 time_window: int = DEFAULT_TIME_WINDOW_HOURS):
        self.failed_threshold = failed_threshold
        self.time_window = time_window
        self.log_entries: List[LogEntry] = []
        self.anomalies: List[Dict] = []
        
    def parse_log_file(self, filename: str) -> bool:
        """Parse the log file and extract log entries."""
        try:
            with open(filename, 'r', encoding='utf-8') as file:
                for line_num, line in enumerate(file, 1):
                    line = line.strip()
                    if not line:
                        continue
                        
                    # Try to match successful login
                    match = re.match(LOG_PATTERNS['successful_login'], line)
                    if match:
                        timestamp, user, ip, location = match.groups()
                        self.log_entries.append(LogEntry(timestamp, user, ip, location, True))
                        continue
                    
                    # Try to match failed login
                    match = re.match(LOG_PATTERNS['failed_login'], line)
                    if match:
                        timestamp, user, ip, location = match.groups()
                        self.log_entries.append(LogEntry(timestamp, user, ip, location, False))
                        continue
                    
                    # If no pattern matches, print warning
                    print(f"{Fore.YELLOW}Warning: Could not parse line {line_num}: {line}")
                    
            print(f"{Fore.GREEN}Successfully parsed {len(self.log_entries)} log entries")
            return True
            
        except FileNotFoundError:
            print(f"{Fore.RED}Error: File '{filename}' not found")
            return False
        except Exception as e:
            print(f"{Fore.RED}Error reading file: {e}")
            return False
    
    def detect_failed_login_anomalies(self) -> List[Dict]:
        """Detect multiple failed login attempts."""
        anomalies = []
        user_failed_attempts = defaultdict(list)
        
        # Group failed attempts by user
        for entry in self.log_entries:
            if not entry.success:
                user_failed_attempts[entry.user].append(entry)
        
        # Check for users with multiple failed attempts
        for user, attempts in user_failed_attempts.items():
            if len(attempts) >= self.failed_threshold:
                # Check if attempts are within time window
                recent_attempts = [
                    attempt for attempt in attempts 
                    if attempt.timestamp >= datetime.now() - timedelta(hours=self.time_window)
                ]
                
                if len(recent_attempts) >= self.failed_threshold:
                    anomaly = {
                        'type': 'failed_login_attempts',
                        'risk_level': 'HIGH',
                        'user': user,
                        'failed_attempts': len(recent_attempts),
                        'timeframe': f'{self.time_window} hours',
                        'details': f'User {user} had {len(recent_attempts)} failed login attempts',
                        'entries': recent_attempts
                    }
                    anomalies.append(anomaly)
        
        return anomalies
    
    def detect_geographic_anomalies(self) -> List[Dict]:
        """Detect logins from unexpected geographic locations."""
        anomalies = []
        user_locations = defaultdict(list)
        
        # Group successful logins by user
        for entry in self.log_entries:
            if entry.success:
                user_locations[entry.user].append(entry)
        
        # Check for geographic anomalies
        for user, logins in user_locations.items():
            if len(logins) < 2:
                continue
                
            # Get unique locations for this user
            locations = list(set(login.location for login in logins))
            
            if len(locations) > 1:
                # Check if locations are from different countries
                countries = set()
                for location in locations:
                    # Extract country from location string (assuming format "City, Country")
                    country = location.split(', ')[-1] if ', ' in location else 'Unknown'
                    countries.add(country)
                
                if len(countries) > 1:
                    anomaly = {
                        'type': 'geographic_anomaly',
                        'risk_level': 'HIGH',
                        'user': user,
                        'locations': locations,
                        'countries': list(countries),
                        'details': f'User {user} logged in from {len(locations)} different locations: {", ".join(locations)}',
                        'entries': logins
                    }
                    anomalies.append(anomaly)
        
        return anomalies
    
    def detect_time_anomalies(self) -> List[Dict]:
        """Detect logins at unusual hours."""
        anomalies = []
        
        for entry in self.log_entries:
            if entry.success:
                hour = entry.timestamp.hour
                
                # Check if login is during unusual hours (11 PM - 6 AM)
                if hour >= UNUSUAL_HOURS_START or hour <= UNUSUAL_HOURS_END:
                    anomaly = {
                        'type': 'time_anomaly',
                        'risk_level': 'MEDIUM',
                        'user': entry.user,
                        'timestamp': entry.timestamp,
                        'hour': hour,
                        'details': f'User {entry.user} logged in at unusual hour: {hour:02d}:00',
                        'entries': [entry]
                    }
                    anomalies.append(anomaly)
        
        return anomalies
    
    def detect_frequency_anomalies(self) -> List[Dict]:
        """Detect unusual login frequency patterns."""
        anomalies = []
        user_login_times = defaultdict(list)
        
        # Group successful logins by user
        for entry in self.log_entries:
            if entry.success:
                user_login_times[entry.user].append(entry.timestamp)
        
        # Check for users with very frequent logins
        for user, login_times in user_login_times.items():
            if len(login_times) < 3:
                continue
            
            # Sort login times
            login_times.sort()
            
            # Check for rapid successive logins (within 5 minutes)
            rapid_logins = 0
            for i in range(len(login_times) - 1):
                time_diff = login_times[i + 1] - login_times[i]
                if time_diff.total_seconds() < 300:  # 5 minutes
                    rapid_logins += 1
            
            if rapid_logins >= 2:
                anomaly = {
                    'type': 'frequency_anomaly',
                    'risk_level': 'MEDIUM',
                    'user': user,
                    'rapid_logins': rapid_logins,
                    'total_logins': len(login_times),
                    'details': f'User {user} had {rapid_logins} rapid successive logins',
                    'entries': [entry for entry in self.log_entries if entry.user == user and entry.success]
                }
                anomalies.append(anomaly)
        
        return anomalies
    
    def analyze(self) -> Dict:
        """Perform complete analysis of the log file."""
        print(f"{Fore.CYAN}Starting log analysis...")
        
        # Detect different types of anomalies
        failed_login_anomalies = self.detect_failed_login_anomalies()
        geographic_anomalies = self.detect_geographic_anomalies()
        time_anomalies = self.detect_time_anomalies()
        frequency_anomalies = self.detect_frequency_anomalies()
        
        # Combine all anomalies
        all_anomalies = (failed_login_anomalies + geographic_anomalies + 
                        time_anomalies + frequency_anomalies)
        
        # Generate statistics
        stats = self.generate_statistics()
        
        return {
            'total_entries': len(self.log_entries),
            'anomalies': all_anomalies,
            'statistics': stats,
            'risk_summary': self.calculate_risk_summary(all_anomalies)
        }
    
    def generate_statistics(self) -> Dict:
        """Generate comprehensive statistics about the log data."""
        if not self.log_entries:
            return {}
        
        # Basic counts
        successful_logins = [e for e in self.log_entries if e.success]
        failed_logins = [e for e in self.log_entries if not e.success]
        
        # User statistics
        users = set(e.user for e in self.log_entries)
        user_login_counts = Counter(e.user for e in successful_logins)
        user_failed_counts = Counter(e.user for e in failed_logins)
        
        # Location statistics
        locations = set(e.location for e in self.log_entries)
        location_counts = Counter(e.location for e in self.log_entries)
        
        # Time statistics
        hours = [e.timestamp.hour for e in self.log_entries]
        hour_counts = Counter(hours)
        
        return {
            'total_entries': len(self.log_entries),
            'successful_logins': len(successful_logins),
            'failed_logins': len(failed_logins),
            'unique_users': len(users),
            'unique_locations': len(locations),
            'success_rate': len(successful_logins) / len(self.log_entries) * 100,
            'most_active_user': user_login_counts.most_common(1)[0] if user_login_counts else None,
            'most_failed_user': user_failed_counts.most_common(1)[0] if user_failed_counts else None,
            'most_common_location': location_counts.most_common(1)[0] if location_counts else None,
            'peak_hour': hour_counts.most_common(1)[0] if hour_counts else None
        }
    
    def calculate_risk_summary(self, anomalies: List[Dict]) -> Dict:
        """Calculate risk summary based on detected anomalies."""
        risk_counts = Counter(anomaly['risk_level'] for anomaly in anomalies)
        
        return {
            'high_risk': risk_counts['HIGH'],
            'medium_risk': risk_counts['MEDIUM'],
            'low_risk': risk_counts['LOW'],
            'total_anomalies': len(anomalies)
        }
    
    def print_results(self, results: Dict):
        """Print analysis results in a user-friendly format."""
        print(f"\n{Fore.CYAN}{'='*60}")
        print(f"{Fore.CYAN}LOG ANALYSIS RESULTS")
        print(f"{Fore.CYAN}{'='*60}")
        
        # Print statistics
        stats = results['statistics']
        print(f"\n{Fore.BLUE}📊 STATISTICS:")
        print(f"  Total log entries: {stats['total_entries']}")
        print(f"  Successful logins: {stats['successful_logins']}")
        print(f"  Failed logins: {stats['failed_logins']}")
        print(f"  Success rate: {stats['success_rate']:.1f}%")
        print(f"  Unique users: {stats['unique_users']}")
        print(f"  Unique locations: {stats['unique_locations']}")
        
        if stats['most_active_user']:
            print(f"  Most active user: {stats['most_active_user'][0]} ({stats['most_active_user'][1]} logins)")
        if stats['most_failed_user']:
            print(f"  User with most failures: {stats['most_failed_user'][0]} ({stats['most_failed_user'][1]} failures)")
        
        # Print anomalies
        anomalies = results['anomalies']
        if not anomalies:
            print(f"\n{Fore.GREEN}✅ No anomalies detected!")
        else:
            print(f"\n{Fore.RED}🚨 DETECTED ANOMALIES ({len(anomalies)} total):")
            
            # Group by risk level
            for risk_level in ['HIGH', 'MEDIUM', 'LOW']:
                level_anomalies = [a for a in anomalies if a['risk_level'] == risk_level]
                if level_anomalies:
                    color = Fore.RED if risk_level == 'HIGH' else Fore.YELLOW if risk_level == 'MEDIUM' else Fore.GREEN
                    print(f"\n{color}{RISK_LEVELS[risk_level]} {risk_level} RISK ({len(level_anomalies)}):")
                    
                    for i, anomaly in enumerate(level_anomalies, 1):
                        print(f"  {i}. {anomaly['details']}")
                        if 'entries' in anomaly and len(anomaly['entries']) <= 3:
                            for entry in anomaly['entries']:
                                print(f"     - {entry}")
        
        # Print risk summary
        risk_summary = results['risk_summary']
        print(f"\n{Fore.MAGENTA}📈 RISK SUMMARY:")
        print(f"  High risk anomalies: {risk_summary['high_risk']}")
        print(f"  Medium risk anomalies: {risk_summary['medium_risk']}")
        print(f"  Low risk anomalies: {risk_summary['low_risk']}")
        print(f"  Total anomalies: {risk_summary['total_anomalies']}")


def main():
    """Main function to run the log analyzer."""
    parser = argparse.ArgumentParser(
        description='Log Analyzer - Detect unusual activities in log files',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python log_analyzer.py --file sample_logs.txt
  python log_analyzer.py --file logs.txt --threshold 5 --time-window 48
        """
    )
    
    parser.add_argument('--file', '-f', required=True,
                       help='Path to the log file to analyze')
    parser.add_argument('--threshold', '-t', type=int, 
                       default=DEFAULT_FAILED_LOGIN_THRESHOLD,
                       help=f'Number of failed attempts before flagging (default: {DEFAULT_FAILED_LOGIN_THRESHOLD})')
    parser.add_argument('--time-window', '-w', type=int,
                       default=DEFAULT_TIME_WINDOW_HOURS,
                       help=f'Time window in hours for analysis (default: {DEFAULT_TIME_WINDOW_HOURS})')
    parser.add_argument('--output', '-o',
                       help='Output file for results (JSON format)')
    
    args = parser.parse_args()
    
    # Create analyzer instance
    analyzer = LogAnalyzer(
        failed_threshold=args.threshold,
        time_window=args.time_window
    )
    
    # Parse log file
    if not analyzer.parse_log_file(args.file):
        return 1
    
    # Perform analysis
    results = analyzer.analyze()
    
    # Print results
    analyzer.print_results(results)
    
    # Save to file if requested
    if args.output:
        try:
            with open(args.output, 'w') as f:
                # Convert datetime objects to strings for JSON serialization
                json_results = {
                    'total_entries': results['total_entries'],
                    'anomalies': [
                        {
                            'type': a['type'],
                            'risk_level': a['risk_level'],
                            'user': a['user'],
                            'details': a['details'],
                            'timestamp': a.get('timestamp', '').isoformat() if a.get('timestamp') else '',
                            'entries_count': len(a.get('entries', []))
                        }
                        for a in results['anomalies']
                    ],
                    'statistics': results['statistics'],
                    'risk_summary': results['risk_summary']
                }
                json.dump(json_results, f, indent=2)
            print(f"\n{Fore.GREEN}Results saved to {args.output}")
        except Exception as e:
            print(f"{Fore.RED}Error saving results: {e}")
    
    return 0


if __name__ == '__main__':
    exit(main())
