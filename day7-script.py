# day 7 
alph = ("A B C D E F G H I J K L M N O P Q R S T U V W X Y Z").split()
print(alph)

def start():
    
    graph_fromto = {}
    graph_tofrom = {}
    
    for letter in alph:
        graph_fromto[letter] = []
        graph_tofrom[letter] = []
    with open('./day7.txt') as f:
        for line in f:
            tmp_line = line.split()
            graph_from = tmp_line[1]
            graph_to = tmp_line[7]
            if graph_fromto.get(graph_from) != None:
                graph_fromto[graph_from].append(graph_to)
            else:
                graph_fromto[graph_from] = [graph_to]

            if graph_tofrom.get(graph_to) != None:
                graph_tofrom[graph_to].append(graph_from)
            else:
                graph_tofrom[graph_to] = [graph_from]

    print(graph_fromto)
    print(graph_tofrom)

start()