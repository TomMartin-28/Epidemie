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
        if len(listeDegres) != self.n :
            print("listeDegres n'a pas le bon nombre de sommets")
            return 0

        nbEchecs = 0
        L = [i for i in range(self.n)]
        d = listeDegres.copy()
        print(d)
        
        while nbEchecs < N and len(L) != 0 :
            i = random.randint(0, (len(L) - 1))
            j = random.randint(0, (len(L) - 1))

            if i != j and self.estArete(L[i],L[j]) == False :
                self.ajoutArete(L[i], L[j])
                d[L[i]] -= 1
                d[L[j]] -= 1

                iSupp = False

                if d[L[i]] == 0 :
                    del L[i]
                    iSupp = True
                
                if i < j and iSupp == True:
                    del L[j-1]
                else :
                    del L[j]
                    
                nbEchecs = 0
            else :
                nbEchecs += 1

        if len(L) > V  :
            G = self.constructionGraphe(listeDegres, N, V)
        return 0

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
