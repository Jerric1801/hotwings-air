from flask import render_template, request, redirect, url_for
from .services import get_all_transactions, add_transaction

def init_app(app):
    @app.route('/transaction')
    def index():
        transactions = get_all_transactions()
        return render_template('index.html', transactions=transactions)

    @app.route('/transaction/add', methods=['POST'])
    def add():
        if request.method == 'POST':
            data = request.form
            add_transaction(data)
            return redirect(url_for('transaction'))
