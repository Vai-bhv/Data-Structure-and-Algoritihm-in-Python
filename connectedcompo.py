def search(graph, visit, node, component): 
    visit[node] = True 
    component.append(node) 
 
    for joint in graph[node]: 
        if not visit[joint]: 
            search(graph, visit, joint, component) 
 
    return component 
 
def con_Comp(graph, n): 
    visit = [False] * (n + 1) 
    connected_components = [] 
 
    for i in range(1, n + 1): 
        if not visit[i]: 
            component = [] 
            connected_components.append(search(graph, visit, i, component)) 
 
    return connected_components 
 
n = int(input().strip()) 
m = int(input().strip()) 
 
graph = {i: [] for i in range(1, n + 1)} 
 
for _ in range(m): 
    u, v = map(int, input().strip().split()) 
    graph[u].append(v) 
    graph[v].append(u) 
 
connected_components = con_Comp(graph, n) 
for i in connected_components: 
    print(*i)