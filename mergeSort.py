from random import randint

def mergeSort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]
        mergeSort(left_half)
        mergeSort(right_half)

        left_index = right_index = new_index = 0
        while left_index < len(left_half) and right_index < len(right_half):
            if left_half[left_index] < right_half[right_index]:
                arr[new_index] = left_half[left_index]
                left_index += 1
            else:
                arr[new_index] = right_half[right_index]
                right_index += 1
            new_index += 1

        while left_index < len(left_half):
            arr[new_index] = left_half[left_index]
            left_index += 1
            new_index += 1
        
        while right_index < len(right_half):
            arr[new_index] = right_half[right_index]
            right_index += 1
            new_index += 1
    # base recusion case is here
    else:
        return arr

# test case is in main
if __name__ == '__main__':
    testdata = []
    for i in range(100):
        testdata.append(randint(0,10000))
    print("Before merge sort:")
    print(testdata)
    # sort it using merge sort function
    mergeSort(testdata)
    print("After merge sort:")
    print(testdata)
