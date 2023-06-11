import os
import logging
from flask import Flask
from flask_migrate import Migrate
from flask_cors import CORS
from dotenv import load_dotenv
from apscheduler.schedulers.background import BackgroundScheduler

from apps.models import *
from apps.candlestick import candlestick
from crons.BinanceApi.croneBinanceApi import collect_ticker_data

app = Flask(__name__)
load_dotenv()

# configure flask application
debug_mode = os.getenv("DEBUG", True)
secret_key = os.getenv("SECRET_KEY")
database_uri = os.getenv("SQLALCHEMY_DATABASE_URI")
track_db_modifications = os.getenv("SQLALCHEMY_TRACK_MODIFICATIONS")

app.config['SECRET_KEY'] = secret_key
app.config['SQLALCHEMY_DATABASE_URI'] = database_uri
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = track_db_modifications

# configure migrations
db.init_app(app)

migrate = Migrate(app, db)

CORS(app)

app.register_blueprint(candlestick)


def cron_job_handler():
    # define yor cron jobs here
    symbol_list = ["ETHUSDT", "BTCUSDT"]
    intervals_for_retriving = '1d'
    scheduler = BackgroundScheduler(daemon=True)
    for symbol in symbol_list:
        scheduler.add_job(collect_ticker_data,
                          'interval',
                          days=1,
                          args=[symbol, intervals_for_retriving]
                          )

    logging.info('Cronjob started, it will retrieve the data each day.')
    scheduler.start()


if __name__ == '__main__':
    # run cron jobs
    cron_job_handler()
    # run flask server
    app.run(debug=debug_mode)
