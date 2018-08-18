from random import randint

def find_smallest(arr):
    smallest_element = arr[0]
    smallest_index = 0
    for i in range(1, len(arr)):
        if arr[i] < smallest_element:
            smallest_element = arr[i]
            smallest_index = i
    return smallest_index

def selection_sort(arr):
    result = []
    for _ in range(len(arr)):
        smallest = find_smallest(arr)
        result.append(arr.pop(smallest))
    return result

if __name__ == '__main__':
    testdata = []
    for i in range(20):
        testdata.append(randint(0, 100))
    print(f"Before selection sort: {testdata}")
    testdata = selection_sort(testdata)
    print(f"After selection sort: {testdata}")