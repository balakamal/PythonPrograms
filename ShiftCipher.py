KEY = 5
s = input()


def encrypt():
    encrypted_data = ""
    for i in s:
        encrypted_data += chr(ord(i) + KEY)
    print(encrypted_data)
    return encrypted_data


def decrypt(ed):
    decrypted_data = ""
    for i in ed:
        decrypted_data += chr(ord(i) - KEY)
    print(decrypted_data)


ed = encrypt()
decrypt(ed)
