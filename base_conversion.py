def decimal_to_base(decimal, base):
    if base < 2 or base > 20:
        raise ValueError("Base must be between 2 and 20, inclusive.")

    if decimal == 0:
        return "0"

    # Characters for bases up to 20
    digits = "0123456789ABCDEFGHIJKLM"
    result = ""
    
    while decimal > 0:
        remainder = decimal % base
        result = digits[remainder] + result
        decimal = decimal // base
    
    return result

# Example usage:
decimal_number = 350
base = 20
print(f"{decimal_number} in base {base} is {decimal_to_base(decimal_number, base)}")
