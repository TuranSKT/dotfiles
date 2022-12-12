"""
Utility functions
"""

from screeninfo import get_monitors

primary_monitor, secondary_monitor = get_monitors()
if not primary_monitor.is_primary:
    secondary_monitor, primary_monitor = get_monitors()

def monitor_adapt(primary, divider, attr):
    return int(getattr(primary_monitor, attr)/divider) if primary else int(getattr(secondary_monitor, attr)/divider)
