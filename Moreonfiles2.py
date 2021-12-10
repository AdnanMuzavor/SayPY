#Opening file with block
#closes file automatically

with open("newfile.txt") as f:
    a=f.read(4)
    print(a)
