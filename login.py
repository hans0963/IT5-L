"""Main entry point for Library Management System"""
import tkinter as tk
from tkinter import ttk
from database import db
from gui.login_window import LoginWindow
from gui.register_window import RegisterWindow
from gui.dashboard import Dashboard



class LibraryLoginSystem:
    """Main application controller"""
    
    def __init__(self, root):
        self.root = root
        self.root.title("SCHOOL LIBRARY BOOK CATALOGING AND BORROWING SYSTEM")
        self.root.geometry("500x600")
        self.root.resizable(False, False)
        
        # Configure style
        style = ttk.Style()
        style.theme_use('clam')
        
        # Initialize database
        db.connect()
        
        # Initialize windows
        self.login_window = LoginWindow(
            self.root,
            on_login_success=self.handle_login_success,
            show_register_callback=self.show_register
        )
        
        self.register_window = RegisterWindow(
            self.root,
            on_register_success=self.show_login,
            show_login_callback=self.show_login
        )
        
        self.dashboard = Dashboard(
            self.root,
            on_logout=self.show_login,
            on_books=self.on_books,
            on_students=self.on_students
        )
        
        # Show login page
        self.show_login()
    
    def show_login(self):
        """Display login page"""
        self.login_window.show()
    
    def show_register(self):
        """Display registration page"""
        self.register_window.show()
    
    def handle_login_success(self, user_data):
        """Handle successful login"""
        self.dashboard.show(user_data)
    
    def on_books(self):
        """Handle books button click"""
        import books
        books.main()
    
    def on_students(self):
        """Handle students button click"""
        import students
        students.main()

    
    def __del__(self):
        """Close database connection when application closes"""
        db.close()


def main():
    root = tk.Tk()
    app = LibraryLoginSystem(root)
    root.mainloop()


if __name__ == "__main__":
    main()