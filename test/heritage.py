import crypt
class User:
    def __init__(self,id, name, password):
        self.id = id
        self.name = name
        self._salt = crypt.mksalt()
        self.password = password
    def crypt_pwd(self,password):
        return crypt.crypt(password, self._salt)
    def check_pwd(self, password):
        return self.password == self.crypt_pwd(password)
class Admin(User):
    def manage(self):
        print("je suis un administrateur")
root = Admin(1,"root","toto")
root.check_pwd("toto")
root.manage()