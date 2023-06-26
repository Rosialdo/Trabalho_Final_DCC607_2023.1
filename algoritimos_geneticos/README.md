# Algoritmo Genético para Coloração de Grafos

Este é um exemplo de implementação de um algoritmo genético para a coloração de grafos. O algoritmo utiliza a biblioteca `networkx` para trabalhar com grafos e a biblioteca `matplotlib` para visualização gráfica.

## Descrição do Código

O código consiste em várias funções que desempenham papéis específicos no algoritmo genético:

- `colorir_grafo(grafo)`: Função que atribui cores aos vértices de um grafo de forma que vértices adjacentes não possuam a mesma cor.

- `avaliar_coloracao(grafo, color_map)`: Função que avalia a qualidade de uma coloração, contando o número de conflitos de cores entre vértices adjacentes.

- `gerar_populacao_inicial(grafo, tamanho_populacao)`: Função que gera uma população inicial de colorações aleatórias.

- `cruzamento(pai1, pai2)`: Função que realiza o cruzamento de dois indivíduos (colorações) para gerar um filho.

- `mutacao(individuo, taxa_mutacao)`: Função que aplica mutações em um indivíduo (coloração) com uma determinada taxa de mutação.

- `algoritmo_genetico(grafo, tamanho_populacao, taxa_cruzamento, taxa_mutacao, num_geracoes)`: Função principal que executa o algoritmo genético para encontrar a melhor coloração para o grafo.

## Utilização

- O código possui um exemplo de uso no final do arquivo.
- O exemplo cria um grafo simples com algumas arestas para ilustrar a execução do algoritmo genético.
- Os parâmetros do algoritmo (tamanho da população, taxa de cruzamento, taxa de mutação, número de gerações) podem ser ajustados de acordo com a necessidade.
- A função `algoritmo_genetico` retorna a melhor coloração encontrada para o grafo.
- O grafo é desenhado com as cores atribuídas aos vértices usando a biblioteca `matplotlib`.

## Requisitos

- Python 3.x
- Bibliotecas: `networkx`, `matplotlib`

## Como Executar

1. Instale as bibliotecas necessárias executando o seguinte comando:

```python
pip install networkx matplotlib
```

2. Execute o código Python:

```python
python coloração_de_grafos.py
```


Espero que este exemplo seja útil para entender o funcionamento de algoritmos genéticos na coloração de grafos. Sinta-se à vontade para utilizar, modificar e aprimorar o código de acordo com suas necessidades.

