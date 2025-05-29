from itertools import permutations
import math

def brute_force(matrix):
    n = len(matrix)
    min_cost = float('inf')
    best_tour = None

    for tour in permutations(range(1, n)):
        tour = (0,) + tour
        cost = sum(matrix[tour[i]][tour[i+1]] for i in range(n-1))
        cost += matrix[tour[-1]][tour[0]]

        if cost < min_cost:
            min_cost = cost
            best_tour = tour
    
    return best_tour + (best_tour[0],), min_cost

def nearest_neighbors(matrix):
    n = len(matrix)
    unvisited = set(range(n))
    tour = [0]
    unvisited.remove(0)

    while unvisited:
        last = tour[-1]
        nearest = min(unvisited, key=lambda city: matrix[last][city])
        tour.append(nearest)
        unvisited.remove(nearest)

    tour.append(tour[0])
    cost = sum(matrix[tour[i]][tour[i+1]] for i in range(len(tour)-1))

    return tour, cost

def cheapest_insertion(matrix):
    n = len(matrix)
    if n < 2:
        return [0]*n, 0
    
    start = 0
    nearest = min((c for c in range(1, n)), key=lambda c: matrix[start][c])
    subtour = [start, nearest, start]
    unvisited = set(range(n)) - set(subtour)
    
    while unvisited:
        best_cost_increase = float('inf')
        best_city = None
        best_position = -1
        
        for city in unvisited:
            for i in range(len(subtour)-1):
                cost_increase = (matrix[subtour[i]][city] + 
                                 matrix[city][subtour[i+1]] - 
                                 matrix[subtour[i]][subtour[i+1]])
                if cost_increase < best_cost_increase:
                    best_cost_increase = cost_increase
                    best_city = city
                    best_position = i+1
        
        subtour.insert(best_position, best_city)
        unvisited.remove(best_city)
        
    cost = sum(matrix[subtour[i]][subtour[i+1]] for i in range(len(subtour)-1))
    return subtour, cost

def mst_approximation(matrix):
    n = len(matrix)
    mst = _prim_mst(matrix)
    tour = _preorder_dfs(mst)
    cost = sum(matrix[tour[i]][tour[i+1]] for i in range(len(tour)-1))
    
    return tour, cost

def _prim_mst(matrix):
    n = len(matrix)
    mst = [[] for _ in range(n)]
    key = [math.inf] * n
    parent = [-1] * n
    in_mst = [False] * n
    key[0] = 0

    for _ in range(n):
        u = min((v for v in range(n) if not in_mst[v]), key=lambda v: key[v])
        in_mst[u] = True

        if parent[u] != -1:
            mst[u].append(parent[u])
            mst[parent[u]].append(u)
        
        for v in range(n):
            if matrix[u][v] > 0 and not in_mst[v] and matrix[u][v] < key[v]:
                key[v] = matrix[u][v]
                parent[v] = u
    
    return mst

def _preorder_dfs(mst):
    n = len(mst)
    tour = []
    visited = [False] * n
    
    def dfs(u):
        visited[u] = True
        tour.append(u)
        for v in mst[u]:
            if not visited[v]:
                dfs(v)
    
    dfs(0)
    tour.append(tour[0])

    return tour