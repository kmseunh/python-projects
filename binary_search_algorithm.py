def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low < high:
        mid = (high + low) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1


list = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
target = 18

result = binary_search(list, target)

if result != -1:
    print(f"원소 {target}는 인덱스 {result}에 있습니다.")
else:
    print(f"원소 {target}는 배열에 없습니다.")
