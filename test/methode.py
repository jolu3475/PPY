class Personne :
    def test_pwd (personne, password):
        return personne.password == password
John = Personne()
John.id= 1
John.nom= 'joh'
John.password = '12345'
print(John.test_pwd('toto')) #false
print(John.test_pwd('12345')) #true