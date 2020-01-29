############### Section 3 Types and Values ################

# Example of 'type'
x = "Hello"
print("x is {}".format(x))
print(type(x))

# Example of positioning arguments
x = "Seven {1} {0}".format(9, 8)
print(x)


# Example of 'f' string [available after python 3.6]
a = 8
b = 9
x = f"Seven {a} {b}"
print(x)

# Primarily 2 numerical types: Integer and Float
a = 2
b = 3.5
print(f"{a} is type: {type(a)} \n{b} is type: {type(b)}")

# Examples of Point division, resultant and remainder
x = 7 / 3   # Will give us 2.3333333
y = 7 // 3  # Will give us 2
z = 7 % 3   # Will give us 1
print(f"point: {x} \nresult: {y} \nremainder: {z}")
