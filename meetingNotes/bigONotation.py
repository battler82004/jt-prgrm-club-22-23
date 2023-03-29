# James Taddei
# Big O Notation
# 3/27/23

# O(1)
print("1")

print()

# O(log n)
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
print(binarySearch([1, 2, 3, 4, 5, 6, 7, 8], 8))

print()

# O(n)
n = 5
for i in range(n):
    print(i)

print()

# O(n log n)

# O(n^2)
n = 5
for i in range(n):
    for j in range(n):
        print(i*n+j)

print()

# O(n^3)
n = 2
for i in range(n):
    for j in range(n):
        for k in range(n):
            print(i * n**2 + j * n + k)

print()

# O(2^n)

# O(n!)
print("a: a: 1! = 1")
print("ab: ab, ba: 2! = 2")
print("abc: abc, acb, bab, bca, cab, cba: 3! = 6")