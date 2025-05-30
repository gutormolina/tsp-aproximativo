import argparse, time
from tsp_solver import brute_force, nearest_neighbors, cheapest_insertion, mst_approximation
from utils import extract_optimal_cost, read_matrix, print_results

def main():
    parser = argparse.ArgumentParser(description='Resolvedor do Problema do Caixeiro Viajante')

    # Adicionei 'mst' nas opções de algoritmos
    parser.add_argument('file', help='Arquivo contendo a matriz de adjacência')
    parser.add_argument('algorithm', choices=['bf', 'nn', 'ci', 'mst'],
                        help='Algoritmo a ser utilizado: bf (brute force), nn (nearest neighbors), ci (cheapest insertion) ou mst (minimum spanning tree)')
    
    args = parser.parse_args()

    try:
        matrix = read_matrix(args.file)
        optimal = extract_optimal_cost(args.file)
        print(f"Matriz carregada: {args.file} ({len(matrix)} cidades)")

        start_time = time.perf_counter()
        if args.algorithm == 'bf':
            print("Executando brute force...")
            tour, cost = brute_force(matrix)
        elif args.algorithm == 'nn':
            print("Executando nearest neighbors...")
            tour, cost = nearest_neighbors(matrix)
        elif args.algorithm == 'ci':
            print("Executando cheapest insertion...")
            tour, cost = cheapest_insertion(matrix)
        elif args.algorithm == 'mst':  # Novo caso para MST
            print("Executando minimum spanning tree...")
            tour, cost = mst_approximation(matrix)
        end_time = time.perf_counter()

        # Adicionei o nome do algoritmo MST
        algorithm_name = {
            'bf' : 'Brute Force',
            'nn' : 'Nearest Neighbors',
            'ci' : 'Cheapest Insertion',
            'mst': 'Minimum Spanning Tree'
        }[args.algorithm]

        print_results(
            tour = tour,
            cost = cost,
            optimal=optimal,
            exec_time=end_time - start_time,
            algorithm_name=algorithm_name
        )

    except Exception as e:
        print(f"\nErro: {e}")

if __name__ == "__main__":
    main()