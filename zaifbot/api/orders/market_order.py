from zaifbot.api.orders.common import OrderBase


class MarketOrder(OrderBase):
    def __init__(self, api, currency_pair, action, amount, comment=''):
        super().__init__(api, currency_pair, comment)
        self._action = action
        self._amount = amount

    @property
    def type(self):
        return 'MarketOrder'

    @property
    def info(self):
        self._info['action'] = self._action
        self._info['currency_pair'] = str(self._currency_pair)
        self._info['price'] = self._round_price()
        self._info['amount'] = self._amount
        return self._info

    def make_order(self):
        self._api.trade(currency_pair=str(self._currency_pair),
                        action=self._action,
                        price=self._round_price(),
                        amount=self._amount,
                        comment=self._comment)
        return self

    def _round_price(self):
        # todo: 未実装
        return self._currency_pair.last_price()