import tkinter as tk
from tkinter import ttk, messagebox
from database import db


class BookWindow:

    def __init__(self, root):
        self.root = root
        self.root.title("Book Management")
        self.root.geometry("1000x600")

        style = ttk.style()
        style.theme_use("clam")

        self.create_widgets()
        self.load_books()

    def create_widgets(self):
        
        # Main Frame
        main_frame = ttk.Frame(self.root, padding=10)
        main_frame.pack(fill=tk.BOTH, expand=True)

        # Title
        title_label = ttk.Label(main_frame, text="Book Mangement", font=('Arial', 18, 'bold'))
        title_label.pack(pady=10)

        # Button Frame
        button_frame = ttk.Frame(main_frame)
        button_frame.pack(fill=tk.X, pady=10)

        add_btn = ttk.Button(button_frame, text="Add Book", command=self.add_book)
        add_btn.pack(side=tk.LEFT, padx=5)

        refresh_btn = ttk.Button(button_frame, text="Refresh", command=self.load_students)
        refresh_btn.pack(side=tk.LEFT, padx=5)

        delete_btn = ttk.Button(button_frame, text="Delete Book", command=self.delete_book)
        delete_btn.pack(side=tk.LEFT, padx=5)

        # Table Frame
        table_frame = ttk.Frame(main_frame)
        table_frame.pack(fill=tk.BOTH, expand=True, pady=10)

        # Scrollbars
        vsb = ttk.Scrollbar(table_frame, orient=tk.VERTICAL)
        vsb.pack(side=tk.RIGHT, fill=tk.Y)

        hsb = ttk.Scrollbar(table_frame, orient=tk.HORIZONTAL)
        hsb.pack(side=tk.BOTTOM, fill=tk.X)

        # Treeview
        self.tree = ttk.Treeview(
            table_frame,
            columns = ('ID', 'Title', 'Author', 'ISBN', 'Publisher', 'Year Published', 'Category', 'Copies Available'),
            height = 20,
            yscrollcommand=vsb.set,
            xscrollcommand=hsb.set
        )

        vsb.config(command=self.tree.yview)
        hsb.config(command=self.tree.xview)

        # Define headings
        self.tree.column('#0', width=0, stretch=tk.NO)
        self.tree.column('ID', anchor=tk.CENTER, width=50)
        self.tree.column('Title', anchor=tk.W, width=200)
        self.tree.column('Author', anchor=tk.W, width=150)
        self.tree.column('ISBN', anchor=tk.W, width=120)
        self.tree.column('Publisher', anchor=tk.W, width=150)
        self.tree.column('Year Published', anchor=tk.CENTER, width=100)
        self.tree.column('Category', anchor=tk.W, width=100)
        self.tree.column('Copies Available', anchor=tk.CENTER, width=120)

        self.tree.heading('#0', text='', anchor=tk.W)
        self.tree.heading('ID', text='ID', anchor=tk.CENTER)
        self.tree.heading('Title', text='Title', anchor=tk.W)
        self.tree.heading('Author', text='Author', anchor=tk.W)
        self.tree.heading('ISBN', text='ISBN', anchor=tk.W)
        self.tree.heading('Publisher', text='Publisher', anchor=tk.W)
        self.tree.heading('Year Published', text='Year Published', anchor=tk.CENTER)
        self.tree.heading('Category', text='Category', anchor=tk.W)
        self.tree.heading('Copies Available', text='Copies Available', anchor=tk.CENTER)

        # Add alternating row colors