import pickle
import requests

# Getting data with help of request.get(url)
data = requests.get(
    "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data")
# print(data.text)
list = []

# Putting each character in list
for line in data.text:

    #print(line, end="")
    list.append(line)


print(list)

# making list of sentences with help of '\n'
list2 = []
str = ""
for item in list:
    if item != '\n':
        str += item
    else:
        # print(str)
        list2.append(str)
        str = ""
print(list2)


"""Writing this list into file"""

# try:
#     file = "ex9.pkl"
#     fileobj = open(file, 'wb')
#     pickle.dump(list2, fileobj)
#     fileobj.close()
# except Exception as e:
#     print(e)

"""Retrieving this list from file"""

file = "ex9.pkl"
fileobj = open(file, 'rb')
mydata = pickle.load(fileobj)
print("DATA RETRIEVED FROM FILE: ", mydata)
