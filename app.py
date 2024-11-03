from flask import Flask, render_template, request
from argument_generator import generate_argument_and_wine, CATEGORIES
import random

app = Flask(__name__)
app.secret_key = "christmas_arguments_2023"

@app.route("/", methods=["GET", "POST"])
def index():
    arguments = []
    wine_pairing = None
    
    if request.method == "POST":
        target_person = request.form.get("target_person")
        topic = request.form.get("topic")
        arguments, wine_pairing = generate_argument_and_wine(target_person, topic)
    
    categories = {k: random.choice(v) for k, v in CATEGORIES.items()}
    
    return render_template("index.html", 
                         arguments=arguments, 
                         wine_pairing=wine_pairing,
                         categories=categories)
