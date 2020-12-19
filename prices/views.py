import os
from . import app
import pandas as pd

from flask import render_template, jsonify

@app.route('/prices')
def check_price():
    return render_template('graph.html')

@app.route('/prices/<start>/<close>')
def check_price_range(start, close):

    return render_template('graph.html', start=start, closes=close)



@app.route('/btc_data')
def btc():

    df = pd.read_csv('./prices/static/assets/Coinbase_BTCUSD.csv')

    df_dict = df.T.to_dict()

    return jsonify(df_dict)


@app.route('/btc_data/<start>/<close>')
def btc_range(start, close):

    df = pd.read_csv('./prices/static/assets/Coinbase_BTCUSD.csv')
    df['unix'] = df['unix'].astype(int)
    df = df[(df['unix'] > int(start)) & (df['unix'] < int(close))]
    df_dict = df.T.to_dict()

    return jsonify(df_dict)