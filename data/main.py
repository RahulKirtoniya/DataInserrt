import mysql.connector


conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Rahul123*#",
    database="std"
)
cursor = conn.cursor()


string1 = "Our"
string2 = "World"
concatenated_string = string1 + " " + string2


query = "INSERT INTO my_table (student) VALUES (%s)"
values = (concatenated_string,)
cursor.execute(query, values)


conn.commit()

print("Data Inserted Successfully! Thank You")

cursor.close()
conn.close()
