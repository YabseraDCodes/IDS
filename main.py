from parser import parse_logs
from detector import detect_bruteforce
from alerts import send_alerts

# Step 1: read logs
logs = parse_logs("logs/auth.log")

# Step 2: detect attacks
alerts = detect_bruteforce(logs)

# Step 3: send alerts
send_alerts(alerts)
