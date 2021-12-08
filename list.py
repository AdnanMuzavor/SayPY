grocery=["veg1","veg2","veg3",5]
print(grocery)

numbers=[1,6,8,12,54,32]
print(numbers)

#methods
numbers.sort()
print(numbers)

numbers.reverse()
print(numbers)

#Returns only list without updating existing list
print(numbers[::2])

print(len(numbers),max(numbers),min(numbers))

#appending
numbers.append(100)
numbers.append(200)
print(numbers)

#insert(index,val)
numbers.insert(2,24)
numbers.insert(4,32)
print(numbers)

#remove(val)
numbers.remove(200)
print(numbers)

numbers.pop()
print(numbers)
