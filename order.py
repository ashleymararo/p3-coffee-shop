from customer import Customer
from coffee import Coffee

class Order:
    def __init__(self, customer, coffee, price):
        # Validate customer
        if not isinstance(customer, Customer):
            raise Exception("customer must be a Customer instance")

        # Validate coffee
        if not isinstance(coffee, Coffee):
            raise Exception("coffee must be a Coffee instance")

        # Validate price
        if not isinstance(price, (int, float)):
            raise Exception("price must be a number")
        if price < 1.0 or price > 10.0:
            raise Exception("price must be between 1.0 and 10.0")

        self._customer = customer
        self._coffee = coffee
        self._price = float(price)

    @property
    def customer(self):
        return self._customer

    @customer.setter
    def customer(self, customer):
        if not isinstance(customer, Customer):
            raise Exception("customer must be a Customer instance")
        self._customer = customer

    @property
    def coffee(self):
        return self._coffee

    @coffee.setter
    def coffee(self, coffee):
        if not isinstance(coffee, Coffee):
            raise Exception("coffee must be a Coffee instance")
        self._coffee = coffee
