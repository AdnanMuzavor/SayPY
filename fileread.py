# 'r' for reading from file
# 'w' for writing into file
# 'x' for creating file if not exist
# 'a' add more content to file
# 't' for text mode
# 'b' for binary mode
# '+' for read and write

# for opening a file
f = open("learnfile.txt", "rt")  # by default read mode "rt"

"""METHOD-1"""
# for reading content of the file(entire)

# content = f.read()
# print(content)

"""METHOD-2"""
# for reading as group of chars provided aboce code must be commented out
# content2=f.read(8) #reads first 3,same fn on next call will read next 3
# print(content2)
# content2=f.read(8)
# print(content2)
# content2=f.read(8) #reads first 3,same fn on next call will read next 3
# print(content2)
# content2=f.read(8)
# print(content2)


"""METHOD-3"""
# reading line by line
# content = f.read()
# for line in content:  # '/n' helps in identifying new line
#     print(line)

"""reading directly from file using f pointer"""
# for line in f:
#     print(line, end="")

"""METHOD-4"""

# # for opening a file
# f = open("learnfile.txt", "rt")  # by default read mode "rt"

# #Using readline function
# print(f.readline())
# print(f.readline())


# # for opening a file
# f = open("learnfile.txt", "rt")  # by default read mode "rt"

# converting lines in file as list items
# print(f.readlines())
# closing a file
f.close()  # to free all resources acting on file

# using other modes
# f=open("learnfile.txt","")
