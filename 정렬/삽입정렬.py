arr = [7,5,9,0,3,1,6,2,4,8]
for i in range(1, len(arr)):   #len의 길이를 전부 훑는 반복문 (그러나, 첫번째 항은 제외)
    for j in range(i, 0, -1):  #선택한 인덱스부터 가장 첫 번째 인덱스까지 훑기
        if arr[j] < arr[j -1]:         #두 인덱스의 값의 크기비교 후 스왑
            arr[j], arr[j-1] = arr[j-1], arr[j]
        else:
            break
    print(arr)
print(arr)