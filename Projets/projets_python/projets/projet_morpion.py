import tkinter as tk

#Constantes
HAUTEUR = 300
LARGEUR = 300

#Variables


liste_jeu = [[0,0,0][0,0,0][0,0,0]]
player = "oval"


#Fonctions
def affichage():
    for i in range(7):
        for j in range(6):
                canvas.create_line(i*100,j*100,i*100,j*100+100,width=3,fill="black")
                canvas.create_line(i*100,j*100,i*100+100,j*100,width=3,fill="black")

def jeu(event):
    global player, nbre, liste_jeu
    nbre = 0
    while nbre < 9:
        if  0 < event.x < 100 and 0 < event.y < 100:
            if  player == "oval" :
                canvas.create_oval(0,0,100,100)
                player = "croix"
                liste_jeu[0][0] = 1
                print(liste_jeu)
    
                
            else:
                canvas.create_line(0,0,100,100)
                canvas.create_line(100,0,0,100)
                player = "oval"
                liste_jeu[0][0] = 2
                print(liste_jeu)
                
            
            nbre += 1
    
        if  100 < event.x < 200 and 0 < event.y < 100:
            if  player == "oval" :
                canvas.create_oval(100,0,200,100)
                player = "croix"
                liste_jeu[0][1] = 1
                print(liste_jeu)
            else:
                canvas.create_line(100,0,200,100)
                canvas.create_line(200,0,100,100)
                player = "oval"
                liste_jeu[0][1] = 2
                print(liste_jeu)

            nbre += 1
            

        if  200 < event.x < 300 and 0 < event.y < 100:
            if  player == "oval" :
                canvas.create_oval(200,0,300,100)
                player = "croix"
                liste_jeu[0][2] = 1
                print(liste_jeu)
            else:
                canvas.create_line(200,0,300,100)
                canvas.create_line(300,0,200,100)
                player = "oval"
                liste_jeu[0][2] = 2
                print(liste_jeu)
                
            nbre += 1


        if  0 < event.x < 100 and 100 < event.y < 200:
            if  player == "oval" :
                canvas.create_oval(0,100,100,200)
                player = "croix"
                liste_jeu[1][0] = 1
                print(liste_jeu)
            
            else:
                canvas.create_line(0,100,100,200)
                canvas.create_line(100,100,0,200)
                player = "oval"
                liste_jeu[1][0] = 2
                print(liste_jeu)
            
            nbre += 1
    
        if  100 < event.x < 200 and 100 < event.y < 200:
            if  player == "oval" :
                canvas.create_oval(100,100,200,200)
                player = "croix"
                liste_jeu[1][1] = 1
                print(liste_jeu)
            else:
                canvas.create_line(100,100,200,200)
                canvas.create_line(200,100,100,200)
                player = "oval"
                liste_jeu[1][1] = 2
                print(liste_jeu)

            nbre += 1
    
        if  200 < event.x < 300 and 100 < event.y < 200:
            if  player == "oval" :
                canvas.create_oval(200,100,300,200)
                player = "croix"
                liste_jeu[1][2] = 1
                print(liste_jeu)
            else:
                canvas.create_line(200,100,300,200)
                canvas.create_line(300,100,200,200)
                player = "oval"
                liste_jeu[1][2] = 2
                print(liste_jeu)

            nbre += 1

        if  0 < event.x < 100 and 200 < event.y < 300:
            if  player == "oval" :
                canvas.create_oval(0,200,100,300)
                player = "croix"
                liste_jeu[2][0] = 1
                print(liste_jeu)
            else:
                canvas.create_line(0,200,100,300)
                canvas.create_line(100,200,0,300)
                player = "oval"
                liste_jeu[2][0] = 2
                print(liste_jeu)
            nbre += 1
    
        if  100 < event.x < 200 and 200 < event.y < 300:
            if  player == "oval" :
                canvas.create_oval(100,200,200,300)
                player = "croix"
                liste_jeu[2][1] = 1
                print(liste_jeu)
            else:
                canvas.create_line(100,200,200,300)
                canvas.create_line(200,200,100,300)
                player = "oval"
                liste_jeu[2][1] = 2
                print(liste_jeu)
            nbre += 1
        
            
    
        if  200 < event.x < 300 and 200 < event.y < 300:
            if  player == "oval" :
               canvas.create_oval(200,200,300,300)
               player = "croix"
               liste_jeu[2][2] = 1
               print(liste_jeu)
            else:
                canvas.create_line(200,200,300,300)
                canvas.create_line(300,200,200,300)
                player = "oval"
                liste_jeu[2][2] = 2
                print(liste_jeu)
            
            nbre += 1
        print(nbre)
    else:
        info.config(text = " fin du jeu")
        
        
        
        
    


def check():
    global liste_jeu
    if (liste_jeu[0][0] == liste_jeu[0][1] == liste_jeu[0][2] == 1) :
        info.config(text = " win crclr")
    
    if liste_jeu[3] == liste_jeu[4] == liste_jeu[5] == 1 or liste_jeu[1] == liste_jeu[4] == liste_jeu[7] == 1 or liste_jeu[6] == liste_jeu[4] == liste_jeu[2] == 1 :
        print("win cercle")
    
    if liste_jeu[6] == liste_jeu[7] == liste_jeu[8] == 1 or liste_jeu[2] == liste_jeu[5] == liste_jeu[8] == 1 :
        print("win cercle")
    
    if liste_jeu[0] == liste_jeu[1] == liste_jeu[2] == 2 or liste_jeu[0] == liste_jeu[3] == liste_jeu[6] == 2 or liste_jeu[0] == liste_jeu[4] == liste_jeu[8] == 2 :
        print("win croix")
    
    if liste_jeu[3] == liste_jeu[4] == liste_jeu[5] == 2 or liste_jeu[1] == liste_jeu[4] == liste_jeu[7] == 2 or liste_jeu[6] == liste_jeu[4] == liste_jeu[2] == 2 :
        print("win croix")
    
    if liste_jeu[6] == liste_jeu[7] == liste_jeu[8] == 2 or liste_jeu[2] == liste_jeu[5] == liste_jeu[8] == 2 :
        print("win croix")
    
    
    
        
   
        


   



    


#Création de la fenêtre
fenetre = tk.Tk()
fenetre.title("Morpion")

#Widgets
canvas = tk.Canvas(fenetre,width=HAUTEUR,height=LARGEUR,bg="white")
info = tk.Label(fenetre, text= " Hi",)
bouton_quitter = tk.Button(fenetre,text="quitter",command= lambda : fenetre.destroy())








#Placement des widgets
canvas.grid()
bouton_quitter.grid()
info.grid()


canvas.bind("<Button-1>", jeu)
affichage()
check()

#Lancement de la boucle
fenetre.mainloop()