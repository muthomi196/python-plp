def large_power(base, exponent):
    result = base ** exponent
    return result > 5000

base = int(input("Enter the base: "))
exponent = int(input("Enter the exponent: "))

if large_power(base, exponent):
    print(f"{base} raised to the power of {exponent} is greater than 5000.")
else:
    print(f"{base} raised to the power of {exponent} is not greater than 5000.")