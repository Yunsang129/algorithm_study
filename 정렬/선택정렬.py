arr = [7,5,9,0,3,1,6,2,4,8]
for i in range(len(arr)):
    min_index = i  #가장 작은 원소의 인덱스
    for j in range(i + 1, len(arr)): #가장 작은 원소보다 +1 해서 그 원소 이후부터 배열의 끝까지 탐색
        if arr[min_index] > arr[j]: #인덱스로 저장
            min_index = j
    arr[i], arr[min_index] = arr[min_index], arr[i] #스왑하기 가장 작은 값을 가진 인덱스를 구하고, 가장 작은 인덱스와 교체하기
print(arr)