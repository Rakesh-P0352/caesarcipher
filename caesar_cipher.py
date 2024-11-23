def encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            ascii_offset = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - ascii_offset + shift) % 26 + ascii_offset)
        else:
            result += char
    return result


test_text = "Udnhvk"
test_shift = 3
encrypted_text = encrypt(test_text, test_shift)
decrypted_text = encrypt(test_text, -test_shift)


print(f"Original Text: {test_text}")
print(f"Shift: {test_shift}")
print(f"Encrypted Text: {encrypted_text}")

print(f"decrypted Text: {decrypted_text}")

