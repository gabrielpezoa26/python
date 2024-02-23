# Write your code below this line 👇

n = int(input('Insert a number here: '))

def prime_checker(n):
    if n % n == 0:
        print(" its a prime number")
    else:
        print(" it's not a prime number")           # WRONG MATH

prime_checker(n)


# Write your code above this line 👆
    
#Do NOT change any of the code below👇
n = int(input()) # Check this number
prime_checker(number=n)