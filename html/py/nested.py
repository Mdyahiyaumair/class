def largest_of_three(a, b, c):
    if a >= b:
        if a >= c:
            return a
        else:
            return c
    else:
        if b >= c:
            return b
        else:
            return c

# Example usage
num1 = 10
num2 = 20
num3 = 15
largest = largest_of_three(num1, num2, num3)
print("The largest number is:", largest)