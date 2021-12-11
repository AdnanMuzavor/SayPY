import random

#getting random integers in given range
randomno = random.randint(0, 5)
print(randomno)

#getting any random number
random2 = random.random()*100  # 1000 or 10000 as per your need
print(random2)

#getting random item from list
list = ["12", "34", "56", "78"]
choice = random.choice(list)
print(list)
