# James Taddei
# Review Meeting 13
# 2/13/23

if (True): # Meeting 10 (Modules)
    # Keywords
    from exModule import num1
    print(num1)
    import math as m
    print(m.pi)
    print(dir(m))

    print()

    # Example Custom Module
    import exModule
    print(exModule.foo())
    print(exModule.num2)

    print()

    # Time Module
    import time
    print(time.perf_counter())
    time.sleep(2)
    print(time.time())

    print()

    # Math Module
    import math
    print(math.ceil(0.4))
    print(math.fabs(-83))
    print(math.floor(0.8))
    print(math.sqrt(16))
    print(math.pi)
    print(math.inf)

    print()

    # Random Module
    import random
    random.seed(3)
    print(random.randint(0, 99))
    options = ["a", "b", "c"]
    print(random.choice(options))
    random.shuffle(options)
    print(options)

print("\n")

if (True): # Meeting 11 (Binary Search)
    def binarySearch(lst: list, target: int) -> int:
        """
        Returns the index of the target if present, otherwise
        returns -1.
        """
        low = 0
        high = len(lst) - 1
        mid = 0

        while low <= high:
            mid = (high + low) // 2

            if lst[mid] < target: # ignore left
                low = mid + 1
            elif lst[mid] > target: # ignore right
                high = mid - 1
            else: # found target
                return mid

        return -1 # target not in list
    
    lst = [2, 3, 4, 10, 40]
    target = 10
    print(f"{target} is at index {binarySearch(lst, target)}.")

print("\n")

if (True): # Meeting 12 (Files)
    fileName = "/Users/james.taddei/Desktop/Programming Club 22-23/Meeting 13 Stuffs/"
    fileName += "reviewMeeting13/file.txt"

    # Picking Mode + Read
    with open(fileName, "r") as f1:
        data1 = f1.read()
        print(data1)

    print()

    # Readlines
    with open(fileName) as f2:
        data2 = f2.readlines()
        print(data2)

    print()

    # Readline
    with open(fileName) as f3:
        data3 = f3.readline()
        print(data3)

    print()

    # Seek
    with open(fileName) as f4:
        f4.seek(10)
        data4 = f4.readline()
        print(data4)

    print()

    # Write
    fileName2 = "/Users/james.taddei/Desktop/Programming Club 22-23/Meeting 13 Stuffs/"
    fileName2 += "reviewMeeting13/file2.txt"
    with open(fileName2, "w") as f5: # write
        f5.write("Hello ")
    with open(fileName2, "a") as f5: # append writing
        f5.write("World!")
    with open(fileName2) as f5: # output
        print(f5.read())

    print()

    # For Loop Read Each Line
    with open(fileName) as f6:
        for line in f6:
            print(line)
