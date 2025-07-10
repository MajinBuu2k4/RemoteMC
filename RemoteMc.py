from flask import Flask, request

app = Flask(__name__)

# Trạng thái điều khiển từ xa (ban đầu là bật)
poll_enabled = True

@app.route("/")
def index():
    if poll_enabled:
        return "/offall"
    else:
        return "noop"  # Không làm gì nếu bị vô hiệu

@app.route("/toggle", methods=["POST"])
def toggle():
    global poll_enabled
    poll_enabled = not poll_enabled
    return f"Polling {'enabled' if poll_enabled else 'disabled'}."

@app.route("/status", methods=["GET"])
def status():
    return f"Polling is currently {'ENABLED' if poll_enabled else 'DISABLED'}."

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
