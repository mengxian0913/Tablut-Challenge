def track(graph, Node, saved):

    if graph[Node][3] == "chosen" or graph[Node][3] in saved:
        saved.append(Node)
        return True
    if graph[Node][3] == "root":
        del graph[Node]
        return False

    check = True
    try:
        check = track(graph, graph[Node][2], saved)
    except IndexError:
        del graph[Node]
        return False
    if not check:
        del graph[Node]
        return False
    else:
        saved.append(Node)
        return True


def backtrack(graph):
    saved = []
    for node in graph:
        if graph[node][3] == "leaf":
            try:
                check = track(graph, node, saved)
            except IndexError:
                del graph[node]
            if not check:
                del graph[node]
