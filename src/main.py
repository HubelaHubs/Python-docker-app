from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    data = [
        {"country": "South Africa", "continent": "Africa", "population": "60,000,000"},
        {"country": "Germany", "continent": "Europe", "population": "83,000,000"},
        {"country": "Brazil", "continent": "South America", "population": "213,000,000"},
        {"country": "Congo", "continent": "Africa", "population": "100,000,000"},
        {"country": "India", "continent": "Asia", "population": "1,400,000,000"},
        {"country": "China", "continent": "Asia", "population": "1,400,000,000"},
        {"country": "United States", "continent": "North America", "population": "331,000,000"},
        {"country": "Canada", "continent": "North America", "population": "38,000,000"},]
    return render_template("index.html", data=data)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
