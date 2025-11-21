"""Authentication module for librarian login and registration"""
import hashlib
from datetime import date
from database import db


class AuthenticationManager:
    """Handles authentication operations"""
    
    @staticmethod
    def hash_password(password):
        """Hash password using SHA-256"""
        return hashlib.sha256(password.encode()).hexdigest()
    
    @staticmethod
    def login(username, password):
        """
        Authenticate librarian login
        Returns: tuple (success: bool, user_data: dict or error_message: str)
        """
        if not username or not password:
            return False, "Please enter both username and password"
        
        hashed_password = AuthenticationManager.hash_password(password)
        query = "SELECT * FROM librarian WHERE username = %s AND password = %s"
        result = db.execute_query_single(query, (username, hashed_password))
        
        if result:
            return True, result
        else:
            return False, "Invalid username or password"
    
    @staticmethod
    def register(first_name, last_name, email, username, password, confirm_password):
        """
        Register new librarian
        Returns: tuple (success: bool, message: str)
        """
        # Validation
        if not all([first_name, last_name, email, username, password, confirm_password]):
            return False, "Please fill in all fields"
        
        if password != confirm_password:
            return False, "Passwords do not match"
        
        if len(password) < 6:
            return False, "Password must be at least 6 characters"
        
        # Insert to database
        hashed_password = AuthenticationManager.hash_password(password)
        query = """
            INSERT INTO librarian (first_name, last_name, email, username, password, hire_date)
            VALUES (%s, %s, %s, %s, %s, %s)
        """
        values = (first_name, last_name, email, username, hashed_password, date.today())
        
        success = db.insert_record(query, values)
        if success:
            return True, "Registration successful! You can now login."
        else:
            return False, "Username or email already exists"
