from database1 import DataBase
class Book:
    def __init__(self, title, autor, year):
        self.title = title
        self.autor = autor
        self.year = year


class BookService:
    def __init__(self, db_name="library.db"):
        self.db = DataBase(db_name)

    def add_book1(self, book):
            if self.find_book_by_title(book.title):
                print("Книга с таким названием уже существует")
            else:
                self.db.add_book(book)
                print("Книга успешно добавлена")
    

    def find_book_by_title(self, title):
        book_data = self.db.get_book(title)
        if book_data:
            return Book(title=book_data[1], autor=book_data[2], year=book_data[3])
        return None
    
    def delete_book_by_title(self, title):
        delete=self.find_book_by_title(title)
        if delete:
            self.db.delete_book(title)
        else:
            None

    def update_year(self, title, new_year):
        book = self.find_book_by_title(title)
        if book:
            self.db.update_year(title, new_year) 
            print(f"Год издания {title} обновлён на {new_year}")
        else:
            print("Книга не найдена")

        
    def close(self):
        self.db.close()



book_service = BookService()
def menu():
    while True:
        print("\nМеню: \n1.Добавить книгу \n2.Найти книгу по названию \n3.Обновить год издания книги \n4.Удалить книгу по названию \n5.Выход из программы")

        choice = input("Выберите действие: ")
        if choice == '1':
            book = Book(title=input('Введите название книги:'), autor=input("Введите автора книги:"), year=int(input('Введите год издания книги:')))

            book_service.add_book1(book)
        
        elif choice == '2':
            title = input("Введите название книги для поиска: ")
            find=book_service.find_book_by_title(title)
            if find:
                print('Книга найдена', find.title, find.autor, find.year)
            else:
                print('Такой книги нет')
        
        elif choice == '3':
            title = input("Введите название книги для обновления года издания: ")
            new_year = int(input("Введите новый год издания: "))
            book_service.update_year(title, new_year)
        
        elif choice == '4':
            title = input("Введите название книги для удаления: ")
            book_service.delete_book_by_title(title)
            
    
        elif choice == '5':
            print("Выход из программы.")
            break
        
        else:
            print("Некорректный выбор. Попробуйте снова.")


menu()
