import math
import heapq
import sys

def dijkstra(graph, source):
    num = len(graph) - 1
    distance = [math.inf] * (num + 1)
    distance[source] = 0
    
    min_heap = [(0, source)]
    
    while min_heap:
        dist, node = heapq.heappop(min_heap)
        
        if dist > distance[node]:
            continue
        
        for neighbor, weight in graph[node]:
            new_dist = dist + weight
            if new_dist < distance[neighbor]:
                distance[neighbor] = new_dist
                heapq.heappush(min_heap, (new_dist, neighbor))
    
    return distance

V, E = map(int, sys.stdin.readline().split())  # 정점의 수와 간선의 수 입력
K = int(sys.stdin.readline())  # 시작 정점 입력

graph = [[] for _ in range(V + 1)]

for _ in range(E):
    u, v, w = map(int, sys.stdin.readline().split())  # 출발 정점, 도착 정점, 가중치 입력
    graph[u].append((v, w))

result = dijkstra(graph, K)

for i in range(1, V + 1):
    if result[i] == math.inf:
        print("INF")
    else:
        print(result[i])
