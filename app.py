from flask import Flask, request, render_template, jsonify
from utilities import (
    nameValidation,
    mobNumValidation,
    passwordValidation,
    ipaddressValidation,
    dateValidation,
    emailValidation,
    fileTypeValidation,
    filesizeValidation
)
import re
from datetime import datetime

app = Flask(__name__)

def analyze_password_strength(password):
    feedback = []
    if len(password) < 8:
        feedback.append("Password is too short")
    if not re.search(r"[A-Z]", password):
        feedback.append("Add uppercase letters")
    if not re.search(r"[a-z]", password):
        feedback.append("Add lowercase letters")
    if not re.search(r"\d", password):
        feedback.append("Add numbers")
    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        feedback.append("Add special characters")
    return feedback

def analyze_email_domain(email):
    domain = email.split('@')[-1]
    common_domains = ['gmail.com', 'yahoo.com', 'hotmail.com', 'outlook.com']
    if domain in common_domains:
        return f"Using common email domain: {domain}"
    return "Using custom email domain"

def analyze_date_pattern(date):
    try:
        date_obj = datetime.strptime(date, '%d-%m-%Y')
        if date_obj.year < 2000:
            return "Date is from the past century"
        elif date_obj.year > datetime.now().year:
            return "Date is in the future"
        return "Date is in the current century"
    except:
        return "Invalid date format"

def analyze_name_pattern(name):
    if len(name.split()) > 1:
        return "Full name detected"
    return "Single name detected"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/validate', methods=['POST'])
def validate():
    data = request.form
    results = {
        "name": nameValidation(data.get("name", "")),
        "mobile": mobNumValidation(data.get("mobile", "")),
        "email": emailValidation(data.get("email", "")),
        "password": passwordValidation(data.get("password", "")),
        "ip": ipaddressValidation(data.get("ip", "")),
        "date": dateValidation(data.get("date", ""))
    }
    
    # AI Analysis
    ai_insights = {
        "password_analysis": analyze_password_strength(data.get("password", "")),
        "email_analysis": analyze_email_domain(data.get("email", "")),
        "date_analysis": analyze_date_pattern(data.get("date", "")),
        "name_analysis": analyze_name_pattern(data.get("name", ""))
    }
    
    # Handle file validation if a file was uploaded
    if 'file' in request.files:
        file = request.files['file']
        if file.filename:
            results["file_type"] = fileTypeValidation(file.filename)
            # Save file temporarily to check size
            temp_path = f"temp_{file.filename}"
            file.save(temp_path)
            results["file_size"] = filesizeValidation(temp_path)
            # Clean up temp file
            import os
            os.remove(temp_path)
    
    return jsonify({
        "validation_results": results,
        "ai_insights": ai_insights
    })

if __name__ == '__main__':
    app.run(debug=True, port=5001) 