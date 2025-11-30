from order import Order

class Coffee:
    all = []

    def __init__(self, name):
        self.name = name
        Coffee.all.append(self)

    # name property
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise Exception("Coffee name must be a string.")
        if len(value) < 3:
            raise Exception("Coffee name must be at least 3 characters long.")
        self._name = value

    # rship methods
    def orders(self):
        return [o for o in Order.all if o.coffee == self]

    def customers(self):
        return list({o.customer for o in self.orders()})

    # aggregate methods
    def num_orders(self):
        return len(self.orders())

    def average_price(self):
        prices = [o.price for o in self.orders()]
        return sum(prices) / len(prices) if prices else 0
