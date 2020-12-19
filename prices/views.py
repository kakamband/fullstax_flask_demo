from . import app

from flask import render_template, jsonify

@app.route('/prices')
def check_price():
    return render_template('graph.html')