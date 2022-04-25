class usuarios:
    def __init__(self, id_user,user_display_name,user_nickname,user_password,user_age,user_career,user_carnet):
        self.id_user=id_user
        self.user_display_name=user_display_name
        self.user_nickname=user_nickname
        self.user_password=user_password
        self.user_age=user_age
        self.user_career=user_career
        self.user_carnet=user_carnet
    def getID(self):
        return self.id_user
    def getDisplay(self):
        return self.user_display_name
    def getNickname(self):
        return self.user_nickname
    def getPassword(self):
        return self.user_password
    def getAge(self):
        return self.user_age
    def getCareer(self):
        return self.user_career
    def getCarnet(self):
        return self.user_carnet

    def setID(self,id_user):
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