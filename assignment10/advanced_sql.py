import os
import sqlite3

# TASK 1 - COMPLEX JOINS WITH AGGREGATIONS

try:
    conn = sqlite3.connect("./db/lesson.db")
    cursor = conn.cursor()

    query = ("""
    SELECT o.order_id,
        SUM(p.price * li.quantity) AS total
    FROM orders o
    JOIN line_items li
        ON o.order_id = li.order_id
    JOIN products p
        ON li.product_id = p.product_id
    GROUP BY o.order_id
    ORDER BY o.order_id
    LIMIT 5;""")

    cursor.execute(query)

    rows = cursor.fetchall()

    for row in rows:
        print(f"Order {row[0]}: ${row[1]:.2f}")

except sqlite3.Error as e:
    print(f"An error occurred while connecting to the database: {e}")





# TASK 2 - UNDERSTANDING SUBQUERIES
# find the average price of each customers' orders
# return the customer_id (as customer_id_B) and total_price (as total_price)
# do a left join of the customer table with the results of the subquery

# use ON customer_id = customer_id_b
# aliased the customer_id column
# do a group by after (group by customer_id)

# get the average of the total price of the customers' orders
# return the customer name and the average_total_price

try:
    conn = sqlite3.connect("./db/lesson.db")
    cursor = conn.cursor()

    query = """
    SELECT 
        c.customer_name,
        AVG(sub.total_price) AS average_total_price
    FROM customers c
    LEFT JOIN (
        SELECT 
            o.customer_id AS customer_id_b,
            SUM(p.price * li.quantity) AS total_price
        FROM orders o
        JOIN line_items li ON o.order_id = li.order_id
        JOIN products p ON li.product_id = p.product_id
        GROUP BY o.order_id, o.customer_id
    ) AS sub 
        ON c.customer_id = sub.customer_id_b
    GROUP BY c.customer_id, c.customer_name;
    """

    cursor.execute(query)
    columns = cursor.fetchall()

    for col in columns:
        name = col[0]
        avg_price = col[1] if col[1] is not None else 0.00
        print(f"Customer: {name:<20} Avg Order Total: ${avg_price:.2f}")

except sqlite3.Error as e:
    print(f"Database error: {e}")





# TASK 3 - AN INSERT TRANSACTION


# STEP 1 - MAKE SEPARATE SELECT STATEMENTS
try:
    cursor.execute("PRAGMA foreign_keys = 1")

    cursor.execute("SELECT customer_id FROM customers WHERE customer_name = 'Perez and Sons'")
    customer = cursor.fetchone()
    customer_id = customer[0]


    cursor.execute("SELECT employee_id FROM employees WHERE first_name = 'Miranda' AND last_name = 'Harris' ")
    employee = cursor.fetchone()
    employee_id = employee[0]

    cursor.execute("SELECT product_id FROM products ORDER BY price ASC LIMIT 5")
    product_ids = cursor.fetchall()
    product_ids = [product_id[0] for product_id in product_ids]

    print(customer)
    print(employee)
    print(product_ids)

# STEP 2 - INSERT NEW RECORDS

    cursor.execute(
    "INSERT INTO orders (customer_id, employee_id) VALUES (?, ?) RETURNING order_id",
    (customer_id, employee_id)
)
    order_id = cursor.fetchone()[0]

    for product_id in product_ids:
        cursor.execute(
            "INSERT INTO line_items (order_id, product_id, quantity) VALUES (?, ?, ?)",
            (order_id, product_id, 10)
        )
    conn.commit()
    print("Transaction committed successfully! New Order ID:", order_id)

except Exception as e:
    conn.rollback()
    print('Error:', e)


# DELETING THE TRANSACTIONS
cursor.execute("DELETE FROM line_items WHERE order_id IN (250);")
cursor.execute("DELETE FROM orders WHERE order_id IN (250);")

conn.commit()


# MAKING A SELECT STATEMENT BY JOIN
transaction_query = """
SELECT li.line_item_id, li.quantity, p.product_name
FROM line_items li
JOIN orders o ON li.order_id = o.order_id
JOIN products p ON p.product_id = li.product_id
WHERE li.order_id = ?;
"""

cursor.execute(transaction_query, (order_id,))
results = cursor.fetchall()

for row in results:
    print(f"Line Item ID: {row[0]} | Quantity: {row[1]} | Product: {row[2]}")




# TASK 4 - AGGREGATION WITH HAVING
having_query = """
SELECT e.employee_id, e.first_name, e.last_name, COUNT(o.order_id) AS count
FROM employees AS e
JOIN orders AS o ON o.employee_id = e.employee_id
GROUP BY e.employee_id, e.first_name, e.last_name
HAVING count > 5;
"""
cursor.execute(having_query)
employee_results = cursor.fetchall()
for row in employee_results:
    print(f"Employee ID: {row[0]} | First Name: {row[1]} | Last Name: {row[2]} | Order Count: {row[3]}")

conn.close()