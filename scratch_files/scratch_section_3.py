############### Section 3: Types and Values ################

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

# Example of Boolean type
x = False
y = True
print(f"{x} {y}")
if y:
    print("Yay")

# Example of Sequence type : List [Created by third bracket and Mutable]
x = [1, 2, 3, 4, 5]
print(f"{type(x)}")
for i in x:
    print(f"{i}")

# Example of Sequence type : Tuple [Created by first bracket and Immutable]
x = (1, 2, 3, 4, 5)
print(f"{type(x)}")
for i in x:
    print(f"{i}")

# Example of Sequence type : Dictionary [Created by second bracket and Mutable]
x = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5}
print(f"{type(x)}")
for k, v in x.items():
    print("'key' {} 'value' {}".format(k, v))

# Example of 'is' and 'isinstance'
# x = (1, 2, 3, 4, 5)
# y = [1, 2, 3, 4, 5]
#
# if x[0] is y[0]:
#     print("Same")
# else:
#     print("Nope")
#
# if isinstance(y, tuple):
#     print("Y is tuple")
# elif isinstance(y, list):
#     print("Y is list")
# else:
#     print("don't know you are talking about")
