# Maze Adventure Game
#
# User chooses between left, straight, or right for 10 turns
#
# This program:
#     -randomly generates required numbers for l, s, & r
#     -keeps counters for how many times the user selects l, s or r
#     -if they ever exceed the amount for any direction, they will
#         run into some kind of obstace and fail the maze
#     -if they make it all 10 turns without exceeding the amount, they win!
#

import random

print("=====================WELCOME TO THE MAZE!!!=====================")
print(" ")
print("Setting the scene:")
print("   (1) You are running away to escape a group of wild animals,")
print("       but the only way out is through this maze!")
print("   (2) You have 10 turns to make it out of the maze")
print("   (3) Each turn, select left, right, or straight (l/r/s)")
print("   (4) But watch out - the animals are coming in after you,")
print("       so don't make any wrong turns...")
print(" ")
print("Do you think you have what it takes to make it to the other side?")
print(" ")
start = input("Type 'e' to enter the maze: ")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print(" ")




def gamePlay():
    
    # randomly select max amounts
    maxL = random.randrange(2,6)
    maxR = random.randrange(2,6)
    maxS = random.randrange(2,6)

    countL = 0
    countR = 0
    countS = 0

    # while 10 turns isn't exceeded, keep taking direction input and act accordingly
    i = 1
    while i < 11:
        
        print("[Turn", i, end='')
        direction = input("] Select 'l', 'r' or 's' : ")
        print(" ")
        #--------------------
        if direction == 'l':
            countL += 1
            if countL > maxL:
                print("SSssssSSSsss...")
                print("Oh no!! You ran into a venomous snake!")
                break
            else:
                i += 1
                print("Nice move... You're safe for now.")
                print(" ")
        #--------------------      
        elif direction == 'r':
            countR += 1
            if countR > maxR:
                print("RaAAWwwRRRRR...")
                print("Oh no!! You ran into an angry lion!")
                break
            else:
                i += 1
                print("Good choice. You're getting closer!")
                print(" ")
        #--------------------   
        elif direction == 's':
            countS += 1
            if countS > maxS:
                print("ScREeeEEECCHHH...")
                print("Oh no!! You ran into a pack of wild bats!")
                break
            else:
                i += 1
                print("You're in the clear.")
                print(" ")
        #--------------------    
        else:
            print("Invalid input. Try again.")
            print(" ")
            
    #if they made it through all turns safely
    if i > 10:
        print(".")
        print(".")
        print(".")
        print("Wow, congratulations! You made it safely through the maze.")
        print("Looks like you got lucky today...")
    else:
        print("Looks like you didn't escape the pack today...")
        print(" ")
        print("Better luck next time :)")
        
    print(" ")
    again = input("Play again? (y/n): ")
    print(" ")
    
    return again


### main function ###
end = gamePlay()
while end == 'y':
    print("`'`'`'`'`'`'`'`'`'`'`'`'`'`'`'`'`'`'`'`'`'`'`'`'`'`'`'`'`'`")
    end = gamePlay()
    
print("___________________")
print(" ")
print("Thanks for playing!")

