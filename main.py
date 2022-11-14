import networkx as nx
import matplotlib.pyplot as plt
import tkinter


class Graph:
    graph = nx.Graph()
    streets = [55, 54, 53, 52, 51, 50]
    avenues = [15, 14, 13, 12, 11, 10]
    path = []

    def __init__(self):
        pass

    def setup_nodes(self):
        pos_x = -15
        pos_y = 55

        for i in self.streets:
            for j in self.avenues:
                node = str(i) + str(j)
                self.graph.add_node(node, pos=(pos_x, pos_y))
                pos_x += 1

            pos_x = -15
            pos_y -= 1

    def setup_edge(self):
        longer_streets = [14, 13, 12]
        for i in self.streets:
            for j in self.avenues:
                current_node = str(i) + str(j)
                previous_node = str(i) + str(j - 1)
                previous_street = str(i - 1) + str(j)
                if i > 50 and j > 10:
                    if j in longer_streets:
                        self.graph.add_edge(
                            current_node, previous_street, weight=7)
                    else:
                        self.graph.add_edge(
                            current_node, previous_street, weight=5)
                    if i == 51:
                        self.graph.add_edge(
                            current_node, previous_node, weight=10)
                    else:
                        self.graph.add_edge(
                            current_node, previous_node, weight=5)

                if i > 50 and j == 10:
                    self.graph.add_edge(
                        current_node, previous_street, weight=5)
                if i == 50 and j > 10:
                    self.graph.add_edge(current_node, previous_node, weight=5)

    def show_graph(self):
        # Dibujar nodos en específico
        color_map = []
        for node in self.graph.nodes():
            if node == '5414' or node == '5213' or node == '5014' or node == '5411' or node == '5012':
                if node == '5414':
                    color_map.append(('#0ea2ea'))
                if node == '5213':
                    color_map.append(('#f1785e'))
                if node == '5014':
                    color_map.append(('#be76ce'))
                if node == '5411':
                    color_map.append(('#d88a02'))
                if node == '5012':
                    color_map.append(('#77a506'))
            else:
                color_map.append(('#a6cfcc'))

        # Obtener la posición en pantalla de los nodos
        pos = nx.get_node_attributes(self.graph, 'pos')
        # Obtener las aristas del grafo
        weights = [self.graph[u][v]['weight'] for u, v in self.graph.edges()]
        # figurar la forma de dibujar el grafo
        nx.draw_networkx_nodes(
            self.graph, pos, node_color=color_map, node_size=800)
        nx.draw_networkx_edges(self.graph, pos, width=weights,
                               alpha=0.6, edge_color='black')
        nx.draw_networkx_edge_labels(self.graph, pos, edge_labels={(
            u, v): self.graph[u][v]['weight'] for u, v in self.graph.edges()}, font_color='#930001', font_size=8)
        nx.draw_networkx_labels(
            self.graph, pos, font_size=6, font_family='sans-serif')
        plt.axis('off')
        plt.show()

    def setup_dijkstra(self):
        for node in self.graph.nodes():
            self.graph.nodes[node]['visited'] = {}
            self.graph.nodes[node]['visitedByJavier'] = False
            self.graph.nodes[node]['visitedByAndreina'] = False

            if (node == '5414'):
                self.graph.nodes[node]['JavierDistance'] = 0
                self.graph.nodes[node]['AndreinaDistance'] = 999
            elif (node == '5213'):
                self.graph.nodes[node]['JavierDistance'] = 999
                self.graph.nodes[node]['AndreinaDistance'] = 0
            else:
                self.graph.nodes[node]['JavierDistance'] = 999
                self.graph.nodes[node]['AndreinaDistance'] = 999

        for edge in self.graph.edges():
            self.graph.edges[edge]['visitedByJavier'] = False
            self.graph.edges[edge]['visitedByAndreina'] = False


#     def rundijkstra(self, initial_node, destination_node, person):
#         # Set the initial node as visited
#         self.graph.nodes[initial_node]['visited'] = True
#         self.graph.nodes[initial_node]['visitedBy' + person] = True

#         # Get the neighbors of the initial node
#         neighbors = self.graph[initial_node]

#         # For each neighbor, calculate the distance to the initial node and update the distance if it's lower
#         for neighbor in neighbors:
#             if self.graph.nodes[neighbor]['visited'] == False:
#                 if self.graph.nodes[neighbor]['visitedBy' + person] == False:
#                     self.graph.nodes[neighbor]['visitedBy' + person] = True
#                     self.graph.nodes[neighbor][person + 'Distance'] = self.graph.nodes[initial_node][person +
#                                                                                                      'Distance'] + self.graph[initial_node][neighbor]['weight']
#                 else:
#                     if self.graph.nodes[neighbor][person + 'Distance'] > self.graph.nodes[initial_node][person + 'Distance'] + self.graph[initial_node][neighbor]['weight']:
#                         self.graph.nodes[neighbor][person + 'Distance'] = self.graph.nodes[initial_node][person +
#                                                                                                          'Distance'] + self.graph[initial_node][neighbor]['weight']

#         # Get the unvisited node with the lowest distance
#         min_distance = 999
#         min_node = ''
#         for node in self.graph.nodes():
#             if self.graph.nodes[node]['visited'] == False:
#                 if self.graph.nodes[node][person + 'Distance'] < min_distance:
#                     min_distance = self.graph.nodes[node][person + 'Distance']
#                     min_node = node

#         # If there's no unvisited node with a lower distance, stop the algorithm
#         if min_node == '':
#             return

#         # If the destination node has been visited, stop the algorithm
#         if self.graph.nodes[destination_node]['visited'] == True:
#             return

#         # Run the algorithm again with the node with the lowest distance as the initial node
#         self.run_dijkstra(min_node, destination_node, person)

#  # generate dijkstra algorithm for Javier and Andreina and return the shortest path for each one and resetting the graph for the next iteration
#     def run_dijkstra(self, initial_node, destination_node, person):
#         self.setup_dijkstra()
#         current_node = initial_node
#         while current_node != destination_node:
#             for edge in self.graph.edges(current_node):
#                 if self.graph.edges[edge]['visitedBy' + person] == False:
#                     if self.graph.nodes[edge[1]]['visitedBy' + person] == False:
#                         if self.graph.nodes[current_node]['visitedBy' + person] == False:
#                             self.graph.nodes[current_node]['visitedBy' + person] = True
#                         if self.graph.nodes[edge[1]]['visitedBy' + person] == False:
#                             if self.graph.nodes[edge[1]][person + 'Distance'] > self.graph.nodes[current_node][person + 'Distance'] + self.graph.edges[edge]['weight']:
#                                 self.graph.nodes[edge[1]][person + 'Distance'] = self.graph.nodes[current_node][person + 'Distance'] + self.graph.edges[edge]['weight']
#                         self.graph.edges[edge]['visitedBy' + person] = True
#             min_distance = 999
#             for node in self.graph.nodes():
#                 if self.graph.nodes[node]['visitedBy' + person] == False:
#                     if self.graph.nodes[node][person + 'Distance'] < min_distance:
#                         min_distance = self.graph.nodes[node][person + 'Distance']
#                         current_node = node
#         shortest_path = []
#         current_node = destination_node
#         while current_node != initial_node:
#             for edge in self.graph.edges(current_node):
#                 if self.graph.nodes[edge[1]][person + 'Distance'] + self.graph.edges[edge]['weight'] == self.graph.nodes[current_node][person + 'Distance']:
#                     shortest_path.append(edge)
#                     current_node = edge[1]
#                     break
#         shortest_path.reverse()
#         return shortest_path

    def run_dijkstra(self, initial_node, destination_node, person):
        previous_node = {}
        non_visited_nodes = nx.Graph()
        non_visited_nodes.add_nodes_from(self.graph.nodes())
        non_visited_nodes.add_edges_from(self.graph.edges())
        # print(non_visited_nodes)
        shortest_path = []
        distance = {}

        while non_visited_nodes:
            minimum_node = None
            for node in non_visited_nodes:
                if minimum_node is None:
                    minimum_node = node
                elif self.graph.nodes[node][person + 'Distance'] < self.graph.nodes[minimum_node][person + 'Distance']:
                    minimum_node = node

            for edge in non_visited_nodes.edges(minimum_node):
                # print(self.graph.nodes['visited'])
                # if self.graph.nodes[edge[1]]['visitedBy' + person] == False and self.graph.nodes[edge[1]]['visitedByJavier'] == False:
                if(self.graph.nodes[edge[1]] not in self.path):
                    if self.graph.nodes[edge[1]][person + 'Distance'] > self.graph.nodes[minimum_node][person + 'Distance'] + self.graph.edges[edge]['weight']:
                        self.graph.nodes[edge[1]][person + 'Distance'] = self.graph.nodes[minimum_node][person +
                                                                                                        'Distance'] + self.graph.edges[edge]['weight']
                        previous_node[edge[1]] = minimum_node
            non_visited_nodes.remove_node(minimum_node)

        current_node = destination_node
        while current_node != initial_node:
            try:
                shortest_path.insert(0, current_node)
                self.graph.edges[current_node, previous_node[current_node]
                                 ]['visitedBy' + person] = True
                self.graph.edges[previous_node[current_node],
                                 current_node]['visitedBy' + person] = True
                current_node = previous_node[current_node]
            except KeyError:
                print('Path not reachable')
                break
        shortest_path.insert(0, initial_node)
        distance['Distance'] = self.graph.nodes[destination_node][person + 'Distance']
        distance['Path'] = shortest_path
        # self.graph.nodes['visited'] = shortest_path
        self.path = shortest_path
        return distance


def main():
    graph = Graph()
    graph.setup_nodes()
    graph.setup_edge()
    graph.setup_dijkstra()
    javier = graph.run_dijkstra('5414', '5012', 'Javier')
    andre = graph.run_dijkstra('5213', '5012', 'Andreina')
    print(javier)
    print(andre)
    graph.show_graph()


main()
