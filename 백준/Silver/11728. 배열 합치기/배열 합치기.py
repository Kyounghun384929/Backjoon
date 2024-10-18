def merge_sorted_arrays(arr1, arr2):
    i, j = 0, 0
    merged = []
    
    # 두 배열을 하나로 병합하는 과정
    while i < len(arr1) and j < len(arr2):
        if arr1[i] <= arr2[j]:
            merged.append(arr1[i])
            i += 1
        else:
            merged.append(arr2[j])
            j += 1
    
    # 남은 요소가 있으면 추가
    while i < len(arr1):
        merged.append(arr1[i])
        i += 1
    
    while j < len(arr2):
        merged.append(arr2[j])
        j += 1
    
    return merged

# 입력 받기
n, m = map(int, input().split())  # 배열 크기 입력
arr1 = list(map(int, input().split()))  # 첫 번째 배열
arr2 = list(map(int, input().split()))  # 두 번째 배열

# 결과 출력
result = merge_sorted_arrays(arr1, arr2)
print(' '.join(map(str, result)))
