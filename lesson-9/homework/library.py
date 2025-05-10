


class BookNotFoundException(Exception):
    pass

class BookAlreadyBorrowedException(Exception):
    pass

class MemberLimitExceededException(Exception):
    pass



class Book:
    def __init__(self, title, author):
        self.title=title
        self.author=author
        self.is_borrowed=False
    def __str__(self):
        return f'{self.title} by{ self.author}'

class Member:
    def __init__(self, name):
        self.name = name
        self.borrowed_books = []

    def borrow_book(self, book):
        if book in self.borrowed_books:
            raise BookAlreadyBorrowedException(f'{self.name} already borrowed{book}!')
        elif len(self.borrowed_books)>=3:
            raise MemberLimitExceededException(f"{self.name} cannot borrow more than 3 books.")
        if book.is_borrowed:
            raise BookAlreadyBorrowedException(f'{self.name} already borrowed{book}!')
        self.borrowed_books.append(book)
        book.is_borrowed=True
        print(f'{self.name} just borrowed {book} now')

            

    def return_book(self, book):
            if book in self.borrowed_books:
                self.borrowed_books.remove(book)
                book.is_borrowed=False
                print(f'{self.name} returned {book} book')
                
            else: 
                print(f'{self.name} did not borrow book')    

class Library:
    
    def __init__(self):
        self.books = {}
        self.members = {}

    
    def add_book(self, title, author):
       book=Book(title, author)
       self.books[title]=book
       print(f"Book '{book}' is added to library")

        
    def add_member(self, name):
        member=Member(name)
        self.members[name]=member
        print(f'{member} is added to membership')


    def borrow_book(self, member_name, book_title):
        if member_name not in self.members:
            raise Exception('Member not found')
        
        if book_title not in self.books:
            raise BookNotFoundException('Book not found')
        member=self.members[member_name]
        book=self.books[book_title]
        member.borrow_book(book)    
     
        
    def return_book(self, member_name, book_title):
        if member_name not in self.members:
            raise Exception('Member not found')
        if book_title not in self.books:
            raise BookNotFoundException('Book not found')
        member=self.members[member_name]
        book=self.books[book_title]
        member.return_book(book)



if __name__=='__main__':
    library=Library()
    def __init__(self):
        self.member_list = {}  

while True:
        print("\n=== Samadjon Library ===")
        print("1. Add Book")
        print("2. Add Member")
        print("3. Borrow Book")
        print("4. Return Book")
        print("5. Exit")
            

        choice=int(input("Enter your choice: "))

        if choice==1:
            title=input('Enter a title: ')
            author=input('Enter a author: ')
            library.add_book(title, author)
        elif choice==2:
            name=input('Enter your name')
            library.add_member(name)


        elif choice==3:
            name=input('Enter your name')
            title=input('Enter name of title: ') 
            try:
                library.borrow_book(name, title)
            except Exception as e:
                print(f'Errow: {e}')    
        elif choice==4:
            name=input('Enter your name')
            title=input('Enter name of title: ') 
            try:
                library.return_book(name, title)
            except Exception as e:
                print(f'Errow: {e}')
        elif choice==5:
            print('Goodbye. Have good one')
            break
        else:
            print("Invalid choice!!!")
                   








