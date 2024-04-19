def caesar_cipher_encrypt(text, shift):
    encrypted_text = ""
    
    for char in text:
        if char.isalpha():
            shifted = ord(char) + shift
            
            if char.islower():
                if shifted > ord('z'):
                    shifted -= 26
                elif shifted < ord('a'):
                    shifted += 26
            elif char.isupper():
                if shifted > ord('Z'):
                    shifted -= 26
                elif shifted < ord('A'):
                    shifted += 26
            
            encrypted_text += chr(shifted)
        else:
            encrypted_text += char
            
    return encrypted_text

def caesar_cipher_decrypt(text, shift):
    return caesar_cipher_encrypt(text, -shift)

def main():
    while True:
        choice = input("Do you want to encrypt or decrypt? (e/d): ").lower()
        
        if choice not in ['e', 'd']:
            print("Please enter 'e' for encrypt or 'd' for decrypt.")
            continue
        
        message = input("Enter the message: ")
        
        try:
            shift = int(input("Enter the shift value (1-25): "))
            
            if not 1 <= shift <= 25:
                print("Shift value must be between 1 and 25.")
                continue
        except ValueError:
            print("Please enter a valid shift value.")
            continue
        
        if choice == 'e':
            encrypted_message = caesar_cipher_encrypt(message, shift)
            print(f"Encrypted message: {encrypted_message}")
        else:
            decrypted_message = caesar_cipher_decrypt(message, shift)
            print(f"Decrypted message: {decrypted_message}")
        
        another = input("Do you want to encrypt/decrypt another message? (y/n): ").lower()
        if another != 'y':
            break

if __name__ == "__main__":
    main()
