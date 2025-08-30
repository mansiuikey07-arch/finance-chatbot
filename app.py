from flask import Flask, request, jsonify
from flask_cors import CORS

# Create Flask app with your name
app = Flask("Finance Chatbot")
CORS(app)  # Allow frontend to connect

# ---------------- Chatbot Logic ----------------
def get_bot_response(user_message: str) -> str:
    msg = user_message.lower()
    if "tax" in msg:
        return "💡 You can save tax by investing in ELSS, PPF, or NPS. Section 80C allows up to ₹1.5 lakh deduction."
    elif "save" in msg or "savings" in msg:
        return "💰 Try the 50-30-20 rule: 50% needs, 30% wants, 20% savings."
    elif "invest" in msg or "investment" in msg:
        return "📈 Diversify across mutual funds, index funds, and government bonds for stability."
    elif "loan" in msg:
        return "🏦 Compare interest rates before borrowing. Pay off high-interest loans first."
    elif "hello" in msg or "hi" in msg:
        return "👋 Hello! I'm your Finance Chatbot. Ask me about savings, taxes, investments, or loans."
    else:
        return "🤔 I can help with savings, taxes, investments, and loans. What would you like to know?"

# ---------------- API Routes ----------------
@app.route("/", methods=["GET"])
def home():
    return jsonify({"message": "✅ Finance Chatbot Backend is running!"})

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    user_message = data.get("message", "")
    reply = get_bot_response(user_message)
    return jsonify({"response": reply})

# ---------------- Run Server ----------------
if __name__ == "__main__":
    app.run(debug=True, port=5000)
pip install flask flask-cors
python app.py
* Running on http://127.0.0.1:5000/
