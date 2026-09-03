import sqlite3
with sqlite3.connect("lesson.db") as conn:
    cursor = conn.cursor()
    # Turn on foreign key checking
    cursor.execute("PRAGMA foreign_keys = ON")
    # -----------------------------
    # 1. CUSTOMERS TABLE
    # -----------------------------
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS customers (
            customer_id INTEGER PRIMARY KEY,
            customer_name TEXT NOT NULL UNIQUE
        )
    """)
    # -----------------------------
    # 2. EMPLOYEES TABLE
    # -----------------------------
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS employees (
            employee_id INTEGER PRIMARY KEY,
            last_name TEXT NOT NULL
        )
    """)
    # -----------------------------
    # 3. PRODUCTS TABLE
    # -----------------------------
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS products (
            product_id INTEGER PRIMARY KEY,
            product_name TEXT NOT NULL,
            price REAL NOT NULL
        )
    """)
    # -----------------------------
    # 4. ORDERS TABLE
    # -----------------------------
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS orders (
            order_id INTEGER PRIMARY KEY,
            customer_id INTEGER NOT NULL,
            employee_id INTEGER NOT NULL,
            FOREIGN KEY (customer_id)
                REFERENCES customers(customer_id),
            FOREIGN KEY (employee_id)
                REFERENCES employees(employee_id)
        )
    """)
    # -----------------------------
    # 5. LINE ITEMS TABLE
    # -----------------------------
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS line_items (
            line_item_id INTEGER PRIMARY KEY,
            order_id INTEGER NOT NULL,
            product_id INTEGER NOT NULL,
            quantity INTEGER NOT NULL,
            FOREIGN KEY (order_id)
                REFERENCES orders(order_id),
            FOREIGN KEY (product_id)
                REFERENCES products(product_id)
        )
    """)
    # -----------------------------
    # ADD CUSTOMERS
    # -----------------------------
    customers = [
        (1, "Alice"),
        (2, "Bright Tech"),
        (3, "Perez and Sons")
    ]
    cursor.executemany("""
        INSERT OR IGNORE INTO customers
        (customer_id, customer_name)
        VALUES (?, ?)
    """, customers)
    # -----------------------------
    # ADD EMPLOYEES
    # -----------------------------
    employees = [
        (1, "Harris"),
        (2, "Johnson")
    ]
    cursor.executemany("""
        INSERT OR IGNORE INTO employees
        (employee_id, last_name)
        VALUES (?, ?)
    """, employees)
    # -----------------------------
    # ADD PRODUCTS
    # -----------------------------
    products = [
        (1, "Notebook", 12.50),
        (2, "Headphones", 45.00),
        (3, "Keyboard", 35.00),
        (4, "Monitor", 120.00),
        (5, "Mouse", 20.00),
        (6, "Webcam", 55.00)
    ]
    cursor.executemany("""
        INSERT OR IGNORE INTO products
        (product_id, product_name, price)
        VALUES (?, ?, ?)
    """, products)
    # -----------------------------
    # ADD ORDERS
    # -----------------------------
    orders = [
        (1, 1, 1),
        (2, 1, 2),
        (3, 2, 1),
        (4, 3, 1),
        (5, 2, 2),
        (6, 3, 1),
        (7, 1, 1),
        (8, 3, 2),
        (9, 1, 1),
        (10, 3, 2)
    ]
    cursor.executemany("""
        INSERT OR IGNORE INTO orders
        (order_id, customer_id, employee_id)
        VALUES (?, ?, ?)
    """, orders)
    # -----------------------------
    # ADD LINE ITEMS
    # -----------------------------
    line_items = [
        # Order 1
        (1, 1, 1, 2),
        (2, 1, 5, 1),
        # Order 2
        (3, 2, 4, 1),
        (4, 2, 3, 1),
        # Order 3
        (5, 3, 2, 2),
        (6, 3, 6, 1),
        # Order 4
        (7, 4, 1, 4),
        (8, 4, 3, 2),
        # Order 5
        (9, 5, 5, 3),
        (10, 5, 2, 1),
        # Order 6
        (11, 6, 4, 2),
        # Order 7
        (12, 7, 6, 2),
        # Order 8
        (13, 8, 1, 1),
        (14, 8, 3, 1),
        # Order 9
        (15, 9, 2, 1),
        (16, 9, 5, 4),
        # Order 10
        (17, 10, 4, 1),
        (18, 10, 6, 1)
    ]
    cursor.executemany("""
        INSERT OR IGNORE INTO line_items
        (line_item_id, order_id, product_id, quantity)
        VALUES (?, ?, ?, ?)
    """, line_items)
    conn.commit()
print("Lesson 10 database created successfully!")