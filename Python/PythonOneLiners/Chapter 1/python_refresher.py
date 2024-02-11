# This is a Python refresher




### Arithmetic Operations

x, y = 3, 2     # Can assign var like this

print(f"{x}\n")


# This Operation(Floor Division) "//" rounds down the sum 

print(f"This is a floor division {x//y}\n") # Normal division will return 1.5 




### Boolean Expressions

print(1<2)
print(f"{1>2}\n")


def torf(x, y, exp):
        if exp == "and":
            return (x and y) == True  #Returns False "(x and y)" returns the last truthy value
        elif exp == "or":
            return (x or y) == True   #Returns True
        elif exp == "not":
            return (not y) == True  #Returns True
        else:
             return "Error"

print(torf(3, 2, "and"))


