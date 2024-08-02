from collections import deque
import sys

def topology_sort(N, graph, in_degree):
    result = []
    queue = deque()

    # 진입 차수가 0인 노드들을 큐에 삽입
    for i in range(1, N + 1):
        if in_degree[i] == 0:
            queue.append(i)

    while queue:
        current = queue.popleft()
        result.append(current)

        for neighbor in graph[current]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    return result

def main():
    input = sys.stdin.read
    data = input().split()
    
    N = int(data[0])
    M = int(data[1])
    
    graph = [[] for _ in range(N + 1)]
    in_degree = [0] * (N + 1)
    
    index = 2
    for _ in range(M):
        A = int(data[index])
        B = int(data[index + 1])
        graph[A].append(B)
        in_degree[B] += 1
        index += 2

    result = topology_sort(N, graph, in_degree)
    print(' '.join(map(str, result)))

if __name__ == "__main__":
    main()
