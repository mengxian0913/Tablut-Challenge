def heur(node, win):
    pass


def dist(node1, node2):
    x_dist = abs(node1.x - node2.x)
    y_dist = abs(node1.y - node2.y)
    # this could be improved by taking in account that we can move by more than 1
    # cell at a time.
    # considering the fact that all children have distance=1 move, we could decide
    # to only use the heuristic.
    return x_dist + y_dist


def find_track(graph, node, list, cost=0):
    list.append(node)
    if graph[3] != "root":
        cost = dist(node, graph[node][3])
        find_track(graph, graph[node][3], list, cost)
    return (list, cost)


def expand(node, graph, state):
    for i in node.children:
        if i == state.win and (i not in graph or dist(state.root, i) < graph[i][1]):
            graph[i] = [i, heur(i, state.win) + dist(state.root, i), "win", node]
        elif i not in graph or dist(state.root, i) < graph[i][1]:
            graph[i] = [i, heur(i, state.win) + dist(state.root, i), "", node]
        expand(i, graph, state)


def search(role, state):
    graph = {state.root: [state.root, heur(state.root, state.win), "win", None]}
    paths = {}
    k = 0
    expand(state.root, graph, state)
    for j in [i for i in graph if graph[i][2] == "win"]:
        paths[k] = find_track(graph, j, [])
        k += 1
    smallest = None
    key = None
    for j in paths:
        if smallest == 1:
            break
        if paths[j][1] < smallest:
            smallest = paths[j][1]
            key = j
    return paths[key]
