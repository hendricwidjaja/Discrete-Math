def decimal_to_binary (decimal):
	if decimal == 0:
		return "0"
	# Initialise an empty string which will be return once the while loop has finished iterating
	base_two = ""

    # While the decimal number is still greater than 0
	while decimal > 0:
		# store the remainder of dividing the decimal number by 2 in a variable called 'remainder'
		remainder = decimal % 2
		# Add the remainder (string) to the beginning of the "base two" variable
		base_two = str(remainder) + base_two
		# Update the value of decimal to its value divided by 2 (floor division)
		decimal = decimal // 2
    # Return the string once decimal is no longer greater than 0
	return base_two
		
decimal = int(input("Insert a number in decimal format: "))
binary = decimal_to_binary(decimal)
print(f"{decimal} in binary format is: '{binary}'")