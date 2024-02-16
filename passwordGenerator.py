import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']   #52
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']  #10
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']   #9

print("Welcome to the PyPassword Generator!")
input_letters = int(input("How many letters would you like in your password?\n")) 
input_symbols = int(input(f"How many symbols would you like?\n"))
input_numbers = int(input(f"How many numbers would you like?\n"))
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
#write below 
password1 = ''
for _ in range(input_letters):
    random_letter = random.choice(letters)
    password1 += random_letter
password2 = ''
for _ in range(input_symbols):
    random_symbols = random.choice(symbols)
    password2 += random_symbols
password3 = ''
for _ in range(input_numbers):
    random_numbers = random.choice(numbers)
    password2 += random_numbers    

final_password = password1 + password2 + password3
print(final_password)
'''
 use each input as a loop for how many characters
 use len function on the lists above
 use random module to pick a number for each list
 figure out how to put the selected as a "print" function
 print finalPassword at the end
'''
      

#chatgpt
#print(finalPassword)

