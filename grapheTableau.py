from graphe import *

class GrapheTableau(Graphe):
    def __init__(self,n):
        Graphe.__init__(self,n)
        self.voisins = [ [] for i in range(n)]# les listes des voisins sont vides au debut

    def __str__(self):# affiche les listes des voisins
        chaine = ''
        for i in range(self.n):
            chaine +="voisins de "+str(i)+" : "
            for j in self.voisins[i]:
                chaine+=str(j)+' '
            chaine+='\n'
        return chaine

    def voisinage(self,i):# on retourne la liste des voisins de i
       # a completer
       return self.voisins[i]

    def ajoutArete(self,i,j):
        #Graphe.ajoutArete(self,i,j)# on appelle la methode de la classe mere
        # a completer
        if self.estArete(i, j) == False and i != j:
            self.voisins[i].append(j)
            self.voisins[j].append(i)
            self.m += 1

    def estArete(self,i,j): # teste si {i,j} est une arete
        # a completer
        if j in self.voisins[i] :
            return True
        return False

n = 500
tabGNP = [0.001, 0.25, 0.305, 0.4005, 0.4555, 0.5, 0.6005, 0.6555, 0.75, 0.805, 0.999]
for i in range(11) :
    G1 = GrapheTableau(n)
    G2 = GrapheTableau(n)
    m = (n * (n-1))/2
    G1.GNP(tabGNP[i])
    G2.GNM(math.floor(m*tabGNP[i]))
    chaine = "nbr d'aretes p = " + str(tabGNP[i]) + " : " + str(G1.m) + "\n" + "nbr d'aretes m = " + str(math.floor(m*tabGNP[i])) + " : " + str(G2.m)
    print(chaine)
