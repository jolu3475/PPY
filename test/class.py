class Personne :
    pass #pour creer une class vide
rakoto = Personne()
rakoto.id= 1
rakoto.nom = 'Rakoto'
rakoto.age = 22
rakoto.password = 'abcdef'
print('Bonjour, je suis {}.'.format(rakoto.nom))
print('Mon Id est {}.'.format(rakoto.id))
print('Mon age est {}.'.format(rakoto.age))
print('Mon password est {}.'.format(rakoto.password))
del rakoto.password #pour effacer la valeur de l'attribut password