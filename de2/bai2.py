def caesar_cipher_encrypt(plaintext, key):
    ciphertext = ""
    for char in plaintext:
        if char.isalpha(): 
            shifted = ord(char) + key
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
            ciphertext += chr(shifted)
        else:
            ciphertext += char
    return ciphertext

plaintext = input("Nhập vào thông điệp cần mã hóa: ")
key = int(input("Nhập vào khóa (số nguyên trong khoảng từ 0 đến 25): "))
encrypted_text = caesar_cipher_encrypt(plaintext, key)
print("Thông điệp đã được mã hóa:", encrypted_text)