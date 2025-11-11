# Caesar Cipher Encryption and Decryption

def encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():  # Check if character is a letter
            shift_base = 65 if char.isupper() else 97  # Uppercase or lowercase
            result += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else:
            result += char  # Non-alphabetic characters remain same
    return result

def decrypt(text, shift):
    return encrypt(text, -shift)  # Just reverse the shift for decryption

# --- Main Program ---
print("=== Caesar Cipher Program ===")
message = input("Enter your message: ")
shift = int(input("Enter shift value (number): "))

encrypted_text = encrypt(message, shift)
print(f"\nEncrypted Message: {encrypted_text}")

decrypted_text = decrypt(encrypted_text, shift)
print(f"Decrypted Message: {decrypted_text}")
