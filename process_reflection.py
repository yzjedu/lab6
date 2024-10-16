import os


def calculate_shift_from_key(key):
    """Calculate a shift value from a given key."""
    return sum(ord(char) for char in key) % 26  # Modulo 26 to stay within the alphabet


def caesar_cipher(text, shift):
    """Encrypt or decrypt text using a Caesar cipher with the given shift."""
    result = []
    for char in text:
        if char.isalpha():  # Only shift alphabetic characters
            shift_base = ord('A') if char.isupper() else ord('a')
            shifted_char = chr((ord(char) - shift_base + shift) % 26 + shift_base)
            result.append(shifted_char)
        else:
            result.append(char)  # Leave non-alphabetic characters unchanged
    return ''.join(result)


def encrypt_file(filename, key):
    """Encrypt the file using a Caesar cipher with the key-based shift, unless already encrypted."""
    try:
        with open(filename, 'r') as file:
            file_data = file.read()

        # Check if the file is already encrypted
        if file_data.startswith("ENCRYPTED:"):
            print(f"\nℹ️ The file '{filename}' is already encrypted. Encryption skipped.")
            return

        # Calculate shift and encrypt the content
        shift = calculate_shift_from_key(key)
        encrypted_data = caesar_cipher(file_data, shift)
        encrypted_data = f"ENCRYPTED:\n{encrypted_data}"

        with open(filename, 'w') as file:
            file.write(encrypted_data)

        print(f"\n✅ Success! The file '{filename}' has been encrypted with your key.")
    except Exception as e:
        print(f"❌ Error: Could not encrypt '{filename}'. {e}")


def decrypt_file(filename, key):
    """Decrypt the file using a Caesar cipher with the key-based shift only if it is encrypted."""
    try:
        with open(filename, 'r') as file:
            content = file.read()

        if not content.startswith("ENCRYPTED:"):
            print("\nℹ️ The file does not appear to be encrypted. Decryption is not required.")
            return

        shift = calculate_shift_from_key(key)
        # Remove the marker and decrypt the content
        encrypted_data = content[len("ENCRYPTED:\n"):]
        decrypted_data = caesar_cipher(encrypted_data, -shift)

        with open(filename, 'w') as file:
            file.write(decrypted_data)

        print(f"\n✅ Success! The file '{filename}' has been decrypted with your key.")
    except Exception as e:
        print(f"❌ Error: Could not decrypt '{filename}'. {e}")


def get_user_input():
    print("\nWelcome to the File Encryption and Decryption Tool!")
    print("This tool will help you encrypt or decrypt text files based on a simple key.")

    # Prompt for the file name
    filename = input("\nPlease enter the file name (e.g., RD1.md): ")
    if not os.path.exists(filename):
        print(f"❌ Error: The file '{filename}' does not exist. Please check the file name and try again.")
        return None, None, None

    # Prompt for the key
    key = input("Please enter a key for encryption/decryption: ")

    # Ask whether to encrypt or decrypt
    action = input("\nDo you want to (e)ncrypt or (d)ecrypt the file? Enter 'e' or 'd': ").strip().lower()

    if action == 'e':
        return filename, key, 'encrypt'
    elif action == 'd':
        return filename, key, 'decrypt'
    else:
        print("❌ Error: Invalid action. Please enter 'e' for encryption or 'd' for decryption.")
        return None, None, None


if __name__ == "__main__":
    filename, key, action = get_user_input()

    if filename and key and action:
        if action == "encrypt":
            encrypt_file(filename, key)
        elif action == "decrypt":
            decrypt_file(filename, key)