print("hello")

liste = [0,0,0,0,0,0,0,0,0]
def affichage():
    print("-----")
    print(liste[0],liste[1],liste[2])
    print(liste[3],liste[4],liste[5])
    print(liste[6],liste[7],liste[8])
    print("-----")

def gagner():
    if (liste[0] == liste[1] == liste[2] !=0 or liste[3] == liste[4] == liste[5] !=0 or liste[6] == liste[7] == liste[8]!=0):
        print("Bravo vous avez gagné")
        return True
    if (liste[0] == liste[3] == liste[6] !=0 or liste[1] == liste[4] == liste[7] !=0 or liste[2] == liste[5] == liste[8]!=0):
        print("Bravo vous avez gagné")
        return True
    if (liste[0] == liste[4] == liste[8] !=0 or liste[2] == liste[4] == liste[6] !=0):
        print("Bravo vous avez gagné")
        return True

def jeu():
    print("Bienvenue dans le morpion, les X commencent en premier puis les O Good luck")
    cases_possible = [i for i in range(0,8)]
    for i in range(0,9):
        affichage()
        choix_joeur = int(input("quel case ?(entre 0 et 8)"))
        while choix_joeur not in cases_possible:
            print("erreur vous devez mettre un chiffre entre 0 et 8")
            choix_joeur = int(input("quel case ?(entre 0 et 8)"))
        cases_possible[choix_joeur] = "None"
        if i % 2 == 0:
            liste[int(choix_joeur)] = "X"
        else:
            liste[int(choix_joeur)] = "O"
        affichage()
        if gagner():
            break

jeu()