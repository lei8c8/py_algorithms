from collections import deque

def breadthFirstSearch(graph, root):
    visitedList = []
    graphQueue = deque([root])
    visitedList.append(root)
    node = root
    while len(graphQueue) > 0:
        node = graphQueue.popleft()
        adjNodes = graph[node]
        remainingNodes = set(adjNodes).difference(set(visitedList))
        if len(remainingNodes) > 0:
            for ele in remainingNodes:
                visitedList.append(ele)
                graphQueue.append(ele)
    return visitedList