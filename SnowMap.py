from Graph import AdjacencySetGraph as ASG
# TODO: Answer the following (Feel free to use multi-line comments)
# Which data structure will you use:
# Why:
'''SnowMap relies heavily on the relations between the vertices, hence I will use
the AdjacencySetGraph'''

# TODO: Define a class SnowMap that inherits from one of the data structure implemented earlier.
# Only implement one method here: plow_from

#use dijkstra for snowmap

class SnowMap(ASG):
    def plow_from(self, city):
        tree, D = self.dijkstra(city)
        
        return D, tree
        pass

if __name__ == '__main__':
    cities = {"Hartford", "Waterbury", "Danbury", "Greenwich",
              "Norwalk", "Bridgeport", "New Haven", "New London", "Mystic"}
    roads = {("Hartford", "Waterbury", 31), ("Hartford", "New Haven", 39),
             ("Hartford", "New London", 51), ("Hartford", "Mystic", 53),
             ("Waterbury", "Danbury", 28), ("New Haven", "Bridgeport", 19),
             ("New Haven", "New London", 48), ("New London", "Mystic", 9),
             ("Danbury", "Greenwich", 40), ("Danbury", "Norwalk", 22),
             ("Danbury", "Bridgeport", 29), ("Bridgeport", "Norwalk", 15),
             ("Norwalk", "Greenwich", 15)}
    sm = SnowMap(cities, roads)
    D, tree = sm.plow_from("Hartford")
    for city, miles in D.items(): print(f"{city:10}{miles:10}")
    #print(tree)
    D2, tree2 = sm.plow_from("Greenwich")
    print()
    for city, miles in D2.items(): print(f"{city:10}{miles:10}")

