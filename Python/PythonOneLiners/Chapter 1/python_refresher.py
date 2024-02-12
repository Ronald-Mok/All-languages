# # This is a Python refresher




# ### Arithmetic Operations

# x, y = 3, 2     # Can assign var like this

# print(f"{x}\n")


# # This Operation(Floor Division) "//" rounds down the sum 

# print(f"This is a floor division {x//y}\n") # Normal division will return 1.5 




# ### Boolean Expressions

# print(1<2)
# print(f"{1>2}\n")


# def torf(x, y, exp):
#         if exp == "and":
#             return (x and y) == True  #Returns False "(x and y)" returns the last truthy value
#         elif exp == "or":
#             return (x or y) == True   #Returns True
#         elif exp == "not":
#             return (not y) == True  #Returns True
#         else:
#              return "Error"

# print(torf(3, 2, "and"))



### "None"

# None refers to not returning a value.

# def f():
#     x = 2

# print(f() == None)  # Example 1

# print("" == None)   # Example 2: This returns False as an empty string still has a value of ""

# print(0 == None)    # Example 3: This returns False as 0 is an int (Has a value)



### Sets

# hero = "Potter"
# villain = "Voldermort"

# movie = {hero, hero, hero, villain}

# print(movie)

# The reason why it only prints one instance of her and villain is that hero has the same hash value, so it cannot be repeated.
# Mutable objects are not hashable such as list and dicts

# Finding the hash value of an object

# print(hash(hero))       # Same hash value
# print(hash(hero))       # Same hash value
# print(hash(villain))    



### Lambdas

# Syntax for Lambda
# lambda <argument>: <return expression>

# Example:

# print((lambda x, y, z: x + y + z)(4, 5, 1))



# map() and reduce()

