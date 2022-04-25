class libros:
    def __init__(self, id_book, book_title, book_type,author,book_count,book_available,book_not_available,book_year,book_editorial):
        self.id_book=id_book
        self.book_title= book_title
        self.book_type=book_type
        self.author=author
        self.book_count=book_count
        self.book_available=book_available
        self.book_not_available=book_not_available
        self.book_year=book_year
        self.book_editorial=book_editorial
    def getID(self):
        return self.id_book
    def getTitle(self):
        return self.book_title
    def getType(self):
        return self.book_type
    def getAuthor(self):
        return self.author
    def getCount(self):
        return self.book_count
    def getAvailable(self):
        return self.book_available
    def getNotAvailable(self):
        return self.book_not_available
    def getYear(self):
        return self.book_year
    def getEditorial(self):
        return self.book_editorial
    
    def setID(self, id_book):
        self.id_book= id_book
    def setTitle(self, book_title):
        self.book_title= book_title
    def setType(self, book_type):
        self.book_type=book_type
    def setAuthor(self, author):
        self.author=author
    def setCount(self, book_count):
        self.book_count=book_count
    def setAvailable(self, book_available):
        self.book_available=book_available
    def setNotAvailable(self, book_not_available):
        self.book_not_available=book_not_available
    def setYear(self, book_year):
        self.book_year=book_year
    def setEditorial(self, book_editorial):
        self.book_editorial=book_editorial