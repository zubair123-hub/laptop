from flask import Flask, request, jsonify
import subprocess
import os
import datetime

app = Flask(__name__)

PASSWORD = "12345"

HTML_FILE = os.path.expanduser("~/Desktop/zubair.html")

browser_process = None

def log(text):
    now = datetime.datetime.now().strftime("%H:%M:%S")
    print(f"[{now}] {text}")

def open_html():
    global browser_process

    browsers = [
        "firefox",
        "chromium",
        "google-chrome"
    ]

    for browser in browsers:
        if os.system(f"which {browser} > /dev/null 2>&1") == 0:
            browser_process = subprocess.Popen(
                [browser, HTML_FILE]
            )

            log(f"{browser} opened")
            return f"{browser} opened"

    subprocess.Popen(["xdg-open", HTML_FILE])

    log("opened with xdg-open")
    return "opened"

def close_browser():
    browsers = [
        "firefox",
        "chromium",
        "chrome",
        "google-chrome"
    ]

    for browser in browsers:
        os.system(f"pkill {browser}")

    log("browser closed")
    return "closed"

@app.route("/cmd", methods=["POST"])
def cmd():

    password = request.form.get("password")
    command = request.form.get("command")

    if password != PASSWORD:
        log("wrong password")
        return jsonify({
            "status": "error",
            "message": "wrong password"
        })

    if not os.path.exists(HTML_FILE):
        return jsonify({
            "status": "error",
            "message": "zubair.html not found"
        })

    if command == "open":
        result = open_html()

    elif command == "close":
        result = close_browser()

    elif command == "restart":
        close_browser()
        result = open_html()

    else:
        result = "unknown command"

    return jsonify({
        "status": "success",
        "message": result
    })

@app.route("/")
def home():
    return "Advanced Control Server Running"

app.run(
    host="0.0.0.0",
    port=5000
)
