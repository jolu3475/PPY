class Calcul:
    def add(calcul):
        return print(calcul.x+calcul.y)
    def sous(calcul):
        return print(calcul.x-calcul.y)
    def multi(calcul):
        return print(calcul.x*calcul.y)
    def div(calcul):
        return print(calcul.x/calcul.y)
    def saisir_valeur(calcul):
        return input("Entrer la valeur du nombre : ")
    def affiche_valeur(calcul):
        print(f'La valeur du nombre 1 : {calcul.x}.')
        print(f'La valeur du nombre 2 : {calcul.y}.')
cal = Calcul()
cal.x= int(cal.saisir_valeur())
cal.y= int(cal.saisir_valeur())
cal.affiche_valeur()
cal.add()
cal.sous()
cal.div()
cal.multi()