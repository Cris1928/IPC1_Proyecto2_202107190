class Prestamos:
    def __init__(self, id_loan, id_book, book_title, book_type,author,book_year,book_editorial,id_user,user_display_name,user_nickname,user_password,user_age,user_career,user_carnet,loan_hora,loan_date,return_date):
        self.id_loan=id_loan
        self.id_book=id_book
        self.book_title= book_title
        self.book_type=book_type
        self.author=author
        self.book_year=book_year
        self.book_editorial=book_editorial
        self.id_user=id_user
        self.user_display_name=user_display_name
        self.user_nickname=user_nickname
        self.user_password=user_password
        self.user_age=user_age
        self.user_career=user_career
        self.user_carnet=user_carnet
        self.loan_hora=loan_hora
        self.loan_date=loan_date
        self.return_date=return_date


    def getLoan(self):
        return self.id_loan
    def getID(self):
        return self.id_book
    def getTitle(self):
        return self.book_title
    def getType(self):
        return self.book_type
    def getAuthor(self):
        return self.author
    def getYear(self):
        return self.book_year
    def getEditorial(self):
        return self.book_editorial
    def getIDuser(self):
        return self.id_user
    def getDisplay(self):
        return self.user_display_name
    def getNickname(self):
        return self.user_nickname
    def getPassword(self):
        return self.user_nickname
    def getAge(self):
        return self.user_age
    def getCareer(self):
        return self.user_career
    def getCarnet(self):
        return self.user_carnet
    def getHora(self):
        return self.loan_hora
    def getDate(self):
        return self.loan_date
    def getRedate(self):
        return self.return_date
    


    def setLoan(self, id_loan):
        self.id_loan=id_loan
    def setID(self, id_book):
        self.id_book=id_book
    def setTitle(self, book_title):
        self.book_title=book_title
    def setType(self, book_type):
        self.book_type=book_type
    def setAuthor(self, author):
        self.author=author
    def setYear(self, book_year):
        self.book_year=book_year
    def setEditorial(self, book_editorial):
        self.book_editorial=book_editorial
    def setIDuser(self,id_user):
        self.id_user=id_user
    def setDisplay(self, user_display_name):
        self.user_display_name=user_display_name
    def setNickname(self, user_nickname):
        self.user_nickname=user_nickname
    def setPassword(self, user_password):
        self.user_password=user_password
    def setAge(self, user_age):
        self.user_age=user_age
    def setCareer(self, user_career):
        self.user_career=user_career
    def setCarnet(self, user_carnet):
        self.user_carnet=user_carnet
    def setHora(self,loan_hora):
        self.loan_hora=loan_hora
    def setDate(self, loan_date):
        self.loan_date=loan_date
    def setRedate(self, return_date):
        self.return_date=return_date