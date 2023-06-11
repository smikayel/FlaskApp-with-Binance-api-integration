from flask import Blueprint, render_template
from .helpers.retrieve_candlestick import retrieve_candlestick_data
from .helpers.retrieve_pie_chart import retrieve_pie_chart_data

candlestick = Blueprint('candlestick', __name__)


@candlestick.route('/', methods=["GET"])
def candlestick_route():
    candlestick_data = retrieve_candlestick_data()
    pie_chart_data = retrieve_pie_chart_data()

    return render_template('index.html', candlestick_data=candlestick_data, pie_chart_data=pie_chart_data)