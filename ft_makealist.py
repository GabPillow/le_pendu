import sys
from tkinter import *
import settings

def ft_makelist():
    file = open("liste_francais.txt", "r")

    lines_list = []
    for line in file:
        stripped_line = line.strip()
        lines_list.append(stripped_line)

    return(lines_list)

def addimage(image):
    
    if settings.life == 9:
        image.canvas.create_image(image.basex, image.basey, image=image.base)
    if settings.life == 8:
        image.canvas.create_image(image.poteaux, image.poteauy, image=image.poteau)
    if settings.life == 7:
        image.canvas.create_image(image.barrex, image.barrey, image=image.barre)
    if settings.life == 6:
        image.canvas.create_image(image.ropex, image.ropey, image=image.rope)
    if settings.life == 5:
        image.canvas.create_image(image.headx, image.heady, image=image.head)
    if settings.life == 4:
        image.canvas.create_image(image.bodyx, image.bodyy, image=image.body)
    if settings.life == 3:
        image.canvas.create_image(image.leftarmx, image.leftarmy, image=image.leftarm)
    if settings.life == 2:
        image.canvas.create_image(image.rightarmx, image.rightarmy, image=image.rightarm)
    if settings.life == 1:
        image.canvas.create_image(image.leftlegx, image.leftlegy, image=image.leftleg)
    if settings.life == 0:
        image.canvas.create_image(image.rightlegx, image.rightlegy, image=image.rightleg)