from random import randint

def sum_recursion(list):
    if len(list) == 0:
        return 0
    elif len(list) == 1:
        return list[0]
    else:
        return list[0] + sum_recursion(list[1:])

if __name__ == '__main__':
    testdata = []
    for i in range(10):
        testdata.append(randint(0, 9))
    print(f"Test data: {testdata}")
    result = sum_recursion(testdata)
    print(f"Result: {result}")