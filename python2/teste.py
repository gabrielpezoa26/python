import random               #chatgpt
import sys                  # editei o print da Maquina, e o exit

# Define choices
rock = 0
paper = 1
scissors = 2

# Generate random choice for the computer
jogadaMaquina = random.randint(0, 2)

# Get user's input and convert it to an integer
jogadaUsuario = int(input("Type 0 for Rock, 1 for Paper, or 2 for Scissors: "))
if jogadaUsuario not in [0, 1, 2]:
    print("Invalid number")
    sys.exit()
print(jogadaMaquina)           

# Determine the winner
if jogadaUsuario == jogadaMaquina:
    print("It's a tie!")
elif (jogadaUsuario == rock and jogadaMaquina == scissors) or \
     (jogadaUsuario == paper and jogadaMaquina == rock) or \
     (jogadaUsuario == scissors and jogadaMaquina == paper):
    print("You win!")
else:
    print("You lose!")