from grapheMatrice import *
from graphe import *
import numpy.random as rd
from random import sample

import numpy as np
import matplotlib.pyplot as plt

class Epidemie(GrapheMatrice):
    def __init__(self, n, p, R, t) :
        GrapheMatrice.__init__(self, n)
        self.R = R
        self.nombreContaminations = [0 for i in range(self.n)]
        self.etat = [0 for i in range(self.n)]
        # 0 = non contaminé
        # 1 = contaminé
        # 2 à t+1 immunisé
        self.GNP(p) #met les voisins
        self.t = t
        self.dejaContamine = [0 for i in range(self.n)]
        

    def equitable(self):
        for i in range(self.n):
            x = rd.geometric(1/self.R)
            if x > len(self.voisinage(i)) :
                self.nombreContaminations[i] = len(self.voisinage(i))
            else :
                self.nombreContaminations[i] = x
    
    def contaminationVoisinage(self, i) :
        return sample(self.voisinage(i), self.nombreContaminations[i])

    def contaminationVoisins(self, i) :
        voisinCon = self.contaminationVoisinage(i)
        #print(str(i) + ":" + str(voisinCon) + ", "+ str(self.nombreContaminations[i]))
        for l in voisinCon :
            #print("l = " + str(l) + ": " + str(self.etat[l]))
            if self.etat[l] == 0 :
                self.etat[l] = -1
    
    def periode(self):
        contPer = 0
        dejaCont = 0
        for i in range(self.n) :
            if self.etat[i] == 1 :
                self.contaminationVoisins(i)
                self.etat[i] = 2
            elif self.etat[i] == -1 :
                self.etat[i] = 1
                self.dejaContamine[i] = 1
                contPer += 1
            elif self.etat[i] == self.t + 1 :
                self.etat[i] = 0
            elif self.etat[i] != 0:
                self.etat[i] +=1
                
            if self.dejaContamine[i] == 1:
                dejaCont += 1
        return [contPer, dejaCont]

    def initialisation(self, k):
        voisin = sample(range(self.n), k)
        for i in range(k) :
            j = voisin[i]
            self.etat[j] = 1
            self.dejaContamine[j] = 1

    def phase(self,k,l):
        contaminePeriode = [0 for i in range(l)]
        contamineDebut = [0 for i in range(l)]
        self.initialisation(k)
        self.equitable()
        for p in range(l):
            periode = self.periode()
            contaminePeriode[p] = periode[0]
            contamineDebut[p] = periode[1]

        return [contaminePeriode, contamineDebut]

    def courbeProgression(self, periode, contaminePeriode, contamineDebut) :
        plt.plot(range(periode), contaminePeriode, label="Nombre de contaminations")
        plt.plot(range(periode), contamineDebut, label="Cumul du nombre de contaminations")
        plt.legend(loc="upper left",fontsize="x-small")
        plt.xlabel("Période")
        plt.ylabel("Contaminations")
        plt.show()
    
    def listeDegres(self):
        list = [0 for i in range(self.n)]
        for i in range(0, self.n):
            list[i] = len(self.voisinage(i))
        return list

    def histogrammeVecteur(self,vecteur,nombreGroupes):
        plt.hist(vecteur,bins=nombreGroupes)
        plt.show()

    def histogrammeDegres(self, nombreGroupes):
        vect = np.array(self.listeDegres())
        self.histogrammeVecteur(vect, nombreGroupes)

    def constructionGraphe(self, listeDegres, N, V):
        g = GrapheMatrice(self.n)
        listeDegres.sort()
        sortedList = listeDegres.copy()
        finished = False
        temp = 0
        while not finished or temp < N:
            i = np.random.randint(len(sortedList)-1)
            j = np.random.randint(len(sortedList)-1)
            val_i = sortedList[i]
            val_j = sortedList[j]
            if val_i != val_j and not g.estArete(val_i, val_j):
                g.ajoutArete(val_i, val_j)
                sortedList.remove(val_i)
                sortedList.remove(val_j)
            if len(sortedList) == 0:
                finished = True
        print(g)
        print(g.m)
        print(V)
        if g.m > V:
            return self.constructionGraphe(listeDegres, N, V)
        return g


E = Epidemie(10, .4, 5.63, 5)
print(E.listeDegres())
print(E.constructionGraphe(E.listeDegres(), 15, 10))
