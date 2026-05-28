import random

ALPHABET = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

def encrypt(plaintext, key):
    ciphertext = ""
    counter = 0
    letter_value = 0
    letter = ''
    current_key_value = 0

    while counter < len(plaintext):
        try:
            letter_value = ALPHABET.index(plaintext[counter])
        except ValueError: #occurs when there is a space, punctuation, etc in the plaintext
            ciphertext = ciphertext + plaintext[counter]
            counter += 1
            continue
    

        current_key_value = ALPHABET.index(key[counter])

        letter = ALPHABET[(letter_value + current_key_value) % len(ALPHABET)]

        ciphertext = ciphertext + letter

        counter += 1

    return ciphertext

def decrypt(ciphertext, key):
    plaintext = ""
    counter = 0
    letter_value = 0
    letter = ''
    current_key_value = 0

    while counter < len(ciphertext):
        try:
            letter_value = ALPHABET.index(ciphertext[counter])
        except ValueError: #occurs when there is a space, punctuation, etc in the plaintext
            plaintext = plaintext + ciphertext[counter]
            counter += 1
            continue
    

        current_key_value = ALPHABET.index(key[counter])

        letter = ALPHABET[((letter_value + len(ALPHABET)) - current_key_value) % len(ALPHABET)]

        plaintext = plaintext + letter

        counter += 1

    return plaintext

def main():
    key = ''
    counter = 0

    print("----------")

    plaintext = input("Input your plaintext: ").upper()

    while (counter < len(plaintext)):
        key = key + ALPHABET[random.randint(0,25)]
        counter += 1
    
    print("----------")
    print("Encrypted Ciphertext:")

    ciphertext = encrypt(plaintext, key)
    print(ciphertext)

    print("----------")
    print("Decrypted Plaintext:")

    decrypted_plaintext = decrypt(ciphertext, key)
    print(decrypted_plaintext)

if __name__ == "__main__":
    main()  