"""Student management module"""
import tkinter as tk
from tkinter import ttk, messagebox
from database import db


class StudentWindow:
    """Displays and manages student table"""
    
    def __init__(self, root):
        self.root = root
        self.root.title("Student Management")
        self.root.geometry("1000x600")
        
        # Configure style
        style = ttk.Style()
        style.theme_use('clam')
        
        self.create_widgets()
        self.load_students()
    
    def create_widgets(self):
        """Create GUI widgets"""
        # Main frame
        main_frame = ttk.Frame(self.root, padding=10)
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Title
        title_label = ttk.Label(main_frame, text="Student Management", font=('Arial', 18, 'bold'))
        title_label.pack(pady=10)
        
        # Button frame
        button_frame = ttk.Frame(main_frame)
        button_frame.pack(fill=tk.X, pady=10)
        
        add_btn = ttk.Button(button_frame, text="Add Student", command=self.add_student)
        add_btn.pack(side=tk.LEFT, padx=5)
        
        refresh_btn = ttk.Button(button_frame, text="Refresh", command=self.load_students)
        refresh_btn.pack(side=tk.LEFT, padx=5)
        
        delete_btn = ttk.Button(button_frame, text="Delete Student", command=self.delete_student)
        delete_btn.pack(side=tk.LEFT, padx=5)


        # Table frame
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
            columns=('ID', 'First Name', 'Last Name', 'Email', 'Phone', 'Registration Date'),
            height=20,
            yscrollcommand=vsb.set,
            xscrollcommand=hsb.set
        )
        
        vsb.config(command=self.tree.yview)
        hsb.config(command=self.tree.xview)
        
        # Define headings
        self.tree.column('#0', width=0, stretch=tk.NO)
        self.tree.column('ID', anchor=tk.CENTER, width=50)
        self.tree.column('First Name', anchor=tk.W, width=120)
        self.tree.column('Last Name', anchor=tk.W, width=120)
        self.tree.column('Email', anchor=tk.W, width=150)
        self.tree.column('Phone', anchor=tk.W, width=100)
        self.tree.column('Registration Date', anchor=tk.CENTER, width=120)
        
        self.tree.heading('#0', text='', anchor=tk.W)
        self.tree.heading('ID', text='ID', anchor=tk.CENTER)
        self.tree.heading('First Name', text='First Name', anchor=tk.W)
        self.tree.heading('Last Name', text='Last Name', anchor=tk.W)
        self.tree.heading('Email', text='Email', anchor=tk.W)
        self.tree.heading('Phone', text='Phone', anchor=tk.W)
        self.tree.heading('Registration Date', text='Registration Date', anchor=tk.CENTER)
        
        # Add alternating row colors
        self.tree.tag_configure('oddrow', background='#f0f0f0')
        self.tree.tag_configure('evenrow', background='white')
        
        self.tree.pack(fill=tk.BOTH, expand=True)
    
    def load_students(self):
        """Load students from database and display in table"""
        # Clear existing items
        for item in self.tree.get_children():
            self.tree.delete(item)
        
        # Query database
        query = "SELECT student_id, first_name, last_name, email, phone, registration_date FROM student"
        students = db.execute_query(query)
        
        if students:
            for idx, student in enumerate(students):
                tag = 'evenrow' if idx % 2 == 0 else 'oddrow'
                self.tree.insert(
                    '',
                    tk.END,
                    values=(
                        student['student_id'],
                        student['first_name'],
                        student['last_name'],
                        student['email'],
                        student['phone'] or 'N/A',
                        student['registration_date']
                    ),
                    tags=(tag,)
                )
            messagebox.showinfo("Success", f"Loaded {len(students)} students")
        else:
            messagebox.showinfo("Info", "No students found in database")
    
    def add_student(self):
        """Add a new student"""
        messagebox.showinfo("Info", "Add Student feature - Coming soon!")
    
    def delete_student(self):
        """Delete selected student"""
        selected = self.tree.selection()
        if not selected:
            messagebox.showwarning("Warning", "Please select a student to delete")
            return
        
        messagebox.showinfo("Info", "Delete Student feature - Coming soon!")


def main():
    """Main entry point"""
    root = tk.Tk()
    app = StudentWindow(root)
    root.mainloop()


if __name__ == "__main__":
    main()
