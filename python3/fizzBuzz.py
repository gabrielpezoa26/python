'''  range 1,101
     if divisible by 3      ("Fizz")
     if divisible by 5  ("Buzz)
     if divisible by 3 and 5 ("FizzBuzz")
     '''

for number in range(1, 101):
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)
    
       