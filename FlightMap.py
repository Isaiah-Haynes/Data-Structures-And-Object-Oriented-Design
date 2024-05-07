from Graph import AdjacencySetGraph as ASG
# TODO: Answer the following (Feel free to use multi-line comments)
# Which data structure will you use:
# Why:
'''I will use the AdjacencySetGraph for FlightMap because FlightMap relies on its neighbors
and the AdjacencySetGraph is faster at accessing its neighbors'''

# TODO: Define a class FlightMap that inherits from one of the data structure implemented earlier.pass
# Only implement one method here: reachable


class FlightMap(ASG):
    def reachable(self, city, n=0, reach=set()):
        nbrs = self.neighbors(city).keys()
        if city not in reach:
            reach.add(city)
        if n == 1:
            for i in nbrs:
                if i not in reach:
                    reach.add(i)
        else:
            for n_city in nbrs:
                self.reachable(n_city, n-1, reach)
        return reach


if __name__ == '__main__':
    cities = {'BOS', 'BDL', 'HND', 'JFK', 'MIA', 'LAX', 'DFW'}
    flights = {('BOS', 'HND'), ('BOS', 'BDL'), ('BOS', 'JFK'), ('BOS', 'MIA'),
               ('JFK', 'LAX'), ('JFK', 'MIA'), ('LAX', 'DFW')}
    fm = FlightMap(cities, flights)
    test1 = fm.reachable('BOS', 1)
    print(test1)
    
    cities2 = {'BOS', 'BDL', 'HND', 'JFK', 'MIA', 'LAX', 'DFW'}
    flights2 = {('BOS', 'HND'), ('BOS', 'BDL'), ('BOS', 'JFK'), ('BOS', 'MIA'),
               ('JFK', 'LAX'), ('JFK', 'MIA'), ('LAX', 'DFW')}
    fm2 = FlightMap(cities, flights)
    test2 = fm.reachable('BOS', 2)
    print(test2)
