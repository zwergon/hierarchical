import csv
import networkx as nx
import matplotlib.pyplot as plt


def importGraph(filename):
    G = nx.Graph()
    link = {}

    with open(filename, 'r', encoding='iso8859-1') as csvfile:
        true_file = csv.reader(csvfile, dialect=csv.excel, delimiter=";")
        for row in true_file:

            key = row[0]
            if key.isdigit():
                G.add_node(key, name=row[1])
                links = []
                for i in range(2, len(row)):
                    ll = row[i]
                    if ll.isdigit():
                        links.append(row[i])
                link[key] = links

    for key in link.keys():
        for ll in link[key]:
            G.add_edge(key, ll)

    return G


def exportGraphToJSon(G, filename):

    file = open(filename, "w", encoding='utf-8')

    file.write("[\n")
    iNode = 1
    allNodes = G.nodes(data=True)
    for node, info in allNodes:
        file.write("{ \"name\": \"" + info['name'] + "\", \"imports\": \n[ ")

        adjancents = G.adj[node];
        i = 1
        for e in adjancents:
            file.write("\"" + G.nodes[e]['name'] + "\"")
            if i < len(adjancents):
                file.write(",")
            i += 1
        file.write("]\n}")
        if  iNode < len(allNodes):
            file.write(",")
        iNode += 1
    file.write("]")


G = importGraph("data/180402_liste_mots.csv")
exportGraphToJSon(G, "data/test.json")
