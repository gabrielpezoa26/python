import random

user_choice = input("Choose! Heads/Tails:")

if user_choice == "Heads":
    user_choice_int = 0
elif user_choice == "Tails":
    user_choice_int = 1
else:
    print("Invalid choice.")
aleatorio = random.randint(0, 1)
if user_choice_int == aleatorio:
 print(" you won")