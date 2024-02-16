#print("Thank you for choosing Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L") 
if size not in ["S", "M", "L"]:
    print("INVALID, please insert S, M or L sizes")
add_pepperoni = input("Do you want pepperoni? Y or N") 
extra_cheese = input("Do you want extra cheese? Y or N") 
 
bill = 0
#size

if size == "S":            #small pizza
 bill += 15
 if add_pepperoni == "Y":  
     bill += 2
     if extra_cheese == "Y":
      bill += 1   
elif size == "M":          #medium pizza
    bill += 20
    if add_pepperoni == "Y":  
     bill += 3
     if extra_cheese == "Y":
      bill += 1
elif size =="L":            #large pizza
 bill += 25
 if add_pepperoni == "Y":  
     bill += 3
     if extra_cheese == "Y":
      bill += 1

print(" your final bill is:", bill)



'''
                                        chat gpt
size = input("What size pizza do you want? S, M, or L: ")
add_pepperoni = input("Do you want pepperoni? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")

bill = 0

# Size
if size == "S":
    bill += 15
elif size == "M":
    bill += 20
elif size == "L":
    bill += 25
else:
    print("Invalid size input")

# Pepperoni
if add_pepperoni == "Y":
    if size == "S":
        bill += 2
    elif size == "M" or size == "L":
        bill += 3

# Extra Cheese
if extra_cheese == "Y":
    bill += 1

print("Your final bill is:", bill)'''