from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

GEMINI_API_KEY = "AIzaSyBM4MZwETBq4EMBNT42m5X-G_lmsEL42IE"
@app.route("/")
def home():
    return "Smart AI Student Assistant Running!"

@app.route("/plan", methods=["POST"])
def plan():
    data = request.json
    days = data.get("days", 5)
    subjects = data.get("subjects", ["Math", "Physics"])

    prompt = f"""
    I have {days} days to study {subjects}.
    Create a smart study plan with priorities, time allocation, and tips.
    """

    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent?key={GEMINI_API_KEY}"

    body = {
        "contents": [{
            "parts": [{"text": prompt}]
        }]
    }

    response = requests.post(url, json=body)
    result = response.json()

    try:
        output = result['candidates'][0]['content']['parts'][0]['text']
    except:
        output = "Error generating plan"

    return jsonify({"plan": output})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)