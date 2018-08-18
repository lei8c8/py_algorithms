from random import randint

def count_recursion(list):
    if len(list) == 0:
        return 0
    else:
        return 1 + count_recursion(list[1:])

if __name__ == "__main__":
    testdata = []
    for i in range(100):
        testdata.append(randint(0,10000))
    result = count_recursion(testdata)
    print(f"Result: {result}")