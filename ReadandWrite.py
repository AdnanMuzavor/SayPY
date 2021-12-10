# opening in both read and file mode
f = open("newfile.txt", "r+")
"""Reading everything"""
print(f.read()) #returns content of file

"""Reading line by line"""
# print(f.readline())
# print(f.readline())

"""Writing i.e content will get appended"""
#to write read file content to tk pointer to last char
f.write("New content")

f.close()
