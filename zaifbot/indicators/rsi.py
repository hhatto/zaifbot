import pandas as pd
from pandas import DataFrame as DF
from talib import abstract as ab
from .indicator import Indicator
from .candle_sticks import CandleSticks

_HIGH = 'high'
_LOW = 'low'
_CLOSE = 'close'
_TIME = 'time'


class RSI(Indicator):
    MAX_LENGTH = 100
    MAX_COUNT = 1000

    def __init__(self, currency_pair='btc_jpy', period='1d', length=14):
        self._currency_pair = currency_pair
        self._period = period
        self._length = min(length, self.MAX_LENGTH)

    def request_data(self, count=MAX_COUNT, to_epoch_time=None):
        adjusted_count = self._get_adjusted_count(count)
        candlesticks = CandleSticks(self._currency_pair, self._period)
        df = DF(candlesticks.request_data(adjusted_count, to_epoch_time))
        rsi = ab.RSI(df, price=_CLOSE, timeperiod=self._length).rename('rsi')
        rsi = pd.concat([df[_TIME], rsi], axis=1).dropna()
        return rsi.astype(object).to_dict(orient='records')

    def _get_adjusted_count(self, count):
        count = min(count, self.MAX_COUNT)
        return count + self._length
