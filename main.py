from flask import Flask, render_template, request, redirect

app = Flask(__name__)

# Module state lưu trong RAM (dùng Redis hoặc file nếu cần persist)
MODULE_STATE = {
    "AutoLoginCum": False,
    "last_user": "Unknown"
}

@app.route("/")
def index():
    return render_template("index.html", module_state=MODULE_STATE)

@app.route("/toggle/<module_name>")
def toggle_module(module_name):
    if module_name in MODULE_STATE:
        MODULE_STATE[module_name] = not MODULE_STATE[module_name]
    return redirect("/")

@app.route("/offall", methods=["GET"])
def offall():
    return str(MODULE_STATE.get("AutoLoginCum", False)).lower()

@app.route("/ping", methods=["POST"])
def receive_ping():
    data = request.get_json()
    if data and "username" in data:
        MODULE_STATE["last_user"] = data["username"]
    return "ok"
