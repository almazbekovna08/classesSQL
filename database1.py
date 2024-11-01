import sqlite3

class DataBase:
    def __init__(self, db_name="library.db"):
        self.connection=sqlite3.connect(db_name)
        self.cursor=self.connection.cursor()
        self.create_table()

    def create_table(self):
        self.cursor.execute("""
                        CREATE TABLE IF NOT EXISTS books(
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        title TEXT NOT NULL,
                        autor TEXT NOT NULL,
                        year INTEGER NOT NULL
    )
""")
        self.connection.commit()



    def add_book(self, book):
        self.cursor.execute("""
                            INSERT INTO books
                            (title, autor, year) 
                            VALUES(?, ?, ?)""", (book.title, book.autor, book.year))
        self.connection.commit()

    def get_book(self, title):
        self.cursor.execute("SELECT * FROM books WHERE title=?", (title,))
        return self.cursor.fetchone()
    
    def update_year(self, title, new_year):
        self.cursor.execute("""
                        UPDATE books  
                        SET year = ? 
                        WHERE title = ?""", (title, new_year))
        
        self.connection.commit()


    def delete_book(self, title):
        self.cursor.execute("DELETE FROM books WHERE title=?", (title,))

        self.connection.commit()
        print(f'Книга с названием {title} была удалена')
