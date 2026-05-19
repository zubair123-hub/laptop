from flask import Flask, request
import os

app = Flask(__name__)

SECRET_KEY = "12345"

@app.route("/command", methods=["POST"])
def command():

    data = request.json

    if data.get("key") != SECRET_KEY:
        return {"error": "Unauthorized"}, 403

    cmd = data.get("command")

    print("Received:", cmd)

    if cmd == "open":
        os.system("gnome-terminal &")

    elif cmd == "close":
        os.system("pkill gnome-terminal")

    return {
        "status": "success",
        "command": cmd
    }

if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000,
        ssl_context=("cert.pem", "key.pem")
    )
