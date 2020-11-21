# Method to calculate checksum
def calculate_checksum(message):
    var_count = 1
    sum = "0b0000000000000000"
    for bit in message:
        bin_str = bin(bit)
        print_variables(bin_str, var_count)
        sum = bin(int(sum, 2) + int(bin_str, 2))

        if var_count > 1:
            sum = get_sum_wrapped(sum)
            print_sum(sum)
        var_count += 1
    cs = print_check_sum(sum)
    return cs


# Method to Validate Data
def validate_data(message, check_sum):
    message.append(check_sum)
    sum = "0b0000000000000000"
    for bit in message:
        bin_str = bin(bit)
        sum = bin(int(sum, 2) + int(bin_str, 2))
        sum = get_sum_wrapped(sum)
    validated_bits = get_formatted_bits(sum)
    if validated_bits == "1111111111111111":
        print("Valid message")
    else:
        print("Corrupted data")


def print_check_sum(sum):
    value = sum[2:]  # Slicing the variable
    check_sum = ""
    for i in value:  # Flipping values to get 1's compliment
        if i == "0":
            check_sum += "1"
        else:
            check_sum += "0"
    print(f"checksum {check_sum}")
    return check_sum


def get_sum_wrapped(sum):
    x = len(sum)
    #print(f"get_sum_wrapped() len {x}")
    if x > 18:
        y = sum[2:]  # removing '0b'
        # print(f"y1    {y}")
        y = y[1:]  # slicing the number except the overflow bit
        # print(f"y2    {y}")
        c = "0b0000000000000001"  # overflow bit
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
    value = value[2:]  # Slicing the variable
    x = len(value)
    if x == 16:
        return value
    else:
        y = 16 - x
        zero = ""
        for k in range(0, y):
            zero += "0"
        value = zero + value
        return value


if __name__ == "__main__":
    a = [0b1010101100110101, 0b1100001111010001, 0b0101001000110001, 0b0011000011101101]
    cs_x = int(calculate_checksum(a), 2)
    """x = [0b01101001, 0b00100000, 0b01101100, 0b01101111]
    y = [0b01110110, 0b01100101, 0b00100000, 0b01110111]
    z = [0b01100101, 0b01100010, 0b00100000, 0b01110011]
    calculate_checksum(x)
    calculate_checksum(y)
    calculate_checksum(z)"""
    # cs_x = int(calculate_checksum(x), 2)
    validate_data(a, cs_x)
