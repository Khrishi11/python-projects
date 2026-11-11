# Activity 4: Fibonacci Series
# Write a code in python which will give you a Fibonacci series to a number when you enter it.

def fibonacci_from_one_number(n, terms):
    # Start with n and n
    series = [n, n]
    
    for _ in range(terms - 2):
        series.append(series[-1] + series[-2])
        
    return series

try: 
    n = int(input("Enter a number: \n"))
    t = int(input("Enter the number of terms you want to generate: \n"))
    print(fibonacci_from_one_number(n, t))
except ValueError:
    print("Please enter a valid integer.")
    exit()

