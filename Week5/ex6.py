import datetime
import time
from typing import Any
class Human:
    def __init__(self, name, age, id_number):
        if age < 0:
            raise ValueError("age cannot be negative")
        self.name = name
        self.age = age
        self.id_number = id_number
    def __str__(self):
        return "Human: "+self.name+" with age "+str(self.age) + " and id "+str(self.id_number)
class Library:
    def __init__(self, name):
        self.name = name
        self.items = []
        self.ban_list = set()
    def add_item(self, item):
        if not isinstance(item, LibraryItem):
            raise ValueError("item must be of type LibraryItem")
        self.items.append(item)
        item.library = self
    def add_to_ban_list(self, human):
        if not isinstance(human, Human):
            raise ValueError("human must be of type Human")
        self.ban_list.add(human.id_number)
    def verify_if_banned(self, human):
        if not isinstance(human, Human):
            raise ValueError("human must be of type Human")
        return human.id_number in self.ban_list
    def get_item(self, index):
        if index < 0 or index >= len(self.items):
            raise ValueError("index out of bounds")
        return self.items[index]


class LibraryItem:
    def __init__(self, title, author, year, ):
        self.validate_input(title, author, year)
        self.title = title
        self.author = author
        self.year = year
        self.is_borrowed = False
        self.borrower = None
        self.borrow_date = None
        self.return_date = None
        self.library = None

    def borrow(self, borrower, borrow_date, return_date):
        if not isinstance(borrower, Human):
            raise ValueError("borrower must be of type Human")
        if self.is_borrowed:
            raise ValueError("Item is already borrowed by "+self.borrower.name)
        if borrow_date > return_date:
            raise ValueError("borrow_date cannot be after return_date")
        if self.library.verify_if_banned(borrower):
            print(ValueError("Borrower " + borrower.name+" is banned"))
            return
        self.is_borrowed = True
        self.borrower = borrower
        self.borrow_date = borrow_date
        self.return_date = return_date
        print(self.borrower.name+" borrowed "+self.title+" on "+str(self.borrow_date)+" until "+str(self.return_date))

    def return_item(self):
        if not self.is_borrowed:
            raise ValueError("Item is not borrowed")
        print(self.title+" returned by " + self.borrower.name)
        if datetime.datetime.now() > self.return_date:
            print("Item is returned late")
            self.library.add_to_ban_list(self.borrower) 
        self.is_borrowed = False
        self.borrower = None
        self.borrow_date = None
        self.return_date = None
        

    def check_availability(self):
        if self.is_borrowed:
            print(self.title+" is borrowed by "+self.borrower.name)
        else:
            print(self.title+" is available")
    
    def get_information(self):
        return "Title: "+self.title+" Author: "+self.author +" Year: "+str(self.year)

    def __str__(self):
        return self.get_information()
    
    def validate_input(self, title, author, year):
        if year < 0:
            raise ValueError("year cannot be negative")
        if title == "":
            raise ValueError("title cannot be empty")
        if author == "":
            raise ValueError("author cannot be empty")
    
class Book(LibraryItem):
    def __init__(self, title, author, year, num_of_pages,genre,description):
        super().__init__(title, author, year)
        self.num_of_pages = num_of_pages
        self.genre = genre
        self.description = description
    
    def read_description(self):
        print(self.description)

    def get_information(self):
        return super().get_information()+" Num of pages: "+str(self.num_of_pages) + " Genre: "+self.genre
    
class DVD(LibraryItem):
    def __init__(self, title, author, year, duration,genre,age_restriction):
        super().__init__(title, author, year)
        self.duration = duration
        self.genre = genre
        self.age_restriction = age_restriction
    
    def play(self):
        if(self.borrower.age < self.age_restriction):
            print("borrower is too young to watch this movie")
        else:
            print("Playing "+self.title)
    def turn_on_subtitles(self):
        print("Subtitles turned on")
    

    def get_information(self):
        return super().get_information()+" Duration: "+str(self.duration) + " Genre: "+self.genre + " Age restriction: "+str(self.age_restriction)
    
class Magazine(LibraryItem):
    def __init__(self, title, author, year, num_of_pages,publisher,date_of_publication):
        super().__init__(title, author, year)
        self.num_of_pages = num_of_pages
        self.publisher = publisher
        self.date_of_publication = date_of_publication
    
    def read_magazine(self):
        print("Reading "+self.title)
    
    def get_information(self):
        return super().get_information()+" Num of pages: "+str(self.num_of_pages) + " Publisher: "+self.publisher + " Date of publication: "+str(self.date_of_publication)
    


try:
    library = Library("Library")
    human = Human("John", 20 , 123)
    human2 = Human("Bob", 30 , 124)
    library.add_item( Book("The Lord of the Rings Book", "Author1", 1954, 1000, "Fantasy", "A cool book"))
    library.add_item( DVD("The Lord of the Rings DVD", "Author2", 2001, 200, "Fantasy", 12))
    library.add_item( Magazine("Forbes", "Author3", 2019, 100, "Forbes", datetime.datetime.now()))
    book = library.get_item(0)
    dvd = library.get_item(1)
    magazine = library.get_item(2)
    book.borrow(human, datetime.datetime.now(), datetime.datetime.now() + datetime.timedelta(days=10))
    book.check_availability()
    book.return_item()
    book.check_availability()
    dvd.borrow(human, datetime.datetime.now(), datetime.datetime.now() + datetime.timedelta(days=10))
    magazine.borrow(human, datetime.datetime.now(), datetime.datetime.now() + datetime.timedelta(days=10))
    magazine.read_magazine()
    print(book)
    print(dvd)
    print(magazine)
    dvd.check_availability()
    dvd.return_item()
    ### check ban feature
    dvd.borrow(human2, datetime.datetime.now(), datetime.datetime.now() + datetime.timedelta(microseconds=1))
    time.sleep(0.1)
    dvd.return_item()
    dvd.borrow(human2, datetime.datetime.now(), datetime.datetime.now() + datetime.timedelta(days=10))
    dvd.borrow(human, datetime.datetime.now(), datetime.datetime.now() + datetime.timedelta(days=10))
    
except ValueError as e:
    print(e)