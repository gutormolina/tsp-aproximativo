import argparse, time
from tsp_solver import brute_force, nearest_neighbors
from utils import extract_optimal_cost, read_matrix, print_results

def main():
    parser = argparse.ArgumentParser(description='Resolvedor do Problema do Caixeiro Viajante')

    parser.add_argument('file', help='Arquivo contendo a matriz de adjacência')
    parser.add_argument('algorithm', choices=['bf', 'nn'],
                        help='Algoritmo a ser utilizado: bf (brute force) ou nn (nearest neighbors)')
    
    args = parser.parse_args()

    try:
        matrix = read_matrix(args.file)
        optimal = extract_optimal_cost(args.file)
        print(f"Matriz carregada: {args.file} ({len(matrix)} cidades)")

        start_time = time.perf_counter()
        if args.algorithm == 'bf':
            print("Executando brute force...")
            tour, cost = brute_force(matrix)
        else:
            print("Executando nearest neighbors...")
            tour, cost = nearest_neighbors(matrix)
        end_time = time.perf_counter()

        algorithm_name="Brute Force" if args.algorithm == 'bf' else "Nearest Neighbors"

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