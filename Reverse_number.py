# Program that prints the reverse of the number given in integer format without using a loop, leaving a space between them.
# For example : num = 7356 Output = 6537

num = int(input("Please enter a four digits integer number: "))
print("Your number: ", num)

digit1 = num % 10
digit2 = (num % 100) // 10
digit3 = (num % 1000) // 100
digit4 = num // 1000

rev_num = digit1 * 1000 + digit2 * 100 + digit3 * 10 + digit4
print("The reverse of number: ", rev_num)