
"""args is list of arguments which allows you to pass multiple argumentsnand whose count is likely to change"""

def fn(val,*args):
    print("Val is: ",val)
    for item in args:
        print(item)


list = ["12", "34", "56", "78"]
fn(*list)
list.append("18")
fn(12,*list)

"""kargs is dictionary of arguments which allows you to pass multiple argumentsnand whose count is likely to change"""

def fn2(normalval,*args,**kwargs):
    print("Normal val: ",normalval)
    for item in args:
        print("item:",item," ",end="")
    print("\n")    
    for itm,key in kwargs.items():
        print(itm," -> ",key)    

dict={"name":"namuuuu","rollno":1235678904,"pp":"gedcr"}        
fn2(10,*list,**dict)
