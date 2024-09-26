from flask import Flask, render_template, request
from datetime import datetime
import requests
import time
import smtplib
import os
from dotenv import load_dotenv
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

app = Flask(__name__)
load_dotenv()

current_year = datetime.now().year
url = os.getenv('PROG_URL')
MY_EMAIL = os.getenv('MY_EMAIL')
MY_PASSWORD = os.getenv('MY_PASSWORD')
RECIPIENT_EMAIL = MY_EMAIL

try:
    response = requests.get(url)
    response.raise_for_status()
    posts = response.json()
except requests.exceptions.RequestException as e:
    print(f"An error occurred: {e}")
    posts = []

def send_email(name, email, phone, message):
    subject = "New User for the Coding Class Whitelist"
    body = f"""
    Name: {name}
    Email: {email}
    Phone: {phone}
    Message: {message}
    """
    # Create the MIMEText object
    msg = MIMEMultipart()
    msg['From'] = MY_EMAIL
    msg['To'] = RECIPIENT_EMAIL
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))
    
    try:
        # Connect to the SMTP server and send the email
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()  # Secure the connection
            server.login(MY_EMAIL, MY_PASSWORD)
            server.send_message(msg)
        print("Email sent successfully")
    except Exception as e:
        print(f"Failed to send email: {e}")

@app.route("/")
def home_page():
    return render_template("index.html", year=current_year, all_post=posts)

@app.route('/about')
def about():
    return render_template('about.html', year=current_year)

@app.route("/post/<int:id>")
def show_post(id):
    requested_post = next((post for post in posts if post["id"] == id), None)
    if requested_post is None:
        return "Post not found", 404 
    return render_template("post.html", post=requested_post, year=current_year)

@app.route('/contact', methods=["POST", "GET"])
def contact():
    if request.method == 'POST':
        name = request.form.get('name')
        email_address = request.form.get('email_address')
        phone_number = request.form.get('phone_number')
        messages = request.form.get('messages')

        print(f"Name: {name}")
        print(f"Email: {email_address}")
        print(f"Phone: {phone_number}")
        print(f"Message: {messages}")

        # Send an email with the form data
        time.sleep(50)
        send_email(name, email_address, phone_number, messages)
        return render_template("contact.html", msg_sent=True, year=current_year)
    return render_template("contact.html", msg_sent=False, year=current_year)

if __name__ == '__main__':
    app.run(debug=True)
