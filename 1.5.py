from tkinter import *
from tkinter.messagebox import *
import random
# A rajouter: un label qui donne le nombre de tours restants, tout le système de combis de scores, le système de  2,3,4... joueurs ET LES PUTAINS DE REGLES




def THEBLINK():
    Dé1.config(state=DISABLED)
    Dé2.config(state=DISABLED)
    Dé3.config(state=DISABLED)
    Dé4.config(state=DISABLED)
    Dé5.config(state=DISABLED)
    Coche1.set(0)
    Coche2.set(0)
    Coche3.set(0)
    Coche4.set(0)
    Coche5.set(0)
    Text1.set(0)
    Text2.set(0)
    Text3.set(0)
    Text4.set(0)
    Text5.set(0)
    BLancer.config(state=NORMAL, text="Lancer")
    Timer.set(0)
    Sommes=[0,0,0,0,0,0]
    Paire=[0,0,0,0,0,0]
    Brelan=[0,0,0,0,0,0]
    Carré=[0,0,0,0,0,0]
    Yams=[0,0,0,0,0,0]

def arreter():
    global attention
    global youpi
    attention.destroy()
    Jeu.destroy()

def messagedesortie():
    global attention
    attention=Tk()
    attention.title('Attention')
    attention.geometry('300x100+500+500')
    Texte=Label(attention,text='Voulez-vous vraiment quitter le jeu ?')
    Texte.grid(row=0)
    Oui=Button(attention,text='Oui',command=arreter)
    Non=Button(attention,text='Non',command=attention.destroy)
    Oui.grid(column=0,row=1,padx=10,pady=20)
    Non.grid(column=1,row=1,padx=10,pady=20)
    attention.mainloop()

def Rules():
    showinfo( "Règles", "Des Règles")

def Lancer1():
    if Coche1.get()==0:
        Dés[0]=random.randint(1,6)
        Lab1.config(text=Dés[0])
    if Coche2.get()==0:
        Dés[1]=random.randint(1,6)
        Lab2.config(text=Dés[1])
    if Coche3.get()==0:
        Dés[2]=random.randint(1,6)
        Lab3.config(text=Dés[2])
    if Coche4.get()==0:
        Dés[3]=random.randint(1,6)
        Lab4.config(text=Dés[3])
    if Coche5.get()==0:
        Dés[4]=random.randint(1,6)
        Lab5.config(text=Dés[4])
    Dé1.config(state=NORMAL)
    Dé2.config(state=NORMAL)
    Dé3.config(state=NORMAL)
    Dé4.config(state=NORMAL)
    Dé5.config(state=NORMAL)
    Timer.set(Timer.get()+1)
    print(Timer.get())
    if Timer.get()>0:
        BLancer.config(text="Relancer")
    if Timer.get()>2:
        BLancer.config(state=DISABLED)

def Tableaudesscores():
    global youpi, EntScore, BPaire, BBrelan, BCarré, BYams, Paire1,Paire2,Paire3,Paire4,Paire5,Paire6,Brelan1,Brelan2,Brelan3,Brelan4,Brelan5,Brelan6,Carré1,Carré2,BCarré3,BCarré4,BCarré5,BCarré6,BCarré2,BCarré3,BCarré4,BCarré5,BCarré6
    COMBIS()
    BLancer.config(state=DISABLED)
    youpi=Tk()
    youpi.title("Tableau des scores")
    youpi.geometry('390x500+500+500')
    Paire1=Checkbutton(youpi,text= 1, textvariable=1)
    Paire1.grid(row=1,column=0)
    Paire2=Checkbutton(youpi,text= 2, textvariable=2)
    Paire2.grid(row=1,column=1)
    Paire3=Checkbutton(youpi,text= 3,textvariable=3)
    Paire3.grid(row=1,column=2,)
    Paire4=Checkbutton(youpi,text= 4,textvariable=4)
    Paire4.grid(row=1,column=3,)
    Paire5=Checkbutton(youpi,text= 5, textvariable=5)
    Paire5.grid(row=1,column=4,)
    Paire6=Checkbutton(youpi,text= 6, textvariable=6)
    Paire6.grid(row=1,column=5)
    BPaire=Button(youpi,text="Paire", command=Mauvais1)
    BPaire.grid(row=1,column=6, pady=20,padx=5)
    Brelan1=Checkbutton(youpi, text=1, textvariable=1)
    Brelan1.grid(row=2,column=0)
    Brelan2=Checkbutton(youpi,text= 2, textvariable=2)
    Brelan2.grid(row=2,column=1)
    Brelan3=Checkbutton(youpi,text= 3, textvariable=3)
    Brelan3.grid(row=2,column=2)
    Brelan4=Checkbutton(youpi,text= 4, textvariable=4)
    Brelan4.grid(row=2,column=3)
    Brelan5=Checkbutton(youpi,text= 5, textvariable=5)
    Brelan5.grid(row=2,column=4)
    Brelan6=Checkbutton(youpi,text= 6, textvariable=6)
    Brelan6.grid(row=2,column=5)
    BBrelan=Button(youpi,text="Brelan", command=Mauvais2)
    BBrelan.grid(pady=20,padx=5,row=2,column=6)
    Carré1=Checkbutton(youpi,text=1, textvariable=1)
    Carré1.grid(row=3,column=0)
    Carré2=Checkbutton(youpi,text= 2, textvariable=2)
    Carré2.grid(row=3,column=1)
    Carré3=Checkbutton(youpi,text= 3,textvariable=3)
    Carré3.grid(row=3,column=2)
    Carré4=Checkbutton(youpi,text= 4,textvariable=4)
    Carré4.grid(row=3,column=3)
    Carré5=Checkbutton(youpi,text= 5, textvariable=5)
    Carré5.grid(row=3,column=4)
    Carré6=Checkbutton(youpi,text= 6, textvariable=6)
    Carré6.grid(row=3,column=5)
    BCarré=Button(youpi,text="Carré", command=Mauvais3)
    BCarré.grid(pady=20,padx=5,row=3,column=6)
    Yams1=Checkbutton(youpi,text=1, textvariable=1)
    Yams1.grid(row=4,column=0)
    Yams2=Checkbutton(youpi,text= 2, textvariable=2)
    Yams2.grid(row=4,column=1)
    Yams3=Checkbutton(youpi,text= 3, textvariable=3)
    Yams3.grid(row=4,column=2)
    Yams4=Checkbutton(youpi,text= 4, textvariable=4)
    Yams4.grid(row=4,column=3)
    Yams5=Checkbutton(youpi,text= 5, textvariable=5)
    Yams5.grid(row=4,column=4)
    Yams6=Checkbutton(youpi,text= 6, textvariable=6)
    Yams6.grid(row=4,column=5)
    BYams=Button(youpi,text="Yam's", command=Mauvais4)
    BYams.grid(pady=20,padx=5,row=4,column=6)
    BFull=Button(youpi,text="Full")
    BFull.grid(pady=20,padx=6,row=6,column=3)
    BPetite=Button(youpi,text="Petite suite", command=Mauvais3)
    BPetite.grid(pady=20,padx=5,row=7,column=1)
    BGrande=Button(youpi,text="Grande suite", command=Mauvais3)
    BGrande.grid(pady=20,padx=5,row=7,column=5)
    BChance=Button(youpi,text="Chance")
    BChance.grid(pady=20,padx=5,row=8,column=3)
    Oui()
    youpi.mainloop()


def Oui():
    x=0
    while x<=5:
        if Paire[x]==1:
            BPaire.config(command=Mauvais)
            if Paire1.cget()==0:
                if Paire1.cget(text)==x:
                    CALCULSAVON()
            if Paire2.get()==0:
                if Paire2.cget(text)==x:
                    CALCULSAVON()
            if Paire3.cget(text)==0:
                if Paire3.cget(text)==x:
                    CALCULSAVON()
            if Paire4.cget(text)==0:
                if Paire4.cget(text)==x:
                    CALCULSAVON()
            if Paire5.cget(text)==0:
                if Paire5.cget(text)==x:
                    CALCULSAVON()
            if Paire6.cget(text)==0:
                if Paire6.cget(text)==x:
                    CALCULSAVON()
        if Brelan[x]==1:
            BBrelan.config(command=Mauvais)
            if Brelan1.cget(text)==0:
                if Brelan1.cget(text)==x:
                    CALCULSAVON()
            if Brelan2.cget(text)==0:
                if Brelan2.cget(text)==x:
                    CALCULSAVON()
            if Brelan3.cget(text)==0:
                if Brelan3.cget(text)==x:
                    CALCULSAVON()
            if Brelan4.cget(text)==0:
                if Brelan4.cget(text)==x:
                    CALCULSAVON()
            if Brelan5.cget(text)==0:
                if Brelan5.cget(text)==x:
                    CALCULSAVON()
            if Brelan6.cget(text)==0:
                if Brelan6.cget(text)==x:
                    CALCULSAVON()
        if Carré[x]==1:
            BCarré.config(command=Mauvais)
            if Carré1.cget(text)==0:
                if Carré1.cget(text)==x:
                    CALCULSAVON()
            if Carré2.cget(text)==0:
                if Carré2.cget(text)==x:
                    CALCULSAVON()
            if Carré3.cget(text)==0:
                if Carré3.cget(text)==x:
                    CALCULSAVON()
            if Carré4.cget(text)==0:
                if Carré4.cget(text)==x:
                    CALCULSAVON()
            if Carré5.cget(text)==0:
                if Carré5.cget(text)==x:
                    CALCULSAVON()
            if Carré6.cget(text)==0:
                if Carré6.cget(text)==x:
                    CALCULSAVON()
        if Yams[x]==1:
            BYams.config(command=Mauvais)
            if Yams1.cget(text)==0:
                if Yams1.cget(text)==x:
                    CALCULSAVON()
            if Yams2.cget(text)==0:
                if Yams2.cget(text)==x:
                    CALCULSAVON()
            if Yams3.cget(text)==0:
                if Yams3.cget(text)==x:
                    CALCULSAVON()
            if Yams4.cget(text)==0:
                if Yams4.cget(text)==x:
                    CALCULSAVON()
            if Yams5.cget(text)==0:
                if Yams5.cget(text)==x:
                    CALCULSAVON()
            if Yams6.cget(text)==0:
                if Yams6.cget(text)==x:
                    CALCULSAVON()
        x=x+1


def Mauvais():
    showinfo("Attention!","Cette Combinaison n'est pas valide")
def Mauvais1():
    showinfo("Erreur","Il n'y a point de paire dans le jet final")
def Mauvais2():
    showinfo("Erreur","Il n'y a point de brelan dans le jet final")
def Mauvais3():
    showinfo("Erreur","Il n'y a point de carré dans le jet final")
def Mauvais4():
    showinfo("Erreur","Il n'y a point de yam's dans le jet final")
def Mauvais5():
    showinfo("Erreur","Il n'y a point de full dans le jet final")
def Mauvais6():
    showinfo("Erreur","Il n'y a point de petite suite dans le jet final")
def Mauvais7():
    showinfo("Erreur","Il n'y a point de grande suite dans le jet final")





def COMBIS():
    u=0
    j=0
    y=1
    w=0
    while y<=6:
        a=y-1
        print(a)
        while w<=4:
            if Dés[w]==y:
                u=u+1
            w=w+1
        if u>=2:
            Paire[a]=1
            if u>=3:
                Brelan[a]=1
                if u>=4:
                    Carré[a]=1
                    if u==5:
                        Yams[a]=1
        u=0
        w=0
        y=y+1





def CALCULSAVON():
    Score.set(Score.get()+25)
    print ("Score= ",Score.get())
    youpi.destroy()
    THEBLINK()


Dés=[0,0,0,0,0]
Sommes=[0,0,0,0,0,0]
Paire=[0,0,0,0,0,0]
Brelan=[0,0,0,0,0,0]
Carré=[0,0,0,0,0,0]
Yams=[0,0,0,0,0,0]

Jeu=Tk()
Timer=IntVar()
Score=IntVar()
Coche1=IntVar()
Coche2=IntVar()
Coche3=IntVar()
Coche4=IntVar()
Coche5=IntVar()


Jeu.title=("Yam's")

Entree=IntVar(Jeu)

Jeu.geometry('600x500+500+150')
Jeu.resizable(width=False, height=False)
Table =Frame(Jeu, borderwidth=6, relief=GROOVE, background= "green")

BRègles=Button(Jeu,text="Règles",fg='black', command= Rules)
BRègles.grid(sticky=W,padx=10,pady=10)
BQuitter=Button(Jeu, text="JPP", fg="red", command= messagedesortie)
BQuitter.grid(sticky=W,padx=10,pady=10)

Table.grid(ipadx= 200, ipady= 250)

Dé1=Checkbutton(Table, background= 'green',activebackground='green',variable=Coche1,state=DISABLED)
Dé1.grid(row=1,padx=20,column=0)
Dé2=Checkbutton(Table, background= 'green',activebackground='green',variable=Coche2,state=DISABLED)
Dé2.grid(row=1,padx=20,column=1)
Dé3=Checkbutton(Table, background= 'green',activebackground='green',variable=Coche3,state=DISABLED)
Dé3.grid(row=1,padx=20,column=2)
Dé4=Checkbutton(Table, background= 'green',activebackground='green',variable=Coche4,state=DISABLED)
Dé4.grid(row=1,padx=20,column=3)
Dé5=Checkbutton(Table, background= 'green',activebackground='green',variable=Coche5,state=DISABLED)
Dé5.grid(row=1,padx=20,column=4)

Lab1=Label(Table, text=Dés[0])
Lab1.grid(row=0,column=0,padx=20)
Lab2=Label(Table, text=Dés[1])
Lab2.grid(row=0,column=1,padx=20)
Lab3=Label(Table, text=Dés[2])
Lab3.grid(row=0,column=2,padx=20)
Lab4=Label(Table, text=Dés[3])
Lab4.grid(row=0,column=3,padx=20)
Lab5=Label(Table, text=Dés[4])
Lab5.grid(row=0,column=4,padx=20)

BLancer=Button(Table, text="Lancer", fg="blue", command=Lancer1)
BLancer.grid(row=3,column=0,padx=10,pady=10)
BTableau=Button(Table,text="Score",fg="blue",command=Tableaudesscores)
BTableau.grid(row=3,column=1,padx=10,pady=10)

Jeu.mainloop()