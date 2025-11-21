"""Login window for librarian authentication"""
import tkinter as tk
from tkinter import ttk, messagebox
from auth import AuthenticationManager


class LoginWindow:
    """Displays and handles login page"""
    
    def __init__(self, root, on_login_success, show_register_callback):
        self.root = root
        self.on_login_success = on_login_success
        self.show_register_callback = show_register_callback
        self.username_entry = None
        self.password_entry = None
    
    def show(self):
        """Display login page"""
        self.clear_frame()
        
        # Main frame
        main_frame = tk.Frame(self.root, bg='#2c3e50')
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Title
        title_label = tk.Label(
            main_frame, 
            text="Library Management System", 
            font=('Arial', 20, 'bold'),
            bg='#2c3e50',
            fg='white'
        )
        title_label.pack(pady=30)
        
        subtitle_label = tk.Label(
            main_frame, 
            text="Librarian Login", 
            font=('Arial', 14),
            bg='#2c3e50',
            fg='#ecf0f1'
        )
        subtitle_label.pack(pady=10)
        
        # Login form frame
        form_frame = tk.Frame(main_frame, bg='#34495e', padx=40, pady=30)
        form_frame.pack(pady=20, padx=50)
        
        # Username
        username_label = tk.Label(
            form_frame, 
            text="Username:", 
            font=('Arial', 11),
            bg='#34495e',
            fg='white'
        )
        username_label.grid(row=0, column=0, sticky='w', pady=10)
        
        self.username_entry = ttk.Entry(form_frame, font=('Arial', 11), width=25)
        self.username_entry.grid(row=1, column=0, pady=(0, 15))
        
        # Password
        password_label = tk.Label(
            form_frame, 
            text="Password:", 
            font=('Arial', 11),
            bg='#34495e',
            fg='white'
        )
        password_label.grid(row=2, column=0, sticky='w', pady=10)
        
        self.password_entry = ttk.Entry(form_frame, font=('Arial', 11), width=25, show='*')
        self.password_entry.grid(row=3, column=0, pady=(0, 20))
        
        # Login button
        login_btn = tk.Button(
            form_frame,
            text="Login",
            font=('Arial', 12, 'bold'),
            bg='#27ae60',
            fg='white',
            cursor='hand2',
            width=20,
            command=self.login
        )
        login_btn.grid(row=4, column=0, pady=10)
        
        # Register link
        register_frame = tk.Frame(main_frame, bg='#2c3e50')
        register_frame.pack(pady=20)
        
        register_label = tk.Label(
            register_frame,
            text="Don't have an account?",
            font=('Arial', 10),
            bg='#2c3e50',
            fg='#ecf0f1'
        )
        register_label.pack(side=tk.LEFT)
        
        register_btn = tk.Button(
            register_frame,
            text="Register Here",
            font=('Arial', 10, 'bold'),
            bg='#2c3e50',
            fg='#3498db',
            border=0,
            cursor='hand2',
            command=self.show_register_callback
        )
        register_btn.pack(side=tk.LEFT, padx=5)
        
        # Bind Enter key to login
        self.password_entry.bind('<Return>', lambda e: self.login())
    
    def login(self):
        """Handle login authentication"""
        username = self.username_entry.get().strip()
        password = self.password_entry.get().strip()
        
        success, result = AuthenticationManager.login(username, password)
        
        if success:
            messagebox.showinfo(
                "Login Successful", 
                f"Welcome, {result['first_name']} {result['last_name']}!"
            )
            self.on_login_success(result)
        else:
            messagebox.showerror("Login Failed", result)
    
    def clear_frame(self):
        """Clear all widgets from the frame"""
        for widget in self.root.winfo_children():
            widget.destroy()
