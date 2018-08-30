def find_max(list):
    if len(list) == 2:
        return list[0] if list[0] > list[1] else list[1]
    submax = find_max(list[1:])
    return list[0] if list[0] > submax else submax

if __name__ == '__main__':
    testdata = [1, 8, 9, 21, 3, 5]
    print(find_max(testdata))