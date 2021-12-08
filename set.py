s=set() #collection of unique elements
print(type(s))

#making set from list
s2=set([1,2,3,4])
print(s2)
print(type(s2))

#adding element in set
s2.add(13)
s2.add(18)
print(s2)

#union of sets
s2=s2.union({40,50})
print(s2)

#intersection
s3=s2.intersection({3,4,40,13})
print(s3)

#getting min/max
print(min(s2),max(s2))

#removing element
s2.remove(max(s2))
print(s2)