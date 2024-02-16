#brinquedo
1
height = 170

if height < 120:
 print("não pode")

#pricing
else:
 age = int(input("What's your age? "))
 if age < 12:
  print("5$") 
 elif 12 <= age <= 18:
  print("7$") 
 elif age >= 18:
  print("12$") 

#photo?
 want_photo = input("Do you want a photo? (yes/no): ")
 if want_photo == "yes":
   print(" that will be 3$")
 elif want_photo == "no":
   print(" ok")
 else:
   print(" Resposta inválida")


   

  
  

 