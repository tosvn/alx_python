import MySQLdb
import sys

# Check if the script is being run directly and not imported
if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python script.py <username> <password> <database_name>")
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    database_name = sys.argv[3]

    try:
        # Connect to MySQL server
        connection = MySQLdb.connect(
            host="localhost",  # Change as needed
            port=3306,         # Change as needed
            user=username,
            passwd=password,
            db=database_name
        )

        # Create a cursor object
        cursor = connection.cursor()

        # Execute the SQL query to fetch states starting with 'N'
        query = "SELECT * FROM states WHERE name LIKE 'N%' ORDER BY states.id ASC"
        cursor.execute(query)

        # Fetch and display the results
        results = cursor.fetchall()
        for row in results:
            print(row)

    except MySQLdb.Error as e:
        print(f"MySQL Error: {e}")
    finally:
        # Close the database connection
        if connection:
            connection.close()

