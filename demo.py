#!/usr/bin/env python3
"""
Demo script for the Log Analyzer
This script demonstrates how to use the log analyzer with different scenarios.
"""

import os
import sys
from log_analyzer import LogAnalyzer

def create_demo_logs():
    """Create demo log files with different scenarios."""
    
    # Demo 1: Normal activity
    normal_logs = """2024-01-15 09:00:00 - User john.doe logged in from 192.168.1.100 (New York, US)
2024-01-15 10:30:00 - User jane.smith logged in from 192.168.1.101 (New York, US)
2024-01-15 14:15:00 - User john.doe logged in from 192.168.1.100 (New York, US)
2024-01-15 16:45:00 - User admin logged in from 192.168.1.50 (New York, US)
2024-01-15 18:20:00 - User jane.smith logged in from 192.168.1.101 (New York, US)"""
    
    # Demo 2: Failed login attempts
    failed_logs = """2024-01-15 09:00:00 - User john.doe logged in from 192.168.1.100 (New York, US)
2024-01-15 10:30:00 - User hacker123 failed login attempt from 203.45.67.89 (Tokyo, JP)
2024-01-15 10:31:00 - User hacker123 failed login attempt from 203.45.67.89 (Tokyo, JP)
2024-01-15 10:32:00 - User hacker123 failed login attempt from 203.45.67.89 (Tokyo, JP)
2024-01-15 10:33:00 - User hacker123 failed login attempt from 203.45.67.89 (Tokyo, JP)
2024-01-15 10:34:00 - User hacker123 failed login attempt from 203.45.67.89 (Tokyo, JP)
2024-01-15 11:00:00 - User admin logged in from 192.168.1.50 (New York, US)"""
    
    # Demo 3: Geographic anomalies
    geo_logs = """2024-01-15 09:00:00 - User john.doe logged in from 192.168.1.100 (New York, US)
2024-01-15 14:00:00 - User john.doe logged in from 203.45.67.89 (Tokyo, JP)
2024-01-15 19:00:00 - User john.doe logged in from 172.16.0.50 (London, UK)
2024-01-16 09:00:00 - User john.doe logged in from 192.168.1.100 (New York, US)"""
    
    # Demo 4: Time anomalies
    time_logs = """2024-01-15 09:00:00 - User john.doe logged in from 192.168.1.100 (New York, US)
2024-01-15 14:00:00 - User jane.smith logged in from 192.168.1.101 (New York, US)
2024-01-15 23:30:00 - User admin logged in from 192.168.1.50 (New York, US)
2024-01-16 02:15:00 - User john.doe logged in from 192.168.1.100 (New York, US)
2024-01-16 03:45:00 - User jane.smith logged in from 192.168.1.101 (New York, US)"""
    
    # Demo 5: Mixed scenarios
    mixed_logs = """2024-01-15 09:00:00 - User john.doe logged in from 192.168.1.100 (New York, US)
2024-01-15 10:30:00 - User hacker123 failed login attempt from 203.45.67.89 (Tokyo, JP)
2024-01-15 10:31:00 - User hacker123 failed login attempt from 203.45.67.89 (Tokyo, JP)
2024-01-15 10:32:00 - User hacker123 failed login attempt from 203.45.67.89 (Tokyo, JP)
2024-01-15 14:00:00 - User john.doe logged in from 203.45.67.89 (Tokyo, JP)
2024-01-15 23:30:00 - User admin logged in from 192.168.1.50 (New York, US)
2024-01-16 02:15:00 - User john.doe logged in from 172.16.0.50 (London, UK)"""
    
    # Write demo files
    demos = {
        'demo_normal.txt': normal_logs,
        'demo_failed.txt': failed_logs,
        'demo_geo.txt': geo_logs,
        'demo_time.txt': time_logs,
        'demo_mixed.txt': mixed_logs
    }
    
    for filename, content in demos.items():
        with open(filename, 'w') as f:
            f.write(content)
        print(f"Created {filename}")
    
    return demos.keys()

def run_demo(filename, description):
    """Run analysis on a demo file."""
    print(f"\n{'='*60}")
    print(f"DEMO: {description}")
    print(f"File: {filename}")
    print(f"{'='*60}")
    
    analyzer = LogAnalyzer()
    if analyzer.parse_log_file(filename):
        results = analyzer.analyze()
        analyzer.print_results(results)
    else:
        print("Failed to parse log file")

def main():
    """Main demo function."""
    print("🚀 LOG ANALYZER DEMO")
    print("This demo will show you different types of anomalies the analyzer can detect.")
    
    # Create demo files
    print("\n📁 Creating demo log files...")
    demo_files = create_demo_logs()
    
    # Run demos
    demos = [
        ("demo_normal.txt", "Normal Activity - No Anomalies"),
        ("demo_failed.txt", "Failed Login Attempts"),
        ("demo_geo.txt", "Geographic Anomalies"),
        ("demo_time.txt", "Time-based Anomalies"),
        ("demo_mixed.txt", "Mixed Scenarios")
    ]
    
    for filename, description in demos:
        run_demo(filename, description)
        input("\nPress Enter to continue to next demo...")
    
    print(f"\n{'='*60}")
    print("🎉 DEMO COMPLETE!")
    print(f"{'='*60}")
    print("\nYou can now:")
    print("1. Run: python log_analyzer.py --file sample_logs.txt")
    print("2. Try: python log_analyzer.py --file demo_mixed.txt --threshold 2")
    print("3. Create your own log files and analyze them!")
    
    # Clean up demo files
    print("\n🧹 Cleaning up demo files...")
    for filename in demo_files:
        try:
            os.remove(filename)
            print(f"Removed {filename}")
        except:
            pass

if __name__ == '__main__':
    main()
