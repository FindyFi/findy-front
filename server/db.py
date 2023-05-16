import psycopg2
import os

# Variables to store the connection and DatabaseManager instance
conn = None
cursor = None

def get_db_manager():
    global conn    
    global cursor

    try:
        if conn is None or conn.closed:
            # Connect to the PostgreSQL database
            conn = psycopg2.connect(
                    host=os.getenv('DB_HOST', 'localhost'),
                    database=os.getenv('DB_NAME', 'findytestfrontdb'),
                    user=os.getenv("DB_USER", "postgres"),
                    password=os.getenv("DB_PASSWORD", "")
                )         
            print("Connected to the PostgreSQL database.")
        
        # Check if the cursor is closed and re-initiate it if necessary
        if cursor is None or cursor.closed:
            cursor = conn.cursor()
            print("DB cursor initiated.")
        
        return cursor
    except (Exception) as error:
        print("Error while connecting to PostgreSQL:", error)
        return None