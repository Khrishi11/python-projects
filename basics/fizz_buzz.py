
# Activity 1: FizzBuzz
# Write a code in python in which you can get “Fizz Buzz” for all numbers which can be divided by (3, 5, 15). The range should from (1 to 100).

for i in range(1, 101):
    if i % 3 == 0 or i % 5 == 0:
        print("FizzBuzz")
    else:
        print(i)
