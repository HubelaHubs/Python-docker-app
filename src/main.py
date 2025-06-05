from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    data = [
        {"cluster": "Sanlam Life Savings (SLS)", "business unit": "Sanlam Retail Mass", "department": "Assupol"},
        {"cluster": "Sanlam Emerging Markets (SEM)", "business unit": "Sanlam Pan-Africa (SPA)", "department": "Life Insurance"},
        {"cluster": "Sanlam Investment", "business unit": "Asset Management", "department": "Satrix"},
        {"cluster": "Santam", "business unit": "Santam Client Solutions", "department": "Client Service Operations"},
        {"cluster": "Sanlam Fintech", "business unit": "Sanlam Rewards", "department": "Sanlam Reality Programme"},
        ]
    return render_template("index.html", data=data)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
