from zaifbot.trade.tools import last_price
from zaifbot.rules.entry.base import Entry


class BuyLowerEntry(Entry):
    def __init__(self, currency_pair, amount, buy_price, name=None):
        super().__init__(currency_pair=currency_pair, amount=amount, action='bid', name=name)
        self.buy_price = buy_price

    def can_entry(self):
        return last_price(self.currency_pair) < self.buy_price
