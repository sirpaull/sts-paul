
class Library:
    # initializing the library

    def __init__(self):
        self.books = []


    def add_book(self,title,author):
        # adding a new book to the library
        self.books.append({"Title":title, "Author": author}) 
        print(f"'{title}' by '{author}' has been added.")
        
        # return self.books

    def remove_book(self, title,author):
        # removing a book from the library checking against title and author
        for book in self.books:
            if book["Title"] == title and book["Author"] == author: 
                self.books.remove(book) 
                print(f"'{title}' has been removed.")
                return 
        print(f"'{title}' not found in the library.")


    def search_book(self, search_items):
        result_list = []

        # search for books by title or author name
        for book in self.books:
            if book["Title"].upper() == search_items.upper() or book["Author"].upper() == search_items.upper():
                result_list.append(book)
                # print(f"Search results: '{book['Title']}' by {book['Author']}' ")
                # return
        if result_list:
            for book in result_list:
                print(f"'{book['Title']} by {book['Author']}' ")      
        else:
            print(f"'{search_items}' not found in the library.")

    #display all books
    def display_books(self):
        for book in self.books:
            print(f"{book["Title"]} by {book["Author"]}")

Book = Library()

# Book.add_book("Ananse", "Kwaku Osei")
Book.add_book("Crab", "Kwaku Osei")
Book.add_book("monkeys", "Ola rotimi")
Book.add_book("Ananse", "Kwaku Osei")

# displaying all books in the library
Book.display_books()

# removing a book from the library
Book.remove_book("Ananse", "Kwaku Osei")

# searching for a book by title or author name
Book.search_book("Crab")

def main():
    Book = Library()
    print('\n')
    while True:
        choice = int(input("Choose an option \n 1. Add a Book: \n 2. Remove a Book \n 3. Search for a Book: \n 4. Display All Books \n 5.Exit "))

        if choice == 1:
            print('\n')
            title = input("Enter the book title: ")
            author = input("Enter the author: ")
            Book.add_book(title, author)
            
        elif choice == 2:
            print('\n')
            title = input("Enter the book title to remove: ")
            author = input("Enter the author of the book to remove: ")
            Book.remove_book(title, author)

        elif choice == 3:
            print('\n')
            search_items = input("Enter the title or author to search: ")
            Book.search_book(search_items)

        elif choice == 4:
            print('\n')
            Book.display_books()

        elif choice == 5:
            print('\n')
            print("Exiting the program...")
            break 
        else:
            print("Invalid choice. Please enter a valod option. ")

if __name__=="__main__"   :    #import this whole script and call it in another program
    main()

