import pandas as pd
from zaifbot.ohlc_prices import OhlcPrices
from pandas import DataFrame as DF
from talib import abstract as ab
from .base import Indicator

_HIGH = 'high'
_LOW = 'low'
_CLOSE = 'close'
_TIME = 'time'

__all__ = ['RSI']


class RSI(Indicator):
    def __init__(self, currency_pair='btc_jpy', period='1d', length=14):
        self._currency_pair = currency_pair
        self._period = period
        self._length = length

    def request_data(self, count=100, to_epoch_time=None):
        count_needed = count + self._length
        ohlc_prices = OhlcPrices(self._currency_pair, self._period)
        df = DF(ohlc_prices.fetch_data(count_needed, to_epoch_time))
        rsi = ab.RSI(df, price=_CLOSE, timeperiod=self._length).rename('rsi')
        rsi = pd.concat([df[_TIME], rsi], axis=1).dropna()
        return rsi.astype(object).to_dict(orient='records')
