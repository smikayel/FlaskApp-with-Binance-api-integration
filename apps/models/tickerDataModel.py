from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


class TickerData(db.Model):
    __tablename__ = 'TickerData'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    symbol = db.Column(db.String(10), nullable=False)
    interval = db.Column(db.String(5), nullable=False)
    open_time = db.Column(db.DateTime, nullable=False)
    open = db.Column(db.Float, nullable=False)
    high = db.Column(db.Float, nullable=False)
    low = db.Column(db.Float, nullable=False)
    close = db.Column(db.Float, nullable=False)
    volume = db.Column(db.Float, nullable=False)
    close_time = db.Column(db.DateTime, nullable=False)
    quote_asset_volume = db.Column(db.Float, nullable=False)
    number_of_trades = db.Column(db.Integer, nullable=False)
    taker_buy_base_asset_volume = db.Column(db.Float, nullable=False)
    taker_buy_quote_asset_volume = db.Column(db.Float, nullable=False)
    ignore = db.Column(db.Integer, nullable=False)

    def __init__(self, **kwargs):
        # initialisation of the model
        super(TickerData, self).__init__(**kwargs)


def create():
    db.drop_all()
    db.create_all()
