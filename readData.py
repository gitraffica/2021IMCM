import csv
import pandas as pd
import networkx as nx
from pyvis.network import Network

class RafficaNode:
    def __init__(self):
        self.name = ""
        self.id = ""
        self.type = ""
        self.time = ""
    def __str__(self):
        return "id: " + self.id + "\n" + "name " + self.name + '\n' + "type: " + self.type + '\n' + "time: " + self.time

class RafficaReadData:

    def __init__(self):
        self.RafficaGraph = nx.MultiDiGraph()
        self.RafficaNodes = {}

    def addEdge(self, u, uname, utype, utime, v, vname, vtype, vtime):
        if u in self.RafficaNodes:
            uu = self.RafficaNodes[u]
        else:
            uu = RafficaNode()
            uu.id, uu.name, uu.type, uu.time = u, uname, utype, utime
            self.RafficaNodes[u] = uu
        if v in self.RafficaNodes:
            vv = self.RafficaNodes[v]
        else:
            vv = RafficaNode()
            vv.id, vv.name, vv.type, vv.time = v, vname, vtype, vtime
            self.RafficaNodes[v] = vv
        #self.RafficaGraph.add_edge(u, v)
        self.RafficaGraph.add_edge(str(self.RafficaNodes[u]), str(self.RafficaNodes[v]))

    def ReadData(self, fileName):
        with open(fileName, "r", encoding = 'utf-8') as f:
            f_csv = csv.reader(f)
            for i, row in enumerate(f_csv):
                self.addEdge(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7])
                if i > 100:
                    break
        pyvis_G = Network()
        pyvis_G.from_nx(self.RafficaGraph)
        file = open("amroptions.inf", "r")
        options = file.read()
        file.close()
        pyvis_G.set_options(options)
        pyvis_G.physics_enabled = True  # html上でレイアウト動かしたくない場合false
        pyvis_G.show("graph.html")


if __name__ == '__main__':
    rd = RafficaReadData()
    rd.ReadData("2021_ICM_Problem_D_Data/influence_data.csv")