"""else in exception handling will execute only if there is no exception"""
"""Finally in exception handling will always be executed"""
"""Finally is used to clear all used data in program"""
"""For eg if file was opend prior to trycatch block,it should be closed"""
f1 = open("Ex5File1.txt")
try:
    # f = open("toro.txt")  # trying to open unexisting file ->exeception block
    f = open("Ex5File1.txt")  # trying to open existing file ->else block
except Exception as e:
    print(e)
except EOFError as e:
    print(e)
except IOError as e:
    print(e)
else:
    print("It did't went in exception block")
finally:
    print("Cloing file which was opened")
    f1.close()
