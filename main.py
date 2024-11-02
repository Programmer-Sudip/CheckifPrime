# program to check if a number is prime or not

from math import sqrt

number = int(input("Enter your number: "))

# if given number is greater than 1
if number > 1:

    # check if number is divisible from 2 and number/2
    for i in range(2, int(sqrt(number)) + 1):

        # if number is divisible by any number it is a non prime number
        if (number % i) == 0:
            print(number, "is not a prime number")
            print(i, "times", number // i, "is", number)
            break
    else:
        print(number, "is a prime number")
else:
    print(number, "is not a prime number")