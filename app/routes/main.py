from flask import Blueprint, render_template, redirect, url_for
from flask_login import login_required, current_user
from app.models.validation import ValidationHistory

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def index():
    return render_template('index.html')

@main_bp.route('/dashboard')
@login_required
def dashboard():
    validations = ValidationHistory.query.filter_by(user_id=current_user.id).order_by(ValidationHistory.created_at.desc()).all()
    return render_template('dashboard.html', validations=validations)

@main_bp.route('/history')
@login_required
def history():
    validations = ValidationHistory.query.filter_by(user_id=current_user.id).order_by(ValidationHistory.created_at.desc()).all()
    return render_template('history.html', validations=validations) 