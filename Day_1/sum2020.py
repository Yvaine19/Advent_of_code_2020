import pandas as pd

# function for returning product of two numbers
def return_product_sum_2020(numbers):
    # init
    product = 0
    for first_number in numbers:
        i = numbers.index(first_number)
        for second_number in numbers[i+1:]:
            if first_number + second_number == 2020:
                product = first_number*second_number
                break
    return product

# product of three numbers
def return_product_sum_three(numbers):
    # init
    product = 0
    for first_number in numbers:
        i = numbers.index(first_number)
        for second_number in numbers[i+1:]:
            j = numbers.index(second_number)
            for third_number in numbers[j+1:]:
                if first_number + second_number + third_number == 2020:
                    product = first_number*second_number*third_number
                    break
    return product


## data load
with open("input.txt") as f:
    data = [int(i) for i in f.read().split("\n") if i != ""]
# first task
return_product_sum_2020(data)
return_product_sum_three(data)