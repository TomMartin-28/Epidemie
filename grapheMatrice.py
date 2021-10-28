from graphe import *
import math

class GrapheMatrice(Graphe):
    def __init__(self,n):
        Graphe.__init__(self,n)
        self.matrice = [[0 for i in range(self.n)] for j in range(self.n)]

    def __str__(self):# permet d'afficher la matrice
        chaine = ""
        for i in range(self.n):
            for j in range(self.n):
                chaine+=str(self.matrice[i][j])+' '
            chaine += '\n'
        return chaine

    def voisinage(self,i):# renvoie la liste des voisins de i
        voisins = []
        # a completer
        for j in range(self.n) :
            if j != i :
                if self.matrice[i][j] == 1 :
                    voisins.append(j)

        return voisins

    def ajoutArete(self,i,j):# ajoute l'arete {i,j}
        #Graphe.ajoutArete(self,i,j)# on appelle la methode de la classe mere
        # a completer
        if self.estArete(i,j) == False and i != j:
            self.matrice[i][j] = 1
            self.matrice[j][i] = 1
            self.m += 1

    def estArete(self,i,j): # teste si {i,j} est une arete
        # a completer
        if self.matrice[i][j] == 1 :
            return True
        return False


#G1 = GrapheMatrice(10)
#G1.GNP(.5)
#print(G1.m)
#n = 500
#tabGNP = [0.001, 0.25, 0.305, 0.4005, 0.4555, 0.5, 0.6005, 0.6555, 0.75, 0.805, 0.999]
#for i in range(11) :
#    G1 = GrapheMatrice(n)
#    G2 = GrapheMatrice(n)
#    m = (n * (n-1))/2
#    G1.GNP(tabGNP[i])
#    G2.GNM(math.floor(m*tabGNP[i]))
#    chaine = "nbr d'aretes p = " + str(tabGNP[i]) + " : " + str(G1.m) + "\n" + "nbr d'aretes m = " + str(math.floor(m*tabGNP[i])) + " : " + str(G2.m)
#    print(chaine)

#G = GrapheMatrice(10)
#G.GNM(.5)
 #print(G)

g = GrapheMatrice(1000)
#vect = [np.random.randint(0, 10) for i in range(100)]
#g.constructionGraphe(ve, 10, 5)

g.histogrammePareto(4, 5)