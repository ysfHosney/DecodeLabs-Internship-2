def encrypt(text, shift):
    encrypted = ""
    for char in text:
        if char.isupper():
            encrypted += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
        elif char.islower():
            encrypted += chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
        else:
            encrypted += char
    return encrypted
def decrypt(text, shift):
    decrypted = ""
    for char in text:
        if char.isupper():
            decrypted += chr((ord(char) - ord('A') - shift) % 26 + ord('A'))
        elif char.islower():
            decrypted += chr((ord(char) - ord('a') - shift) % 26 + ord('a'))
        else:
            decrypted += char
    return decrypted

text = input("Enter text: ")
shift = int(input("Enter shift: "))
encrypted = encrypt(text, shift)
print(encrypted)
decrypted = decrypt(text, shift)
print(decrypted)