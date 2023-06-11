from flask import Blueprint, render_template
from .helpers.retrieve_candlestick import retrieve_candlestick_data
from .helpers.retrieve_pie_chart import retrieve_pie_chart_data
import plotly.graph_objs as go
import datetime
candlestick = Blueprint('candlestick', __name__)


@candlestick.route('/', methods=["GET"])
def candlestick_route():
    candlestick_data = retrieve_candlestick_data()
    candlestick_chart = go.Candlestick(
        x=candlestick_data[0]['x'],
        open=candlestick_data[0]['open'],
        high=candlestick_data[0]['high'],
        low=candlestick_data[0]['low'],
        close=candlestick_data[0]['close'],
        increasing_line_color='green',
        decreasing_line_color='red'
    )
    candlestick_data = [candlestick_chart]
    symbols = ["BTC", "ETH", "XRP", "LTC", "BCH", "ADA", "DOT", "XLM", "LINK", "USDT"]
    market_caps = [1000000, 2000000, 1500000, 800000, 1200000, 900000, 700000, 600000, 500000, 1000000]
    pie_chart = go.Pie(
        labels=symbols,
        values=market_caps
    )
    pie_data = [pie_chart]

    candlestick_div = go.Figure(data=candlestick_data).to_html(full_html=False)
    pie_div = go.Figure(data=pie_data).to_html(full_html=False)

    return render_template('index.html', candlestick_div=candlestick_div, pie_div=pie_div)
