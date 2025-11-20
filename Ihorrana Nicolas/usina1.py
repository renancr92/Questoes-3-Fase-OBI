import heapq
import sys
input = sys.stdin.readline
inf = 10**18

N, M, C, K = map(int, input().split())
pessoas = list(map(int, input().split()))

grafo = [[] for _ in range(N+1)]
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
    print(0)
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

print(dist[N] if dist[N] < inf else -1)
