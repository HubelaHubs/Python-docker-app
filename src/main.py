from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    data = [
        {"cluster": "Sanlam Life Savings (SLS)", "businessunit": "Sanlam Retail Mass", "department": "Assupol"},
        {"cluster": "Sanlam Emerging Markets (SEM)", "businessunit": "Sanlam Pan-Africa (SPA)", "department": "Life Insurance"},
        {"cluster": "Sanlam Investment", "businessunit": "Asset Management", "department": "Satrix"},
        {"cluster": "Santam", "businessunit": "Santam Client Solutions", "department": "Client Service Operations"},
        {"cluster": "Sanlam Fintech", "businessunit": "Sanlam Rewards", "department": "Sanlam Reality Programme"},
        {"cluster": "Sanlam Corporate", "businessunit": "Employee Benefits", "department": "Pension Fund Administration"}
        {"cluster": "Sanlam Personal Finance (SPF)", "businessunit": "Wealth Management", "department": "Financial Planning"},
        {"cluster": "Sanlam Group", "businessunit": "Group Finance", "department": "Financial Reporting"},
        {"cluster": "Sanlam Group", "businessunit": "Group Risk", "department": "Risk Management"},
        {"cluster": "Sanlam Group", "businessunit": "Group Technology", "department": "IT Infrastructure"},
        {"cluster": "Sanlam Group", "businessunit": "Group Marketing", "department": "Brand Management"},
        {"cluster": "Sanlam Group", "businessunit": "Group Human Resources", "department": "Talent Management"},
        {"cluster": "Sanlam Group", "businessunit": "Group Legal", "department": "Compliance and Governance"},
        {"cluster": "Sanlam Group", "businessunit": "Group Strategy", "department": "Corporate Strategy"},
        ]
    return render_template("index.html", data=data)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
