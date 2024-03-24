import sqlite3
import pandas as pd

# Connect to the SQLite database
conn = sqlite3.connect('EN_ATM_GHGT_AIP.db')
cursor = conn.cursor()

# Queries to execute
queries = [
    "SELECT COUNT(*) AS num_countries FROM emissions",
    "SELECT * FROM emissions LIMIT 5",
    """
    SELECT * FROM emissions ORDER BY RANDOM() LIMIT 5
    """
]

# Execute each query and print the results
for query in queries:
    print(f"**`{query}`**")
    print()
    cursor.execute(query)
    result = cursor.fetchall()
    print(pd.DataFrame(result, columns=[desc[0] for desc in cursor.description]).to_markdown(tablefmt="pipe"))
    print()

# Close connection
conn.close()
