import networkx as nx
import matplotlib.pyplot as plt
import random

def colorir_grafo(grafo):
    color_map = {}  #Dicionário para armazenar as cores atribuídas a cada vértice

    for vertice in grafo.nodes:
        vizinhos_cores = set()  #Conjunto para armazenar as cores dos vizinhos do vértice

        #Obtém as cores dos vizinhos do vértice atual
        for vizinho in grafo.neighbors(vertice):
            if vizinho in color_map:
                vizinhos_cores.add(color_map[vizinho])

        #Encontra a cor disponível para o vértice
        for cor in range(len(grafo.nodes)):
            if cor not in vizinhos_cores:
                color_map[vertice] = cor
                break

    return color_map

def avaliar_coloracao(grafo, color_map):
    conflitos = 0

    #Verifica conflitos de cores entre vértices adjacentes
    for aresta in grafo.edges:
        v1, v2 = aresta
        if color_map[v1] == color_map[v2]:
            conflitos += 1

    return conflitos

def gerar_populacao_inicial(grafo, tamanho_populacao):
    populacao = []

    #Gera uma população inicial de colorações aleatórias
    for _ in range(tamanho_populacao):
        color_map = {}

        for vertice in grafo.nodes:
            cor = random.randint(0, len(grafo.nodes) - 1)
            color_map[vertice] = cor

        populacao.append(color_map)

    return populacao

def cruzamento(pai1, pai2):
    filho = {}

    #Realiza o cruzamento dos genes dos pais para gerar um filho
    for vertice in pai1:
        if random.random() < 0.5:
            filho[vertice] = pai1[vertice]
        else:
            filho[vertice] = pai2[vertice]

    return filho

def mutacao(individuo, taxa_mutacao):
    #Aplica mutações nos genes de um indivíduo com uma determinada taxa de mutação
    for vertice in individuo:
        if random.random() < taxa_mutacao:
            individuo[vertice] = random.randint(0, len(individuo) - 1)

    return individuo

def algoritmo_genetico(grafo, tamanho_populacao, taxa_cruzamento, taxa_mutacao, num_geracoes):
    populacao = gerar_populacao_inicial(grafo, tamanho_populacao)

    for geracao in range(num_geracoes):
        aptidoes = [avaliar_coloracao(grafo, individuo) for individuo in populacao]

        melhores_indices = sorted(range(len(aptidoes)), key=lambda k: aptidoes[k])[:int(tamanho_populacao/2)]
        melhores_individuos = [populacao[i] for i in melhores_indices]

        filhos = []
        while len(filhos) < tamanho_populacao - len(melhores_individuos):
            pai1 = random.choice(melhores_individuos)
            pai2 = random.choice(melhores_individuos)
            filho = cruzamento(pai1, pai2)
            filhos.append(filho)

        filhos_mutados = [mutacao(filho, taxa_mutacao) for filho in filhos]

        nova_populacao = melhores_individuos + filhos_mutados

        populacao = nova_populacao

    aptidoes = [avaliar_coloracao(grafo, individuo) for individuo in populacao]
    melhor_indice = aptidoes.index(min(aptidoes))
    melhor_coloracao = populacao[melhor_indice]

    return melhor_coloracao

#Cria um grafo com 10 vértices para exemplo
grafo = nx.Graph()
grafo.add_edges_from([(1, 2), (1, 3), (2, 3), (3, 4), (4, 5), (4, 6), (5, 6), (6, 7), (6, 8), (7, 8), (8, 9), (8, 10)])

#Parâmetros do algoritmo genético
tamanho_populacao = 100
taxa_cruzamento = 0.8
taxa_mutacao = 0.2
num_geracoes = 50

#Executa o algoritmo genético para colorir o grafo
melhor_coloracao = algoritmo_genetico(grafo, tamanho_populacao, taxa_cruzamento, taxa_mutacao, num_geracoes)

#Desenha o grafo com as cores atribuídas aos vértices
pos = nx.spring_layout(grafo)
nx.draw(grafo, pos, with_labels=True, node_color=[melhor_coloracao[v] for v in grafo.nodes], node_size=500, font_size=12, font_color='black')

#Exibe o grafo
plt.show()