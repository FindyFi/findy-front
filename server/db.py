import psycopg2
import os

# Variables to store the connection and DatabaseManager instance
conn = None
cursor = None

def get_db_manager():
    global conn    
    global cursor

    if conn is None:
        # Connect to the PostgreSQL database
        conn = psycopg2.connect(
                host=os.getenv('DB_HOST', 'localhost'),
                database=os.getenv('DB_NAME', 'findytestfrontdb'),
                user=os.getenv("DB_USER", "postgres"),
                password=os.getenv("DB_PASSWORD", "")
            )        

        # Create a cursor object to interact with the database
        cursor = conn.cursor()        

        print("Connected to the PostgreSQL database.")
    
    return cursor