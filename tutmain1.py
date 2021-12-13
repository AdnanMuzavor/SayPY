#Refer tutmain1 and tutmain2
def fn(str):
    print(f"this fn will print {str}")


def add(a, b):
    print(a+b)


print("Name is: ", __name__)
if __name__ == '__main__':
    fn("Harry")
    add(2, 6)
