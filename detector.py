from collections import defaultdict
from datetime import timedelta

def detect_bruteforce(logs, threshold=4, window_seconds=60):
    alerts = []

    # Group failed attempts by IP
    failed_attempts = defaultdict(list)

    for log in logs:
        if log["status"] == "FAIL":
            failed_attempts[log["ip"]].append(log["time"])

    # Check each IP
    for ip, times in failed_attempts.items():
        times.sort()

        for i in range(len(times)):
            count = 1
            start_time = times[i]

            for j in range(i + 1, len(times)):
                if times[j] - start_time <= timedelta(seconds=window_seconds):
                    count += 1
                else:
                    break

            if count >= threshold:
                duration = calculate_time_span(times, i, count)

                alerts.append({
                    "ip": ip,
                    "type": "Brute Force Attack",
                    "count": count,
                    "within time": f"{duration} seconds",
                    "time_window": f"{window_seconds} seconds"
                })
                break  # avoid duplicate alerts for same IP

    return alerts

#Added

def calculate_time_span(times, start_index, count):
    """
    Calculate actual time span (in seconds) for a sequence of attempts
    """
    end_index = start_index + count - 1

    # Safety check
    if end_index >= len(times):
        end_index = len(times) - 1

    start_time = times[start_index]
    end_time = times[end_index]

    
    return int((end_time - start_time).total_seconds())

    #For more detail
"""
    return {
    "seconds": int((end_time - start_time).total_seconds()),
    "start": start_time,
    "end": end_time }
"""

# test it directly
if __name__ == "__main__":
    from parser import parse_logs

    logs = parse_logs("logs/auth.log")
    alerts = detect_bruteforce(logs)

    for alert in alerts:
        print(alert)
