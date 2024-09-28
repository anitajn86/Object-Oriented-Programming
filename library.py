class Book:
    def __init__(self,title,author,isbn):
        self.title=title
        self.author=author
        self.isbn=isbn
        self.status="available"
        print(f"{self.title} by {self.author} (IsbN{self.isbn}) is {self.status}")

class Member:
    def __init__(self,name,member_id):
        self.name=name
        self.member_id=member_id
        self.borrowed_books=[]

    def borrowBook(self,book):
        if book.status=="available":
            self.borrowed_books=self.borrowed_books.append(book)
            book.status="borrowwed"
            print(f"{self.name} has borrowed {book.title}")
        else:
            print(f"Sorry, {book.title} is already borrowed")

