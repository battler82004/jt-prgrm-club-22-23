# James Taddei
# Loop Speed
# 10/12/22

import time

runs = 100_000

startTime = time.time()

i = 0
while(i < runs):
    print(i)
    i += 1

whileTime = time.time() - startTime

startTime = time.time()
for i in range(runs):
    print(i)

forTime = time.time() - startTime

print(f"Counting while = {whileTime} seconds")
print(f"For loop = {forTime} seconds")