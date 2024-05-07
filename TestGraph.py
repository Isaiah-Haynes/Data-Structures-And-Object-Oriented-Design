from Graph import Graph, AdjacencySetGraph as ASG, EdgeSetGraph as ESG

V = {1,2,3}
E = {(1,2, 4.6), (2, 3, 9.2), (1, 3, 3.1)}
G = ASG(V, E)
tree, D = G.dijkstra(1)

print(tree, D)
