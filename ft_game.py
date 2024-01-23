import sys
from tkinter import *
import settings
from ft_makealist import *
import tkinter.messagebox as tkmb

def verificating(letter, answer):

    verif = False
    index = 1

    for l in answer:
        for lb in letter:
            if l == lb:
                verif = True
                settings.PlayerAnswer = settings.PlayerAnswer[:index] + l + settings.PlayerAnswer[index + 1:]
        index = index + 2
    return(verif)

def playing(letter, phrases, Answer, Button, image):
    if verificating(letter, Answer) == False:
        settings.life = settings.life - 1
        phrases.intro.set("Le mot que tu dois trouver contient "+str(len(Answer))+" lettres.\nTu as "+str(settings.life)+\
    " vie.\nLe jeu se termine quand tes vies atteignent zéro ou si tu trouves le mot.")
        addimage(image)
        if settings.life == 0:
            tkmb.showinfo("GAME OVER", "Vous avez échoué le mot était " + Answer)
    phrases.PlayerAnswerWin.set(settings.PlayerAnswer)
    Button["state"] = "disabled"