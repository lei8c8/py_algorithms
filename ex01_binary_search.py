def binary_search(list, item):
    low = 0
    high = len(list) - 1
    while low <= high:
        mid = (low + high) // 2
        if list[mid] == item:
            return mid
        elif list[mid] < item:
            low = mid + 1
        else:
            high = mid -1
    return None

if __name__ == '__main__':
    testdata = []
    for i in range(100):
        testdata.append(i)
    result = binary_search(testdata, 40)
    print(f"result is {result}")