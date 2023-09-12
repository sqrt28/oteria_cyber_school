import tkinter as tk
import random as rd

liste_identifiant = []
liste_code = []
liste_jeu = []
liste_jeu2 = []
liste_veri1,liste_veri2,liste_veri3,liste_veri4,liste_veri5,liste_veri6,liste_veri7,liste_veri8,liste_veri9,liste_veri10 = [],[],[],[],[],[],[],[],[],[]
cdt = 0

def affichage():
    global  liste_identifiant, liste_jeu
    for i in range(10):
        for j in range(10):
            liste_identifiant.append(canvas.create_rectangle(i*50,j*50,i*50+50,j*50+50))
    print(liste_identifiant)
    liste_jeu.append([liste_identifiant[0],liste_identifiant[10],liste_identifiant[20],liste_identifiant[30]])
    liste_jeu.append([liste_identifiant[1],liste_identifiant[11],liste_identifiant[21],liste_identifiant[31]])
    liste_jeu.append([liste_identifiant[2],liste_identifiant[12],liste_identifiant[22],liste_identifiant[32]])
    liste_jeu.append([liste_identifiant[3],liste_identifiant[13],liste_identifiant[23],liste_identifiant[33]])
    liste_jeu.append([liste_identifiant[4],liste_identifiant[14],liste_identifiant[24],liste_identifiant[34]])
    liste_jeu.append([liste_identifiant[5],liste_identifiant[15],liste_identifiant[25],liste_identifiant[35]])
    liste_jeu.append([liste_identifiant[6],liste_identifiant[16],liste_identifiant[26],liste_identifiant[36]])
    liste_jeu.append([liste_identifiant[7],liste_identifiant[17],liste_identifiant[27],liste_identifiant[37]])
    liste_jeu.append([liste_identifiant[8],liste_identifiant[18],liste_identifiant[28],liste_identifiant[38]])
    liste_jeu.append([liste_identifiant[9],liste_identifiant[19],liste_identifiant[29],liste_identifiant[39]])

    liste_jeu2.append([liste_identifiant[60],liste_identifiant[70],liste_identifiant[80],liste_identifiant[90]])
    liste_jeu2.append([liste_identifiant[61],liste_identifiant[71],liste_identifiant[81],liste_identifiant[91]])
    liste_jeu2.append([liste_identifiant[62],liste_identifiant[72],liste_identifiant[82],liste_identifiant[92]])
    liste_jeu2.append([liste_identifiant[63],liste_identifiant[73],liste_identifiant[83],liste_identifiant[93]])
    liste_jeu2.append([liste_identifiant[64],liste_identifiant[74],liste_identifiant[84],liste_identifiant[94]])
    liste_jeu2.append([liste_identifiant[65],liste_identifiant[75],liste_identifiant[85],liste_identifiant[95]])
    liste_jeu2.append([liste_identifiant[66],liste_identifiant[76],liste_identifiant[86],liste_identifiant[96]])
    liste_jeu2.append([liste_identifiant[67],liste_identifiant[77],liste_identifiant[87],liste_identifiant[97]])
    liste_jeu2.append([liste_identifiant[68],liste_identifiant[78],liste_identifiant[88],liste_identifiant[98]])
    liste_jeu2.append([liste_identifiant[69],liste_identifiant[79],liste_identifiant[89],liste_identifiant[99]])
    print(liste_jeu2)


def mode_solo():
    global liste_code
    liste_tirage = ["red", "yellow", "blue", "green","white","black"]
    for i in range(4):
        tirage = rd.choice(liste_tirage)
        liste_code.append(tirage)
        del liste_tirage[tirage.index(tirage)]
    print(liste_code)

def mode_duo():
    global liste_code
    for i in range(4):
        c = input('donner une couleur en anglais #jaune, bleu, rouge, vert, blanc, noir : ')
        liste_code.append(c)
    print(liste_code)

def Essaie1():
    global cdt
    for i in range(4):
        c = input('donner une couleur en anglais : ')
        canvas.itemconfigure(liste_jeu[0][i], fill = c)
        liste_veri1.append(c)
def Essaie2():
    global cdt
    for i in range(4):
        c = input('donner une couleur en anglais : ')
        canvas.itemconfigure(liste_jeu[1][i], fill = c)
        liste_veri2.append(c)
    cdt+=1
def Essaie3():
    global cdt
    for i in range(4):
        c = input('donner une couleur en anglais : ')
        canvas.itemconfigure(liste_jeu[2][i], fill = c)
        liste_veri3.append(c)
    cdt+=1
def Essaie4():
    global cdt
    for i in range(4):
        c = input('donner une couleur en anglais : ')
        canvas.itemconfigure(liste_jeu[3][i], fill = c)
        liste_veri4.append(c)
    cdt+=1
def Essaie5():
    global cdt
    for i in range(4):
        c = input('donner une couleur en anglais : ')
        canvas.itemconfigure(liste_jeu[4][i], fill = c)
        liste_veri5.append(c)
    cdt+=1
def Essaie6():
    global cdt
    for i in range(4):
        c = input('donner une couleur en anglais : ')
        canvas.itemconfigure(liste_jeu[5][i], fill = c)
        liste_veri6.append(c)
    cdt+=1
def Essaie7():
    global cdt
    for i in range(4):
        c = input('donner une couleur en anglais : ')
        canvas.itemconfigure(liste_jeu[6][i], fill = c)
        liste_veri7.append(c)
    cdt+=1
def Essaie8():
    global cdt
    for i in range(4):
        c = input('donner une couleur en anglais : ')
        canvas.itemconfigure(liste_jeu[7][i], fill = c)
        liste_veri8.append(c)
    cdt+=1
def Essaie9():
    global cdt
    for i in range(4):
        c = input('donner une couleur en anglais : ')
        canvas.itemconfigure(liste_jeu[8][i], fill = c)
        liste_veri9.append(c)
    cdt+=1
def Essaie10():
    global cdt
    for i in range(4):
        c = input('donner une couleur en anglais : ')
        canvas.itemconfigure(liste_jeu[9][i], fill = c)
        liste_veri10.append(c)
    cdt+=1
        
def verification():
    global cdt
    if cdt == 0:
        if liste_code[0] == liste_veri1[0]:
            canvas.itemconfigure(liste_jeu2[0][0], fill = "red")
        if liste_code[1] == liste_veri1[1]:
            canvas.itemconfigure(liste_jeu2[0][1], fill = "red")
        if liste_code[2] == liste_veri1[2]:
            canvas.itemconfigure(liste_jeu2[0][2], fill = "red")
        if liste_code[3] == liste_veri1[3]:
            canvas.itemconfigure(liste_jeu2[0][3], fill = "red")
        
        if liste_code[0] != liste_veri1[0] and liste_code[0] == liste_veri1[1] or liste_code[0] == liste_veri1[2] or liste_code[0] == liste_veri1[3]:
            canvas.itemconfigure(liste_jeu2[0][0], fill = "grey")
        if liste_code[1] != liste_veri1[1] and liste_code[1] == liste_veri1[0] or liste_code[1] == liste_veri1[2] or liste_code[1] == liste_veri1[3]:
            canvas.itemconfigure(liste_jeu2[0][1], fill = "grey")
        if liste_code[2] != liste_veri1[2] and liste_code[2] == liste_veri1[0] or liste_code[2] == liste_veri1[1] or liste_code[2] == liste_veri1[3]:
            canvas.itemconfigure(liste_jeu2[0][2], fill = "grey")
        if liste_code[3] != liste_veri1[3] and liste_code[3] == liste_veri1[0] or liste_code[3] == liste_veri1[1] or liste_code[3] == liste_veri1[2]:
            canvas.itemconfigure(liste_jeu2[0][3], fill = "grey")
    
    if cdt == 1:
        if liste_code[0] == liste_veri2[0]:
            canvas.itemconfigure(liste_jeu2[1][0], fill = "red")
        if liste_code[1] == liste_veri2[1]:
            canvas.itemconfigure(liste_jeu2[1][1], fill = "red")
        if liste_code[2] == liste_veri2[2]:
            canvas.itemconfigure(liste_jeu2[1][2], fill = "red")
        if liste_code[3] == liste_veri2[3]:
            canvas.itemconfigure(liste_jeu2[1][3], fill = "red")
        
        if liste_code[0] != liste_veri2[0] and liste_code[0] == liste_veri2[1] or liste_code[0] == liste_veri2[2] or liste_code[0] == liste_veri2[3]:
            canvas.itemconfigure(liste_jeu2[1][0], fill = "grey")
        if liste_code[1] != liste_veri2[1] and liste_code[1] == liste_veri2[0] or liste_code[1] == liste_veri2[2] or liste_code[1] == liste_veri2[3]:
            canvas.itemconfigure(liste_jeu2[1][1], fill = "grey")
        if liste_code[2] != liste_veri2[2] and liste_code[2] == liste_veri2[0] or liste_code[2] == liste_veri2[1] or liste_code[2] == liste_veri2[3]:
            canvas.itemconfigure(liste_jeu2[1][2], fill = "grey")
        if liste_code[3] != liste_veri2[3] and liste_code[3] == liste_veri2[0] or liste_code[3] == liste_veri2[1] or liste_code[3] == liste_veri2[2]:
            canvas.itemconfigure(liste_jeu2[1][3], fill = "grey")
        
    if cdt == 2:
        if liste_code[0] == liste_veri3[0]:
            canvas.itemconfigure(liste_jeu2[2][0], fill = "red")
        if liste_code[1] == liste_veri3[1]:
            canvas.itemconfigure(liste_jeu2[2][1], fill = "red")
        if liste_code[2] == liste_veri3[2]:
            canvas.itemconfigure(liste_jeu2[2][2], fill = "red")
        if liste_code[3] == liste_veri3[3]:
            canvas.itemconfigure(liste_jeu2[2][3], fill = "red")
        
        if liste_code[0] != liste_veri3[0] and liste_code[0] == liste_veri3[1] or liste_code[0] == liste_veri3[2] or liste_code[0] == liste_veri3[3]:
            canvas.itemconfigure(liste_jeu2[2][0], fill = "grey")
        if liste_code[1] != liste_veri3[1] and liste_code[1] == liste_veri3[0] or liste_code[1] == liste_veri3[2] or liste_code[1] == liste_veri3[3]:
            canvas.itemconfigure(liste_jeu2[2][1], fill = "grey")
        if liste_code[2] != liste_veri3[2] and liste_code[2] == liste_veri3[0] or liste_code[2] == liste_veri3[1] or liste_code[2] == liste_veri3[3]:
            canvas.itemconfigure(liste_jeu2[2][2], fill = "grey")
        if liste_code[3] != liste_veri3[3] and liste_code[3] == liste_veri3[0] or liste_code[3] == liste_veri3[1] or liste_code[3] == liste_veri3[2]:
            canvas.itemconfigure(liste_jeu2[2][3], fill = "grey")
        
    if cdt == 3:
        if liste_code[0] == liste_veri4[0]:
            canvas.itemconfigure(liste_jeu2[3][0], fill = "red")
        if liste_code[1] == liste_veri4[1]:
            canvas.itemconfigure(liste_jeu2[3][1], fill = "red")
        if liste_code[2] == liste_veri4[2]:
            canvas.itemconfigure(liste_jeu2[3][2], fill = "red")
        if liste_code[3] == liste_veri4[3]:
            canvas.itemconfigure(liste_jeu2[3][3], fill = "red")
        
        if liste_code[0] != liste_veri4[0] and liste_code[0] == liste_veri4[1] or liste_code[0] == liste_veri4[2] or liste_code[0] == liste_veri4[3]:
            canvas.itemconfigure(liste_jeu2[3][0], fill = "grey")
        if liste_code[1] != liste_veri4[1] and liste_code[1] == liste_veri4[0] or liste_code[1] == liste_veri4[2] or liste_code[1] == liste_veri4[3]:
            canvas.itemconfigure(liste_jeu2[3][1], fill = "grey")
        if liste_code[2] != liste_veri4[2] and liste_code[2] == liste_veri4[0] or liste_code[2] == liste_veri4[1] or liste_code[2] == liste_veri4[3]:
            canvas.itemconfigure(liste_jeu2[3][2], fill = "grey")
        if liste_code[3] != liste_veri4[3] and liste_code[3] == liste_veri4[0] or liste_code[3] == liste_veri4[1] or liste_code[3] == liste_veri4[2]:
            canvas.itemconfigure(liste_jeu2[3][3], fill = "grey")
        
    if cdt == 4:
        if liste_code[0] == liste_veri5[0]:
            canvas.itemconfigure(liste_jeu2[4][0], fill = "red")
        if liste_code[1] == liste_veri5[1]:
            canvas.itemconfigure(liste_jeu2[4][1], fill = "red")
        if liste_code[2] == liste_veri5[2]:
            canvas.itemconfigure(liste_jeu2[4][2], fill = "red")
        if liste_code[3] == liste_veri5[3]:
            canvas.itemconfigure(liste_jeu2[4][3], fill = "red")
        
        if liste_code[0] != liste_veri5[0] and liste_code[0] == liste_veri5[1] or liste_code[0] == liste_veri5[2] or liste_code[0] == liste_veri5[3]:
            canvas.itemconfigure(liste_jeu2[4][0], fill = "grey")
        if liste_code[1] != liste_veri5[1] and liste_code[1] == liste_veri5[0] or liste_code[1] == liste_veri5[2] or liste_code[1] == liste_veri5[3]:
            canvas.itemconfigure(liste_jeu2[4][1], fill = "grey")
        if liste_code[2] != liste_veri5[2] and liste_code[2] == liste_veri5[0] or liste_code[2] == liste_veri5[1] or liste_code[2] == liste_veri5[3]:
            canvas.itemconfigure(liste_jeu2[4][2], fill = "grey")
        if liste_code[3] != liste_veri5[3] and liste_code[3] == liste_veri5[0] or liste_code[3] == liste_veri5[1] or liste_code[3] == liste_veri5[2]:
            canvas.itemconfigure(liste_jeu2[4][3], fill = "grey")
        
    if cdt == 5:
        if liste_code[0] == liste_veri6[0]:
            canvas.itemconfigure(liste_jeu2[5][0], fill = "red")
        if liste_code[1] == liste_veri6[1]:
            canvas.itemconfigure(liste_jeu2[5][1], fill = "red")
        if liste_code[2] == liste_veri6[2]:
            canvas.itemconfigure(liste_jeu2[5][2], fill = "red")
        if liste_code[3] == liste_veri6[3]:
            canvas.itemconfigure(liste_jeu2[5][3], fill = "red")
        
        if liste_code[0] != liste_veri6[0] and liste_code[0] == liste_veri6[1] or liste_code[0] == liste_veri6[2] or liste_code[0] == liste_veri6[3]:
            canvas.itemconfigure(liste_jeu2[5][0], fill = "grey")
        if liste_code[1] != liste_veri6[1] and liste_code[1] == liste_veri6[0] or liste_code[1] == liste_veri6[2] or liste_code[1] == liste_veri6[3]:
            canvas.itemconfigure(liste_jeu2[5][1], fill = "grey")
        if liste_code[2] != liste_veri6[2] and liste_code[2] == liste_veri6[0] or liste_code[2] == liste_veri6[1] or liste_code[2] == liste_veri6[3]:
            canvas.itemconfigure(liste_jeu2[5][2], fill = "grey")
        if liste_code[3] != liste_veri6[3] and liste_code[3] == liste_veri6[0] or liste_code[3] == liste_veri6[1] or liste_code[3] == liste_veri6[2]:
            canvas.itemconfigure(liste_jeu2[5][3], fill = "grey")
        
    if cdt == 6:
        if liste_code[0] == liste_veri7[0]:
            canvas.itemconfigure(liste_jeu2[6][0], fill = "red")
        if liste_code[1] == liste_veri7[1]:
            canvas.itemconfigure(liste_jeu2[6][1], fill = "red")
        if liste_code[2] == liste_veri7[2]:
            canvas.itemconfigure(liste_jeu2[6][2], fill = "red")
        if liste_code[3] == liste_veri7[3]:
            canvas.itemconfigure(liste_jeu2[6][3], fill = "red")
        
        if liste_code[0] != liste_veri7[0] and liste_code[0] == liste_veri7[1] or liste_code[0] == liste_veri7[2] or liste_code[0] == liste_veri7[3]:
            canvas.itemconfigure(liste_jeu2[6][0], fill = "grey")
        if liste_code[1] != liste_veri7[1] and liste_code[1] == liste_veri7[0] or liste_code[1] == liste_veri7[2] or liste_code[1] == liste_veri7[3]:
            canvas.itemconfigure(liste_jeu2[6][1], fill = "grey")
        if liste_code[2] != liste_veri7[2] and liste_code[2] == liste_veri7[0] or liste_code[2] == liste_veri7[1] or liste_code[2] == liste_veri7[3]:
            canvas.itemconfigure(liste_jeu2[6][2], fill = "grey")
        if liste_code[3] != liste_veri7[3] and liste_code[3] == liste_veri7[0] or liste_code[3] == liste_veri7[1] or liste_code[3] == liste_veri7[2]:
            canvas.itemconfigure(liste_jeu2[6][3], fill = "grey")
        
    if cdt == 7:
        if liste_code[0] == liste_veri8[0]:
            canvas.itemconfigure(liste_jeu2[7][0], fill = "red")
        if liste_code[1] == liste_veri8[1]:
            canvas.itemconfigure(liste_jeu2[7][1], fill = "red")
        if liste_code[2] == liste_veri8[2]:
            canvas.itemconfigure(liste_jeu2[7][2], fill = "red")
        if liste_code[3] == liste_veri8[3]:
            canvas.itemconfigure(liste_jeu2[7][3], fill = "red")
        
        if liste_code[0] != liste_veri8[0] and liste_code[0] == liste_veri8[1] or liste_code[0] == liste_veri8[2] or liste_code[0] == liste_veri8[3]:
            canvas.itemconfigure(liste_jeu2[7][0], fill = "grey")
        if liste_code[1] != liste_veri8[1] and liste_code[1] == liste_veri8[0] or liste_code[1] == liste_veri8[2] or liste_code[1] == liste_veri8[3]:
            canvas.itemconfigure(liste_jeu2[7][1], fill = "grey")
        if liste_code[2] != liste_veri8[2] and liste_code[2] == liste_veri8[0] or liste_code[2] == liste_veri8[1] or liste_code[2] == liste_veri8[3]:
            canvas.itemconfigure(liste_jeu2[7][2], fill = "grey")
        if liste_code[3] != liste_veri8[3] and liste_code[3] == liste_veri8[0] or liste_code[3] == liste_veri8[1] or liste_code[3] == liste_veri8[2]:
            canvas.itemconfigure(liste_jeu2[7][3], fill = "grey")
        
    if cdt == 8:
        if liste_code[0] == liste_veri9[0]:
            canvas.itemconfigure(liste_jeu2[8][0], fill = "red")
        if liste_code[1] == liste_veri9[1]:
            canvas.itemconfigure(liste_jeu2[8][1], fill = "red")
        if liste_code[2] == liste_veri9[2]:
            canvas.itemconfigure(liste_jeu2[8][2], fill = "red")
        if liste_code[3] == liste_veri9[3]:
            canvas.itemconfigure(liste_jeu2[8][3], fill = "red")
        
        if liste_code[0] != liste_veri9[0] and liste_code[0] == liste_veri9[1] or liste_code[0] == liste_veri9[2] or liste_code[0] == liste_veri9[3]:
            canvas.itemconfigure(liste_jeu2[8][0], fill = "grey")
        if liste_code[1] != liste_veri9[1] and liste_code[1] == liste_veri9[0] or liste_code[1] == liste_veri9[2] or liste_code[1] == liste_veri9[3]:
            canvas.itemconfigure(liste_jeu2[8][1], fill = "grey")
        if liste_code[2] != liste_veri9[2] and liste_code[2] == liste_veri9[0] or liste_code[2] == liste_veri9[1] or liste_code[2] == liste_veri9[3]:
            canvas.itemconfigure(liste_jeu2[8][2], fill = "grey")
        if liste_code[3] != liste_veri9[3] and liste_code[3] == liste_veri9[0] or liste_code[3] == liste_veri9[1] or liste_code[3] == liste_veri9[2]:
            canvas.itemconfigure(liste_jeu2[8][3], fill = "grey")
        
    if cdt == 9:
        if liste_code[0] == liste_veri10[0]:
            canvas.itemconfigure(liste_jeu2[9][0], fill = "red")
        if liste_code[1] == liste_veri10[1]:
            canvas.itemconfigure(liste_jeu2[9][1], fill = "red")
        if liste_code[2] == liste_veri10[2]:
            canvas.itemconfigure(liste_jeu2[9][2], fill = "red")
        if liste_code[3] == liste_veri10[3]:
            canvas.itemconfigure(liste_jeu2[9][3], fill = "red")
        
        if liste_code[0] != liste_veri10[0] and liste_code[0] == liste_veri10[1] or liste_code[0] == liste_veri10[2] or liste_code[0] == liste_veri10[3]:
            canvas.itemconfigure(liste_jeu2[9][0], fill = "grey")
        if liste_code[1] != liste_veri10[1] and liste_code[1] == liste_veri10[0] or liste_code[1] == liste_veri10[2] or liste_code[1] == liste_veri10[3]:
            canvas.itemconfigure(liste_jeu2[9][1], fill = "grey")
        if liste_code[2] != liste_veri10[2] and liste_code[2] == liste_veri10[0] or liste_code[2] == liste_veri10[1] or liste_code[2] == liste_veri10[3]:
            canvas.itemconfigure(liste_jeu2[9][2], fill = "grey")
        if liste_code[3] != liste_veri10[3] and liste_code[3] == liste_veri10[0] or liste_code[3] == liste_veri10[1] or liste_code[3] == liste_veri10[2]:
            canvas.itemconfigure(liste_jeu2[9][3], fill = "grey")

fenetre = tk.Tk()
fenetre.title("mastermind")
canvas = tk.Canvas(fenetre,height=500,width=500,bg = "white")
canvas.grid(row = 1,column= 1,rowspan = 10 ,columnspan= 4)
bouton_solo = tk.Button(fenetre, text = "mode solo", command= mode_solo)
bouton_solo.grid()
bouton_duo = tk.Button(fenetre, text = "mode duo", command= mode_duo)
bouton_duo.grid()
bouton_jeu1 = tk.Button(fenetre, text = "Essaie1", command=  Essaie1)
bouton_jeu1.grid(column=0,row=1)
bouton_jeu2 = tk.Button(fenetre, text = "Essaie2", command=  Essaie2)
bouton_jeu2.grid(column=0,row=2)
bouton_jeu3 = tk.Button(fenetre, text = "Essaie3", command=  Essaie3)
bouton_jeu3.grid(column=0,row=3)
bouton_jeu4 = tk.Button(fenetre, text = "Essaie4", command=  Essaie4)
bouton_jeu4.grid(column=0,row=4)
bouton_jeu5 = tk.Button(fenetre, text = "Essaie5", command=  Essaie5)
bouton_jeu5.grid(column=0,row=5)
bouton_jeu6 = tk.Button(fenetre, text = "Essaie6", command=  Essaie6)
bouton_jeu6.grid(column=0,row=6)
bouton_jeu7 = tk.Button(fenetre, text = "Essaie7", command=  Essaie7)
bouton_jeu7.grid(column=0,row=7)
bouton_jeu8 = tk.Button(fenetre, text = "Essaie8", command=  Essaie8)
bouton_jeu8.grid(column=0,row=8)
bouton_jeu9 = tk.Button(fenetre, text = "Essaie9", command=  Essaie9)
bouton_jeu9.grid(column=0,row=9)
bouton_jeu10 = tk.Button(fenetre, text = "Essaie10", command=  Essaie10)
bouton_jeu10.grid(column=0,row=10)
bouton_veri = tk.Button(fenetre, text = "Vérification", command=  verification)
bouton_veri.grid()
label_jeu = tk.Label(fenetre, text= "Cliquer pour effectuer un essaie \n Faites les  dans l'ordre")
label_veri = tk.Label(fenetre, text= "Vérification de la combinaison")
label_essaie = tk.Label(fenetre, text= "afffichage des essaies")
label_jeu.grid(row = 0, column= 0)
label_essaie.grid(row = 0, column= 1)
label_veri.grid(row= 0, column= 4)
affichage()
fenetre.mainloop()
