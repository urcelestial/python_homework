import sqlite3
import pandas as pd

# 1 & 2. Connect to the database and read data into a DataFrame using SQL JOIN
conn = sqlite3.connect("../db/lesson.db")

query = """
SELECT 
    line_items.line_item_id,
    line_items.quantity,
    products.product_id,
    products.product_name,
    products.price
FROM line_items
JOIN products 
    ON line_items.product_id = products.product_id;
"""

df = pd.read_sql_query(query, conn)
conn.close()

# 3. Print the first 5 lines of the initial DataFrame
print("--- Initial DataFrame (First 5 lines) ---")
print(df.head())

# 4. Add 'total' column (quantity * price) and print first 5 lines
df['total'] = df['quantity'] * df['price']
print("\n--- DataFrame with 'total' column (First 5 lines) ---")
print(df.head())

# 5. Group by product_id and aggregate
summary_df = df.groupby('product_id').agg({
    'line_item_id': 'count',
    'total': 'sum',
    'product_name': 'first'
}).reset_index()

print("\n--- Summary DataFrame after groupby (First 5 lines) ---")
print(summary_df.head())

# 6. Sort by product_name column
summary_df = summary_df.sort_values(by='product_name')

# 7. Write the final DataFrame to order_summary.csv in assignment9
summary_df.to_csv("order_summary.csv", index=False)
print("\nSummary successfully written to order_summary.csv")