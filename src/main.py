from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = "25177"  # Replace with a secure random key in production

@app.route("/login", methods=["GET", "POST"])
def login():
    error = None
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        # Simple check (replace with real authentication)
        if username == "admin" and password == "password":
            session["logged_in"] = True
            return redirect(url_for("home"))
        else:
            error = "Invalid username or password."
    return render_template("login.html", error=error)

@app.route("/")
def home():
    if not session.get("logged_in"):
        return redirect(url_for("login"))
    data = [
        {"cluster": "Sanlam Life Savings (SLS)", "businessunit": "Sanlam Retail Mass", "department": "Assupol"},
        {"cluster": "Sanlam Emerging Markets (SEM)", "businessunit": "Sanlam Pan-Africa (SPA)", "department": "Life Insurance"},
        {"cluster": "Sanlam Investment", "businessunit": "Asset Management", "department": "Satrix"},
        {"cluster": "Santam", "businessunit": "Santam Client Solutions", "department": "Client Service Operations"},
        {"cluster": "Sanlam Fintech", "businessunit": "Sanlam Rewards", "department": "Sanlam Reality Programme"},
        {"cluster": "Sanlam Corporate", "businessunit": "Employee Benefits", "department": "Pension Fund Administration"},
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

@app.route("/logout")
def logout():
    session.pop("logged_in", None)
    return redirect(url_for("login"))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)