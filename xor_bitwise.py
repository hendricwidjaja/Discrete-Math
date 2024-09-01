def decimal_to_binary(decimal):
    if decimal == 0:
        return "0"
    base_two = ""
    while decimal > 0:
        remainder = decimal % 2
        base_two = str(remainder) + base_two
        decimal = decimal // 2
    return base_two

def exclusive_or(num1, num2):
    # Use decimal to binary function to convert decimal numbers to binary
    binary_num1 = decimal_to_binary(num1)
    binary_num2 = decimal_to_binary(num2)
    # Calculate max length of each binary number and store in "max bit length"
    max_bit_length = max(len(binary_num1), len(binary_num2))
    # Adjust the length of each binary number to have same number of digits by using zfill to pencil in any extra required 0s
    adj_bin_num1 = binary_num1.zfill(max_bit_length)
    adj_bin_num2 = binary_num2.zfill(max_bit_length)
    # Initialise an empty string
    xor_bit_string = ""
    # For each digit in each binary number, the modulo 2 of each addition will equal 0 if the values are the same (e.g. (1 + 1) % 2 = 0 . Similarly, (0 + 0) % 2 = 0. However, (1 + 0) % 2 = 1
    for i in range(max_bit_length):
        xor_bit = (int(adj_bin_num1[i]) + int(adj_bin_num2[i])) % 2
        # Store the result as a string and append it to the 'xor_bit_string" variable.
        xor_bit_string += str(xor_bit)
    # Return the integer version of the xor bit sring in decimal
    return int(xor_bit_string, 2)