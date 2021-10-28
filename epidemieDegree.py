import graphe
from grapheMatrice import *
from random import sample


class EpidemieDegree(GrapheMatrice):
    '''
    __init__\n
    n: nombre de sommets\n
    m: la plus petit valeur pour un degré d'un sommet (à utiliser avec la loi de pareto)\n
    M: le degré moyen d'un sommet\n
    q: la probabilité de transmission du virus\n
    N: nombre d'essais pour la construction du graphe (cf. Graphe.contructionGrahe)\n
    V: nombre d'arêtes du graphe à ne pas dépasser pour la construction du graphe (cf. Graphe.contructionGrahe)\n
    t: nombre d'étapes d'immunité
    k: nombre de personnes contaminées au début de l'épidémie
    l: temps de l'épidemie
    '''

    def __init__(self, n, m, M, q, N, V, t, k, l):
        GrapheMatrice.__init__(self, n)
        self.m = m
        self.M = M
        self.q = q
        self.listeDegree = self.pareto(m, M)
        self.constructionGraphe(self.listeDegree, N, V)
        self.nbContaminations = [0 for i in range(self.n)]
        self.nombreContaminations()

        self.etat = [0 for i in range(self.n)]
        # 0 = non contaminé
        # 1 = contaminé
        # 2 à t+1 immunisé
        self.t = t
        self.dejaContamine = [0 for i in range(self.n)]
        self.tab = self.phase(k, l)
        self.courbeProgression(l, self.tab[0], self.tab[1])

    def nombreContaminations(self):
        for i in range(self.n):
            self.nbContaminations[i] = int(self.q * self.listeDegree[i])

    def equitable(self):
        for i in range(self.n):
            if self.nbContaminations[i] > len(self.voisinage(i)):
                self.nbContaminations[i] = len(self.voisinage(i))

    """
    Selection de i voisins
    """
    def contaminationVoisinage(self, i) :
        return sample(self.voisinage(i), self.nbContaminations[i])

    """
    Selection de i voisins et changement de leur état
    """
    def contaminationVoisins(self, i) :
        voisinCon = self.contaminationVoisinage(i)
        for l in voisinCon:
            if self.etat[l] == 0 :
                self.etat[l] = -1

    """
    Changement des états de chaque personne pour une étape
    """
    def periode(self):
        contPer = 0
        dejaCont = 0
        for i in range(self.n):
            if self.etat[i] == 1:
                self.contaminationVoisins(i)
                self.etat[i] = 2
            elif self.etat[i] == -1:
                self.etat[i] = 1
                self.dejaContamine[i] = 1
                contPer += 1
            elif self.etat[i] == self.t + 1:
                self.etat[i] = 0
            elif self.etat[i] != 0:
                self.etat[i] += 1

            if self.dejaContamine[i] == 1:
                dejaCont += 1
        return [contPer, dejaCont]

    '''
    On contamine k personnes pour le lancement de l'épidémie
    '''
    def initialisation(self, k):
        voisin = sample(range(self.n), k)
        for i in range(k) :
            j = voisin[i]
            self.etat[j] = 1
            self.dejaContamine[j] = 1

    """
    Epidemie sur un temps l
    """
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

    """
    Affichage de la courbe de contamination
    periode: période (voir méthode periode())
    contaminePeriode: valeur retournée par phase()
    contamineDebut: valeur retournée par phase()
    """
    def courbeProgression(self, periode, contaminePeriode, contamineDebut) :
        plt.plot(range(periode), contaminePeriode, label="Nombre de contaminations")
        plt.plot(range(periode), contamineDebut, label="Cumul du nombre de contaminations")
        plt.legend(loc="upper left",fontsize="x-small")
        plt.xlabel("Période")
        plt.ylabel("Contaminations")
        plt.show()


e = EpidemieDegree(100, 3, 5, 0.4, 10, 7, 5, 10, 50)

