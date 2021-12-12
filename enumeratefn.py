l1=["ab","cd","eg","gh"]
i=1
print("Running: ")
for item in l1:
    if i%2!=0:
        print(f"------>{item}")
    i+=1    

"""enumerate gives both index and item of listitems """

for index,item in enumerate(l1):
    if (index+1)%2!=0:
        print(f"{item} at {index+1}")