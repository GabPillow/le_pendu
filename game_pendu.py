from tkinter import *
import random
from ft_makealist import *
from ft_game import *
import settings

Answer = random.choice(ft_makelist())
settings.init()

for lettre in Answer:
    if lettre != '-' and lettre != ' ':
        settings.PlayerAnswer = settings.PlayerAnswer + " _"

fenetre = Tk()

fenetre.geometry("1000x700")
fenetre.title("Pendu")
class labelphrases:
    intro = StringVar()
    PlayerAnswerWin = StringVar()

class images:
    head = PhotoImage(file="head.png")
    headx = 213
    heady = 256
    body = PhotoImage(file="body.png")
    bodyx = 215
    bodyy = 328
    barre = PhotoImage(file="barre.png")
    barrex = 320
    barrey = 165
    base = PhotoImage(file="base.png")
    basex = 425
    basey = 445
    leftarm = PhotoImage(file="leftarm.png")
    leftarmx = 180
    leftarmy = 337
    rightarm = PhotoImage(file="rightarm.png")
    rightarmx = 240
    rightarmy = 337
    leftleg = PhotoImage(file="leftleg.png")
    leftlegx = 223
    leftlegy = 423
    rightleg = PhotoImage(file="rightleg.png")
    rightlegx = 224
    rightlegy = 423
    poteau = PhotoImage(file="poteau.png")
    poteaux = 435
    poteauy = 338
    rope = PhotoImage(file="rope.png")
    ropex = 210
    ropey = 206
    canvas = Canvas(fenetre, bg='white', width=520, height=1000)

images.canvas.pack(anchor=W)

fenetre['bg']='white'

Frame1 = Frame(fenetre, borderwidth=2, relief=GROOVE)
Frame1.place(x=520, y=0)

Label(Frame1, textvariable=labelphrases.intro).pack()

TopFrame = Frame(Frame1)
BottFrame = Frame(Frame1)
BottFrameb = Frame(Frame1)
BottFramec = Frame(Frame1)
TopFrame.pack(side=TOP, pady=20)
BottFrame.pack(side=TOP, pady=5)
BottFrameb.pack(side=TOP, pady=5)
BottFramec.pack(side=BOTTOM, pady=5)

labelphrases.intro.set("Le mot que tu dois trouver contient "+str(len(Answer))+" lettres.\nTu as "+str(settings.life)+\
    " vie.\nLe jeu se termine quand tes vies atteignent zéro ou si tu trouves le mot.")

label1 = Label(Frame1, textvariable=labelphrases.PlayerAnswerWin, font=(40))
label1.pack(in_=TopFrame)

labelphrases.PlayerAnswerWin.set(settings.PlayerAnswer)

AButton = Button(Frame1, text ='A', command = lambda: playing("Aaâà", labelphrases, Answer, AButton, images), font="20", width=1)
AButton.pack(in_=BottFrame, side=LEFT, padx=3)
BButton = Button(Frame1, text ='B', command = lambda: playing("Bb", labelphrases, Answer, BButton, images), font="20", width=1)
BButton.pack(in_=BottFrame, side=LEFT, padx=3)
CButton = Button(Frame1, text ='C', command = lambda: playing("Ccç", labelphrases, Answer, CButton, images), font="20", width=1)
CButton.pack(in_=BottFrame, side=LEFT, padx=3)
DButton = Button(Frame1, text ='D', command = lambda: playing("Dd", labelphrases, Answer, DButton, images), font="20", width=1)
DButton.pack(in_=BottFrame, side=LEFT, padx=3)
EButton = Button(Frame1, text ='E', command = lambda: playing("Eeêëéè", labelphrases, Answer, EButton, images), font="20", width=1)
EButton.pack(in_=BottFrame, side=LEFT, padx=3)
FButton = Button(Frame1, text ='F', command = lambda: playing("Ff", labelphrases, Answer, FButton, images), font="20", width=1)
FButton.pack(in_=BottFrame, side=LEFT, padx=3)
GButton = Button(Frame1, text ='G', command = lambda: playing("Gg", labelphrases, Answer, GButton, images), font="20", width=1)
GButton.pack(in_=BottFrame, side=LEFT, padx=3)
HButton = Button(Frame1, text ='H', command = lambda: playing("Hh", labelphrases, Answer, HButton, images), font="20", width=1)
HButton.pack(in_=BottFrame, side=LEFT, padx=3)
IButton = Button(Frame1, text ='I', command = lambda: playing("Iiï", labelphrases, Answer, IButton, images), font="20", width=1)
IButton.pack(in_=BottFrame, side=LEFT, padx=3)
JButton = Button(Frame1, text ='J', command = lambda: playing("Jj", labelphrases, Answer, JButton, images), font="20", width=1)
JButton.pack(in_=BottFrame, side=LEFT, padx=3)
KButton = Button(Frame1, text ='K', command = lambda: playing("Kk", labelphrases, Answer, KButton, images), font="20", width=1)
KButton.pack(in_=BottFrameb, side=LEFT, padx=3)
LButton = Button(Frame1, text ='L', command = lambda: playing("Ll", labelphrases, Answer, LButton, images), font="20", width=1)
LButton.pack(in_=BottFrameb, side=LEFT, padx=3)
MButton = Button(Frame1, text ='M', command = lambda: playing("Mm", labelphrases, Answer, MButton, images), font="20", width=1)
MButton.pack(in_=BottFrameb, side=LEFT, padx=3)
NButton = Button(Frame1, text ='N', command = lambda: playing("Nn", labelphrases, Answer, NButton, images), font="20", width=1)
NButton.pack(in_=BottFrameb, side=LEFT, padx=3)
OButton = Button(Frame1, text ='O', command = lambda: playing("Ooô", labelphrases, Answer, OButton, images), font="20", width=1)
OButton.pack(in_=BottFrameb, side=LEFT, padx=3)
PButton = Button(Frame1, text ='P', command = lambda: playing("Pp", labelphrases, Answer, PButton, images), font="20", width=1)
PButton.pack(in_=BottFrameb, side=LEFT, padx=3)
QButton = Button(Frame1, text ='Q', command = lambda: playing("Qq", labelphrases, Answer, QButton, images), font="20", width=1)
QButton.pack(in_=BottFrameb, side=LEFT, padx=3)
RButton = Button(Frame1, text ='R', command = lambda: playing("Rr", labelphrases, Answer, RButton, images), font="20", width=1)
RButton.pack(in_=BottFrameb, side=LEFT, padx=3)
SButton = Button(Frame1, text ='S', command = lambda: playing("Ss", labelphrases, Answer, SButton, images), font="20", width=1)
SButton.pack(in_=BottFrameb, side=LEFT, padx=3)
TButton = Button(Frame1, text ='T', command = lambda: playing("Tt", labelphrases, Answer, TButton, images), font="20", width=1)
TButton.pack(in_=BottFrameb, side=LEFT, padx=3)
UButton = Button(Frame1, text ='U', command = lambda: playing("Uuûü", labelphrases, Answer, UButton, images), font="20", width=1)
UButton.pack(in_=BottFramec, side=LEFT, padx=3)
VButton = Button(Frame1, text ='V', command = lambda: playing("Vv", labelphrases, Answer, VButton, images), font="20", width=1)
VButton.pack(in_=BottFramec, side=LEFT, padx=3)
WButton = Button(Frame1, text ='W', command = lambda: playing("Ww", labelphrases, Answer, WButton, images), font="20", width=1)
WButton.pack(in_=BottFramec, side=LEFT, padx=3)
XButton = Button(Frame1, text ='X', command = lambda: playing("Xx", labelphrases, Answer, XButton, images), font="20", width=1)
XButton.pack(in_=BottFramec, side=LEFT, padx=3)
YButton = Button(Frame1, text ='Y', command = lambda: playing("Yy", labelphrases, Answer, YButton, images), font="20", width=1)
YButton.pack(in_=BottFramec, side=LEFT, padx=3)
ZButton = Button(Frame1, text ='Z', command = lambda: playing("Zz", labelphrases, Answer, ZButton, images), font="20", width=1)
ZButton.pack(in_=BottFramec, side=LEFT, padx=3)

fenetre.mainloop()