import json

data = '{"var1":"harry","vat2":56}'  # Data in json format
print(data)
# This considered as just a string hence you cannot do print(data['var1])
try:
    print(data['var1'])
except Exception as e:
    print(e)

"""JSON loads function"""
# After parsing it's no longet a string but similar to dictionary type
# Hence we can access elements as we used to incase of dictionary
parsed = json.loads(data)
print(parsed)
print(type(parsed))
print(parsed['var1'])


"""JSON load function"""
"""Used for opening json file """
f = open("data.json")
print("Type of f: -> ", type(f))
print("Data of of before parsing/load fn-> ", f)
fileparsed = json.load(f)
print("Data of of after parsing/load fn-> ", fileparsed)
for emps in fileparsed['emp_details']:
    print(emps)

"""JSON dump function"""
#This is dictionary

# This code being python won't work properly in javascript
data2 = {
    "channel_name": "CodeWithHarry",
    "cars": ['bmw', 'audi a8', 'ferrari'],
    "fridge": ('roti', 540),
    "isbad": False
}
print(data2)
print(type(data2))
# Hence to convert it into proper JS we use json.dump

jscomp = json.dumps(data2)  # Returns JS compaitable object
print(jscomp)
print(type(jscomp))


"""JSON sort_keys parameter"""
