class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.availability_status = True

    def display_details(self):
        print(f"Title: {self.title}, Author: {self.author}, ISBN: {self.isbn}, Availability: {'Available' if self.availability_status else 'Not Available'}")

    def update_availability(self, status):
        self.availability_status = status


class User:
    def __init__(self, user_id, name):
        self.user_id = user_id
        self.name = name
        self.books_borrowed = []

    def display_details(self):
        print(f"User ID: {self.user_id}, Name: {self.name}")

    def borrow_book(self, book):
        if book.availability_status:
            self.books_borrowed.append(book)
            book.update_availability(False)
            print(f"{self.name} borrowed '{book.title}' successfully.")
        else:
            print(f"Sorry, '{book.title}' is not available for borrowing.")

    def return_book(self, book):
        if book in self.books_borrowed:
            self.books_borrowed.remove(book)
            book.update_availability(True)
            print(f"{self.name} returned '{book.title}' successfully.")
        else:
            print(f"You did not borrow '{book.title}'. Cannot return.")

class Library:
    def __init__(self):
        self.books = []
        self.users = []
        self.transactions = []

    def add_book(self, book):
        self.books.append(book)
        print(f"Book '{book.title}' added to the library.")

    def register_user(self, user):
        self.users.append(user)
        print(f"User '{user.name}' registered successfully.")

    def borrow_book(self, user, book):
        if user in self.users and book in self.books:
            user.borrow_book(book)
            transaction = f"{user.name} borrowed '{book.title}'."
            self.transactions.append(transaction)
            print(transaction)
        else:
            print("Invalid user or book. Cannot perform the transaction.")

    def return_book(self, user, book):
        if user in self.users and book in self.books:
            user.return_book(book)
            transaction = f"{user.name} returned '{book.title}'."
            self.transactions.append(transaction)
            print(transaction)
        else:
            print("Invalid user or book. Cannot perform the transaction.")

    def generate_transaction_report(self):
        print("\nTransaction Report:")
        for transaction in self.transactions:
            print(transaction)