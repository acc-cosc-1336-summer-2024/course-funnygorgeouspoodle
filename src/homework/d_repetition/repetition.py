def get_factorial(num):
    factorial = 1
    for i in range(1, num+1):
        factorial *= i        
    return factorial

def sum_odd_numbers(num):
    total = 0
    number = 1
    while number <= num:
        if number % 2 != 0:
            total += number
        number += 1
    return total


