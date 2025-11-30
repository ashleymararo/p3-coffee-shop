from customer import Customer
from coffee import Coffee
from order import Order

# Create Customers
ashley = Customer("Ashley")
victor = Customer("Victor")

# Create Coffees
latte = Coffee("Latte")
espresso = Coffee("Espresso")

# Create Orders
ashley.create_order(latte, 5.0)
ashley.create_order(latte, 6.0)
victor.create_order(latte, 4.5)
victor.create_order(espresso, 3.0)

# Test customer methods
print("Ashley's coffees:", [c.name for c in ashley.coffees()])
print("Victor's coffees:", [c.name for c in victor.coffees()])
print("Ashley's orders count:", len(ashley.orders()))

# Test coffee methods
print("Latte orders:", latte.num_orders())
print("Latte average price:", latte.average_price())
print("Customers who ordered Latte:", [c.name for c in latte.customers()])

# Test most_aficionado
print("Latte aficionado:", Customer.most_aficionado(latte).name)
print("Espresso aficionado:", Customer.most_aficionado(espresso).name)
