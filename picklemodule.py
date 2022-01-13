import pickle

"""pickling python object"""

# pickling is process of preserving
# cars = ["pp", "qq", "rr", "ss"]
# file = "mycar.pkl"
# fileobj = open(file, 'wb') #'wb' -> write binary mode
#  # retruns file object
# # dumping/preserving cars/something in file so that it can be retrived later
# pickle.dump(cars, fileobj)
# fileobj.close()

"""Retrieving from pickle/stored file"""

# file = "mycar.pkl"
# fileobj = open(file, 'rb')  # 'rb'-> read binary mode
# mycars = pickle.load(fileobj)
# print(mycars)
# print(type(mycars))
# fileobj.close()

"""pickling python dictinaey"""
# dict={"hello":"hi","gg":"pp","rr":"qq","mm":"nn"}
# file="dict.pkl"
# fileobj=open(file,'wb')
# pickle.dump(dict,fileobj)
# fileobj.close()

"""Reading data from dictionary"""
file = "dict.pkl"
fileobj = open(file, 'rb')
mydict = pickle.load(fileobj)
print(mydict)
print(type(mydict))
