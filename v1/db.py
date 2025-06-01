import mysql.connector

conn = mysql.connector.connect(
    host="192.168.1.100",
    user="root",
    password="MyStrongPass123!",
    port=3306,
    database="bot"
)

cursor = conn.cursor()

tables = ['gigs', 'users']

for table_name in tables:
    print(f"\nContents of table `{table_name}`:")
    cursor.execute(f"SELECT * FROM `{table_name}` LIMIT 10;")  # Limit to 10 rows to avoid huge outputs
    
    # Fetch column names to print nicely
    column_names = [desc[0] for desc in cursor.description]
    print("\t".join(column_names))
    
    for row in cursor.fetchall():
        print("\t".join(str(item) for item in row))

cursor.close()
conn.close()
