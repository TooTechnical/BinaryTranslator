import os
from colorama import Fore, Style, init

# Initialize colorama for cross-platform colored terminal text
init(autoreset=True)


def clear_screen():
    """Clear the console screen."""
    os.system('cls' if os.name == 'nt' else 'clear')


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
        print(Fore.RED + f"Error converting text to binary: {e}" + Style.RESET_ALL)
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
        if not binary:
            raise ValueError("Binary input cannot be empty.")
        if len(binary) % 8 != 0:
            raise ValueError("Binary string length must be a multiple of 8.")
        if not all(char in '01' for char in binary):
            raise ValueError("Binary string should contain only 0s and 1s.")
        
        binary_values = [binary[i:i+8] for i in range(0, len(binary), 8)]
        ascii_characters = [chr(int(bv, 2)) for bv in binary_values]
        text_result = ''.join(ascii_characters)
        return text_result
    except ValueError as ve:
        print(Fore.YELLOW + f"Input error: {ve}" + Style.RESET_ALL)
        return None
    except Exception as e:
        print(Fore.RED + f"Error converting binary to text: {e}" + Style.RESET_ALL)
        return None


def get_user_choice():
    """
    Get the user's choice for conversion type.

    Returns:
        str: The user's choice ('1' for English to Binary, '2' for Binary to English).
    """
    while True:
        print(Fore.CYAN + "\nMain Menu:" + Style.RESET_ALL)
        print(Fore.CYAN + "1. English to Binary" + Style.RESET_ALL)
        print(Fore.CYAN + "2. Binary to English" + Style.RESET_ALL)
        print(Fore.CYAN + "3. Exit" + Style.RESET_ALL)
        choice = input(Fore.GREEN + "Enter your choice (1/2/3): " + Style.RESET_ALL)
        if choice in ['1', '2', '3']:
            return choice
        print(Fore.RED + "Invalid choice. Please enter 1, 2, or 3." + Style.RESET_ALL)


def handle_english_to_binary():
    """Handle the conversion from English text to binary."""
    while True:
        text = input(Fore.GREEN + "Enter English text (or 'back' to return to the main menu): " + Style.RESET_ALL)
        if text.lower() == 'back':
            return
        binary_result = text_to_binary(text)
        if binary_result:
            print(Fore.BLUE + "Binary result: " + binary_result + Style.RESET_ALL)
            if not ask_to_continue():
                return


def handle_binary_to_english():
    """Handle the conversion from binary string to English text."""
    while True:
        binary = input(Fore.GREEN + "Enter binary string (or 'back' to return to the main menu): " + Style.RESET_ALL)
        if binary.lower() == 'back':
            return
        text_result = binary_to_text(binary)
        if text_result:
            print(Fore.BLUE + "English text: " + text_result + Style.RESET_ALL)
            if not ask_to_continue():
                return


def ask_to_continue():
    """
    Ask the user if they want to continue with the same operation.

    Returns:
        bool: True if the user wants to continue, False to return to the main menu.
    """
    while True:
        choice = input(Fore.GREEN + "Do you want to perform another operation? (yes/no): " + Style.RESET_ALL).lower()
        if choice in ['yes', 'no']:
            return choice == 'yes'
        print(Fore.RED + "Invalid input. Please type 'yes' or 'no'." + Style.RESET_ALL)


def main():
    """Main function to run the binary translator application."""
    while True:
        clear_screen()
        choice = get_user_choice()

        if choice == '1':
            handle_english_to_binary()
        elif choice == '2':
            handle_binary_to_english()
        elif choice == '3':
            print(Fore.YELLOW + "Exiting the program. Goodbye!" + Style.RESET_ALL)
            break


if __name__ == "__main__":
    main()
