# import for exercise 1
import random
# PRACTICE: Random Numbers
# 1. Use the following code to create a list of 10 random numbers. Each number will be between 0 and 6.

my_randoms = list()
for i in range(10):
    my_randoms.append(random.randrange(1, 6))

# 2. Then iterate a different list of numbers that are sequential from 1 to 10. Use the following code as your starting point.

"""
Print a message to the console indicating whether each value of
`number` is in the `my_randoms` list.
"""
print(f'the random numbers: {my_randoms}')
# Generate a list of numbers 1..10
numbers_1_to_10 = range(1, 11)
print(f'the list of numbers 1-10: {numbers_1_to_10}')

# Iterate from 1 to 10
for number in numbers_1_to_10:
    the_numbers_match = False

    # Iterate your random number list here
    # Does my_randoms contain number? Change the boolean.
    # loop way
    for random_num in my_randoms:
        if random_num == number:
            the_numbers_match = True

    # if-in way
    # if number in my_randoms:
    #     print(f'INSIDE IF-IN {number}')
    #     the_numbers_match = True
    #
    print(f'{number} is in the random list') if the_numbers_match else print(f'{number} is NOT the random list')