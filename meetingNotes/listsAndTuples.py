# James Taddei
# Lists and Tuples
# 11/9/22

# Basic List
lst = [1, 2, 3, 4, 2]
print(lst)
multiType = [1, "hello", 3.8, True]
print(multiType)
blankList1 = []
blankList2 = list()

print()

# Loop Through List
for num in lst:
    print(num)

print()

# 2d Array
array = [[1, 2], [2, 3], [3, 4]]

print()

# Indexing
print(lst[1]) # Starts at 0
lst[1] = 7
print(lst)
lst[2:5] = [9, 10]
print(lst)

print()

# Other Commands
print(f"Length: {len(lst)}")
print(10 in lst)
print(-1 in lst)
del blankList1
print(min(lst))
print(max(lst))

print()

# Methods
accounts = [2, 5.3, -89, 200]
accounts.append(9)
print(f"Append 9: {accounts}")
accounts.insert(1, 9)
print(f"Insert 1,9: {accounts}")
print(f"Index 9: {accounts.index(9)}")
print(f"Pop 2 return: {accounts.pop(2)}")
print(f"Pop 2: {accounts}")
print(f"Count 9: {accounts.count(9)}")
if (True): # Copy by reference
    accounts2 = accounts
    accounts[0] = 7
    print(f"Accounts2: {accounts2}")
accounts2 = accounts.copy()
accounts[0] = 93
print(f"Accounts2 Copied: {accounts2}")
accounts.sort()
print(f"Sorted: {accounts}")
accounts.extend(accounts2)
print(f"Extend: {accounts}")
accounts.reverse()
print(f"Reverse: {accounts}")
accounts.clear()
print(f"Clear: {accounts}")

print()

# Tuple
t = (3,5)
print(t)
# t[0] = 8 # causes error

# Returning w/ Tuple
def getLocation():
    return (8,1)
x, y = getLocation()
print(f"x: {x}, y: {y}")