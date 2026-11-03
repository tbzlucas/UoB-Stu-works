# My$$Name$$Is$$King
print("My", "Name", "is", "King", sep="$$")


# Ali Syed Tom
name = input("Enter three names: ")
names = name.split()

print("Name1:", names[0])
print("Name2:", names[1])
print("Name3:", names[2])

# just 2 decimals
print("%.2f" % 5.26459884)

# f-strings
year = 2023
quantity = 3
Price = 450000

print(f"I have bought {quantity} footballs for {Price:,}£, in the year {year}")

# Length

sentence = "I have bought 3 footballs"
print(len(sentence))

# Date

from datetime import date

today = date.today()
print(today)

# random number 1-100

import random

print(random.randint(1, 100))

# 1 random numbers from user

import random

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

print(random.randint(num1, num2))

# add 2 numbers from user and display

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

total = num1 + num2

print("The sum is:", total)