initial_bit_size = 10
formatted_bit_size = initial_bit_size - 2
perfect_sum = "11111111"  # same size bit as 'formatted_bit_size'
main_overflow_bit = "0b00000001"  # same size bit as 'initial_bit_size'
initial_sum = "0b00000000"  # same size bit as 'initial_bit_size'


# Method to calculate checksum
def calculate_checksum(message):
    var_count = 1
    sum = initial_sum
    for bit in message:
        bin_str = bin(bit)
        print_variables(bin_str, var_count)
        sum = bin(int(sum, 2) + int(bin_str, 2))

        if var_count > 1:
            sum = get_sum_wrapped(sum)
            print_sum(sum)
        var_count += 1
    cs = print_check_sum(get_formatted_bits(sum))
    return cs


# Method to Validate Data
def validate_data(message, check_sum):
    message.append(check_sum)
    sum = initial_sum
    for bit in message:
        bin_str = bin(bit)
        sum = bin(int(sum, 2) + int(bin_str, 2))
        sum = get_sum_wrapped(sum)
    validated_bits = get_formatted_bits(sum)
    if validated_bits == perfect_sum:
        print("Valid message")
    else:
        print("Corrupted data")


def print_check_sum(sum):
    # value = sum[2:]  # Slicing the variable
    check_sum = ""
    # print(f"print_check_sum {len(sum)}")
    for i in sum:  # Flipping values to get 1's compliment
        if i == "0":
            check_sum += "1"
        else:
            check_sum += "0"
    print(f"checksum {check_sum}")
    return check_sum


def get_sum_wrapped(sum):
    x = len(sum)
    # print(f"get_sum_wrapped() len {x}")
    if x > initial_bit_size:
        y = sum[2:]  # removing '0b'
        # print(f"y1    {y}")
        y = y[1:]  # slicing the number except the overflow bit
        # print(f"y2    {y}")
        c = main_overflow_bit  # overflow bit
        z = bin(int(y, 2) + int(c, 2))
        # print(f"z     {z}")
        return z
    else:
        return sum


def print_sum(sum):
    print(f"sum   {get_formatted_bits(sum)}")


def print_variables(value, count):
    print(f"var {count} {get_formatted_bits(value)}")


def get_formatted_bits(value):
    # print(f"get_formatted_bits() {value}")
    value = value[2:]  # Slicing the variable
    x = len(value)
    if x == formatted_bit_size:
        return value
    else:
        y = formatted_bit_size - x
        zero = ""
        for k in range(0, y):
            zero += "0"
        value = zero + value
        return value


if __name__ == "__main__":
    # a = [0b1010101100110101, 0b1100001111010001, 0b0101001000110001, 0b0011000011101101]
    # cs_x = int(calculate_checksum(a), 2)
    x = [0b01101001, 0b00100000, 0b01101100, 0b01101111]
    y = [0b01110110, 0b01100101, 0b00100000, 0b01110111]
    z = [0b01100101, 0b01100010, 0b00100000, 0b01110011]

    cs_x = int(calculate_checksum(z), 2)
    validate_data(z, cs_x)
