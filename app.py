from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "Smart Student Assistant is running!"

@app.route("/plan", methods=["POST"])
def plan():
    data = request.json
    days = data.get("days", 5)
    subjects = data.get("subjects", ["Math", "Physics"])

    plan = []
    for i in range(days):
        plan.append(f"Day {i+1}: Study {subjects[i % len(subjects)]} for 2 hours")

    return jsonify({"study_plan": plan})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)