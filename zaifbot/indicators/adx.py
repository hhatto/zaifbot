import pandas as pd
from zaifbot.ohlc_prices import OhlcPrices
from pandas import DataFrame as DF
from talib import abstract as ab
from .base import Indicator

_HIGH = 'high'
_LOW = 'low'
_CLOSE = 'close'
_TIME = 'time'

__all__ = ['ADX']


class ADX(Indicator):
    def __init__(self, currency_pair='btc_jpy', period='1d', length=14):
        self._currency_pair = currency_pair
        self._period = period
        self._length = min(length, self.MAX_LENGTH)

    def request_data(self, count=100, to_epoch_time=None):
        count = min(count, self.MAX_COUNT)
        count_needed = 2 * self._length - 1 + count
        ohlc_prices = OhlcPrices(self._currency_pair, self._period)
        df = DF(ohlc_prices.fetch_data(count_needed, to_epoch_time))
        adx = ab.ADX(df, timeperiod=self._length, prices=[_HIGH, _LOW, _CLOSE], output_names=['adx']).rename('adx')
        adx = pd.concat([df[_TIME], adx], axis=1).dropna()
        return adx.astype(object).to_dict(orient='records')
