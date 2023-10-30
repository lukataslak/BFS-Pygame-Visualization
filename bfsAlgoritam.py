def findNode(graph, ele):
    for i, x in enumerate(graph):
        if ele in x:
            return (i, x.index(ele))

def bfs(graph):
    
    node = findNode(graph, 'B')
    end = findNode(graph, 'E')
    path = []

    visited = []
    queue = []

    visited.append(node)
    queue.append(node)
    
    while queue:     
        s = queue.pop(0)
        path.append(s)        
        
        legalMoves = []
        if (s[0]-1 > -1):
            if graph[s[0]-1][s[1]] != 'W': legalMoves.append((s[0]-1, s[1])) # up
        if (s[0]+1 < len(graph)):
            if graph[s[0]+1][s[1]] != 'W': legalMoves.append((s[0]+1, s[1])) # down
        if (s[1]+1 < len(graph)):
            if graph[s[0]][s[1]+1] != 'W': legalMoves.append((s[0], s[1]+1)) # right
        if (s[1]-1 > -1):
            if graph[s[0]][s[1]-1] != 'W': legalMoves.append((s[0], s[1]-1)) # left

        for n in legalMoves:
            if n not in visited:
                visited.append(n)
                queue.append(n)
            
            if n == end:
                path.append(n)
                return path   

    return path

    
def reconstructPath(graph, path):
    
    end = findNode(graph, 'E')
    shortest = [path.pop()]

    while path:

        s = path.pop()
        neighbors = []
        if (s[0]-1 > -1): neighbors.append((s[0]-1, s[1])) # up
        if (s[0]+1 < len(graph)): neighbors.append((s[0]+1, s[1])) # down
        if (s[1]+1 < len(graph)):neighbors.append((s[0], s[1]+1)) # right
        if (s[1]-1 > -1): neighbors.append((s[0], s[1]-1)) # left

        if shortest[len(shortest)-1] in neighbors:
            shortest.append(s)
        
    return shortest


