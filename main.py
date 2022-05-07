#!/usr/bin/python
# coding: utf-8
from flask import Flask, jsonify, request, render_template
from templates import logic
from datetime import date
import pandas as pd
# import pandas_datareader as web
import numpy as np

app = Flask(__name__)

# curr_flag = 0


@app.route('/')
def api():
    return render_template('index.html')


@app.route('/predict/<string:stock>')
def signup(stock):
    start_date = date.today()
    e = start_date.strftime("%Y-%m-%d")
    # print(e)
    dataframe, pred = logic.model(stock, e)
    # print(dataframe)
    try:
        with open(f'{stock}flag.txt', 'r') as flag_saver:
            curr_flag = int(flag_saver.read())
    except FileNotFoundError:
        with open(f'{stock}flag.txt', 'w') as flag_saver:
            flag_saver.write(str(0))
            curr_flag = 0
    buy, sell, flag = logic.buy_sell_short(
        dataframe, stock, curr_flag)
    with open(f'{stock}flag.txt', 'w') as flag_saver:
        flag_saver.write(str(flag))
    print(flag)
    if len(buy) != 0:
        buyFlag = True
    else:
        buyFlag = False
    if len(sell) != 0:
        sellFlag = True
    else:
        sellFlag = False

    result = {
        "Stock": stock,
        "Buy": buyFlag,
        "Sell": sellFlag,
        "Flag": flag,
    }
    # print(result)
    return jsonify(result)


@app.route('/current/<string:stock>')
def current(stock):
    return jsonify(logic.current(stock))


@app.route('/week/<string:stock>')
def week(stock):
    df = logic.week(stock)
    return jsonify(df)


@app.route('/rawpredict/<string:stock>')
def data(stock):
    df, pred = logic.model(stock)
    return jsonify(pred)


@app.route('/rawdata/<string:stock>/<int:days>')
def raw(stock, days):
    df = logic.getraw(stock, days)
    return jsonify(df)


if __name__ == '__main__':
    app.run(debug=True)
