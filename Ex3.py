guess=200
guesscnt=6
while(True and guesscnt):
    value=input("Enter the val: ")
    if int(value)>guess:
        guesscnt-=1
        print("Val greater, ",guesscnt,"trials left")
        continue
    elif int(value)<guess:
        guesscnt-=1
        print("Val smaller,",guesscnt,"trails left")
        continue
    else:
        print("Yess")
        break