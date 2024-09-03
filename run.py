def text_to_binary(text):
    """
    Convert English text to its binary representation.

    Args:
        text (str): The text to be converted.

    Returns:
        str: The binary representation of the text.
    """
    try:
        if not text:
            raise ValueError("Input text cannot be empty.")
        binary_result = ''.join(format(ord(char), '08b') for char in text)
        return binary_result
    except Exception as e:
        print(f"Error converting text to binary: {e}")
        return None


def binary_to_text(binary):
    """
    Convert binary string to its English text representation.

    Args:
        binary (str): The binary string to be converted.

    Returns:
        str: The English text representation of the binary string.
    """
    try:
        # Validate the binary string
        if not binary:
            raise ValueError("Binary input cannot be empty.")
        if len(binary) % 8 != 0:
            raise ValueError("Binary string length must be a multiple of 8.")
        if not all(char in '01' for char in binary):
            raise ValueError("Binary string should contain only 0s and 1s.")
        
        # Split the binary string into chunks of 8 bits
        binary_values = [binary[i:i+8] for i in range(0, len(binary), 8)]
        # Convert each chunk of 8 bits to an ASCII character
        ascii_characters = [chr(int(bv, 2)) for bv in binary_values]
        # Join all ASCII characters to form the final text
        text_result = ''.join(ascii_characters)
        return text_result
    except Exception as e:
        print(f"Error converting binary to text: {e}")
        return None


def get_user_choice():
    """
    Get the user's choice for conversion type.

    Returns:
        str: The user's choice ('1' for English to Binary, '2' for Binary to English).
    """
    while True:
        print("1. English to Binary")
        print("2. Binary to English")
        choice = input("Enter your choice (1/2): ")
        if choice in ['1', '2']:
            return choice
        else:
            print("Invalid choice. Please enter 1 or 2.")


def main():
    """
    Main function to run the binary translator application.
    """
    choice = get_user_choice()

    if choice == '1':
        # Convert English text to binary
        text = input("Enter English text: ")
        binary_result = text_to_binary(text)
        if binary_result:
            print("Binary result:", binary_result)
    elif choice == '2':
        # Convert binary string to English text
        binary = input("Enter binary string: ")
        text_result = binary_to_text(binary)
        if text_result:
            print("English text:", text_result)


if __name__ == "__main__":
    main()
