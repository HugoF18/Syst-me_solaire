"""
Simulation du système solaire avec les planètes : Venus, Terre, Mars, Jupiter, Saturne
Ecriture dans différent fichier csv :
- position de la planète en fonction du jour
-distance entre la Terre et la planète en question
+ Affichage de la distance min entre la terre et la planète en question
"""
# -------------------Appel des bibliotheques--------------
from tkinter import *
import tkinter
import math
import csv
# -------------------------------------------------------

# ---------------------création des fonctions nécessaires-------------
def Distance(x1, y1, x2, y2):  # permet de calculer la distance entre 2 points
    return math.sqrt((y2 - y1) ** 2 + (x2 - x1) ** 2)


def _create_circle(self, x, y, r, **kwargs):  # Permet de créer des cercles plus facilement
    return self.create_oval(x - r, y - r, x + r, y + r, **kwargs)


tkinter.Canvas.create_circle = _create_circle  # permet d'intégrer à tkinter la fonction creat_circle
# ------------------------------------------------------------------

#------------------------------code principal----------------------
flag = 0  # commutateur


class Application(Tk):  # Classe permettant de créer une fenètre Tkinter
    def __init__(self):  # initialisation de l'appli
        Tk.__init__(self)  # constructeur de la classe parente
        self.can = Canvas(self, width=1200, height=800, bg="#000354")  # création de la fenêtre
        self.can.pack(side=LEFT, padx=5, pady=5)
        self.can.create_circle(400, 400, 10, fill="yellow")  # Création du soleil sur l'appli
        Button(self, text="planète", command=self.planète).pack(side=TOP)  # Boutton appelant la fonction planete
        Button(self, text="trajectoire", command=self.trajectoire).pack(
            side=TOP)  # Boutton appelant la fonction trajectoire
        Button(self, text="mouvement", command=self.mouvement).pack(side=TOP)  # Boutton appelant la fonction mouvement
        Button(self, text="stop", command=self.stop_it).pack(side=TOP)  # Boutton appelant la fonction stop_it
        Button(self, text="clear", command=self.effacer).pack(side=TOP)  # Boutton appelant la fonction effacer

    def planète(self):  # fonction permettant d'appeler les planètes
        """ la classe planète a besoin de 8 variables (Nom de la planete, masse de la planète, distance de la planete en 10^8 km
         , la période que la planète a besoin pour faire un tour complet, la périhélie de l'ellipse, l'anaphélie de l'ellpise
         , le canvas où il faut appliquer le dessin , la couleur de la planète sur le canvas"""
        self.Venus = Planète("Venus", 0.82, 1.08, 224.7, 1.07, 1.09, self.can, "blue")
        self.Terre = Planète("Terre", 1.00, 1.50, 365.3, 1.47, 1.52, self.can, "green")
        self.Mars = Planète("Mars", 0.11, 2.28, 687.0, 2.07, 2.49, self.can, "red")
        self.Jupiter = Planète("Jupiter", 339.42, 7.78, 4332.6, 7.40, 8.15, self.can, "yellow")
        self.Saturne = Planète("Saturne", 107.45, 14.27, 10759, 13.52, 15.14, self.can, "white")

    def trajectoire(self):  # fonction permettant de dessiner les trajectoires des planètes
        self.Venus.trajectoir()  # appel de la trajectoire de Venus
        self.Terre.trajectoir()  # appel de la trajectoire de la Terre
        self.Mars.trajectoir()  # appel de la trajectoire de Mars
        self.Jupiter.trajectoir()  # appel de la trajectoire de Jupiter
        self.Saturne.trajectoir()  # appel de la trajectoire de Saturne

    def mouvement(self):  # fonction permettant d'appliquer les mouvements au planètes
        global flag  # appel d'une variable globale

        if flag == 0:  # pour ne lancer qu'une seule boucle
            flag = 1
        self.Venus.move()  # appel de la fonction permettant de faire bouger la planète Venus
        self.Terre.move()  # appel de la fonction permettant de faire bouger la planète Terre
        self.Mars.move()  # appel de la fonction permettant de faire bouger la planète Mars
        self.Jupiter.move()  # appel de la fonction permettant de faire bouger la planète Jupiter
        self.Saturne.move()  # appel de la fonction permettant de faire bouger la planète Saturne

    def stop_it(self):  # fonction permettant d'affecter la variable globale flag ce qui permet de stopper l'animation
        global flag
        flag = 0

    def effacer(self): # fonction permettant d'effacer les contenus des fichiers csv

        f = open("Jupiter.csv", "w") #ouvrir le fichier de la planète jupiter
        f.truncate() #efface le contenu du fichier csv Jupiter
        f.close() #fermer le fichier csv de la planète

        f = open("Mars.csv", "w") #ouvrir le fichier de la planète
        f.truncate() #efface le contenu du fichier csv Mars
        f.close()#fermer le fichier csv de la planète

        f = open("Saturne.csv", "w") #ouvrir le fichier de la planète
        f.truncate() #efface le contenu du fichier csv Saturne
        f.close()#fermer le fichier csv de la planète

        f = open("Terre.csv", "w")#ouvrir le fichier de la planète
        f.truncate()#efface le contenu du fichier csv Terre
        f.close()#fermer le fichier csv de la planète

        f = open("Venus.csv", "w")#ouvrir le fichier de la planète
        f.truncate()#efface le contenu du fichier csv Venus
        f.close()#fermer le fichier csv de la planète

class Planète():
    def __init__(self, nom, masse, distance, période, périhélie, aphélie, canev, colors):
        self.name = nom  # nom de la planete
        self.mass = masse  # masse de la planete
        self.distance = distance  # distance de ka planete
        self.période = période  # periode d'une planete
        self.périhélie = périhélie #périhélie de la trajectoire de la planète
        self.aphélie = aphélie  #aphélie de la trajectoire de la planète
        self.coefficientdangle = 2 * math.pi / round(période)  # révolution de la planète (permet d'obtenir l'angle de la planete)
        self.canev = canev  # canvas sur lequel appliquer

        self.grandaxe= (périhélie + aphélie)/2  #création d'une variable permettant de sauvegarder la longueur du grand axe de l'ellipse de la trajectoire de la planète
        self.écartcentre= (aphélie-périhélie)/2 #création de la variable permettant de trouver le centre de l'ellipse de la trajectoire de la planète par rapport au soleil, un des foyers de l'ellipse représentant la trajectoire
        self.petitaxe= (math.sqrt(self.grandaxe**2-self.écartcentre**2))/2 #création d'une variable permettant de sauvegarder la longueur du petit axe de l'ellipse de la trajectoire de la planète

        self.planète = self.canev.create_circle((distance+self.écartcentre) * 20 + 400, 400, masse / 20, fill=colors)  # création du canvas représentant la planète
        self.t = 0  # variable permettant de sauvegarder l'angle de la planète
        self.jour = 0  # variable permettant d'obtenir le jour


        self.angleT=0 # variable permettant de sauvegarder l'angle de la planète
        self.revoT= 2 * math.pi / 365 #révolution de la Terre
        self.distT= 1.50 #distance terre soleil
        self.périhélieT =1.47#périhélie de la trajectoire de la Terre
        self.aphélieT= 1.52  #aphélie de la trajectoire de la Terre
        self.grandaxeT = (self.périhélieT + self.aphélieT) / 2 #création d'une variable permettant de sauvegarder la longueur du grand axe de l'ellipse de la trajectoire de la Terre
        self.écartcentreT = (self.aphélieT - self.périhélieT) / 2#création de la variable permettant de trouver le centre de l'ellipse de la trajectoire de la Terre par rapport au soleil, un des foyers de l'ellipse représentant la trajectoire
        self.petitaxeT = (math.sqrt(self.grandaxeT ** 2 - self.écartcentreT ** 2)) / 2#création d'une variable permettant de sauvegarder la longueur du petit axe de l'ellipse de la trajectoire de la Terre

        self.distPtmin= 100000000 # variable permettant d'enregistrer la distance la plus petite entre la Terre et la planète

    def trajectoir(self):  # fonction permettant de dessiner l'ellipse la trajectoir de la planète
        self.canev.create_oval((400+self.écartcentre) - (self.grandaxe+self.écartcentre) * 20,(400+self.écartcentre) + (self.petitaxe+self.écartcentre) * 20, (400+self.écartcentre) + (self.grandaxe+self.écartcentre) * 20,
                               (400+self.écartcentre) - (self.petitaxe+self.écartcentre) * 20, fill="", outline="#3154A1")

    def move(self):
        "déplacement de la planete"
        global flag
        if flag > 0: #condition de démarrage
            self.t += self.coefficientdangle  #ajout du coefficent pour obtenir l'angle du jour d'après de la planete en question
            self.angleT+= self.revoT #ajout du coefficent pour obtenir l'angle du jour d'après de la Terre
            x1 = (400+self.écartcentre) + (self.grandaxe+self.écartcentre) * 20 * math.cos(self.t)  # formule permettant de trouver la position x d'une planète en fonction de l'angle t
            y1 = (400+self.écartcentre) + (self.petitaxe+self.écartcentre) * 20 * math.sin(self.t)  # formule permettant de trouver la position y d'une planète en fonction de l'angle t
            self.jour += 1
            x0=  (400+self.écartcentreT) + (self.grandaxeT+self.écartcentreT) * 20 * math.cos(self.angleT) # formule permettant de trouver la position x de la terre en fonction de l'angle
            y0=  (400+self.écartcentreT) + (self.petitaxeT+self.écartcentre) * 20 * math.sin(self.angleT) # formule permettant de trouver la position y de la terre en fonction de l'angle
            ecart= Distance(x0,y0,x1,y1) # ecart de distance entre la Terre et la planète
            if self.jour > round(self.période):  # permet de réinitialiser le jour de la planète lorsqu'il termine son tour
                self.jour = self.jour - round(self.période)
            if ecart < self.distPtmin: #permet de mettre à jour la distance min entre la Terre et la planète en comparant la valeur actuelle avec la valeur précédemment enregistrer
                self.distPtmin= ecart
                Tterre= self.angleT//self.revoT
                anneeT= Tterre// 365
                jourT= Tterre % 365
                print("nouvelle distance min Terre -",self.name,"est de",ecart,"10^8 km à T de la planète=",self.jour,"et T de la Terre=", Tterre,"soit le jour ",jourT,"de l'année",anneeT )
                print("")
            nom = self.name + ".csv"

            with open(nom, 'a', newline='') as csvfile:  # ajout des résultats dans un fichier csv
                spamwriter = csv.writer(csvfile, delimiter=' ',
                                        quotechar='|', quoting=csv.QUOTE_MINIMAL)
                spamwriter.writerow(["position x y:", x1, y1, "au jour de la planete", self.jour])
                spamwriter.writerow(["distance Terre planete=",ecart,"10^8 km"])
                spamwriter.writerow([""])

            self.canev.coords(self.planète, x1 - 15, y1 - 15, x1 + 15,
                              y1 + 15)  # changement des coordonnées de la planete pour le faire déplacer
            self.canev.after(5, self.move)  # appel de la fonction deplacement pour creer le "mouvement"


app = Application()
app.mainloop()  # appel de la fenêtre Tkinter et de ses applications
#------------------------------------------------------------------