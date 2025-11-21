import tkinter as tk


class Dashboard:
    
    def __init__(self, root, on_logout, on_books=None, on_students=None):
        self.root = root
        self.on_logout = on_logout
        self.on_books = on_books or (lambda: print("Books module not yet implemented"))
        self.on_students = on_students or (lambda: print("Students module not yet implemented"))
    
    def show(self, user_data):
        """Display dashboard page"""
        self.clear_frame()
        
        # Main frame
        main_frame = tk.Frame(self.root, bg='#2c3e50')
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Welcome message
        welcome_label = tk.Label(
            main_frame,
            text=f"Welcome, {user_data['first_name']} {user_data['last_name']}!",
            font=('Arial', 18, 'bold'),
            bg='#2c3e50',
            fg='white'
        )
        welcome_label.pack(pady=40)
        
        info_label = tk.Label(
            main_frame,
            text="Dashboard - Book Cataloging and Borrowing System",
            font=('Arial', 14),
            bg='#2c3e50',
            fg='#ecf0f1'
        )
        info_label.pack(pady=20)
        
        # Buttons frame for books and students
        buttons_frame = tk.Frame(main_frame, bg='#2c3e50')
        buttons_frame.pack(pady=20)
        
        # Book button
        book_btn = tk.Button(
            buttons_frame,
            text="books",
            font=('Arial', 12, 'bold'),
            bg='#3498db',
            fg='white',
            cursor='hand2',
            width=15,
            command=self.on_books
        )
        book_btn.pack(pady=10)
    
        # Student Button    
        student_btn = tk.Button(
            buttons_frame,
            text="students",
            font=('Arial', 12, 'bold'),
            bg='#27ae60',
            fg='white',
            cursor='hand2',
            width=15,
            command=self.on_students
        )
        student_btn.pack(pady=10)

        
        # Bottom frame for logout button
        bottom_frame = tk.Frame(main_frame, bg='#2c3e50')
        bottom_frame.pack(side=tk.BOTTOM, fill=tk.X, padx=20, pady=20)

        logout_btn = tk.Button(
            bottom_frame,
            text="Logout",
            font=('Arial', 10, 'bold'),
            bg='#e74c3c',
            fg='white',
            cursor='hand2',
            width=10,
            command=self.on_logout
        )
        logout_btn.pack(side=tk.RIGHT)


    def clear_frame(self):
        """Clear all widgets from the frame"""
        for widget in self.root.winfo_children():
            widget.destroy()
