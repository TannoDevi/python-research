class Book:
    def __init__(self, title, author, pages, price):
        self.title = title
        self.author = author
        self.pages = pages
        self.price = price

    def getprice(self):
        if hasattr(self,"discount"):
         return self.price - (self.price * self.discount)
        else:
            return self.price

    def setDiscount(self, amount):
        self.discount = amount

    def __str__(self):
        price = str(self.price)
        return f"Our book for sale: {self.title}  Is now {price})"


# create an instance
book1 = Book("Harry potter", "J.k rwoling", 245, 22.50)
book2 = Book("Python", " someone Smart", 500, 89.88)
# book3 = Book("Social Science", "Royal King" 300, 20.70)

# test 1
print(book1)
print(book2.setDiscount(5))
book2.getprice