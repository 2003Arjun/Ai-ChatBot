from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
from chatbot import get_response
from gemini_chat import GeminiChat
import os

app = Flask(__name__)
CORS(app)

# Initialize Gemini chat
try:
    gemini_chat = GeminiChat()
    use_gemini = True
except:
    use_gemini = False
    print("Gemini API not configured, using local chatbot")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()
    message = data.get("message")
    
    # Use Gemini if available, otherwise fallback to local chatbot
    if use_gemini and not message.startswith('!'):
        response = gemini_chat.get_response(message)
    else:
        response = get_response(message)
    
    return jsonify({"answer": response})

if __name__ == "__main__":
    app.run(debug=True, port=8000)
