from flask import jsonify, request, render_template
from app import app


@app.route('/flight_tracker')
def flight_tracker():
    return render_template('index.html.j2') 