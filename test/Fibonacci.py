n=int(input("Veuiller entrer un nombre: "))
for i in range (0,n+1):
    if (i == 0):
        R=0
        S=0
        F=0
    elif(i == 1):
        S=R
        R=F
        F=1
    else:
        S=R
        R=F
        F=R+S
    print (F)