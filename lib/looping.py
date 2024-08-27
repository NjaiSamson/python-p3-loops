#!/usr/bin/env python3

def happy_new_year():
    num = 10
    while num > 0:
        print(num)
        num -=1
    print("Happy New Year!")

happy_new_year()


def square_integers(int_list):
    int_list_squared = [int_num ** 2 for int_num in int_list ]
    return int_list_squared

square_integers([1, 2, 3, 4, 5])

def fizzbuzz():
    num = 1
    while num <= 100:
        if num % 3 == 0 and num % 5 == 0:
            print("FizzBuzz")
        elif num % 3 == 0:
            print("Fizz")
        elif num % 5 == 0:
            print("Buzz")
        else:
            print(num)
        num += 1

fizzbuzz()