l1 = ["hello", "pello", "vello", "dello"]
for i in l1:
    print(i)

#Handling list of list
l2 = [["hello", 2], ["rello", 4], ["vello", 8], ["dello", 10]]
print(l2)
for  itm, cnt in enumerate(l2):
    print("index:","itm: ",itm, "->", cnt[0],cnt[1])

#typacasting list to dictionary
dict = dict(l2)
print(dict)

for itm,cnt in dict.items():
    print(itm,"---->",cnt)
