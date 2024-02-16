target = int(input("Enter a number: ")) 

total = 0

for pairs in range(2, target+1, 2):
    total += pairs

print(total)