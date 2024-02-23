# Write your code below this line 👇
import math

def paint_calc(test_h, test_w, coverage):
    n_cans = (test_w * test_h) / 5
    n_cans = math.ceil(n_cans)
    print(f" u will need {n_cans} cans of paint for that job")
   
        
# Write your code above this line 👆
# 🚨 Don't change the code below 👇

test_h = int(input('whats the height of the wall?')) # Height of wall (m)
test_w = int(input('whats the width of the wall?')) # Width of wall (m)
coverage = 5
paint_calc(test_h, test_w, coverage)



