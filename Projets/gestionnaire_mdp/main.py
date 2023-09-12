#!/usr/bin/python3
import os, random, string, subprocess,stdiomask

def check_existence():
    if os.path.exists("coffre.txt"):
        pass
    else:
        file = open("coffre.txt","w")
        file.close()

def append_new_password():
    with open("coffre.txt","a") as appender:
        site = input("name of site ?")
        user = input("what is you username ?")
        password = stdiomask.getpass(prompt = "mdp ?",mask = "*")
        site_user_password = "site" + ":" + site+" user : " + user + " password : " + password +"\n"
        appender.write(site_user_password)

def read_password():
    with open("coffre.txt","r") as r:
        lignes = r.readlines()
        for ligne in lignes:
            print(ligne)


def generate_new_password(password_len):
    new_password = ""
    liste_char = string.ascii_letters + string.punctuation +string.digits
    for i in range(password_len):
        new_password += str(liste_char[random.randint(0,len(liste_char))-1])
    return new_password

print(generate_new_password(7))

subprocess.call("clear")
print('-' * 60)
print("Bienvenue dans le gestionnaire de mot de pass")
print('-' * 60)
 
print("Menu: 0 = pour les vos mots de pass, 1 pour ajouter des mots de pass, 2 pour génerer un nouveau mdp")
while 1:
    try:
        choix_user = int(input("que voulez vous faire ?"))
        break
    except ValueError:
        print("entrer une valeur autorisée (type int() only)")

 
if choix_user == 1:
    while 1:
        try:
            nbreEnregistrement = int(input("combien de mdp voulez vous stocker ?"))
            break
        except ValueError:
            print("entrer une valeur autorisée (type int() only)")

    for i in range(nbreEnregistrement):
        check_existence()
        append_new_password()

elif choix_user == 0:
    read_password()
elif choix_user == 2:
    while 1:
        try:
            lenght = int(input("quel taille pour votre mdp ?"))
            break
        except ValueError:
            print("entrer une valeur autorisée (type int() only)")
    nv_mdp = generate_new_password(lenght)
    print("voici le mdp généré :", nv_mdp)
else:
    exit()

