def send_alerts(alerts):
    """
    This function receives a list of detected alerts
    and prints them in a readable way.

    Example input:
    [
        {
            "ip": "192.168.1.10",
            "type": "Brute Force Attack",
            "count": 5,
            "time_window": "60 seconds"
        }
    ]
    """

    # If no alerts → nothing to show
    if not alerts:
        print("No suspicious activity detected.")
        return

    print("\n⚠️ ===== ALERTS DETECTED ===== ⚠️\n")

    # Loop through each alert
    for alert in alerts:
        ip = alert["ip"]
        attack_type = alert["type"]
        count = alert["count"]
        window = alert["time_window"]

        # Print clean formatted message
        print(f"[ALERT] {attack_type}")
        print(f"IP Address   : {ip}")
        print(f"Attempts     : {count}")
        print(f"Time Window  : {window}")
        print("-" * 40)

if __name__ == "__main__":
    sample_alerts = [
        {
            "ip": "192.168.1.10",
            "type": "Brute Force Attack",
            "count": 5,
            "time_window": "60 seconds"
        }
    ]

    send_alerts(sample_alerts)
