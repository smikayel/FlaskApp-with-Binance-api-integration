from ..models.tickerDataModel import TickerData


def retrieve_candlestick_data():
    candlestick_data = TickerData.query.all()
    candlestick_chart_data = []
    for data in candlestick_data:
        candlestick = {
            "x": [data.open_time, data.close_time],
            "open": data.open,
            "high": data.high,
            "low": data.low,
            "close": data.close,
        }
        candlestick_chart_data.append(candlestick)

    return candlestick_chart_data
