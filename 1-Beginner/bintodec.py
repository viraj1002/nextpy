import math

def bin_to_dec(binary_str):
    decimal_result = 0

    for i in range(len(binary_str)):
        if binary_str[i] not in ('0', '1'):
            return None  # Invalid input

        decimal_result += int(binary_str[i]) * (2 ** (len(binary_str) - 1 - i))

    return decimal_result

def main():
    binary_input = input("Enter a binary number : ")

    if len(binary_input) > 8:
        print("Error: Input should have at most 8 binary digits.")
        return

    result = bin_to_dec(binary_input)

    if result is not None:
        print("Decimal equivalent:", result)
    else:
        print("Error: Invalid input. Please enter only 0s and 1s.")

if __name__ == "__main__":
    main()
