from itertools import permutations

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