class Order:
    _all = []

    def __init__(self, customer, coffee, price):
        # Validation done using type-checking AFTER classes load
        from customer import Customer
        from coffee import Coffee

        if not isinstance(customer, Customer):
            raise Exception("customer must be a Customer instance.")
        if not isinstance(coffee, Coffee):
            raise Exception("coffee must be a Coffee instance.")
        if not (isinstance(price, float) or isinstance(price, int)):
            raise Exception("price must be a number.")
        if not (1.0 <= float(price) <= 10.0):
            raise Exception("price must be between 1.0 and 10.0")

        self._customer = customer
        self._coffee = coffee
        self._price = float(price)

        Order._all.append(self)

    @property
    def customer(self):
        return self._customer

    @property
    def coffee(self):
        return self._coffee

    @property
    def price(self):
        return self._price
