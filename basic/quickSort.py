def quickSort(list):
    if len(list) == 0 or len(list) == 1:
        return list
    else:
        p = list[0]
        smaller = []
        bigger = []
        for i in range(1, len(list)):
            if list[i] <= p:
                smaller.append(list[i])
            else:
                bigger.append(list[i])
        return quickSort(smaller) + [p] + quickSort(bigger)

if __name__ == '__main__':
    testdata = [8, 7, 9, 0, 2, 1, 3]
    result = quickSort(testdata)
    print(result)
