n, k = map(int, input().split())
jo = [i for i in range(1 , n+1)]

answer = []
num = 0

for j in range(n):
    num += k-1
    if num >= len(jo):
        num = num % len(jo)
        
    answer.append(str(jo.pop(num)))
print("<", ", ".join(answer), ">", sep='')