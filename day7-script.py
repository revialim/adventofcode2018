# day 7 
def getExecutable(graph): #graph has to be reversed graph
    ex_set = set()
    for k, v in graph.items():
        for letter in v:
            if graph.get(letter) == None or graph.get(letter) == []:
                ex_set.add(letter)

    ex = []
    for item in ex_set:
        ex.append(item)
    return ex

def extendExecutable(list1, list2):
    merged = set()
    mer_list = []
    for item in list1:
        merged.add(item)
    for item in list2:
        merged.add(item)
    for item in merged:
        mer_list.append(item)
    mer_list.sort()
    return mer_list

def getReversed(graph): #reversed graph where keys are the nodes that are pointed towards
    rev = {}
    for k, v in graph.items():
        for letter in v:
            if rev.get(letter) != None:
                rev[letter].append(k)
            else:
                rev[letter] = [k]
    return rev

def start():
    graph = {}
    with open('./day7.txt') as f:
        for line in f:
            tmp_line = line.split()
            if graph.get(tmp_line[1]) != None:
                graph[tmp_line[1]].append(tmp_line[7])
            else:
                graph[tmp_line[1]] = [tmp_line[7]]

    executable = []
    executed = []
    while(len(graph)>0):
        # print("graph", graph)
        rev_graph = getReversed(graph)
        tmp = getExecutable(rev_graph)
        executable = extendExecutable(executable, tmp)
        executed.append(executable[0])
        del graph[executable[0]]
        executable = executable[1:]

    # print("graph", graph)
    print("need to add the N")
    print("executed", executed)
    print("joined", ''.join(executed))
start()