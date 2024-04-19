
from PIL import Image
from pyparsing import C

def swap_pixels(image):
    width, height = image.size
    pixels = image.load()

    for i in range(width):
        for j in range(height):
            r, g, b = pixels[i, j]
            pixels[i, j] = (b, r, g)

    return image

def shift_pixels(image, shift_value):
    width, height = image.size
    pixels = image.load()

    for i in range(width):
        for j in range(height):
            r, g, b = pixels[i, j]
            pixels[i, j] = ((r + shift_value) % 256, 
                            (g + shift_value) % 256, 
                            (b + shift_value) % 256)

    return image

def encrypt_image(image_path, method):
    image = Image.open(image_path)

    if method == 'swap':
        encrypted_image = swap_pixels(image)
    elif method == 'shift':
        
        try:
            shift_value = int(input("Enter the shift value (0-255): "))
            encrypted_image = shift_pixels(image, shift_value)
        except ValueError:
            print("Please enter a valid shift value.")
            return

    encrypted_image.save("encrypted_image.png")
    print(f"Image encrypted successfully and saved as encrypted_image.png.")

def decrypt_image(image_path, method):
    image = Image.open(image_path)

    if method == 'swap':
        decrypted_image = swap_pixels(image)
    elif method == 'shift':
        try:
            shift_value = int(input("Enter the shift value (0-255): "))
            decrypted_image = shift_pixels(image, -shift_value)
        except ValueError:
            print("Please enter a valid shift value.")
            return

    decrypted_image.save("decrypted_image.png")
    print(f"Image decrypted successfully and saved as decrypted_image.png.")

def main():
    while True:
        choice = input("Do you want to encrypt or decrypt an image? (e/d): ").lower()
        
        if choice not in ['e', 'd']:
            print("Please enter 'e' for encrypt or 'd' for decrypt.")
            continue

        image_path = input("Enter the path to the image file: ")

        if choice == 'e':
            method = input("Choose encryption method (swap/shift): ").lower()
            if method not in ['swap', 'shift']:
                print("Please choose a valid encryption method.")
                continue
            encrypt_image(image_path, method)
        else:
            method = input("Choose decryption method (swap/shift): ").lower()
            if method not in ['swap', 'shift']:
                print("Please choose a valid decryption method.")
                continue
            decrypt_image(image_path, method)

        another = input("Do you want to encrypt/decrypt another image? (y/n): ").lower()
        if another != 'y':
            break

if __name__ == "__main__":
    main()
