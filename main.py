from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)

# Biến lưu trạng thái module
module_enabled = {
    "AutoLoginCum": True
}

# Biến lưu người dùng gửi request gần nhất (nếu có)
last_username = "Không rõ"

@app.route('/')
def index():
    return render_template("dashboard.html", 
        username=last_username, 
        module_name="AutoLoginCum", 
        is_enabled=module_enabled["AutoLoginCum"]
    )

@app.route('/offall', methods=['GET'])
def offall():
    # Nếu trả về "true" → client sẽ tắt module
    return jsonify(str(not module_enabled["AutoLoginCum"]).lower())

@app.route('/toggle', methods=['POST'])
def toggle_module():
    global last_username

    data = request.get_json()
    new_state = data.get("enable", False)
    user = data.get("username", "Không rõ")

    module_enabled["AutoLoginCum"] = bool(new_state)
    last_username = user

    return jsonify({
        "success": True,
        "module": "AutoLoginCum",
        "enabled": module_enabled["AutoLoginCum"],
        "set_by": user
    })

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
