f = open("newfile.txt")
print(f.tell())  # tell location of the pointer
print(f.readline())
print(f.tell())
print(f.readline())
print(f.tell())

f.seek(10) #brings pointer to char no we want
print(f.tell()) #shows 10 as ptr shifted to 10
f.close()
