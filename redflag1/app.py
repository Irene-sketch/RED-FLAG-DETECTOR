from flask import Flask, render_template, request, jsonify
import re

app = Flask(__name__)

# Red flag keywords and patterns
RED_FLAG_KEYWORDS = ["controlling", "toxic", "abusive", "dishonest","suspicious", "danger", "illegal","manipulation",
        "gaslighting","manipulative",
        "dishonesty",
        "abuse",
        "neglect",
        "business",
        "scam",
        "fraud",
        "unreliable",
        "untrustworthy",
        "hidden fees",
        "lack of transparency",
        "misleading",
        "burnout",
        "chronic stress",
        "emotional instability",
        "anxiety",
        "depression",
        "isolation",
        "unsafe",
        "threats",
        "risky",
        "unpredictable",
        "unstable",
        "hostile environment",
        "peer pressure",
        "dangerous"]
RED_FLAG_PATTERNS = [re.compile(r"too good to be true", re.IGNORECASE)]

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/detector')
def detector():
    return render_template('detector.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    data = request.get_json()
    description = data.get('description', '')

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

if __name__ == '__main__':
    app.run(debug=True)
