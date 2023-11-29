#programe pour créer une calculatrice

#adition
def add(x, y):
    return x + y 

#multiplication
def mult(x, y):
    return x * y

#soustraction
def sous(x, y):
    return x - y 

#division
def div(x, y):
    return x / y

#ont permet a l'utilisateur de choisire si il veut diviser multiplier aditioner ect
print("""choix option \n
      1 addition \n
      2 multiplication\n
      3 soustraction\n
      4 division \n""")

while True :
#recuperation du choix de l'utilisateur
    choix = input("Entrez votre choix (1,2,3,4): ")

#selection des valeur grace a la boucle while (si le choix est compris entre )
    if choix in ("1","2","3","4") :
        num1 = float(input("Entrez votre premiere valeur : "))
        num2 = float (input("Entrez votre deuxieme valeur : "))

#variable capable d'aditioner soustraire ect
        if choix == "1" :
            print(num1, "+", num2, "=", add(num1 , num2))
    
        if choix == "2" :
            print(num1, "x", num2, "=", mult(num1 , num2))

        if choix == "3" :
            print(num1, "-", num2, "=",sous(num1 , num2))

        if choix == "4" :
            print(num1, "/", num2, "=", div(num1 , num2))
        
#check si l'utilisateur veut faire un autre calcul
#cassage de la boucle si non
        next_calcul = input("voulez vous faire un autre calcul ? (oui/non) : ")
        if next_calcul.lower() == "non" :
            break