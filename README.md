# Introdução à Programação Dinâmica: História, Conceitos e Aplicações

**Programação Dinâmica (PD)** é uma técnica essencial na resolução de problemas de otimização, utilizada amplamente em diversos campos como ciência da computação, pesquisa operacional, e economia. A técnica foi introduzida por Richard Bellman na década de 1950, com o objetivo de abordar problemas que podiam ser decompostos em subproblemas menores e mais simples de resolver.

A palavra "dinâmica" refere-se à natureza do problema que se desenvolve ao longo do tempo, enquanto "programação" é usada no sentido matemático de planejamento ou tomada de decisão. Essa técnica tem se mostrado incrivelmente útil em uma variedade de contextos onde a eficiência e a otimização são cruciais.

## Comparação com Outros Métodos de Design de Algoritmos

A programação dinâmica é uma das várias abordagens para o design de algoritmos. Para entender sua relevância, é interessante compará-la com outros métodos, como os **algoritmos gulosos**.

### Algoritmos Gulosos

Os algoritmos gulosos são caracterizados por tomarem decisões locais ótimas em cada etapa, com a esperança de que essas escolhas resultem em uma solução globalmente ótima. Eles são rápidos e simples de implementar, sendo extremamente eficazes em problemas como o da **mochila fracionária** e **algoritmo de Prim** para árvores geradoras mínimas. Contudo, a abordagem gulosa não garante uma solução ótima em todos os casos, especialmente quando o problema não possui uma estrutura que permita tal comportamento.

### Programação Dinâmica

Por outro lado, a programação dinâmica lida com problemas que possuem **subestrutura ótima** e **sobreposição de subproblemas**. Isso significa que o problema maior pode ser dividido em subproblemas menores, cujas soluções podem ser reutilizadas várias vezes. Em vez de tomar decisões imediatas e locais, como os algoritmos gulosos, a programação dinâmica resolve subproblemas de maneira sistemática, armazenando os resultados para evitar a redundância computacional e, eventualmente, combinando essas soluções para resolver o problema maior.

## Abordagens de Programação Dinâmica: Memoization e Bottom-Up

Existem duas abordagens principais para implementar a programação dinâmica:

### Memoization (Top-Down Approach)

A **Memoization** é uma técnica que resolve o problema de maneira recursiva. Ao calcular a solução de um subproblema, o resultado é armazenado em uma tabela (ou dicionário) para futuras referências. Se o mesmo subproblema for encontrado novamente, o resultado armazenado é reutilizado, evitando o recálculo.

Essa abordagem é conhecida como **top-down** porque começa resolvendo o problema maior e vai quebrando-o em subproblemas menores, armazenando os resultados à medida que avança. Embora seja uma forma eficiente de implementar a programação dinâmica, a memoization pode consumir mais espaço devido à recursão, comparado ao método bottom-up.

### Bottom-Up Approach

O **Bottom-Up Approach** resolve os subproblemas menores primeiro e usa suas soluções para construir a solução do problema maior. Nesta abordagem, todos os subproblemas são resolvidos de maneira iterativa, e os resultados são armazenados em uma tabela. Isso elimina a necessidade de chamadas recursivas, tornando o processo mais eficiente em termos de espaço.

Essa abordagem é especialmente útil em problemas onde todos os subproblemas precisam ser resolvidos, e é frequentemente utilizada em problemas como cálculo de sequência de Fibonacci e solução de grafos acíclicos direcionados (DAGs).

## Aplicações Comuns da Programação Dinâmica

A programação dinâmica é uma ferramenta versátil e é aplicada em várias áreas. Aqui estão algumas aplicações comuns:

- **Problemas de Sequência:** Encontrar a subsequência comum mais longa (LCS) ou alinhamento de sequências na bioinformática.
- **Problemas de Caminho Mínimo:** Resolver problemas como o do caixeiro-viajante em grafos ou o cálculo do caminho mais curto em grafos acíclicos direcionados (DAGs).
- **Problemas de Corte de Hastes e Mochila:** Maximizar o valor ou minimizar o custo ao cortar hastes ou ao encher uma mochila com itens de valor.

## Algoritmo de Memoization: Explicação Teórica

A **Memoization** é uma técnica de otimização que armazena os resultados de funções computacionalmente caras com base em seus parâmetros de entrada. Quando uma função é chamada novamente com os mesmos parâmetros, o resultado é recuperado diretamente da memória, em vez de ser recalculado.

### Definição Teórica

Para um problema definido por uma função \( f(n) \), a ideia é computar e armazenar \( f(n) \) na primeira vez que é chamado. Se \( f(n) \) for chamado novamente, retornamos o valor armazenado, o que evita cálculos redundantes e melhora a eficiência do algoritmo.

## Exemplo Prático: Sequência de Fibonacci

A sequência de Fibonacci é um clássico exemplo para ilustrar a programação dinâmica. A sequência é definida como:

<div align="center">

![Sequência de Fibonacci](/images/formula-sequencia-fibonacci.webp)

[Imagem disponivel em deverdecasaalumnus](https://deverdecasaalumnus.wordpress.com/2020/09/04/sequencia-fibonacci/)

</div>

### Implementação Recursiva Simples

A implementação recursiva tradicional de Fibonacci tem uma complexidade exponencial \( O(2^n) \), devido ao cálculo repetitivo dos mesmos valores:

```python
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
```

### Implementação com Memoization
Com a memoization, o tempo de execução é reduzido para 𝑂(𝑛), pois armazenamos os resultados dos cálculos anteriores:

```python
def fibonacci_memo(n, memo={}):
    if n in memo:
        return memo[n]
    if n == 0:
        result = 0
    elif n == 1:
        result = 1
    else:
        result = fibonacci_memo(n-1, memo) + fibonacci_memo(n-2, memo)
    memo[n] = result
    return result
```

### Exemplo Prático: Grafos Acíclicos Direcionados (DAGs)

Outro exemplo comum é a busca do caminho mais curto em um DAG. A programação dinâmica pode ser aplicada usando uma ordenação topológica dos vértices.

#### Implementação Simplificada

Suponha que graph[u][v] represente o peso da aresta de u para v. Podemos calcular o caminho mais curto de um vértice inicial para todos os outros vértices em um DAG com a seguinte abordagem:


```python
def shortest_path_dag(graph, start):
    order = topological_sort(graph)
    dist = {v: float('inf') for v in graph}
    dist[start] = 0
    
    for u in order:
        for v in graph[u]:
            if dist[v] > dist[u] + graph[u][v]:
                dist[v] = dist[u] + graph[u][v]
                
    return dist

```
A ordenação topológica garante que os vértices sejam processados na ordem correta, permitindo que as soluções dos subproblemas menores sejam usadas para resolver subproblemas maiores de forma eficiente.


## Conclusão

A programação dinâmica é uma técnica fundamental na ciência da computação, permitindo a solução eficiente de problemas complexos que, de outra forma, seriam computacionalmente inviáveis. Com a utilização de técnicas como memoization e abordagem bottom-up, é possível evitar redundâncias e reduzir drasticamente o tempo de execução de algoritmos. Suas aplicações vão desde problemas de otimização clássicos até questões práticas em engenharia e ciência, tornando-se uma ferramenta indispensável para qualquer cientista da computação ou engenheiro de software.

## Links Importantes

- [Memoization](https://en.wikipedia.org/wiki/Memoization)
  - Página da Wikipedia sobre Memoization
- [Greedy vs dynamic algorithms](http://www.cs.otago.ac.nz/cosc242/pdf/L22.pdf)
  - Material que compara greedy e dynamic, da Universidade de Otago
- [A Comparison of Greedy Algorithm and Dynamic Programming Algorithm](https://www.shs-conferences.org/articles/shsconf/abs/2022/14/shsconf_stehf2022_03009/shsconf_stehf2022_03009.html)
  - Uma comparação entre algoritmo guloso e o algoritmo de programação dinâmica
- [A Sequência de Fibonacci](https://deverdecasaalumnus.wordpress.com/2020/09/04/sequencia-fibonacci/)
  - Explicação sobre a Sequência de Fibonacci
- [Sequência de Fibonacci em Python](https://www.youtube.com/watch?v=CPm9jyw5zKk)
  - Video no youtube sobre Sequência de Fibonacci em Python
- [Caminhos Mínimos Ponderados em DAGs e em Grafos Gerais](https://www.youtube.com/watch?v=VlqfMJDit20)
  - Video no youtube sobre Caminhos Mínimos em DAGs
