
def caesar_cipher(phrase, shift):
    """
      Perform Caesar Shift by shifing by an offset mod 26
    """
    encoded_phrase = ""

    for char in phrase:
        if char.isalpha():
            # Calculate the offset for uppercase and lowercase letters
            offset = 65 if char.isupper() else 97
            # Apply the shift and wrap around using modulo
            encoded_char = chr((ord(char) - offset + shift) % 26 + offset)
            encoded_phrase += encoded_char
        else:
            # Non-alphabetic characters remain unchanged
            encoded_phrase += char

    return encoded_phrase


# Phrase to encrypt
phrase_input = "THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG"
# Let's try to encrypt -3 characters
encoded_phrase1 = caesar_cipher(phrase_input, -3)
# Let's try to encrypt +16 characters
encoded_phrase2 = caesar_cipher(phrase_input, +16)
# Print result
print("Encoded phrase1:", encoded_phrase1)
print("Encoded phrase2:", encoded_phrase2)
