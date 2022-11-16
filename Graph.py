import networkx as nx
import matplotlib.pyplot as plt


class Graph:
    graph = nx.Graph()
    streets = [55, 54, 53, 52, 51, 50]
    avenues = [15, 14, 13, 12, 11, 10]
    destinies = ['5411', '5014', '5012', '5213', '5414']
    path = []
    andreina_path = []
    javier_path = []
    andreina_time = 0
    javier_time = 0

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
            if node in self.destinies:
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

    def run_dijkstra(self, initial_node, destination_node, person):
        previous_node = {}
        non_visited_nodes = nx.Graph()
        non_visited_nodes.add_nodes_from(self.graph.nodes())
        non_visited_nodes.add_edges_from(self.graph.edges())
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
                if (self.graph.nodes[edge[1]] not in self.path):
                    if self.graph.nodes[edge[1]][person + 'Distance'] > self.graph.nodes[minimum_node][person + 'Distance'] + self.graph.edges[edge]['weight']:
                        self.graph.nodes[edge[1]][person + 'Distance'] = self.graph.nodes[minimum_node][person +
                                                                                                        'Distance'] + self.graph.edges[edge]['weight'] + (2 if (person == 'Andreina') else 0)
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
        self.path = shortest_path
        if (person == "Andreina"):
            self.andreina_path = shortest_path
            self.andreina_time = distance['Distance']
        if (person == "Javier"):
            self.javier_path = shortest_path
            self.javier_time = distance['Distance']
        return distance

    def update_graph(self, destiny):
        color_map = []
        color_edges = []

        for node in self.graph.nodes():
            if node in self.destinies:
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

        auxiliar_graph_javier = nx.subgraph(self.graph, self.javier_path)
        auxiliar_graph_andreina = nx.subgraph(self.graph, self.andreina_path)

        for edge in self.graph.edges():
            auxiliar_edge_javier = None
            auxiliar_edge_andreina = None

            try:
                auxiliar_edge_javier = auxiliar_graph_javier.edges[edge]
            except KeyError:
                auxiliar_edge_javier = None

            try:
                auxiliar_edge_andreina = auxiliar_graph_andreina.edges[edge]
            except KeyError:
                auxiliar_edge_andreina = None

            if (auxiliar_edge_javier != None):
                color_edges.append(('#0ea2ea'))
            elif (auxiliar_edge_andreina != None):
                color_edges.append(('#f1785e'))
            else:
                color_edges.append(('#a6cfcc'))

        # Obtener la posición en pantalla de los nodos
        pos = nx.get_node_attributes(self.graph, 'pos')
        # Obtener las aristas del grafo
        weights = [self.graph[u][v]['weight'] for u, v in self.graph.edges()]
        # figurar la forma de dibujar el grafo
        nx.draw_networkx_nodes(
            self.graph, pos, node_color=color_map, node_size=800)
        nx.draw_networkx_edges(self.graph, pos, width=weights,
                               alpha=0.6, edge_color=color_edges)
        nx.draw_networkx_edge_labels(self.graph, pos, edge_labels={(
            u, v): self.graph[u][v]['weight'] for u, v in self.graph.edges()}, font_color='#930001', font_size=8)
        nx.draw_networkx_labels(
            self.graph, pos, font_size=6, font_family='sans-serif')
        plt.axis('off')
        plt.show()

    def shortest_distance(self, javier, andreina):
        '''Comparar los tiempos de los dos caminos y retornar un str
        con la persona que deba esperar x minutos para salir'''

        aux = javier['Distance'] - andreina['Distance']
        if (aux < 0):
            aux = aux * -1
            text = '      Javier debe esperar:\n' + \
                str(aux) + ' minutos para salir'
            return text
        else:
            text = 'Andreina  debe esperar: \n' + \
                str(aux) + ' minutos para salir'
            return text
