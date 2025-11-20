import heapq
import sys
inf = 10**18

N = int(input("Digite o número de salas: "))
M = int(input("Digite o número de escorregadores: "))
C = int(input("Digite a quantidade de pessoas que ouviram o grito: "))
K = int(input("Digite a distância máxima que o grito alcança (K): "))

print(f"\nDigite os {C} números das salas onde há pessoas que ouviram o grito:")
pessoas = list(map(int, input().split()))

grafo = [[] for _ in range(N+1)]
print(f"\nDigite os {M} escorregadores (formato: origem destino distância):")
for _ in range(M):
    A, B, D = map(int, input().split())
    grafo[A].append((B, D))  

alcanca = set(pessoas)
fila = [(0, p) for p in pessoas]
heapq.heapify(fila)

while fila:
    dist, s = heapq.heappop(fila)
    if dist > K:
        continue
    for nxt, d in grafo[s]:
        if nxt not in alcanca and dist + d <= K:
            alcanca.add(nxt)
            heapq.heappush(fila, (dist + d, nxt))

if N in alcanca:
    print("\nO técnico ouviu o grito diretamente! Tempo = 0")
    sys.exit()

dist = [inf] * (N+1)
pq = []
for s in alcanca:
    dist[s] = 0
    heapq.heappush(pq, (0, s))

while pq:
    tempo, s = heapq.heappop(pq)
    if tempo > dist[s]:
        continue
    for nxt, d in grafo[s]:
        novo = tempo + d
        if novo < dist[nxt]:
            dist[nxt] = novo
            heapq.heappush(pq, (novo, nxt))

if dist[N] < inf:
    print(f"\nO tempo mínimo para alcançar o técnico é: {dist[N]} segundos")
else:
    print("\nNão foi possível alcançar o técnico.")
