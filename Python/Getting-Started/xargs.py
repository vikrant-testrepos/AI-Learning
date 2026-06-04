def multiply(*numbers): #to use multiple arguments at once * is important.
    total = 1
    for number in numbers:
        total *= number
    return total


print(multiply(2, 3, 4, 5, 6))
