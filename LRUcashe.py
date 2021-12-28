from functools import lru_cache
import time

"""Some fn cosuming n seconds"""
"""If again and again this fn is called this will result in waiti ng making program inefficient"""
"""The best way is to use lru cashe which when is executed once saves it's result to display for next n runs"""


# Now output of this fn will besaved for next 3 runs and hence itll give result faster for next 3 runs
#Only for same value of n
@lru_cache(maxsize=3)
def somework(n):
    time.sleep(n)
    return n


if __name__ == '__main__':
    n = input("Enter n: ")
    print(f"Running fn talking {n} seconds, calling first time")
    # 3 seconds will be consumed here
    somework(int(n))
    n = input("Enter n: ")
    print(f"Running fn talking {n} seconds, calling second time")
    # 3 seconds won't be consumed here
    somework(int(n))
    n = input("Enter n: ")
    print(f"Running fn talking {n} seconds, calling third time")
    # 3 seconds won't be consumed here
    somework(int(n))
    n = input("Enter n: ")

    print(f"Running fn talking {n} seconds, calling forth time")
    # 3 seconds won't be consumed here
    somework(int(n))
    n = input("Enter n: ")
    print(f"Running fn talking {n} seconds, calling fifth time")
    # 3 seconds will be consumed here
    somework(int(n))
    n = input("Enter n: ")
    print(f"Running fn talking {n} seconds, calling sixth time")
    # 3 seconds will be consumed here
    somework(int(n))
    print("Done!")
