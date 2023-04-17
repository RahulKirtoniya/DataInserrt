import mysql.connector

# Connect to MySQL
conn = mysql.connector.connect(
    host="localhost",
    user="your_username",
    password="your_password",
    database="your_database"
)
cursor = conn.cursor()

# Concatenate two strings
string1 = "Hello"
string2 = "World"
concatenated_string = string1 + " " + string2

# Insert data into MySQL
query = "INSERT INTO your_table_name (column_name) VALUES (%s)"
values = (concatenated_string,)
cursor.execute(query, values)

# Commit the transaction
conn.commit()

# Close the database connection
cursor.close()
conn.close()
