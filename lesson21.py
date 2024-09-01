import psycopg2
from psycopg2 import OperationalError, sql
import os
from dotenv import load_dotenv
from pathlib import Path

load_dotenv()  # Load environment variables from.env file


# print("CHULA",os.getenv('CHULA'))


class Library:
    def __init__(self):
        self.connect_to_db()

    def connect_to_db(self):
        try:
            self.conn = psycopg2.connect(
            host=os.getenv('HOSTNAME'),
            database=os.getenv('DATABASE'),
            user=os.getenv('USER'),
            password=os.getenv('PASSWORD'),
            port=os.getenv('PORT')
            )
            print("Connected to the database")
            return self.conn
        except OperationalError as e:
            print(f"Unable to connect to the database: {e}")
#conn = connect_to_db()            
#library = Library()


    def add_book(self, title, author, year, genre):
        cursor = self.conn.cursor()
        cursor.execute(
            "INSERT INTO book (title, author, year_published, genre) VALUES (%s, %s, %s, %s)",
            (title, author, year, genre)
        )
        self.conn.commit()
        cursor.close()
        print("Book added successfully")
    
#add1 = library()
#add1.add_book("To kill two birds"

    def search_books(self,search_term):
        cursor = self.conn.cursor()
        cursor.execute(
            "SELECT title, author FROM book WHERE title = %s OR author = %s",
            (search_term.lower(), search_term.lower())
        )
        results = cursor.fetchall()


        # Destructuring
        if results:
            for title, author in results:
                print(f"{title} by {author}")
        else:
            print(f"'{search_term}' not found in the library.")
        # cursor.close()

    def remove_book(self,title):
        cursor = self.conn.cursor()
        cursor.execute(
            "DELETE FROM book WHERE title = %s",
            (title,) #single element in a tuple add a , 
        )
        self.conn.commit()
        cursor.close()
        print("Book removed successfully")

    def display_books(self):
        cursor = self.conn.cursor()
        cursor.execute(
            "SELECT * FROM book"
        )
        results = cursor.fetchall()
        
        for title, author, year_published, genre in results:
            print(f"{title} by {author} published by {year_published}, {genre}")
        cursor.close()
        
def main():
    library = Library()
    while True:
        try:
            print("\nChoose an option:")
            print("1. Add a book")
            print("2. Search for a book")
            print("3. Remove a book")
            print("4. Display all books")
            print("5. Exit")
        
            choice = int(input("Enter your choice: "))
            
            if choice == 1:
                title = input("Enter the title of the book: ")
                author = input("Enter the author of the book: ")
                year = int(input("Enter the year of publication: "))
                genre = input("Enter the genre of the book: ")
                library.add_book(title, author, year, genre)
                
            elif choice == 2:
                search_term = input("Enter the title or author of the book you want to search for: ")
                library.search_books(search_term)
                
            elif choice == 3:
                title = input("Enter the title of the book you want to search for: ")
                library.remove_book(title)

            elif choice == 4:
                library.display_books()
                
            elif choice == 5:
                print("Exiting the program...")
                break
            
            else:
                print("Invalid choice. Please try again.")
        except ValueError as e:
            print("Invalid entry. Try again.")
if __name__ == "__main__":
    main()

            

# library = Library()
#test.connect_to_db
    

