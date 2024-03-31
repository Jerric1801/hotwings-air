from flask import render_template, request, redirect, url_for, session
from .services import get_logs


def init_app(app):
    @app.route('/')
    def index():
        if not session.get('logged_in'):
            return redirect(url_for('login'))
        log_entries = get_logs()
        return render_template('index.html', logs=log_entries)

    @app.route('/login', methods=['GET', 'POST'])
    def login():
        if request.method == 'POST':
            session['logged_in'] = True
            return redirect(url_for('index'))
        return render_template('login.html')
