import csv as csv
from grapheMatrice import *

with open('deezer_europe_edges.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)   
    g = GrapheMatrice(28281)
    for row in reader:
         g.ajoutArete(row['node_1'], row['node_2'])
    g.histogrammePareto(5, 20)