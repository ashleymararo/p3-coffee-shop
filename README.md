# Phase 3 Code Challenge — p3-coffee-shop

This project models a small coffee shop domain using Object-Oriented Programming principles in Python.
It implements three main entities:
- Customer
- Coffee
- Order

The relationships follow:
- A Customer can have many Orders.
- A Coffee can have many Orders.
- An Order belongs to one Customer and one Coffee.
- Customer ↔ Coffee is a many-to-many relationship through Order.

## **Features Implemented**
**Customer**
- Name validation (1–15 chars, must be string)
- orders() — returns all orders by the customer
- coffees() — unique coffees ordered
- create_order(coffee, price) — creates an Order instance
- most_aficionado(coffee) — class method that returns the - customer who spent the most on a given coffee

**Coffee**
- Name validation (string, at least 3 chars)
- orders() — returns all orders for this coffee
- customers() — unique customers who purchased it
- num_orders() — total number of orders
- average_price() — average price across all orders

**Order**
- Validates:
  - customer must be a Customer instance
  - coffee must be a Coffee instance
  - price must be float between 1.0 and 10.0
- Belongs to one customer and one coffee

## **Project Structure**
p3-coffee-shop/
│── coffee_shop/
│   ├── customer.py
│   ├── coffee.py
│   ├── order.py
│   ├── debug.py
│   └── tests/
│       └── test_basic.py
│
├── Pipfile
├── Pipfile.lock
└── README.md

## **Installation & Setup
1. Clone the repo:
   ```
   git clone https://github.com/ashleymararo/p3-coffee-shop.git
   cd p3-coffee-shop/coffee_shop
   ```
2. Install dependencies:
   ```
   pipenv install
   pipenv shell
   pipenv install pytest
   ```
3. Debugging / Running the Demo
   Use the included debug.py file to test behaviors:
   ```
   python debug.py
   ```
   **Example Output(from debug.py)**
   ```
   Ashley's coffees: ['Latte']
   Victor's coffees: ['Latte', 'Espresso']
   Ashley's orders count: 2
   Latte orders: 3
   Latte average price: 5.16
   Customers who ordered Latte: ['Victor', 'Ashley']
   Latte aficionado: Ashley
   Espresso aficionado: Victor
   ```

## **Author**
Ashley Mararo


