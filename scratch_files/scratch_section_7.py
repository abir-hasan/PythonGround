############### Section 7: Functions ################

# Example of start from a 'main' function
def start():
    print("Inside start")
    normal_method(1, 2)
    method_with_default_value(3, 4, 5)
    method_with_default_value(3, 4, 5, 100)


def normal_method(a, b):
    print(f"{a} {b}")


def method_with_default_value(a, b, c, d=6):
    print(f"{a} {b} {c} {d}")


# Example of call by value(Here base arg won't change as it's Types i.e Int is Immutable)
def start2():
    x = 5
    second(x)
    print(f"x in start-2 after is {x}")


def second(a):
    a = 3
    print("inside second")
    print(f"a: {a}")


# Example of call by reference(Here base arg has changed as it's Types i.e List is Mutable)
def start3():
    x = [5]
    third(x)
    print(f"x in start-3 after is {x}")


def third(a):
    a[0] = 3
    print("inside third")
    print(f"a: {a}")


if __name__ == "__main__":
    start()
    start2()
    start3()
