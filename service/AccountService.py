import psycopg2

# Database connection parameters
DB_HOST = "14.225.192.31"      # Change if using a remote database
DB_NAME = "ngonc_db"
DB_USER = "ngonc"
DB_PASSWORD = "ngonc@19"
DB_PORT = "5432"           # Default PostgreSQL port

def GetAccountByUsernamePassword(username, password):
    result = None
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
        cur.execute("SELECT * FROM accounts WHERE username = %s AND password = %s", (username, password))
        result = cur.fetchall()

    # Close cursor and connection
        cur.close()
        conn.close()
        print("Connection closed.")
    except Exception as e:
        print("Error:", e)
        
    return result

def GetAccountByUsername(username):
    result = None
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
        cur.execute("SELECT * FROM accounts WHERE username = %s", (username,))
        result = cur.fetchall()

    # Close cursor and connection
        cur.close()
        conn.close()
        print("Connection closed.")
    except Exception as e:
        print("Error:", e)
        
    return result
