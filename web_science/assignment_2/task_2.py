# Web Science Assignment - 2
# Team - Mike
# Task 2 - Python Programming
# 2.1 Checksum
# Write a method that computes and returns the checksum of a message. The input message
# contains four segments and each segment represents a 8-bit binary data.
# 1. In the method, make sure that each step is printed out in the console.
# 2. Fill out the following table with the checksum values that are computed by the
#    method.
# 3. Write another method that validates or rejects given data and checksum. For the
#    corrupted data, the method should output an error message.


# Configuration Variables
initial_bit_size = 10  # For example, String value of a certain 8 bit bin : '0b01101001'
formatted_bit_size = initial_bit_size - 2  # So 8 bit Bin from initial string: '01101001'
perfect_sum = "11111111"  # same size bit as 'formatted_bit_size'
overflow_bit = "0b00000001"  # same size bit as 'initial_bit_size'
initial_sum = "0b00000000"  # same size bit as 'initial_bit_size'


# Method to calculate checksum (Answer of 2.1.1)
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


# Answer to task 2.1.2
# Printing Checksum of given list of messages
def answer_to_task_2_1_2():
    x = [0b01101001, 0b00100000, 0b01101100, 0b01101111]
    y = [0b01110110, 0b01100101, 0b00100000, 0b01110111]
    z = [0b01100101, 0b01100010, 0b00100000, 0b01110011]

    cs_x = int(calculate_checksum(x), 2)
    cs_y = int(calculate_checksum(y), 2)
    cs_z = int(calculate_checksum(z), 2)


# Method to Validate Message against checksum (Answer of 2.1.3)
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


# Calculate checksum and print
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
        y = sum[2:]  # Slicing the variable(Removing 0b)
        y = y[1:]  # slicing the number except the overflow bit
        z = bin(int(y, 2) + int(overflow_bit, 2))  # Add overflow bit to the sum
        return z  # Return new sum
    else:
        return sum


def print_sum(sum):
    print(f"sum   {get_formatted_bits(sum)}")


def print_variables(value, count):
    print(f"var {count} {get_formatted_bits(value)}")


# A method to format incoming Binary String values
# Format them to required length
def get_formatted_bits(value):
    value = value[2:]  # Slicing the variable(Removing 0b)
    x = len(value)
    if x == formatted_bit_size:
        return value
    else:
        y = formatted_bit_size - x  # Get required size to fill '0's with
        zero = ""
        for k in range(0, y):
            zero += "0"
        value = zero + value  # Make formatted 8 bit bin String
        return value


if __name__ == "__main__":
    # # Change Upper Configuration Variables values first to run 16 bit inputs
    # a = [0b1010101100110101, 0b1100001111010001, 0b0101001000110001, 0b0011000011101101]
    a = [0b01101001, 0b00100000, 0b01101100, 0b01101111]
    calculate_checksum(a)   # Task 2.1.1
    answer_to_task_2_1_2()  # Task 2.1.2
    validate_data(a, 152)   # Task 2.1.3 (154 is the correct checksum)
