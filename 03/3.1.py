import sys
import math

first_number=int(input("Enter first number:"))
second_number=int(input("Enter second number:"))
signs=input("Enter signs:")

if signs=="+":
    print(first_number+second_number)
elif signs=="-":
    print(first_number-second_number)
elif signs=="*":
    print(first_number*second_number)
elif signs=="/":
    if second_number==0:
        print("YOU CANT DO THIS ")
    else:
        print(first_number/second_number)

























