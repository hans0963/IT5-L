"""Database schema initialization"""
from database import db


def create_tables():
    """Create all necessary database tables"""
    
    # Create librarian table
    librarian_table = """
    CREATE TABLE IF NOT EXISTS librarian (
        librarian_id INT AUTO_INCREMENT PRIMARY KEY,
        first_name VARCHAR(100) NOT NULL,
        last_name VARCHAR(100) NOT NULL,
        email VARCHAR(100) UNIQUE NOT NULL,
        username VARCHAR(50) UNIQUE NOT NULL,
        password VARCHAR(255) NOT NULL,
        hire_date DATE NOT NULL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    """
    
    # Create book table
    book_table = """
    CREATE TABLE IF NOT EXISTS book (
        book_id INT AUTO_INCREMENT PRIMARY KEY,
        isbn VARCHAR(20) UNIQUE NOT NULL,
        title VARCHAR(255) NOT NULL,
        author VARCHAR(100) NOT NULL,
        publisher VARCHAR(100),
        publication_year INT,
        category VARCHAR(50),
        location VARCHAR(100),
        status VARCHAR(50) DEFAULT 'available',
        date_added DATE,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    """
    
    # Create student table
    student_table = """
    CREATE TABLE IF NOT EXISTS student (
        student_id INT AUTO_INCREMENT PRIMARY KEY,
        first_name VARCHAR(100) NOT NULL,
        last_name VARCHAR(100) NOT NULL,
        email VARCHAR(100) UNIQUE NOT NULL,
        phone VARCHAR(15),
        registration_date DATE NOT NULL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    """
    
    # Create borrow_transaction table
    borrow_transaction_table = """
    CREATE TABLE IF NOT EXISTS borrow_transaction (
        transaction_id INT AUTO_INCREMENT PRIMARY KEY,
        book_id INT NOT NULL,
        student_id INT NOT NULL,
        librarian_id INT NOT NULL,
        borrow_date DATE NOT NULL,
        due_date DATE NOT NULL,
        return_date DATE,
        status VARCHAR(50) DEFAULT 'borrowed',
        is_overdue BOOLEAN DEFAULT FALSE,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (book_id) REFERENCES book(book_id),
        FOREIGN KEY (student_id) REFERENCES student(student_id),
        FOREIGN KEY (librarian_id) REFERENCES librarian(librarian_id)
    )
    """
    
    # Create reservation table
    reservation_table = """
    CREATE TABLE IF NOT EXISTS reservation (
        reservation_id INT AUTO_INCREMENT PRIMARY KEY,
        book_id INT NOT NULL,
        student_id INT NOT NULL,
        reservation_date DATE NOT NULL,
        status VARCHAR(50) DEFAULT 'pending',
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (book_id) REFERENCES book(book_id),
        FOREIGN KEY (student_id) REFERENCES student(student_id)
    )
    """
    
    # Create fine table
    fine_table = """
    CREATE TABLE IF NOT EXISTS fine (
        fine_id INT AUTO_INCREMENT PRIMARY KEY,
        transaction_id INT NOT NULL,
        fine_amount DECIMAL(10, 2) NOT NULL,
        calculated_date DATE NOT NULL,
        paid_date DATE,
        payment_status VARCHAR(50) DEFAULT 'unpaid',
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (transaction_id) REFERENCES borrow_transaction(transaction_id)
    )
    """
    
    # Create catalog table
    catalog_table = """
    CREATE TABLE IF NOT EXISTS catalog (
        catalog_id INT AUTO_INCREMENT PRIMARY KEY,
        book_id INT NOT NULL,
        librarian_id INT NOT NULL,
        cataloged_date DATE NOT NULL,
        catalog_status VARCHAR(50) DEFAULT 'active',
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (book_id) REFERENCES book(book_id),
        FOREIGN KEY (librarian_id) REFERENCES librarian(librarian_id)
    )
    """
    
    tables = [
        ("librarian", librarian_table),
        ("book", book_table),
        ("student", student_table),
        ("borrow_transaction", borrow_transaction_table),
        ("reservation", reservation_table),
        ("fine", fine_table),
        ("catalog", catalog_table)
    ]
    
    try:
        cursor = db.get_cursor()
        if cursor:
            for table_name, table_sql in tables:
                cursor.execute(table_sql)
                print(f"✓ {table_name} table created successfully!")
            
            db.connection.commit()
            cursor.close()
            print("\n✓ All tables created successfully!")
            return True
    except Exception as e:
        print(f"✗ Error creating tables: {e}")
        return False


if __name__ == "__main__":
    db.connect()
    create_tables()
    db.close()
