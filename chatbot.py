from flask import Flask, request, jsonify
from flask_cors import CORS
from openai import OpenAI
import os
from dotenv import load_dotenv
from database import init_db, create_alert
from alerts import alerts_bp
from message_flagger import analyze_message

# Load .env file
load_dotenv()

app = Flask(__name__)
CORS(app)

# Initialize database
init_db()

# Register alerts blueprint
app.register_blueprint(alerts_bp)

# Get API key from .env
api_key = os.getenv("OPENAI_API_KEY") or "fake_key"

if not api_key:
    raise ValueError("OPENAI_API_KEY not found in .env file")

client = OpenAI(api_key=api_key)

SYSTEM_PROMPT = """You are a Socratic tutor for students. 
Your role is to guide students to discover answers themselves — never give direct answers outright.

Rules:
1. Ask students what they have tried first if they don't show work.
2. If they show effort, guide them step by step using questions.
3. Be short (2–4 sentences max).
4. Always end with a guiding question.
5. Be friendly and supportive.
6. Adapt to any subject.
"""

@app.route("/chat", methods=["POST"])
def chat():
    try:
        data = request.json
        user_message = data.get("message", "")
        history = data.get("history", [])
        student_name = data.get("student_name", "Student")

        flag_result = analyze_message(user_message, history)
        if flag_result.get("should_flag"):
            create_alert(
                student_name=student_name,
                alert_type=flag_result.get("alert_type", "Other"),
                message=flag_result.get("note", "Flagged by the message scanner."),
                source_message=user_message,
                analysis_model=flag_result.get("analysis_model"),
            )

        messages = [{"role": "system", "content": SYSTEM_PROMPT}]
        messages.extend(history)
        messages.append({"role": "user", "content": user_message})

        response = client.chat.completions.create(
            model="gpt-4o",
            messages=messages,
            temperature=0.7,
            max_tokens=300
        )

        reply = response.choices[0].message.content

        return jsonify({"reply": reply})

    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route("/")
def home():
    return "Chatbot backend is running 🚀"


if __name__ == "__main__":
    app.run(debug=True)
