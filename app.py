from flask import Flask, render_template_string

# Import your own modules
from parser import parse_logs
from detector import detect_bruteforce

# Create Flask app
app = Flask(__name__)

# Simple HTML template (embedded, no separate file needed)
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

# Route: homepage
@app.route("/")
def home():
    """
    This function runs when user opens the website
    """

    # Step 1: read logs
    logs = parse_logs("logs/auth.log")

    # Step 2: detect attacks
    alerts = detect_bruteforce(logs)

    # Step 3: send data to HTML
    return render_template_string(HTML_TEMPLATE, alerts=alerts)


# Run the app
if __name__ == "__main__":
    app.run()
