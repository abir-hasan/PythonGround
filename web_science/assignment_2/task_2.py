initial_bit_size = 10
formatted_bit_size = initial_bit_size - 2
perfect_sum = "11111111"  # same size bit as 'formatted_bit_size'
overflow_bit = "0b00000001"  # same size bit as 'initial_bit_size'
initial_sum = "0b00000000"  # same size bit as 'initial_bit_size'


# Method to calculate checksum
def calculate_checksum(message):
    sum = initial_sum
    for bit in message:
        bin_str = bin(bit)
        print_variables(sum, 1)
        print_variables(bin_str, 2)
        sum = bin(int(sum, 2) + int(bin_str, 2))

        sum = get_sum_wrapped(sum)
        print_sum(sum)
    cs = print_check_sum(get_formatted_bits(sum))
    return cs


# Method to Validate Message against checksum
def validate_data(message, check_sum):
    message.append(check_sum)
    sum = initial_sum
    for bit in message:
        bin_str = bin(bit)
        print_variables(sum, 1)
        print_variables(bin_str, 2)
        sum = bin(int(sum, 2) + int(bin_str, 2))
        sum = get_sum_wrapped(sum)
        print_sum(sum)
    validated_bits = get_formatted_bits(sum)
    if validated_bits == perfect_sum:
        print(f"Got the following sum {validated_bits} after the validation")
        return True
    else:
        print("Corrupted data")
        return False


def print_check_sum(sum):
    check_sum = ""
    for i in sum:  # Flipping values to get 1's compliment
        if i == "0":
            check_sum += "1"
        else:
            check_sum += "0"
    print(f"checksum {check_sum}")
    return check_sum


# Get the wrapped value
# If there is an overflow then
# Add it to the sum and return
def get_sum_wrapped(sum):
    x = len(sum)
    if x > initial_bit_size:
        y = sum[2:]  # removing '0b'
        y = y[1:]  # slicing the number except the overflow bit
        z = bin(int(y, 2) + int(overflow_bit, 2))  # Add overflow bit to the sum
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
    # a = [0b1010101100110101, 0b1100001111010001, 0b0101001000110001, 0b0011000011101101] # Change Upper values

    x = [0b01101001, 0b00100000, 0b01101100, 0b01101111]
    y = [0b01110110, 0b01100101, 0b00100000, 0b01110111]
    z = [0b01100101, 0b01100010, 0b00100000, 0b01110011]

    cs_x = int(calculate_checksum(z), 2)
    validate_data(z, cs_x)
