def map_coloring(graph, colors):
    result = {}
    
    def is_safe(node, color):
        for neighbor in graph[node]:
            if neighbor in result and result[neighbor] == color:
                return False
        return True
    
    def solve(node_list):
        if not node_list:
            return True
        node = node_list[0]
        for color in colors:
            if is_safe(node, color):
                result[node] = color
                if solve(node_list[1:]):
                    return True
                del result[node]
        return False
    
    nodes = list(graph.keys())
    if solve(nodes):
        return result
    else:
        return None

graph = {'WA':['NT','SA'], 'NT':['WA','SA','Q'], 'SA':['WA','NT','Q','NSW','V'], 'Q':['NT','SA','NSW'], 'NSW':['Q','SA','V'], 'V':['SA','NSW'], 'T':[]}
colors = ['Red','Green','Blue']
solution = map_coloring(graph, colors)
print(solution)
