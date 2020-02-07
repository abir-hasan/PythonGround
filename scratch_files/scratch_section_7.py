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


# Example of argument lists
def start4():
    print_sounds("meow", "roar", "purr", "bark")


def print_sounds(*args):
    if len(args):  # Check if the set arguments length is greater than 0
        for x in args:
            print(x)
    else:
        print("No sound available!")


# Example of keyword argument with Dictionary
def start5():
    x = dict(Buffy="meows", Tom="roars", Belgie="barks")
    print_key_value(**x)


def print_key_value(**kwargs):
    if len(kwargs):
        for k in kwargs:
            print(f"{k} -> {kwargs[k]}")


# Main function which is calling every example
if __name__ == "__main__":
    start()
    start2()
    start3()
    start4()
    start5()
