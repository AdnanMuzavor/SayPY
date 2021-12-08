#Faulty calculator

var1 = input("Enter n1: ")
var1 = int(var1)
var2 = input("Enter n2: ")
var2 = int(var2)
operator = input("Enter operator: ")
if operator == "*":
    print(var1, "*", var2, "=", var1+var2+var1*var2)
elif operator == "+":
    print(var1, "+", var2, "=", var1*var1+var2+var2*var2)
elif operator == "/":
    print(var1, "/", var2, "=", var1/var1+var2+var2/var2)
else:
    print(var1, "-", var2, "=", var1-var2)
