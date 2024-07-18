def text_to_binary(text):
    """
    Convert English text to its binary representation.

    Args:
        text (str): The text to be converted.

    Returns:
        str: The binary representation of the text.
    """
    binary_result = ''.join(format(ord(char), '08b') for char in text)
    return binary_result


def binary_to_text(binary):
    """
    Convert binary string to its English text representation.

    Args:
        binary (str): The binary string to be converted.

    Returns:
        str: The English text representation of the binary string.
    """
    # Split the binary string into chunks of 8 bits
    binary_values = [binary[i:i+8] for i in range(0, len(binary), 8)]
    # Convert each chunk of 8 bits to an ASCII character
    ascii_characters = [chr(int(bv, 2)) for bv in binary_values]
    # Join all ASCII characters to form the final text
    text_result = ''.join(ascii_characters)
    return text_result


def main():
    """
    Main function to run the binary translator application.
    """
    # Display the options to the user
    print("1. English to Binary")
    print("2. Binary to English")
    choice = input("Enter your choice (1/2): ")

    if choice == '1':
        # Convert English text to binary
        text = input("Enter English text: ")
        binary_result = text_to_binary(text)
        print("Binary result:", binary_result)
    elif choice == '2':
        # Convert binary string to English text
        binary = input("Enter binary string: ")
        # Validate the binary string
        if len(binary) % 8 != 0 or not all(char in '01' for char in binary):
            print("Invalid binary string. It should be multiple of 8 bits and contain only 0s and 1s.")
        else:
            text_result = binary_to_text(binary)
            print("English text:", text_result)
    else:
        # Handle invalid choice
        print("Invalid choice. Please enter 1 or 2.")


if __name__ == "__main__":
    main()

