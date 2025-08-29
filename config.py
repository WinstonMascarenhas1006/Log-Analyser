"""
Configuration settings for the Log Analyzer
"""

# Default thresholds
DEFAULT_FAILED_LOGIN_THRESHOLD = 3
DEFAULT_TIME_WINDOW_HOURS = 24

# Time-based anomaly settings
UNUSUAL_HOURS_START = 23  # 11 PM
UNUSUAL_HOURS_END = 6     # 6 AM

# Geographic anomaly settings
MAX_DISTANCE_KM = 1000  # Maximum reasonable distance between logins in km

# Risk levels
RISK_LEVELS = {
    'LOW': '🟢',
    'MEDIUM': '🟡', 
    'HIGH': '🔴'
}

# Log patterns for parsing - more flexible patterns
LOG_PATTERNS = {
    'successful_login': r'(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}) - User (\S+) logged in from (\S+) \((.+?)\)',
    'failed_login': r'(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}) - User (\S+) failed login attempt from (\S+) \((.+?)\)'
}

# Sample locations for testing (city, country, lat, lon)
SAMPLE_LOCATIONS = {
    'New York': {'country': 'US', 'lat': 40.7128, 'lon': -74.0060},
    'London': {'country': 'UK', 'lat': 51.5074, 'lon': -0.1278},
    'Tokyo': {'country': 'JP', 'lat': 35.6762, 'lon': 139.6503},
    'Sydney': {'country': 'AU', 'lat': -33.8688, 'lon': 151.2093},
    'Berlin': {'country': 'DE', 'lat': 52.5200, 'lon': 13.4050},
    'Moscow': {'country': 'RU', 'lat': 55.7558, 'lon': 37.6176},
    'Beijing': {'country': 'CN', 'lat': 39.9042, 'lon': 116.4074},
    'Mumbai': {'country': 'IN', 'lat': 19.0760, 'lon': 72.8777}
}
