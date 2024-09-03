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
    except ValueError as ve:
        print(f"Input error: {ve}")
        return None
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
        print("3. Exit")
        choice = input("Enter your choice (1/2/3): ")
        if choice in ['1', '2', '3']:
            return choice
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")


def handle_english_to_binary():
    """
    Handle the conversion from English text to binary.
    """
    while True:
        text = input("Enter English text (or type 'back' to go to the main menu): ")
        if text.lower() == 'back':
            return
        binary_result = text_to_binary(text)
        if binary_result:
            print("Binary result:", binary_result)
            break


def handle_binary_to_english():
    """
    Handle the conversion from binary string to English text.
    """
    while True:
        binary = input("Enter binary string (or type 'back' to go to the main menu): ")
        if binary.lower() == 'back':
            return
        text_result = binary_to_text(binary)
        if text_result:
            print("English text:", text_result)
            break
        else:
            print("Please enter a valid binary string that is a multiple of 8 bits and contains only 0s and 1s.")


def main():
    """
    Main function to run the binary translator application.
    """
    while True:
        choice = get_user_choice()

        if choice == '1':
            handle_english_to_binary()
        elif choice == '2':
            handle_binary_to_english()
        elif choice == '3':
            print("Exiting the program. Goodbye!")
            break


if __name__ == "__main__":
    main()
