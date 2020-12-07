class Library:

    def __init__(self,list_of_books,library_name):
        self.list_of_books=list_of_books
        self.library_name=library_name
        self.lend_data={}
        for book in self.list_of_books:
            self.lend_data[book]=None
        
    def add_book(self,addbook):
        self.list_of_books.append(addbook)
        self.lend_data[addbook]=None

    def lend_book(self,book,reader):
        if book in self.list_of_books:
            if self.lend_data[book] is None:
                self.lend_data[book]=reader
            else:
                print(f"sorry this book is lend by {self.lend_data[book]}")
        else:
            print("you have written wrong book name")
    def returnbook(self,book,reader):
        if book in self.list_of_books:
            if self.lend_data[book] is not None:
                self.lend_data[book]=None
            else:
                print("sorry this book not lend")
        else:
            print("you have written wrong book name")

    def display(self):
        for index,books in enumerate(self.list_of_books):
            print(f"{index} : {books}")

def operator_program():
    listofbook=["ram charit manas","geeta","godan","harry potter","life of pie",]
    ram=Library(listofbook,"ram")
    print(f"welcome to {ram.library_name}\n please read the caption carefully and choose option :\n"
          f"for display books 'd'\n for add book 'a'\n  for return book 'r'\n for lend book 'l' \n for exit 'q'")

    exit1=False
    while(exit1 is not True):
        input1 = input("press your option:")
        if input1=='q':
            exit1=True
        elif input1=='d':
            ram.display()
        elif input1=='a':
            abook=input("enter your book name:")
            ram.add_book(abook)
        elif input1=="r":
            rbook=input("book name:")
            rname=input("enter your name:")
            ram.returnbook(rbook,rname)
        elif input1=='l':
            lbook = input("book name:")
            lname = input("enter your name:")
            ram.lend_book(lbook,lname)
            print("book lend.....")
        else:
            print("wrong input \n please read caption carefully")


if __name__ == '__main__':
    operator_program()
















l=["ram","rahim","kalia"]
emp1=Library(l,"salim")
