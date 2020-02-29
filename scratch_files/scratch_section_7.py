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


# Example of Generators
def start6():
    for i in inclusive_range(5, 30, 3):
        print(i, end=' ')
    print("\n---------*----------")


def inclusive_range(*args):
    num_args = len(args)
    first = 0
    step = 1

    # Initialize parameters
    if num_args < 1:
        raise TypeError(f"expected at least 1 argument, got {num_args}")
    elif num_args == 1:
        stop = args[0]
    elif num_args == 2:
        (first, stop) = args
    elif num_args == 3:
        (first, stop, step) = args
    else:
        raise TypeError(f"expected at most 3 arguments, got {num_args}")

    # Generator
    i = first
    while i <= stop:
        yield i  # yield like a return. But it doesn't stop the loop, it simply returns a value then continues to run
        i += step


# Example of Decorators
import time


def decorator_fun(f):
    print("Inside the decorator_fun")
    def wrapper():
        print("Inside the wrapper")
        t1 = time.time()
        f()
        t2 = time.time()
        print(f"Elapsed time: {(t2 - t1) * 1000} ms")

    print("Getting out of decorator_fun")
    return wrapper


@decorator_fun
def start7():
    num_list = []
    for i in (range(0, 100000)):
        num_list.append(i)
    print(f"Sum: {sum(num_list)}")


# Main function which is calling every example
if __name__ == "__main__":
    start()
    start2()
    start3()
    start4()
    start5()
    start6()
    start7()
