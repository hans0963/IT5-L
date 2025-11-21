"""Database connection and operations module"""
import mysql.connector
from mysql.connector import Error
from config import DB_CONFIG


class DatabaseConnection:
    """Handles MySQL database connections"""
    
    def __init__(self):
        self.connection = None
    
    def connect(self):
        """Connect to MySQL database"""
        try:
            self.connection = mysql.connector.connect(**DB_CONFIG)
            if self.connection.is_connected():
                print("Successfully connected to database")
                return True
        except Error as e:
            print(f"Error connecting to database: {e}")
            return False
    
    def is_connected(self):
        """Check if connected to database"""
        return self.connection and self.connection.is_connected()
    
    def get_cursor(self, dictionary=False):
        """Get a database cursor"""
        if self.is_connected():
            return self.connection.cursor(dictionary=dictionary)
        return None
    
    def execute_query(self, query, values=None):
        """Execute a query and return results"""
        cursor = self.get_cursor(dictionary=True)
        if cursor:
            try:
                cursor.execute(query, values)
                return cursor.fetchall()
            except Error as e:
                print(f"Query execution error: {e}")
                return None
            finally:
                cursor.close()
        return None
    
    def execute_query_single(self, query, values=None):
        """Execute a query and return single result"""
        cursor = self.get_cursor(dictionary=True)
        if cursor:
            try:
                cursor.execute(query, values)
                return cursor.fetchone()
            except Error as e:
                print(f"Query execution error: {e}")
                return None
            finally:
                cursor.close()
        return None
    
    def insert_record(self, query, values):
        """Insert a record and commit"""
        cursor = self.get_cursor()
        if cursor:
            try:
                cursor.execute(query, values)
                self.connection.commit()
                print("Record inserted successfully")
                return True
            except mysql.connector.IntegrityError as e:
                print(f"Integrity error: {e}")
                return False
            except Error as e:
                print(f"Insert error: {e}")
                return False
            finally:
                cursor.close()
        return False
    
    def close(self):
        """Close database connection"""
        if self.connection and self.connection.is_connected():
            self.connection.close()
            print("Database connection closed")


# Global database instance
db = DatabaseConnection()
