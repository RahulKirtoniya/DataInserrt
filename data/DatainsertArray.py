import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Rahul123*#",
    database="std"
)
cursor = conn.cursor()


stored_array = ["Hello", "Chinu"]
concatenated_string = " ".join(stored_array)


query = "INSERT INTO my_table (student) VALUES (%s)"
values = (concatenated_string,)
cursor.execute(query, values)

conn.commit()
print("Insert Data Successfully! Please check!")

cursor.close()
conn.close()
