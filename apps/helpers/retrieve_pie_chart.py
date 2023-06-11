from ..models.tickerDataModel import TickerData, db

def retrieve_pie_chart_data():
    # Retrieve the market cap data from the database
    symbols = TickerData.query.with_entities(TickerData.symbol).distinct().limit(10).all()

    # Calculate the market cap for each symbol
    market_caps = {}
    for symbol in symbols:
        total_market_cap = TickerData.query.with_entities(db.func.sum(TickerData.quote_asset_volume)).filter_by(symbol=symbol).scalar()
        market_caps[symbol] = total_market_cap

    pie_chart_data = []
    for symbol, market_cap in market_caps.items():
        data_point = {
            "label": symbol,
            "value": market_cap,
        }
        pie_chart_data.append(data_point)

    return pie_chart_data
