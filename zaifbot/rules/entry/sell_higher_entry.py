from zaifbot.trade_tools.last_price import last_price
from zaifbot.rules.entry import Entry


class SellHigherEntry(Entry):
    def __init__(self, amount, sell_price, *, mode='normal'):
        super().__init__(amount=amount, action='ask', mode=mode)
        self.sell_price = sell_price

    def can_entry(self):
        return last_price(self.currency_pair) > self.sell_price
