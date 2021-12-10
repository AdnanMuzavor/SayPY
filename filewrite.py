# #getting the file in write method
"""Writing in created file"""
# f=open("learnfile.txt","w")
# #it'll clear content of the file
# f.write("Writing in a file")
# #closing file
# f.close()
"""Writing in file not created"""
# f=open("newfile.txt","w") #this file is not pre-made but il'll get created
# f.write("File created by py")
# f.close()


"""Appending in a file"""
f=open("newfile.txt","a") #opening file in appending mode
a=f.write("File created by py\n") #content of file won't get cleared instead code will be appended
print(a) #write fn returns no of chars written/appended
f.close()