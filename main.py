# coding=utf-8
# Sum of Numbers

import functools
def sum_of_numbers(n):

    sum = 0
    while n!= 0:
        sum += n%10
        n = n//10
    print(sum)

# sum of numbers comprehensions
def sum_of_numbers_comp(n):
    array = [int(i) for i in str(n)]
    sum = reduce(lambda num1, num2: num1 + num2, array)
    print("sum is {}".format(sum))

sum_of_numbers_comp(123456)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    sum_of_numbers(123456)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
