import os
import requests
from datetime import datetime
from apps.models.tickerDataModel import TickerData
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def collect_ticker_data(symbol, interval):
    database_uri = os.getenv("SQLALCHEMY_DATABASE_URI")

    engine = create_engine(database_uri)
    Session = sessionmaker(bind=engine)
    session = Session()

    base_url = "https://api.binance.com/api/v3/klines"
    params = {
        "symbol": symbol,
        "interval": interval,
        "limit": 1000  # Maximum limit per request
    }

    response = requests.get(base_url, params=params)
    data = response.json()

    ticker_data_objects = []
    for item in data:
        ticker_data_dict = {
            'symbol': symbol,
            'interval': interval,
            'open_time': datetime.fromtimestamp(item[0] / 1000),
            'open': float(item[1]),
            'high': float(item[2]),
            'low': float(item[3]),
            'close': float(item[4]),
            'volume': float(item[5]),
            'close_time': datetime.fromtimestamp(item[6] / 1000),
            'quote_asset_volume': float(item[7]),
            'number_of_trades': int(item[8]),
            'taker_buy_base_asset_volume': float(item[9]),
            'taker_buy_quote_asset_volume': float(item[10]),
            'ignore': int(item[11])
        }
        ticker_data = TickerData(**ticker_data_dict)
        ticker_data_objects.append(ticker_data)

    session.add_all(ticker_data_objects)
    session.commit()
    session.close()
