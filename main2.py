#height define if the person can or not join the park. it has to be more than 120cm to enter the park.
height = int(input("What's your height? "))
if height < 120:
 print(" you are too young! ")                 #add "you are X cm short"
 
#pricing is based on age
else:
 age = int(input("What's your age? "))
 if age < 12:
  ticket_price = 5 
 elif 12 <= age <= 18:
  ticket_price = 7
 elif age >= 18:  #elif 45 <= age <= 55:
  ticket_price = 12 

#photo?      if yes, the program has to add 3$ on the prior price.
 want_photo = input("Do you want a photo? (yes/no): ")
 if want_photo == "yes":
   ticket_price += 3
   print(" Thank you! That will be:", ticket_price)
 
 elif want_photo == "no":
   print("Your total bill is:", ticket_price)
 else:
   print(" invalid")

