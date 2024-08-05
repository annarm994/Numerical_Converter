def convert_number(number, from_base, to_base):
    decimal_number = int(number, from_base)    
    if to_base == 10:
        return str(decimal_number)
    else:
        digits = "0123456789ABCDEF"
        result = ""
        while decimal_number > 0:
            remainder = decimal_number % to_base
            result = digits[remainder] + result
            decimal_number = decimal_number // to_base
        return result

def main():
    print("Number Base Converter")
    print("---------------------")
    number = input("Enter the number to be converted: ")
    from_base = int(input("Enter the base of the input number (2-16): "))
    to_base = int(input("Enter the base to which the number should be converted (2-16): "))
    
    try:
        converted_number = convert_number(number, from_base, to_base)
        print(f"The number {number} in base {from_base} is {converted_number} in base {to_base}.")
    except ValueError:
        print("Invalid input. Please make sure the number and bases are correct.")

if __name__ == "__main__":
    main()
