#dictionary is key value pair
d1={} #blanlk tuple and not dictionary

#eg-1
d2={1:"Harruy",2:"parruy"}
print(d2)
print(d2[1])

#eg2->nesting list in dictionarya nd again dictionary in list
d3={"Ad":"pc","g":456,"e":['8','2',{3:'4',5:'6'}]}
print(d3["Ad"])
print(d3["e"])
print(d3["e"][2])
print(d3["e"][2][3])

#Appending elements in dictionary
d3["ff"]="gg"
print(d3)

d3[120]=246
print(d3)

#Removing elements from dictionary
del d3["g"]
print(d3)

#d4=d3 means bothreferring to same dictionary and any changes in d4 will reflect in d3 and vice-versa
d4=d3
del d4["ff"]
print(d3)

#to avoid above problem use copy fn
d5=d3.copy()

#get gn
print(d5.get("e"))

#update fn
print(d5.update({"leeeeee":"veeeeeee"}))
print(d5)

#printing keys and items
print(d5.keys())

print(d5.items())

