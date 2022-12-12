import csv
import networkx as net
import matplotlib.pyplot as plt


def make_graph(name_datafile):
    data = []
    with open(name_datafile, 'r') as file:
        csvreader = csv.reader(file)
        for row in csvreader:
            for value in row:
                open_values = value.split(';')
                print(open_values)
                data.append([open_values[0], open_values[1], int(open_values[2])])

    G = net.Graph()
    for value in data:
        G.add_edge(value[0], value[1], weight = value[2])

    print(G)
    return G


def draw(graph, name_pic):
    pos = net.spring_layout(graph)
    net.draw_networkx(graph, pos)
    plt.title(name_pic)
    plt.show()


def get_path(graph, city_1, city_2):
    path = net.shortest_path(graph, city_1, city_2, weight = 'weight')
    len_path = net.shortest_path_length(graph, city_1, city_2, weight = 'weight' )

    print(f"From {city_1} to {city_2} shortest path will take {len_path} km your path is: {path}")
    return path, len_path

#make_graph('cities.csv')
G = make_graph('cities.csv')
draw(G, 'cities')
get_path(G, 'Lviv', 'Poltava')