import sys
import random
list = ["snake", "water", "gun"]


def compoutput(n):
    if n < 10:

        return 0
    elif n >= 10 and n < 20:

        return 1
    else:

        return 2





while True:
    m = int(input("Enter 1 to play\nEnter 2 to exit\nYour choice: "))
    if m == 1:
        chances = 10
        player = 0
        comp = 0
        print("Welcome to the come\nYou have 10 chances\n")

        while chances:
            m = int(input(
                f"Enter 1 for {list[0]}\nEnter 2 for {list[1]}\nEnter 3 for {list[2]}\nYour choice: "))
            m=m-1    
            comp1 = random.randint(0, 30)
            comp2 = compoutput(comp1)
            user = m
            print("m val: ",m,"comp val: ",comp2)
            chances = chances-1
            print(f"\nComp chose: {list[comp2]}\t\tUser chose: {list[m]}")
            if user == comp2:
                print(
                    f"\nDraw\tPlayer score: {player}\t\tComp score: {comp}\t\tChances left: {chances}")
            else:
                if m == 0 and comp2 == 2 or m == 0 and comp2 == 1 or m == 2 and comp2 == 1:
                    comp = comp+1
                    print(
                        f"\nComp won this round\t\tPlayer score: {player}\t\tComp score:{comp}\t\tChances left: {chances}")
                elif m == 2 and comp2 == 0 or m == 1 and comp2 == 0 or m == 1 and comp2 == 2:
                    player = player+1
                    print(
                        f"\nPlayer won this round\t\tPlayer score: {player}\t\tComp score:{comp}\t\tChances left: {chances}")
        if player > comp:
            print(
                f"Player won the game with score: {player} and diff: {player-comp}")
        else:
            print(
                f"Comp won the game with score: {comp} and diff: {comp-player}")
    elif m == 0:
        sys.exit()
    else:
        print("Invalid input")
