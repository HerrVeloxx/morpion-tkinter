from tkinter import *
import tkinter as tk #importe le module pour les interfaces graphiques
from tkinter import messagebox

class Morpion(tk.Tk): #crée le morpion en tant que classe
    def __init__(self): #crée un constructeur
        tk.Tk.__init__(self) #permet d'initialiser la fenêtre Tk dans la variable self
        self.size=325 #définit la taille du Canvas qui va servir de base et de grille
        self.nb_tours=0
        self.n_joueur=StringVar()
        self.creer_case()
        self.L=[[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
        self.fin_jeu=False

    def fin(self):
        self.bouton_rejouer=tk.Button(self, text="Rejouer", command=self.rejouer)
        self.bouton_rejouer.grid(padx=3, pady=3, row=0, column=0)
        self.bouton_quitter=tk.Button(self, text="Quitter", command=self.quitter)
        self.bouton_quitter.grid(padx=3, pady=3, row=0, column=1)
        self.bouton_rester=tk.Button(self, text="Rester", command=self.rester)
        self.bouton_rester.grid(padx=3, pady=3, row=0, column=2)

    def rejouer(self):
        self.destroy()
        jeu=Morpion()
        jeu.title("Tic Tac Toe")
        jeu.mainloop()

    def quitter(self):
        self.destroy()

    def rester(self):
        self.bouton_rejouer.destroy()
        self.bouton_quitter.destroy()
        self.bouton_rester.destroy()

    def tour_joueur(self):
        if self.nb_tours%2==0:
            self.n_joueur.set("Joueur 1")
        else:
            self.n_joueur.set("Joueur 2")

    def gagnant(self):
        for i in range(3):
            if self.L[i][0]==self.L[i][1]==self.L[i][2]!=" ":
                self.fin()
                self.joueur.destroy()
                self.fin_jeu=True
                if self.L[i][0]=="X":
                    messagebox.showinfo("Résultat", "Le joueur 1 a gagné !")
                    break
                elif self.L[i][0]=="O":
                	messagebox.showinfo("Résultat", "Le joueur 2 a gagné !")
                	break
            elif self.L[0][i]==self.L[1][i]==self.L[2][i]!=" ":
                self.fin()
                self.joueur.destroy()
                self.fin_jeu=True
                if self.L[0][i]=="X":
                    messagebox.showinfo("Résultat", "Le joueur 1 a gagné !")
                    break
                elif self.L[0][i]=="O":
                	messagebox.showinfo("Résultat", "Le joueur 2 a gagné !")
                	break
        if self.L[0][0]==self.L[1][1]==self.L[2][2]!=" " or self.L[0][2]==self.L[1][1]==self.L[2][0]!=" ":
            self.fin()
            self.joueur.destroy()
            self.fin_jeu=True
            if self.L[1][1]=="X":
                messagebox.showinfo("Résultat", "Le joueur 1 a gagné !")
            elif self.L[1][1]=="O":
                messagebox.showinfo("Résultat", "Le joueur 2 a gagné !")
        elif self.nb_tours==9 and self.fin_jeu==False:
            self.fin()
            self.joueur.destroy()
            messagebox.showinfo("Résultat", "Match nul !")

    def click1(self):
        self.bouton1.destroy()
        self.nb_tours +=1
        if self.nb_tours%2==0 :
            self.L[0][0]="O"
            self.case1.create_oval(15, 15, 85, 85, outline="blue", width=5)
        else :
            self.L[0][0]="X"
            self.case1.create_line(15, 15, 85, 85, fill="red", width=5)
            self.case1.create_line(85, 15, 15, 85, fill="red", width=5)
        self.tour_joueur()
        self.gagnant()
    def click2(self):
        self.bouton2.destroy()
        self.nb_tours +=1
        if self.nb_tours%2==0 :
            self.L[1][0]="O"
            self.case2.create_oval(15, 15, 85, 85, outline="blue", width=5)
        else :
            self.L[1][0]="X"
            self.case2.create_line(15, 15, 85, 85, fill="red", width=5)
            self.case2.create_line(85, 15, 15, 85, fill="red", width=5)
        self.tour_joueur()
        self.gagnant()
    def click3(self):
        self.bouton3.destroy()
        self.nb_tours +=1
        if self.nb_tours%2==0 :
            self.L[2][0]="O"
            self.case3.create_oval(15, 15, 85, 85, outline="blue", width=5)
        else :
            self.L[2][0]="X"
            self.case3.create_line(15, 15, 85, 85, fill="red", width=5)
            self.case3.create_line(85, 15, 15, 85, fill="red", width=5)
        self.tour_joueur()
        self.gagnant()
    def click4(self):
        self.bouton4.destroy()
        self.nb_tours +=1
        if self.nb_tours%2==0 :
            self.L[0][1]="O"
            self.case4.create_oval(15, 15, 85, 85, outline="blue", width=5)
        else :
            self.L[0][1]="X"
            self.case4.create_line(15, 15, 85, 85, fill="red", width=5)
            self.case4.create_line(85, 15, 15, 85, fill="red", width=5)
        self.tour_joueur()
        self.gagnant()
    def click5(self):
        self.bouton5.destroy()
        self.nb_tours +=1
        if self.nb_tours%2==0 :
            self.L[1][1]="O"
            self.case5.create_oval(15, 15, 85, 85, outline="blue", width=5)
        else :
            self.L[1][1]="X"
            self.case5.create_line(15, 15, 85, 85, fill="red", width=5)
            self.case5.create_line(85, 15, 15, 85, fill="red", width=5)
        self.tour_joueur()
        self.gagnant()
    def click6(self):
        self.bouton6.destroy()
        self.nb_tours +=1
        if self.nb_tours%2==0 :
            self.L[2][1]="O"
            self.case6.create_oval(15, 15, 85, 85, outline="blue", width=5)
        else :
            self.L[2][1]="X"
            self.case6.create_line(15, 15, 85, 85, fill="red", width=5)
            self.case6.create_line(85, 15, 15, 85, fill="red", width=5)
        self.tour_joueur()
        self.gagnant()
    def click7(self):
        self.bouton7.destroy()
        self.nb_tours +=1
        if self.nb_tours%2==0 :
            self.L[0][2]="O"
            self.case7.create_oval(15, 15, 85, 85, outline="blue", width=5)
        else :
            self.L[0][2]="X"
            self.case7.create_line(15, 15, 85, 85, fill="red", width=5)
            self.case7.create_line(85, 15, 15, 85, fill="red", width=5)
        self.tour_joueur()
        self.gagnant()
    def click8(self):
        self.bouton8.destroy()
        self.nb_tours +=1
        if self.nb_tours%2==0 :
            self.L[1][2]="O"
            self.case8.create_oval(15, 15, 85, 85, outline="blue", width=5)
        else :
            self.L[1][2]="X"
            self.case8.create_line(15, 15, 85, 85, fill="red", width=5)
            self.case8.create_line(85, 15, 15, 85, fill="red", width=5)
        self.tour_joueur()
        self.gagnant()
    def click9(self):
        self.bouton9.destroy()
        self.nb_tours +=1
        if self.nb_tours%2==0 :
            self.L[2][2]="O"
            self.case9.create_oval(15, 15, 85, 85, outline="blue", width=5)
        else :
            self.L[2][2]="X"
            self.case9.create_line(15, 15, 85, 85, fill="red", width=5)
            self.case9.create_line(85, 15, 15, 85, fill="red", width=5)
        self.tour_joueur()
        self.gagnant()
        
    def creer_case(self):
        self.tour_joueur()
        #création du label qui va annoncer le numéro du joueur
        self.joueur=tk.Label(self, textvariable=self.n_joueur, font=15)
        self.joueur.grid(row=0, column=0, columnspan=3)
        #récupère l'image et la rend utilisable par Tkinter
        self.blanc=tk.PhotoImage(file="blanc.gif")
        #création du Canvas qui va servir de grille
        self.cnv=tk.Canvas(self, width=self.size, height=self.size, bg="dark grey")
        self.cnv.grid(row=1, column=0, columnspan=3, rowspan=3)
        #création des Canvas qui vont servir à dessiner le symbole
        self.case1=tk.Canvas(self, width=100, height=100, bg="white")
        self.case1.grid(padx=2, pady=2, row=1)
        self.case2=tk.Canvas(self, width=100, height=100, bg="white")
        self.case2.grid(padx=2, pady=2, row=2)
        self.case3=tk.Canvas(self, width=100, height=100, bg="white")
        self.case3.grid(padx=2, pady=2, row=3)
        self.case4=tk.Canvas(self, width=100, height=100, bg="white")
        self.case4.grid(padx=2, pady=2, row=1, column=1)
        self.case5=tk.Canvas(self, width=100, height=100, bg="white")
        self.case5.grid(padx=2, pady=2, row=2, column=1)
        self.case6=tk.Canvas(self, width=100, height=100, bg="white")
        self.case6.grid(padx=2, pady=2, row=3, column=1)
        self.case7=tk.Canvas(self, width=100, height=100, bg="white")
        self.case7.grid(padx=2, pady=2, row=1, column=2)
        self.case8=tk.Canvas(self, width=100, height=100, bg="white")
        self.case8.grid(padx=2, pady=2, row=2, column=2)
        self.case9=tk.Canvas(self, width=100, height=100, bg="white")
        self.case9.grid(padx=2, pady=2, row=3, column=2)
        #création des boutons permettent de choisir une case
        self.bouton1=tk.Button(self, width=100, height=100, image=self.blanc, command=self.click1)
        self.bouton1.grid(padx=2, pady=2, row=1)
        self.bouton2=tk.Button(self, width=100, height=100, image=self.blanc, command=self.click2)
        self.bouton2.grid(padx=2, pady=2, row=2)
        self.bouton3=tk.Button(self, width=100, height=100, image=self.blanc, command=self.click3)
        self.bouton3.grid(padx=2, pady=2, row=3)
        self.bouton4=tk.Button(self, width=100, height=100, image=self.blanc, command=self.click4)
        self.bouton4.grid(padx=2, pady=2, row=1, column=1)
        self.bouton5=tk.Button(self, width=100, height=100, image=self.blanc, command=self.click5)
        self.bouton5.grid(padx=2, pady=2, row=2, column=1)
        self.bouton6=tk.Button(self, width=100, height=100, image=self.blanc, command=self.click6)
        self.bouton6.grid(padx=2, pady=2, row=3, column=1)
        self.bouton7=tk.Button(self, width=100, height=100, image=self.blanc, command=self.click7)
        self.bouton7.grid(padx=2, pady=2, row=1, column=2)
        self.bouton8=tk.Button(self, width=100, height=100, image=self.blanc, command=self.click8)
        self.bouton8.grid(padx=2, pady=2, row=2, column=2)
        self.bouton9=tk.Button(self, width=100, height=100, image=self.blanc, command=self.click9)
        self.bouton9.grid(padx=2, pady=2, row=3, column=2)
        
jeu=Morpion()
jeu.title("Tic Tac Toe") #nomme la fenêtre
jeu.mainloop() #lance le GUI
