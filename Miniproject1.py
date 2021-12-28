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
            self.books[author] = [book, "No"]
        self.display()

    def addtoexisting(self):
        book = input(f"Enter book : ")
        author = input(f"Enter author : ")
        self.books[author] = [book, "No"]

    def display(self):
        print("Author\tBook\tBorrowed")
        for key, item in self.books.items():
            print(f"{key}\t{item[0]}\t{item[1]} ")


while True:
    n = input("Enter 1 make library\nEnter 2 to get all books displayed\nEnter 3 to borrow a book\nEnter 4 to return a book\nEnter 5 to add book in library\nEnter 6 to exit\nYour choice:  ")
    print("\n")
    if int(n) == 1:
        l1 = Library("Libos")
    elif int(n) == 2:
        l1.display()
    elif int(n) == 3:
        print("Borrowing")
    elif int(n) == 4:
        print("Returning")
    elif int(n) == 5:
        l1.addtoexisting()
    elif int(n) == 6:
        break
    else:
        print(f"{n} is invalid input")
