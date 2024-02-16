import random

rock = "pedra"
paper = "papel"
scissors = "tesoura"
#Write your code below this line 

jogadaMaquina = random.randint(0,2)    #jogadaMáquina
jogadaUsuario = input(" Type 0 for Rock, 1 for Paper or 2 for Scissors! (0,1,2)")

rock = 0
paper = 1
scissors = 2



#print(num_aleatorio)      #teste

'''
import random

# Define choices
rock = 0
paper = 1
scissors = 2

# Generate random choice for the computer
jogadaMaquina = random.randint(0, 2)

# Get user's input and convert it to an integer
jogadaUsuario = int(input("Type 0 for Rock, 1 for Paper, or 2 for Scissors: "))

# Determine the winner
if jogadaUsuario == jogadaMaquina:
    print("It's a tie!")
elif (jogadaUsuario == rock and jogadaMaquina == scissors) or \
     (jogadaUsuario == paper and jogadaMaquina == rock) or \
     (jogadaUsuario == scissors and jogadaMaquina == paper):
    print("You win!")
else:
    print("You lose!")
    '''
 










''' pedir input                       ok
    associar variaveis de 0 a 2 aos objetos    rock = 0   paper = 1 scissors = 2        ok
    gerar random.int(0,2)  ** listas??          ok
    declarar qual obj. ganha de qual
    output         

'''