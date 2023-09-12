import tkinter as tk
import random as rd

# créer une direction et une orientation
# tourner de 90 si case blanc/noir
liste = []
liste_indentifiant = []
fen = tk.Tk()
fen.title("fourmie de langton")
canvas = tk.Canvas(fen, width= 500, height= 500, bg = "white")
canvas.grid()
cdt = "droite"
#focntions

def fourmie():
    """création de la fourmie"""
    global id1, id2
    id1 = canvas.create_rectangle(0,0,100,100, fill = "green")
    #id2 = canvas.create_oval(275,275,325,325, fill = "green")

def deplacement():
    global  x0, y0, x1, y1, cdt
    x0, y0, x1, y1 = canvas.coords(id1)
    for i in liste_indentifiant:
        
        if i % 2:
            if cdt == "droite":
                canvas.move(id1,100,0)
            if cdt == "gauche":
                canvas.move(id1,-100,0)
            if cdt == "haut":
                canvas.move(id1,0,100)
            if cdt == "bas":
                canvas.move(id1,0,-100)
        else:
            if cdt == "droite":
                cdt == "haut"
            if cdt == "gauche":
                cdt == "bas"
            if cdt == "haut":
                cdt == "gauche"
            if cdt == "bas":
                cdt == "droite"

def deplacement():
    global  x0, y0, x1, y1, cdt
    x0, y0, x1, y1 = canvas.coords(id1)
        
    if liste_indentifiant[0] == "white":
            if cdt == "droite":
                canvas.move(id1,100,0)
            if cdt == "gauche":
                canvas.move(id1,-100,0)
            
            if cdt == "haut":
                canvas.move(id1,0,100)
             
            if cdt == "bas":
                canvas.move(id1,0,-100)
              
    else:
            if cdt == "droite":
                cdt == "haut"
                
            if cdt == "gauche":
                cdt == "bas"
               
            if cdt == "haut":
                cdt == "gauche"
               
            if cdt == "bas":
                cdt == "droite"
                
    
    

def rebond():
    if y0 < 0:
        canvas.move(id1, 0, 400)
        
    if y1 > 500:
        canvas.move(id1, 0, -400)
        
    if x0 < 0:
        canvas.move(id1,400, 0)
        
    if x1 > 500:
        canvas.move(id1,-400, 0)
        

for i in range(5):
    for j in range(5):
        liste_indentifiant.append(canvas.create_rectangle(i*100, j*100, i*100+100, j*100+100, fill = "white"))
        canvas.create_line(i*100, j*100, i*100, j*100+100, fill = "black")
        canvas.create_line(i*100, j*100, i*100+100, j*100, fill = "black")
        
for i in range(len(liste_indentifiant)):
    if i % 2 == 0:
        canvas.itemconfigure(liste_indentifiant[i], fill = "black")
        liste.append(1)
    else:
        liste.append(0)
bouton_play = tk.Button(fen, text = "play", command = deplacement)
bouton_play.grid()

fourmie()
fen.mainloop()