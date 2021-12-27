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
            self.books[author] = book
        self.display()

    def display(self):
        for key, item in self.books.items():
            print(f"{item} written by {key} ")


l1 = Library("Libos")
