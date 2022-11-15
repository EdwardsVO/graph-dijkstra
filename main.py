import tkinter

from Graph import Graph

def main():
    graph = Graph()
    graph.setup_nodes()
    graph.setup_edge()
    graph.setup_dijkstra()
    javier = graph.run_dijkstra('5414', '5410', 'Javier')
    andre = graph.run_dijkstra('5213', '5410', 'Andreina')
    print(javier)
    print(andre)
    graph.show_graph()
    graph.update_graph('5014')

main()
