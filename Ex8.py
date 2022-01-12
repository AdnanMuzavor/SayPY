import os

"""Part-1: open open folder with help of path and list all docs"""
"""Part-2: open file and make first char of each line capitalise"""


def formatter(path, filename, extension):
    originalpath = path+"/"+filename
    print(originalpath)

    try:
        files = os.listdir(path)
        for f in files:
            print(f)

        "For making first letter of each word capital while reading"
        file2 = open(f"{path}/{filename}.txt", "r+")
        for line in file2:
            output = line.title()
           # file2.write(output)
            print(output)
        file2.close()

        """This lines will change .txt to .py and .py to .txt"""
        fullfilename = f"{path}/{filename}.txt"  # change this as per preference
        name, ext = os.path.splitext(fullfilename)
        if ext == ".txt":

            print(name, "->extension->", ext)

            os.rename(fullfilename, name+".py")

        else:
            fullfilename = f"{path}/{filename}.py"
            print(name, "->extension->", ext)
            os.rename(fullfilename, name+".txt")

    except Exception as e:
        print(e)


path = f"ex8folder"

file = "ex8doc"

formatter(path, file, "png")
