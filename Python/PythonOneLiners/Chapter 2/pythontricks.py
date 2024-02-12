### Learning 10 basic python one-liners



## Chapter 2.1 (The Basics)

## A program to find out if employees make at least $100,000

# employees = {"Alice": 100000,
#              "Bob": 99817,
#              "Carol": 122908,
#              "Frank": 88123,
#              "Eve": 93121
#              }

# top_earners = []

# for name, salary in employees.items():
#     if salary >= 100000:
#         top_earners.append((name, salary))

# print(top_earners)

## Example of a python one-liner (list-comprehension)

[x * 2 for x in range(3)]       # Results are [0, 2, 4]

## Syntax: [<expression> <context>]


