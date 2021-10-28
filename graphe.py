#coding:utf8
import random
import math

import numpy as np
import matplotlib.pyplot as plt
#from grapheMatrice import *

class Graphe(object): # classe abstraite
    def __init__(self,n):
        self.n = n #nombre de sommets
        self.m = 0 #nombre d'arêtes

    def __str__(self):# permet l'affichage du graphe
       pass # à compléter dans la classe dérivée

    def voisinage(self,i): # retourne une liste contenant les sommets voisins du sommet i
        pass # à compléter dans la classe dérivée

    def estArete(self,i,j): # teste si {i,j} est une arête
        pass # à compléter dans la classe dérivée

    def ajoutArete(self,i,j): # ajoute l'arête {i,j}
        pass
        #à compléter dans la classe dérivée

    def GNP(self,p): # ajoute des arêtes avec le modèle GNP
        # a compléter
        if p > 0 and p < 1 :
            for i in range(self.n) :
                for j in range(i+1, self.n) :
                    rand = random.random()
                    if rand < p :
                        self.ajoutArete(i, j)

    def GNM(self,m): # ajoute m arêtes avec le modèle GNM
        # a compléter
        while self.m < m :
            i = random.randint(0, self.n -1)
            j = random.randint(0, self.n - 1)

            if self.estArete(i, j) == False and i != j:
                self.ajoutArete(i, j)

    """def histogrammeDegres(self,nombreGroupes):
        population = np.array([len(self.voisinage(i)) for i in range(self.n)])
        plt.hist(population,bins=nombreGroupes)
        plt.show()"""

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
        listeDegres.sort()
        sortedList = listeDegres.copy()
        finished = False
        temp = 0
        while not finished and temp < N:
            i = np.random.randint(len(sortedList)-1)
            j = np.random.randint(len(sortedList)-1)
            val_i = sortedList[i]
            val_j = sortedList[j]
            if val_i != val_j and not self.estArete(val_i, val_j):
                self.ajoutArete(val_i, val_j)
                sortedList.remove(val_i)
                sortedList.remove(val_j)
            else:
                temp+=1
            if len(sortedList) == 0:
                finished = True
        print(V)
        if self.m > V:
            self.constructionGraphe(listeDegres, N, V)

    def pareto(self, m, M):
        if m > 0 and M > 0:
            a = M/(M-m)
            return (np.random.pareto(a, self.n) + 1)* m
        return None

    def histogrammePareto(self, m, M):
        a = M/(M-m)
        count, bins, _ = plt.hist(self.pareto(m, M), 100, density=True)
        fit = a*m**a / bins**(a+1)
        plt.plot(bins, max(count)*fit/max(fit), linewidth=2, color='r')
        plt.show()