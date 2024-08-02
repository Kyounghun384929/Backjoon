N = int(input())

A = list(map(int, input().split()))
B = list(map(int, input().split()))

A_sort = sorted(A, reverse=True)
B_sort = sorted(B)

S = 0
for i in range(N):
    S += A_sort[i] * B_sort[i]
    
print(S)
