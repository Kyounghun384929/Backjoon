n= int(input())
stu_num = []

for _ in range(n):
    stu_num.append(str(input()))

for i in range(1, len(stu_num[0])+1):
    results = []
    for j in range(n):
        if stu_num[j][-i:] in results:
            break
        else:
            results.append(stu_num[j][-i:])
        
    if len(results) == n:
        print(i)
        break
