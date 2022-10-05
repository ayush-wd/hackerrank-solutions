class Graph():
    def __init__(self,vertices):
        self.V = vertices
        self.graph = [[0 for column in range(vertices)]
                        for row in range(vertices)]
    
    def print(self,dist):
        for node in range(self.V):
            print(node, "\t\t", dist[node])
    
    def mindist(self,dist,sptSet):
        min = 1e7
        for v in range(self.V):
            if dist[v] < min and sptSet[v] == False:
                min = dist[v]
                min_index = v
        return min_index
    
    def dijkstra(self, src):
        dist = [1e7] * self.V
        dist[src] = 0
        sptSet = [False] * self.V

        for cout in range(self.V):
            u = self.mindist(dist, sptSet)
            sptSet[u] = True

            for v in range(self.V):
                if( self.graph[u][v] > 0 and 
                    sptSet[v] == False and
                    dist[v] > dist[u] + self.graph[u][v]) :
                    dist[v] = dist[u] + self.graph[u][v]
        
        self.print(dist)

g = Graph(4)
g.graph = [[0,1,0,0],
            [0,0,1,0],
            [0,0,0,1],
            [1,0,0,0]
           ]
 
g.dijkstra(0)