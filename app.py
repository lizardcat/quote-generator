from flask import Flask, render_template, jsonify
import random
import json

app = Flask(__name__)

def load_quotes():
    with open('quotes.json', 'r', encoding='utf-8') as f:
        return json.load(f)

@app.route("/")
def home():
    quotes = load_quotes()
    quote = random.choice(quotes)
    return render_template("index.html", quote=quote)

if __name__ == "__main__":
    app.run(debug=True)
