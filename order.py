from customer import Customer
from coffee import Coffee

class Order:
    all = []

    def __init__(self, customer, coffee, price):
        self.customer = customer
        self.coffee = coffee
        self.price = price
        Order.all.append(self)

    # customer property
    @property
    def customer(self):
        return self._customer

    @customer.setter
    def customer(self, value):
        if not isinstance(value, Customer):
            raise Exception("customer must be a Customer instance")
        self._customer = value

    # coffee property
    @property
    def coffee(self):
        return self._coffee

    @coffee.setter
    def coffee(self, value):
        if not isinstance(value, Coffee):
            raise Exception("coffee must be a Coffee instance")
        self._coffee = value

    # price property
    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if not isinstance(value, (int, float)):
            raise Exception("price must be a number")
        if not 1.0 <= value <= 10.0:
            raise Exception("price must be between 1.0 and 10.0")
        self._price = float(value)
