import re, time
from datetime import timedelta

def read_matrix(filename):
    with open(filename, 'r') as f:
        return [[int(num) for num in line.split()] for line in f]

def extract_optimal_cost(filename):
    match = re.search(r'tsp\d+_(\d+)\.txt$', filename)
    return int(match.group(1)) if match else None

def print_results(tour, cost, optimal=None, exec_time=None, algorithm_name=""):
    if algorithm_name:
        print(f"\n{'='*50}")
        print(f" RESULTADOS - {algorithm_name.upper()} ".center(50, '='))
        print(f"{'='*50}\n")
    
    print(f"🔹 Rota encontrada ({len(tour)} cidades):")
    print(f"   {tour}\n")
    print(f"💰 Custo total: {cost}")
    
    if optimal is not None:
        diff = cost - optimal
        percent = (diff / optimal) * 100
        print(f"\n🏆 Valor ótimo conhecido: {optimal}")
        print(f"📊 Diferença: {diff:+} ({percent:+.2f}%)", end=" ")
        
        if abs(percent) < 5:
            print("| ✅ Próximo do ótimo")
        elif percent < 0:
            print("| ❗ MELHOR que o ótimo (verifique os dados)")
        else:
            print("| ⚠️ Pode ser melhorado")
    
    if exec_time is not None:
        if exec_time < 1:
            print(f"\n⏱️ Tempo de execução: {exec_time:.6f} segundos")
        else:
            print(f"\n⏱️ Tempo de execução: {str(timedelta(seconds=exec_time)).split('.')[0]}")
    
    print("\n" + "="*50)
