import sqlite3
import json

# Function to create the database schema
def create_schema(cursor):
    cursor.execute('''CREATE TABLE IF NOT EXISTS emissions
                    (country_code TEXT, year INTEGER, emission REAL)''')

# Function to insert data into the database
def insert_data(cursor, data):
    cursor.executemany("INSERT INTO emissions (country_code, year, emission) VA>

# Connect to the SQLite database
conn = sqlite3.connect('EN_ATM_GHGT_AIP.db')
cursor = conn.cursor()

# Create the database schema
create_schema(cursor)

# Load data from JSON file
with open('data_sorted.json', 'r') as f:
    data = json.load(f)

# Prepare data for insertion
formatted_data = []
for item in data:
    country_code = item['country_code']
    emissions = item['data']
    for emission in emissions:
        formatted_data.append((country_code, int(emission['year']), float(emiss>

# Insert data into the database
insert_data(cursor, formatted_data)

# Commit changes and close connection
conn.commit()
conn.close()

print("Database created successfully and data uploaded.")

