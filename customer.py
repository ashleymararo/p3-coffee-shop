class Customer:
    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise Exception("Name must be a string.")
        if not (1 <= len(value) <= 15):
            raise Exception("Name must be between 1 and 15 characters.")
        self._name = value

from order import Order

    def orders(self):
        return [order for order in Order.all if order.customer == self]

    def coffees(self):
        return list({order.coffee for order in self.orders()})

    def create_order(self, coffee, price):
        return Order(self, coffee, price)

    @classmethod
    def most_aficionado(cls, coffee):

        max_customer = None
        max_spent = 0

        for customer in cls.all:
            total = sum(order.price for order in customer.orders() if order.coffee == coffee)
            if total > max_spent:
                max_spent = total
                max_customer = customer

        return max_customer

    def orders(self):
        from order import Order
        return [order for order in Order._all if order.customer == self]

    def coffees(self):
        return list(set(order.coffee for order in self.orders()))

    def create_order(self, coffee, price):
        from order import Order
        return Order(self, coffee, price)

    @classmethod
    def most_aficionado(cls, coffee):
        # Find the customer who spent the most on this specific coffee
        top_customer = None
        highest_total = 0

        for customer in cls._all:
            # Filter orders for this coffee
            total_spent = sum(
                order.price for order in customer.orders()
                if order.coffee is coffee
            )

            if total_spent > highest_total:
                highest_total = total_spent
                top_customer = customer

        return top_customer if highest_total > 0 else None
