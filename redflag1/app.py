from flask import Flask, render_template, request, jsonify
import re

app = Flask(__name__)

# Red flag keywords and patterns
RED_FLAG_KEYWORDS = [
    "controlling", "toxic", "abusive", "dishonest", "suspicious", "danger", "illegal", "manipulation",
    "gaslighting", "manipulative", "dishonesty", "abuse", "neglect", "business", "scam", "fraud",
    "unreliable", "untrustworthy", "hidden fees", "lack of transparency", "misleading", "burnout",
    "chronic stress", "emotional instability", "anxiety", "depression", "isolation", "unsafe",
    "threats", "risky", "unpredictable", "unstable", "hostile environment", "ignores others", "peer pressure", "dangerous"
]

# Red flag patterns to match specific phrases or behaviors
RED_FLAG_PATTERNS = [
    re.compile(r"too good to be true", re.IGNORECASE),
    re.compile(r"unreliable", re.IGNORECASE),
    re.compile(r"scam", re.IGNORECASE),
    re.compile(r"hidden fees", re.IGNORECASE),
    re.compile(r"manipulation", re.IGNORECASE),
    re.compile(r"gaslighting", re.IGNORECASE),
    re.compile(r"you can't trust anyone", re.IGNORECASE),
    re.compile(r"just do what I say", re.IGNORECASE),
    re.compile(r"it's all your fault", re.IGNORECASE),
    re.compile(r"emotional abuse", re.IGNORECASE),
    re.compile(r"violence", re.IGNORECASE),
    re.compile(r"you're crazy", re.IGNORECASE),
    re.compile(r"nobody else will love you", re.IGNORECASE),
    re.compile(r"chronic stress", re.IGNORECASE),
    re.compile(r"burnout", re.IGNORECASE),
    re.compile(r"you're being paranoid", re.IGNORECASE),
    re.compile(r"dangerous", re.IGNORECASE),
    re.compile(r"don't tell anyone", re.IGNORECASE),
    re.compile(r"isolated", re.IGNORECASE),
    re.compile(r"too possessive", re.IGNORECASE)
]

# Quiz data categorized by topics
QUIZ_DATA = {
    "toxic_behaviors": [
        {"id": 1, "question": "Do they gaslight or dismiss your feelings?", "options": ["Yes", "Maybe", "No"], "red_flag": "Yes"},
        {"id": 2, "question": "Do they manipulate or guilt-trip you?", "options": ["Yes", "Maybe", "No"], "red_flag": "Yes"},
        {"id": 3, "question": "Are they honest and transparent?", "options": ["Yes", "Maybe", "No"], "red_flag": "No"},
        {"id": 4, "question": "Do they try to isolate you from friends and family?", "options": ["Yes", "Maybe", "No"], "red_flag": "Yes"},
        {"id": 5, "question": "Do they respect your boundaries?", "options": ["Yes", "Maybe", "No"], "red_flag": "No"},
        {"id": 6, "question": "Do they often make you feel guilty for no reason?", "options": ["Yes", "Maybe", "No"], "red_flag": "Yes"},
        {"id": 7, "question": "Do they take accountability for their actions?", "options": ["Yes", "Maybe", "No"], "red_flag": "No"},
        {"id": 8, "question": "Do they belittle or insult you in public or private?", "options": ["Yes", "Maybe", "No"], "red_flag": "Yes"}
    ],
    "business_dealings": [
        {"id": 1, "question": "Does the deal seem too good to be true?", "options": ["Yes", "Maybe", "No"], "red_flag": "Yes"},
        {"id": 2, "question": "Is the other party avoiding clear communication?", "options": ["Yes", "Maybe", "No"], "red_flag": "Yes"},
        {"id": 3, "question": "Have they been reliable in the past?", "options": ["Yes", "Maybe", "No"], "red_flag": "No"},
        {"id": 4, "question": "Are there hidden terms or fees in the contract?", "options": ["Yes", "Maybe", "No"], "red_flag": "Yes"},
        {"id": 5, "question": "Is the party willing to sign a written agreement?", "options": ["Yes", "Maybe", "No"], "red_flag": "No"},
        {"id": 6, "question": "Are they pressuring you to make a quick decision?", "options": ["Yes", "Maybe", "No"], "red_flag": "Yes"},
        {"id": 7, "question": "Have they provided verifiable credentials or references?", "options": ["Yes", "Maybe", "No"], "red_flag": "No"},
        {"id": 8, "question": "Is their payment method secure and transparent?", "options": ["Yes", "Maybe", "No"], "red_flag": "No"}
    ],
    "mental_health": [
        {"id": 1, "question": "Do you often feel overwhelmed or burned out?", "options": ["Yes", "Maybe", "No"], "red_flag": "Yes"},
        {"id": 2, "question": "Have you noticed recent changes in mood or energy?", "options": ["Yes", "Maybe", "No"], "red_flag": "Yes"},
        {"id": 3, "question": "Are you making time for self-care?", "options": ["Yes", "Maybe", "No"], "red_flag": "No"},
        {"id": 4, "question": "Do you feel supported by those around you?", "options": ["Yes", "Maybe", "No"], "red_flag": "No"},
        {"id": 5, "question": "Have you experienced prolonged sadness or anxiety?", "options": ["Yes", "Maybe", "No"], "red_flag": "Yes"},
        {"id": 6, "question": "Do you have trouble focusing or remembering things?", "options": ["Yes", "Maybe", "No"], "red_flag": "Yes"},
        {"id": 7, "question": "Are you engaging in activities you enjoy?", "options": ["Yes", "Maybe", "No"], "red_flag": "No"},
        {"id": 8, "question": "Do you avoid seeking help when needed?", "options": ["Yes", "Maybe", "No"], "red_flag": "Yes"}
    ],
    "social_situations": [
        {"id": 1, "question": "Do you feel physically unsafe in this environment?", "options": ["Yes", "Maybe", "No"], "red_flag": "Yes"},
        {"id": 2, "question": "Do you feel pressured to do something you're uncomfortable with?", "options": ["Yes", "Maybe", "No"], "red_flag": "Yes"},
        {"id": 3, "question": "Are your boundaries respected?", "options": ["Yes", "Maybe", "No"], "red_flag": "No"},
        {"id": 4, "question": "Do you feel included in group discussions or activities?", "options": ["Yes", "Maybe", "No"], "red_flag": "No"},
        {"id": 5, "question": "Do people in the group show genuine concern for your well-being?", "options": ["Yes", "Maybe", "No"], "red_flag": "No"},
        {"id": 6, "question": "Do you feel judged or criticized frequently in the group?", "options": ["Yes", "Maybe", "No"], "red_flag": "Yes"},
        {"id": 7, "question": "Are you able to freely express your opinions?", "options": ["Yes", "Maybe", "No"], "red_flag": "No"},
        {"id": 8, "question": "Do you feel drained or stressed after social interactions?", "options": ["Yes", "Maybe", "No"], "red_flag": "Yes"}
    ],
    # Define other categories as you have in the original code
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

@app.route("/behaviour")
def behaviour():
    return render_template("behaviour.html")

@app.route("/care")
def care():
    return render_template("care.html")

@app.route("/relation")
def relation():
    return render_template("relation.html")

@app.route("/analyze", methods=["POST"])
def analyze():
    data = request.get_json()
    description = data.get("description", "")

    if not description:
        return jsonify({"error": "Description is required."}), 400

    is_red_flag = False
    reasons = []

    # Check for red flag keywords
    for keyword in RED_FLAG_KEYWORDS:
        if keyword.lower() in description.lower():
            is_red_flag = True
            reasons.append("⚠️ Something seems off in the description. It could be a sign of unhealthy behavior or a concerning pattern.")

    # Check for red flag patterns
    for pattern in RED_FLAG_PATTERNS:
        if pattern.search(description):
            is_red_flag = True
            reasons.append("⚠️ The description seems to follow a pattern that might indicate something is not quite right.")

    response = {
        "isRedFlag": is_red_flag,
        "reason": " ".join(reasons) if reasons else "It seems like everything is okay! There’s no indication of any red flags at the moment. 😌",
        "guidance": "🚨 It might be a good idea to talk to someone you trust, or take a step back to reflect. Be cautious, your well-being matters." if is_red_flag else "❤️ All seems good! Keep trusting your instincts, and feel free to reach out if you need advice or support."
    }

    return jsonify(response)

if __name__ == "__main__":
    app.run(debug=True)
