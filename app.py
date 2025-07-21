from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from dotenv import load_dotenv
load_dotenv()

import smtplib, os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

app = Flask(__name__, static_folder="static", template_folder="templates")
CORS(app)

EMAIL = os.getenv("EMAIL")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")
TO_EMAIL = os.getenv("TO_EMAIL") or EMAIL

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/software")
def software():
    return render_template("software.html")

@app.route("/hr")
def hr():
    return render_template("hr.html")
if __name__ == "__main__":
    app.run(debug=True)