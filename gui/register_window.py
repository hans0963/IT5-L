"""Registration window for new librarian accounts"""
import tkinter as tk
from tkinter import ttk, messagebox
from auth import AuthenticationManager


class RegisterWindow:
    """Displays and handles registration page"""
    
    def __init__(self, root, on_register_success, show_login_callback):
        self.root = root
        self.on_register_success = on_register_success
        self.show_login_callback = show_login_callback
        self.reg_firstname = None
        self.reg_lastname = None
        self.reg_email = None
        self.reg_username = None
        self.reg_password = None
        self.reg_confirm_password = None
    
    def show(self):
        """Display registration page"""
        self.clear_frame()
        
        # Main frame
        main_frame = tk.Frame(self.root, bg='#2c3e50')
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Title
        title_label = tk.Label(
            main_frame, 
            text="Librarian Registration", 
            font=('Arial', 18, 'bold'),
            bg='#2c3e50',
            fg='white'
        )
        title_label.pack(pady=20)
        
        # Registration form frame
        form_frame = tk.Frame(main_frame, bg='#34495e', padx=40, pady=30)
        form_frame.pack(pady=10, padx=50)
        
        # First Name
        tk.Label(form_frame, text="First Name:", font=('Arial', 10), bg='#34495e', fg='white').grid(row=0, column=0, sticky='w', pady=5)
        self.reg_firstname = ttk.Entry(form_frame, font=('Arial', 10), width=25)
        self.reg_firstname.grid(row=1, column=0, pady=(0, 10))
        
        # Last Name
        tk.Label(form_frame, text="Last Name:", font=('Arial', 10), bg='#34495e', fg='white').grid(row=2, column=0, sticky='w', pady=5)
        self.reg_lastname = ttk.Entry(form_frame, font=('Arial', 10), width=25)
        self.reg_lastname.grid(row=3, column=0, pady=(0, 10))
        
        # Email
        tk.Label(form_frame, text="Email:", font=('Arial', 10), bg='#34495e', fg='white').grid(row=4, column=0, sticky='w', pady=5)
        self.reg_email = ttk.Entry(form_frame, font=('Arial', 10), width=25)
        self.reg_email.grid(row=5, column=0, pady=(0, 10))
        
        # Username
        tk.Label(form_frame, text="Username:", font=('Arial', 10), bg='#34495e', fg='white').grid(row=6, column=0, sticky='w', pady=5)
        self.reg_username = ttk.Entry(form_frame, font=('Arial', 10), width=25)
        self.reg_username.grid(row=7, column=0, pady=(0, 10))
        
        # Password
        tk.Label(form_frame, text="Password:", font=('Arial', 10), bg='#34495e', fg='white').grid(row=8, column=0, sticky='w', pady=5)
        self.reg_password = ttk.Entry(form_frame, font=('Arial', 10), width=25, show='*')
        self.reg_password.grid(row=9, column=0, pady=(0, 10))
        
        # Confirm Password
        tk.Label(form_frame, text="Confirm Password:", font=('Arial', 10), bg='#34495e', fg='white').grid(row=10, column=0, sticky='w', pady=5)
        self.reg_confirm_password = ttk.Entry(form_frame, font=('Arial', 10), width=25, show='*')
        self.reg_confirm_password.grid(row=11, column=0, pady=(0, 15))
        
        # Buttons frame
        btn_frame = tk.Frame(form_frame, bg='#34495e')
        btn_frame.grid(row=12, column=0, pady=10)
        
        # Register button
        register_btn = tk.Button(
            btn_frame,
            text="Register",
            font=('Arial', 11, 'bold'),
            bg='#27ae60',
            fg='white',
            cursor='hand2',
            width=12,
            command=self.register
        )
        register_btn.pack(side=tk.LEFT, padx=5)
        
        # Back button
        back_btn = tk.Button(
            btn_frame,
            text="Back to Login",
            font=('Arial', 11),
            bg='#95a5a6',
            fg='white',
            cursor='hand2',
            width=12,
            command=self.show_login_callback
        )
        back_btn.pack(side=tk.LEFT, padx=5)
    
    def register(self):
        """Handle librarian registration"""
        first_name = self.reg_firstname.get().strip()
        last_name = self.reg_lastname.get().strip()
        email = self.reg_email.get().strip()
        username = self.reg_username.get().strip()
        password = self.reg_password.get().strip()
        confirm_password = self.reg_confirm_password.get().strip()
        
        success, message = AuthenticationManager.register(
            first_name, last_name, email, username, password, confirm_password
        )
        
        if success:
            messagebox.showinfo("Success", message)
            self.on_register_success()
        else:
            messagebox.showerror("Registration Error", message)
    
    def clear_frame(self):
        """Clear all widgets from the frame"""
        for widget in self.root.winfo_children():
            widget.destroy()
