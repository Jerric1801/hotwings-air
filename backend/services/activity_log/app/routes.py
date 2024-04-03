from flask import Flask, render_template, request, redirect, url_for, session
# from services import get_logs
from app import app

@app.route('/')
def index():
    # if not session.get('logged_in'):
    #     return redirect(url_for('login'))
    
    # log_entries = get_logs()  # This calls the get_logs function
    return render_template('index.html.js')

# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     if request.method == 'POST':
#         session['logged_in'] = True
#         return redirect(url_for('index'))
#     return render_template('login.html')