from flask import Flask, render_template, request, jsonify
from chat import chatbot

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("chat.html")

@app.route("/ask", methods=["POST"])
def ask():
    message = request.form["messageText"]
    bot_response = chatbot(message)
    return jsonify({"status": "OK", "answer": bot_response})

if __name__ == "__main__":
    app.run(debug=True)