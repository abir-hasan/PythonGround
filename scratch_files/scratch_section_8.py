############### Section 8: Structured Data ################

# List Comprehension
def dict_ex():
    seq = range(5)
    d = {x: x ** 3 for x in seq}
    print(f"Dictionary example: {d}")


def set_ex(): # Set is a DS with unique values in it, which are not sequential
    seq = range(5)
    d = {x for x in 'superduper' if x not in 'pd'}
    print(f"Set example: {d}")
    print_list(d)


def list_comp():
    seq = range(11)
    print_list(seq)
    seq1 = [x * 2 for x in seq]
    print_list(seq1)
    seq2 = [x for x in seq if x % 3 != 0]
    print_list(seq2)
    seq3 = [(x, x ** 2) for x in seq]
    print_list(seq3)


def print_list(list):
    for i in list:
        print(i, end=" ")
    print()


if __name__ == '__main__':
    list_comp()
    dict_ex()
    set_ex()
