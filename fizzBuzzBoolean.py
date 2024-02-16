'''  range 1,101
     if divisible by 3      ("Fizz")
     if divisible by 5  ("Buzz)
     if divisible by 3 and 5 ("FizzBuzz")
     boolean
     '''
for number in range(1, 101):
    condition1 = number % 3 == 0 and number % 5 == 0
    condition2 = number % 3 == 0
    condition3 = number % 5 == 0

    if condition1:
        print("FizzBuzz")
        continue
    elif condition2:
        print("Fizz")
        continue
    elif condition3:
        print("Buzz")
        continue

    print(number)