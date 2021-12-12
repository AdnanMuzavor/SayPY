
"""Use for calculating time for program running"""

import time
init1 = time.time()
k = 0
while(k < 45):
    print(k)
    k += 1
print("Time taken:", (time.time()-init1)*1000, "s")

init2 = time.time()
for i in range(45):
    print(i)
    i += 1
print("Time taken:", (time.time()-init2)*1000, "s")

"""This will return tupal"""
print(time.localtime(time.time()))
"""This wil convert tupal to understandable"""
localtm = time.asctime(time.localtime(time.time()))
print(localtm)
