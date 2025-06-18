'''
program to create a book class declare  the states as 
bookname,authorname,publishername,publisheddate,categoryofbook
Create the 5 objects & initalise the values using contructor
	------Create 1st Object using one parameterized
	------Create 2nd Object using 2 parameters constructor
	------Create 3rd Object using zero parameterized constructor
	------Create 4th Object using four parameters constructor
	------Create 5th Object using five parameters constructor
Access the values using accessor methods
Update the values using mutators method for name of the book 
'''
class Book:
    def __init__(self, bookname=None, authorname=None, publishername=None, publisheddate=None, categoryofbook=None):
        self.bookname = bookname
        self.authorname = authorname
        self.publishername = publishername
        self.publisheddate = publisheddate
        self.categoryofbook = categoryofbook
    # Accessor methods
    def get_bookname(self):
        return self.bookname

    def get_authorname(self):
        return self.authorname

    def get_publishername(self):
        return self.publishername

    def get_publisheddate(self):
        return self.publisheddate

    def get_categoryofbook(self):
        return self.categoryofbook
    
    # Mutator method
    def set_bookname(self, new_name):
        self.bookname = new_name

    # Display method
    def display(self):
        print(f"Book Name: {self.get_bookname()}")
        print(f"Author Name: {self.get_authorname()}")
        print(f"Publisher Name: {self.get_publishername()}")
        print(f"Published Date: {self.get_publisheddate()}")
        print(f"Category of Book: {self.get_categoryofbook()}")


# Creating objects using different constructors
# 1. One parameter constructor
book1 = Book("Python Basics")
# 2. Two parameters constructor
book2 = Book("C++ Primer", "Bjarne Stroustrup")
# 3. Zero parameter constructor
book3 = Book()
# 4. Four parameters constructor
book4 = Book("Java Core", "James Gosling", "Sun Microsystems", "1995")
# 5. Five parameters constructor
book5 = Book("Clean Code", "Robert C. Martin", "Prentice Hall", "2008", "Software Engineering")
print("Details of Book 1:")
book1.display()
print("Details of Book 2:")
book2.display()
print("Details of Book 3:")
book3.display()
print("Details of Book 4:")
book4.display()
print("Details of Book 5:")
book5.display()
# Update book name of book3 using mutator method
print("Updating book name for Book 3...")
book3.set_bookname("Unknown Book")
# Display updated book3
print("Updated Details of Book 3:")
book3.display()
