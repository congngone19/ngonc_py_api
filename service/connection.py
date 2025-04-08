import psycopg2

# Database connection parameters
DB_HOST = "localhost"      # Change if using a remote database
DB_NAME = "postgres"
DB_USER = "postgres"
DB_PASSWORD = "ngonc"
DB_PORT = "5432"           # Default PostgreSQL port

def Connect():
    try:
    # Connect to PostgreSQL
        conn = psycopg2.connect(
        host=DB_HOST,
        database=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD,
        port=DB_PORT
        )
        print("Connected to PostgreSQL successfully!")

    # Create a cursor object
        cur = conn.cursor()

    # Execute a query (fetch PostgreSQL version)
        cur.execute("SELECT version();")
        version = cur.fetchone()
        print("PostgreSQL Version:", version)

    # Close cursor and connection
        cur.close()
        conn.close()
        print("Connection closed.")
    except Exception as e:
        print("Error:", e)
