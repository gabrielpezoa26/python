print('''aaa''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 
#Write your code below this line 

decision = input(" Do you wanna go left or right? left/right").lower()
if decision == "left":
    decision = input(" congratulations! now liugdasydgsayli, u wanna swim or wait? swim/wait")
    if decision == "wait":
        decision = input(" you waited for the king to arrive in his castle, now, u have to choose among 3 magic potions: blue/yellow/red")
        if decision == "yellow":
            print(" YOU WON!")
        elif decision == "blue":
            print(" u just got sick and died lol")    
        elif decision == "red":
            print(" u lost ur head and died")
        else:
            print(" died again asuhaushaushu")    
    else: print(" you're dead LOL")    
else: print(" you're dead :( )")