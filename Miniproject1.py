import time
from datetime import date

today = date.today()


class Library:
    def __init__(self, name):
        self.name = name
        self.books = {}
        self.addbook()
        pass

    def addbook(self):
        count1 = input("Enter count of books")
        count1 = int(count1)
        print(count1)
        for i in range(int(count1)):
            book = input(f"Enter book no {i+1}: ")
            author = input(f"Enter author no {i+1}: ")
            self.books[author] = [book, "No", " - ", " - ", " - "]
        self.display()

    def addtoexisting(self):
        book = input(f"Enter book : ")
        author = input(f"Enter author : ")
        self.books[author] = [book, "No", " - ", " - ", " - "]

    def display(self):
        print("\t\tAuthor\t\t\tBook\t\t\tBorrow\t\t\tTaken\t\t   Last borrowed\t\t    Last Returned")
        for key, item in self.books.items():
            print(
                f"\t\t{key}\t\t\t{item[0]}\t\t\t{item[1]}\t\t\t{item[2]}\t\t      {item[3]}\t\t     {item[4]} ")

    def borrow(self):
        flag = 0
        search = ""
        while flag == 0:
            self.display()
            search = input("\t\tEnter Author or Book name: ")
            for author, booklist in self.books.items():
                if (search == author or search == booklist[0]):
                    if booklist[1] == "No":
                        print("\t\t\t\tBook Found\t\t\t\t")
                        flag = 1
                        break
                    else:
                        print(
                            f"Book found but is being borrowed on {self.books[search][3]},Take some other book you interested in.")
                        return

                else:
                    print("\t\tBook not found,Plz re-enter\t\t")
                    break
        boroowername = input("Enter Your name: ")

        # dd/mm/YY
        d1 = today.strftime("%d/%m/%Y")
        timeis = d1
        print(
            f"\t\tValid Borrower\t\t, Book borrowed by {boroowername} on {timeis}")
        self.books[search][2] = boroowername
        self.books[search][3] = timeis
        self.books[search][1] = "Yes"

    def returnbook(self):
        flag = 0
        search = ""
        while flag == 0:
            self.display()
            search = input(
                "\t\tEnter Author or Book name you want to return: ")
            for author, booklist in self.books.items():
                if (search == author or search == booklist[0]):
                    if booklist[1] == "Yes":
                        print("\t\t\t\tBook Found\t\t\t\t")
                        flag = 1
                        break
                    else:
                        print("Book with this name was not borrowed")

                else:
                    print("\t\tBook not found,Plz re-enter\t\t")
                    break
        boroowername = input("Enter Your name: ")
        if self.books[search][2] == boroowername:
            # dd/mm/YY
            d1 = today.strftime("%d/%m/%Y")
            timeis = d1
            print(
                f"\t\tValid Borrower\t\t, Book returned by {boroowername} on {timeis}")
            self.books[search][2] = " - "
            self.books[search][1] = "No"
            self.books[search][4] = timeis
        else:
            print("Invalid borrower details")


while True:
    n = input("Enter 1 make library\nEnter 2 to get all books displayed\nEnter 3 to borrow a book\nEnter 4 to return a book\nEnter 5 to add book in library\nEnter 6 to exit\nYour choice:  ")
    print("\n")
    if int(n) == 1:
        l1 = Library("Libos")
    elif int(n) == 2:
        l1.display()
    elif int(n) == 3:
        print("\t\tBorrowing Section\t\t")
        l1.borrow()
    elif int(n) == 4:
        print("\t\tReturning\t\t")
        l1.returnbook()
    elif int(n) == 5:
        l1.addtoexisting()
    elif int(n) == 6:
        break
    else:
        print(f"{n} is invalid input")
