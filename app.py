import os
from flask import Flask, render_template_string
from parser import parse_logs
from detector import detect_bruteforce

app = Flask(__name__)

HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <meta http-equiv="refresh" content="5">
    <title>IDS Dashboard</title>
</head>
<body>
    <h1>🚨 Intrusion Detection System</h1>

    {% if alerts %}
        <h2>Alerts:</h2>
        <ul>
        {% for alert in alerts %}
            <li>
                <b> 🔴 Type:</b> {{ alert.type }} |
                <b>IP:</b> {{ alert.ip }} |
                <b>Attempts:</b> {{ alert.count }}
            </li>
        {% endfor %}
        </ul>
    {% else %}
        <p>No suspicious activity detected.</p>
    {% endif %}
</body>
</html>
"""

@app.route("/")
def home():
    logs = parse_logs("logs/auth.log")  # Ensure this path exists on Railway
    alerts = detect_bruteforce(logs)
    return render_template_string(HTML_TEMPLATE, alerts=alerts)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  # Railway dynamic port
    app.run(host="0.0.0.0", port=port)       # Important for Railway
