import itertools
import math

cidades = {
    "Fortaleza": (0, 0),
    "Juazeiro do Norte": (250, 400),
    "Sobral": (200, 50),
    "Crato": (240, 390),
    "Quixadá": (100, 150),
    "Canindé": (80, 100),
    "Iguatu": (200, 350),
    "Aracati": (150, 50),
    "Tauá": (300, 450),
    "Itapipoca": (180, 120),
}

# Função para calcular a distância Euclidiana
def distancia(cidade1, cidade2):
    x1, y1 = cidades[cidade1]
    x2, y2 = cidades[cidade2]
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# Algoritmo força bruta para encontrar a melhor e pior rotas
def caixeiro_viajante(cidades):
    menor_distancia = float("inf")
    melhor_caminho = None
    
    maior_distancia = 0
    pior_caminho = None
    
    todas_as_cidades = list(cidades.keys())
    
    for permutacao in itertools.permutations(todas_as_cidades):
        distancia_total = 0
        for i in range(len(permutacao) - 1):
            distancia_total += distancia(permutacao[i], permutacao[i + 1])
        # Voltar para a cidade inicial
        distancia_total += distancia(permutacao[-1], permutacao[0])
        
        # Atualizar menor distância (melhor caminho)
        if distancia_total < menor_distancia:
            menor_distancia = distancia_total
            melhor_caminho = permutacao
        
        # Atualizar maior distância (pior caminho)
        if distancia_total > maior_distancia:
            maior_distancia = distancia_total
            pior_caminho = permutacao
    
    return melhor_caminho, menor_distancia, pior_caminho, maior_distancia

# Executar o algoritmo
melhor_caminho, menor_distancia, pior_caminho, maior_distancia = caixeiro_viajante(cidades)

# Mostrar a melhor rota
print("Melhor rota:")
print(" -> ".join(melhor_caminho))
print(f"Distância total: {menor_distancia:.2f} km")

# Mostrar a distância entre cada cidade no melhor caminho
print("\nDetalhes da melhor rota:")
for i in range(len(melhor_caminho) - 1):
    cidade1 = melhor_caminho[i]
    cidade2 = melhor_caminho[i + 1]
    print(f"{cidade1} -> {cidade2}: {distancia(cidade1, cidade2):.2f} km")
# Voltar à cidade inicial
print(f"{melhor_caminho[-1]} -> {melhor_caminho[0]}: {distancia(melhor_caminho[-1], melhor_caminho[0]):.2f} km")

# Mostrar a pior rota
print("\nPior rota:")
print(" -> ".join(pior_caminho))
print(f"Distância total: {maior_distancia:.2f} km")

# Mostrar a distância entre cada cidade no pior caminho
print("\nDetalhes da pior rota:")
for i in range(len(pior_caminho) - 1):
    cidade1 = pior_caminho[i]
    cidade2 = pior_caminho[i + 1]
    print(f"{cidade1} -> {cidade2}: {distancia(cidade1, cidade2):.2f} km")
# Voltar à cidade inicial
print(f"{pior_caminho[-1]} -> {pior_caminho[0]}: {distancia(pior_caminho[-1], pior_caminho[0]):.2f} km")
