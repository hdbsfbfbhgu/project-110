import random

roll_again = "y"

while roll_again == "y":
    no = random.randint(1,6)

    if no==1:
        print("{-----}")
        print("{     }")
        print("{  0  }")
        print("{     }")
        print("{-----}")
        input("press y to continue and n to exit")

    if no==2:
        print("{-----}")
        print("{     }")
        print("{ 0 0 }")
        print("{     }")
        print("{-----}") 
        input("press y to continue and n to exit")

    if no==3:
        print("{-----}")
        print("{  0  }")
        print("{   0 }")
        print("{    0}")
        print("{-----}")
        input("press y to continue and n to exit")

    if no==4:
        print("{-----}")
        print("{0   0}")
        print("{     }")
        print("{0   0}")
        print("{-----}")
        input("press y to continue and n to exit")

    if no==5:
        print("{-----}")
        print("{0   0}")
        print("{  0  }")
        print("{0   0}")
        print("{-----}")
        input("press y to continue and n to exit")

    if no==6:
        print("{-----}")
        print("{0   0}")
        print("{0   0}")
        print("{0   0}")
        print("{-----}")
        input("press y to continue and n to exit")