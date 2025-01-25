from flask import Flask, render_template, request, jsonify
import re

app = Flask(__name__)

# Red flag keywords and patterns
RED_FLAG_KEYWORDS = [
    "controlling", "toxic", "abusive", "dishonest", "suspicious", "danger", "illegal", "manipulation",
    "gaslighting", "manipulative", "dishonesty", "abuse", "neglect", "business", "scam", "fraud",
    "unreliable", "untrustworthy", "hidden fees", "lack of transparency", "misleading", "burnout",
    "chronic stress", "emotional instability", "anxiety", "depression", "isolation", "unsafe",
    "threats", "risky", "unpredictable", "unstable", "hostile environment", "peer pressure", "dangerous"
]
RED_FLAG_PATTERNS = [re.compile(r"too good to be true", re.IGNORECASE)]

# Quiz data categorized by topics
QUIZ_DATA = {
    "toxic_behaviors": [
        {"id": 1, "question": "Do they gaslight or dismiss your feelings?", "options": ["Yes", "No"], "red_flag": "Yes"},
        {"id": 2, "question": "Do they manipulate or guilt-trip you?", "options": ["Yes", "No"], "red_flag": "Yes"},
        {"id": 3, "question": "Are they honest and transparent?", "options": ["Yes", "No"], "red_flag": "No"},
    ],
    "business_dealings": [
        {"id": 1, "question": "Does the deal seem too good to be true?", "options": ["Yes", "No"], "red_flag": "Yes"},
        {"id": 2, "question": "Is the other party avoiding clear communication?", "options": ["Yes", "No"], "red_flag": "Yes"},
        {"id": 3, "question": "Have they been reliable in the past?", "options": ["Yes", "No"], "red_flag": "No"},
    ],
    "mental_health": [
        {"id": 1, "question": "Do you often feel overwhelmed or burned out?", "options": ["Yes", "No"], "red_flag": "Yes"},
        {"id": 2, "question": "Have you noticed recent changes in mood or energy?", "options": ["Yes", "No"], "red_flag": "Yes"},
        {"id": 3, "question": "Are you making time for self-care?", "options": ["Yes", "No"], "red_flag": "No"},
    ],
    "social_situations": [
        {"id": 1, "question": "Do you feel physically unsafe in this environment?", "options": ["Yes", "No"], "red_flag": "Yes"},
        {"id": 2, "question": "Do you feel pressured to do something you're uncomfortable with?", "options": ["Yes", "No"], "red_flag": "Yes"},
        {"id": 3, "question": "Are your boundaries respected?", "options": ["Yes", "No"], "red_flag": "No"},
    ],
}

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/categories")
def categories():
    categories = list(QUIZ_DATA.keys())
    return render_template("categories.html", categories=categories)

@app.route("/quiz/<category>")
def quiz(category):
    questions = QUIZ_DATA.get(category, [])
    if not questions:
        return "Category not found", 404
    return render_template("quiz.html", questions=questions, category=category)

@app.route("/result", methods=["POST"])
def result():
    data = request.json
    category = data.get("category")
    answers = data.get("answers", {})
    questions = QUIZ_DATA.get(category, [])
    red_flags = sum(1 for q in questions if answers.get(str(q["id"])) == q["red_flag"])
    return jsonify({"red_flags": red_flags, "total_questions": len(questions)})

@app.route("/detector")
def detector():
    return render_template("detector.html")

@app.route("/analyze", methods=["POST"])
def analyze():
    data = request.get_json()
    description = data.get("description", "")

    if not description:
        return jsonify({"error": "Description is required."}), 400

    is_red_flag = False
    reasons = []

    for keyword in RED_FLAG_KEYWORDS:
        if keyword.lower() in description.lower():
            is_red_flag = True
            reasons.append(f"The keyword '{keyword}' indicates a red flag.")

    for pattern in RED_FLAG_PATTERNS:
        if pattern.search(description):
            is_red_flag = True
            reasons.append(f"The pattern '{pattern.pattern}' suggests a red flag.")

    response = {
        "isRedFlag": is_red_flag,
        "reason": " ".join(reasons) if reasons else "None",
        "guidance": "Be cautious and seek advice." if is_red_flag else "All seems fine."
    }

    return jsonify(response)

if __name__ == "__main__":
    app.run(debug=True)
