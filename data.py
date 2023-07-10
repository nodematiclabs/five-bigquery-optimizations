import csv
import random
from faker import Faker

# Initialize faker
fake = Faker()

# Headers
customer_headers = ["id", "name", "email"]
order_headers = ["id", "product", "quantity", "customer_id"]

# List of possible products
products = ["Apple", "Orange", "Banana", "Pear", "Grapes"]

# Generate Customers data
customers = [customer_headers]
for i in range(1, 80001):
    name = fake.name()
    email = fake.email()
    customers.append([i, name, email])

# Generate Orders data
orders = [order_headers]
for i in range(1, 500001):
    product = random.choice(products)
    quantity = random.randint(1, 20)
    customer_id = random.randint(1, 80000) # assuming we have 80000 customers
    orders.append([i, product, quantity, customer_id])

# Writing customers data to customers.csv
with open('customers.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(customers)

# Writing orders data to orders.csv
with open('orders.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(orders)
