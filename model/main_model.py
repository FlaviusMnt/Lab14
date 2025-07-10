from database.DAO import DAO
import networkx as nx
import copy

class Model:
    def __init__(self):
        self._nodes = []
        self._edges = []
        self._grafo = nx.DiGraph()

        self.mappaOrderId = {}

    def getAllStores(self):
        return DAO.getAllStores()

    def buildGraph(self,store,numeroGiorniK):
        self._grafo.clear()
        self._nodes = []
        self._edges = []
        self.mappaOrderId = {}

        self._nodes = DAO.getAllNodes(store)
        for nodo in self._nodes:
            self.mappaOrderId[nodo.order_id] = nodo
        self._grafo.add_nodes_from(self._nodes)

        self._edges = DAO.getAllEdges(store,numeroGiorniK,self.mappaOrderId)
        for arco in self._edges:
            self._grafo.add_edge(arco[0],arco[1], weight = arco[2])

    def get_num_of_nodes(self):
        return self._grafo.number_of_nodes()
    def get_num_of_edges(self):
        return self._grafo.number_of_edges()

    def get_nodes(self):
        return list(self._grafo.nodes())
    def get_edges(self):
        return list(self._grafo.edges(data=True))

    # def trovaPercorsoMassimo(self, N):
    #     self._best_peso = 0
    #     self._best_percorso = []
    #
    #     for nodo in self._grafo.nodes:
    #         self._ricorsione([nodo], 0, N)
    #
    #     return self._best_percorso, self._best_peso
    #
    # def _ricorsione(self, parziale, peso_attuale, N):
    #     if len(parziale) == N + 1:
    #         # controllo chiusura ciclo
    #         if parziale[0] == parziale[-1]:
    #             if peso_attuale > self._best_peso:
    #                 self._best_peso = peso_attuale
    #                 self._best_percorso = list(parziale)  # copia
    #         return
    #
    #     ultimo = parziale[-1]
    #     for vicino in self._grafo.neighbors(ultimo):
    #         if vicino not in parziale:
    #             # lo posso aggiungere se non è stato ancora visitato
    #             peso = self._grafo[ultimo][vicino]["weight"]
    #             parziale.append(vicino)
    #             self._ricorsione(parziale, peso_attuale + peso, N)
    #             parziale.pop()
    #         elif vicino == parziale[0] and len(parziale) == N:
    #             # chiusura del ciclo esattamente all’N-esimo arco
    #             peso = self._grafo[ultimo][vicino]["weight"]
    #             parziale.append(vicino)
    #             self._ricorsione(parziale, peso_attuale + peso, N)
    #             parziale.pop()





    # def getBestPath(self, startStr):
    #     self._bestPath = []  # cammino migliore trovato finora
    #     self._bestScore = 0 # punteggio (somma dei pesi) del cammino migliore
    #
    #     start = self._idMap[int(startStr)]  # converte l'ID da stringa a nodo vero e proprio
    #
    #     parziale = [start] # cammino attuale in costruzione
    #
    #     vicini = self._graph.neighbors(start) # vicini del nodo iniziale
    #     for v in vicini:
    #         parziale.append(v)
    #         self._ricorsione(parziale) # avvia la ricorsione
    #         parziale.pop() # backtracking
    #
    #     return self._bestPath, self._bestScore

    # def _ricorsione(self, parziale):
    #     if self.getScore(parziale) > self._bestScore:  # *** Se il punteggio attuale è migliore del migliore trovato finora
    #         self._bestScore = self.getScore(parziale)  # *** Aggiorna il punteggio migliore
    #         self._bestPath = copy.deepcopy(parziale)   # *** Salva una copia del cammino migliore (deepcopy evita modifiche future)
    #
    #     for v in self._graph.neighbors(parziale[-1]):   # *** Per ogni vicino del nodo corrente (ultimo nel cammino)
    #         if (v not in parziale and #check if not in parziale   # *** Se il vicino non è già nel cammino (per evitare cicli)
    #                 self._graph[parziale[-2]][parziale[-1]]["weight"] >   # *** E se il peso dell'arco precedente è maggiore di quello nuovo
    #                 self._graph[parziale[-1]][v]["weight"]): #check if peso nuovo arco è minore del precedente # *** (cioè: il peso decresce lungo il cammino)
    #             parziale.append(v)   # *** Aggiunge il nodo al cammino attuale
    #             self._ricorsione(parziale)  # *** Chiama ricorsivamente per continuare l’esplorazione
    #             parziale.pop()  # *** Backtracking: rimuove l’ultimo nodo per provare altri percorsi
    #
    # def getScore(self, listOfNodes):
    #     tot = 0  # *** Inizializza il punteggio totale a zero
    #     for i in range(len(listOfNodes) - 1):  # *** Scorre ogni coppia di nodi consecutivi nel cammino
    #         tot += self._graph[listOfNodes[i]][listOfNodes[i + 1]]["weight"]  # *** Aggiunge il peso dell’arco tra i due nodi
    #
    #     return tot  # *** Restituisce il punteggio totale del cammino




   # def getBFSNodesFromTree(self, source):
   #      tree = nx.bfs_tree(self._graph, self._idMap[int(source)])
   #      archi = list(tree.edges())
   #      nodi = list(tree.nodes())
   #      return nodi[1:]
   #
   #  def getDFSNodesFromTree(self, source):
   #      tree = nx.dfs_tree(self._graph, source)
   #      nodi = list(tree.nodes())
   #      return nodi[1:]
   #
   #  def getCammino(self, sourceStr):
   #      source = self._idMap[int(sourceStr)]
   #      lp = []
   #
   #      #for source in self._graph.nodes:
   #      tree = nx.dfs_tree(self._graph, source)
   #      nodi = list(tree.nodes())
   #
   #      for node in nodi:
   #          tmp = [node]
   #
   #          while tmp[0] != source:
   #              pred = nx.predecessor(tree, source, tmp[0])
   #              tmp.insert(0, pred[0])
   #
   #          if len(tmp) > len(lp):
   #              lp = copy.deepcopy(tmp)
   #
   #      return lp


# # PARTE 2
# def getBFSNodesFromTree(self, sorgente):
#     tree = nx.bfs_tree(self._grafo, sorgente)
#     archi = list(tree.edges())
#     nodi = list(tree.nodes())
#     # ESCLUSO IL PRIMO SORGENTE
#     return nodi[1:]
#
#
# def getDFSNodesFromTree(self, sorgente):
#     tree = nx.dfs_tree(self._grafo, sorgente)
#     archi = list(tree.edges())
#     nodi = list(tree.nodes())
#     return nodi[1:]
#
#
# def getCammino(self, sorgenteStr):
#     sorgente = self.mappaOrdineId[sorgenteStr]
#     longestPath = []
#
#     tree = nx.dfs_tree(self._grafo, sorgente)
#     nodi = list(tree.nodes())
#     for nodo in nodi:
#         temporaneo = [nodo]
#         # LA PRIMA ITERAZIONE SARA FASA OVVIAMENTE E RITORNA NEL FOR
#
#         while temporaneo[0] != sorgente:
#             # è una lista "predecessore"
#             listaPredecessori = nx.predecessor(tree, sorgente, temporaneo[0])
#             temporaneo.insert(0, listaPredecessori[0])
#
#             if len(temporaneo) > len(longestPath):
#                 # viene usata per salvare il cammino tmp più lungo trovato finora,
#                 # in modo sicuro, senza rischiare che lp venga modificato accidentalmente in seguito.
#                 longestPath = copy.deepcopy(temporaneo)
#
#     return longestPath


if __name__ == "__main__":
    model = Model()

    listaStore = model.getAllStores()
    for store in listaStore:
        print(store.store_id)

    model.buildGraph(3,1)
    print(model.get_num_of_nodes())
    listaNodi = model.get_nodes()
    for nodo in listaNodi:
        print(nodo)

    print("")
    listaArchi = model.get_edges()
    for arco in listaArchi:
        print(arco[0].order_id, arco[1].order_id, arco[2]["weight"])




