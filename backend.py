from flask import Flask, request, jsonify
from flask_cors import CORS

# Initialize Flask app
app = Flask(__chatbot__)
CORS(app)  # Allow frontend (HTML/JS) to connect

# ----------- Chatbot Logic -----------
def get_bot_response(user_message: str) -> str:
    """Simple finance assistant logic"""
    msg = user_message.lower()
    if "tax" in msg:
        return "💡 You can save tax by investing in ELSS, PPF, or NPS. Section 80C allows up to ₹1.5 lakh deduction."
    elif "save" in msg or "savings" in msg:
        return "💰 A good practice is the 50-30-20 rule: 50% needs, 30% wants, 20% savings."
    elif "invest" in msg or "investment" in msg:
        return "📈 Diversify across mutual funds, index funds, stocks, and government bonds for stability."
    elif "loan" in msg:
        return "🏦 Compare interest rates before borrowing. Paying off high-interest loans first is wise."
    elif "hello" in msg or "hi" in msg:
        return "👋 Hello! I'm your Finance Assistant. Ask me about savings, taxes, investments, or loans."
    else:
        return "🤔 I can help with savings, taxes, investments, and loans. What would you like to know?"

# ----------- API Routes -----------
@app.route("/", methods=["GET"])
def home():
    return jsonify({"message": "✅ Finance Chatbot Backend is running!"})

@app.route("/chat", methods=["POST"])
def chat():
    try:
        data = request.get_json()
        print("📩 Received:", data)   # Debug log
        user_message = data.get("message", "")
        if not user_message.strip():
            return jsonify({"response": "⚠️ Please type something."}), 400
        reply = get_bot_response(user_message)
        print("🤖 Reply:", reply)     # Debug log
        return jsonify({"response": reply})
    except Exception as e:
        print("❌ Error:", str(e))    # Debug log
        return jsonify({"error": str(e)}), 500

# ----------- Start Server -----------
if __name__ == "__main__":
    print("🚀 Starting Finance Chatbot Backend...")
    app.run(debug=True, port=5000)
