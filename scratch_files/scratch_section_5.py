############### Section 5: Operators ################

# Boolean operators
x = True
y = False

if x and y:
    print("Inside IF")
else:
    print("Inside else")

if x and y:
    print("Inside IF")
else:
    print("Inside else")

a = ['bear', 'bunny', 'tree', 'sky', 'rain']
b = 'bear'

if b in a:
    print("b is in list a")
else:
    print("false")

if b is a[0]:
    print("values are same")
else:
    print("values are not the same")

# Values are the same cause, the immutable string objects have the same id
print(id(b))
print(id(a[0]))
