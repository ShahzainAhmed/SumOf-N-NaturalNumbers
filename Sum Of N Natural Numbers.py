# Taking input from the user.
n = int(input("Enter a number: "))

# Declaring and initializing a variable.
sum1 = 0

# Using while loop, and setting 'n' value to be greater than 0, only then the while loop would work.
while(n > 0):
    sum1=sum1+n
    n=n-1
print("The sum of first n natural numbers is",sum1)
