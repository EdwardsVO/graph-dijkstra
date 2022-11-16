import tkinter
from Graph import Graph


def __init__():
    graph = Graph()
    graph.setup_nodes()
    graph.setup_edge()
    graph.setup_dijkstra()
    window = tkinter.Tk()
    window.geometry('355x200')
    window.wm_title('Proyecto-1')
    return graph, window


def main():
    graph, window = __init__()
    options = [
        'Discoteca Darkness (5014)', 'Bar la Pasion (5411)', 'Cerveceria Mi Rolita (5012)']
    option = tkinter.StringVar(window)
    option.set('Elige un destino: ')
    drop = tkinter.OptionMenu(window, option, *options)
    drop.config(font=("verdana", 10))
    drop.pack(side='left')

    tkinter.Label(window,
                  text='Bogota Best Route').place(x=110, y=25)

    def get_option():
        '''Corre el algoritmo de Dijkstra según la opción seleccionada'''

        if option.get() == 'Discoteca Darkness (5014)':

            graph.setup_dijkstra()
            javier = graph.run_dijkstra('5414', '5014', 'Javier')
            andreina = graph.run_dijkstra('5213', '5014', 'Andreina')
            graph.update_graph('5014')
            tkinter.Label(window, text=graph.shortest_distance(
                javier, andreina)).place(x=10, y=150)
            tkinter.Label(window, text='Tiempo de viaje: \n' + 'Javier -> '+str(javier['Distance'])+' Minutos\n'
                          + 'Andreina -> '+str(andreina['Distance'])+' Minutos').place(x=180, y=140)

        elif option.get() == 'Bar la Pasion (5411)':

            graph.setup_dijkstra()
            javier = graph.run_dijkstra('5414', '5411', 'Javier')
            andreina = graph.run_dijkstra('5213', '5411', 'Andreina')
            graph.update_graph('5411')
            tkinter.Label(window, text=graph.shortest_distance(
                javier, andreina)).place(x=10, y=150)
            tkinter.Label(window, text='Tiempo de viaje: \n'+'Javier -> '+str(javier['Distance'])+' Minutos\n'
                          + 'Andreina -> '+str(andreina['Distance'])+' Minutos').place(x=180, y=140)
        else:
            graph.setup_dijkstra()
            javier = graph.run_dijkstra('5414', '5012', 'Javier')
            andreina = graph.run_dijkstra('5213', '5012', 'Andreina')
            graph.update_graph('5012')
            tkinter.Label(window, text=graph.shortest_distance(
                javier, andreina)).place(x=10, y=150)
            tkinter.Label(window, text='Tiempo de viaje: \n'+'Javier -> '+str(javier['Distance'])+' Minutos\n'
                          + 'Andreina -> '+str(andreina['Distance'])+' Minutos').place(x=180, y=140)

    tkinter.Button(
        window, text='Calcular!', command=lambda: get_option()).pack(side='right')
    graph.show_graph()
    window.mainloop()


main()
