# Regular expressions
# functions: findall, search, split, sub, finditer

"""row string"""
import re
print("\n")  # Will leave a line
print(r"\n")  # takes '\n' as character
mystr = "You are given an array prices where prices[i] is the price of a given stock on the ith dayFind many +91-12348901 the maximum profit you can achieve. You may complete as many transactions as you like (i.e., buy one and sell one share of the stock multiple times) with many the following restrictions:After you sell your stock, you cannot buy +91-1234567 stock on the next day (i.e., cooldown one day).Note: You may not engage in multiple transactions many simultaneously (i.e., you must sell the stock before +91-98453271 you buy again 12345-6789"

print(re.findall("multiple", mystr))  # gives all occurence of multiple

print(re.search("are", mystr))  # gives starting and end character of string

# returns string separated at places where 'many' was found
print(re.split("many", mystr))

# Finding word 'sell' using finditr
# finditr returns list
mystrnew = re.compile(r'sell')
mystrnew = re.compile(r'..ll')  # '.' stands for any character so it's same as sell,foll
matches = mystrnew.finditer(mystr)
for match in matches:
    print(match)

"""tO check of string starts with certain character"""
mystrnew = re.compile(r'^You')  # '^' stands for any first word of string
matches = mystrnew.finditer(mystr)
for match in matches:
    print(match)    

"""tO check of string ends with certain character"""
mystrnew = re.compile(r'again$')  # '^' stands for any first word of string
matches = mystrnew.finditer(mystr)
for match in matches:
    print(match)    

"""tO check of string has character with n number of next chars eg (ai*) for ai,aii,aiiii (existance of i not compulsory) """
mystrnew = re.compile(r'ai*')  # '^' stands for any first word of string
matches = mystrnew.finditer(mystr)
for match in matches:
    print(match)   

print("_______________________________")
"""tO check of string has character with n number of next chars eg (ai*) for ai,aii,aiiii (existance of i compulsory) """
mystrnew = re.compile(r'ai+')  # '^' stands for any first word of string
matches = mystrnew.finditer(mystr)
for match in matches:
    print(match)     

print("_______________________________")
"""tO check of string has character with exact number(here, 2) of next chars eg (ai*) for ai,aii,aiiii (existance of i compulsory) """
mystrnew = re.compile(r'fol{2}')  # '^' stands for any first word of string
matches = mystrnew.finditer(mystr)
for match in matches:
    print(match)        

print("_______________________________")
"""tO check of string has character with exact number(here, 2) of next chars or find some other word instead  """
mystrnew = re.compile(r'fol{2}|you')  # '^' stands for any first word of string
matches = mystrnew.finditer(mystr)
for match in matches:
    print(match)      

print("_______________________________")
"""Find words starting with certain chars"""
mystrnew = re.compile(r'\by')  # '^' stands for any first word of string
matches = mystrnew.finditer(mystr)
for match in matches:
    print(match)   

print("_______________________________")
"""Find words ending with certain chars"""
mystrnew = re.compile(r'ly\b')  # '^' stands for any first word of string
matches = mystrnew.finditer(mystr)
for match in matches:
    print(match)   

print("_______________________________")  
"""To find number of type 11111-2222"""
mystrnew = re.compile(r'\d{5}-\d{4}')  # '^' stands for any first word of string
matches = mystrnew.finditer(mystr)
for match in matches:
    print(match)  

"""TASK find phone numbers starting with +91"""
print("_______________________________")  
"""To find number of type 11111-2222"""
mystrnew = re.compile(r'\d{2}-\d{8}')  # '^' stands for any first word of string
matches = mystrnew.finditer(mystr)
for match in matches:
    print(match)  
