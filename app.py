from flask import Flask, request
import requests
import os

app = Flask(__name__)

LINE_TOKEN = os.environ.get("LINE_TOKEN")

@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.json

    try:
        user_id = data["events"][0]["source"]["userId"]
        text = data["events"][0]["message"]["text"]
    except:
        return "OK"

    # 何も返さない
    return "OK"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
