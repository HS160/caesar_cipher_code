alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

def encrypt(original_text, shift):
    return caesar_cipher(original_text, shift)

def decrypt(cipher_text, shift):
    return caesar_cipher(cipher_text, -shift)

def caesar_cipher(text, shift):
    result = ""
    for letter in text.lower():
        if letter in alphabet:
            index = alphabet.index(letter)
            shifted_index = (index + shift) % 26
            result += alphabet[shifted_index]
        else:
            result += letter
    return result
         
should_continue = True

while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:").lower()
    if direction == 'encode':
        text = input("Enter your message\n").lower()
        shift = int(input("Type the shift number\n"))
        encode = encrypt(text,shift)
        print(encode)
    
    elif direction == 'decode':
        text = input("Enter your message\n").lower()
        shift = int(input("Type the shift number\n"))
        decode = decrypt(text,shift)
        print(decode)
    else:
        print("ERROR")
        
    choice = input("If you want to continue type 'Yes', if not type 'NO'\n").lower()
    if choice == "no":
        print("GOODBYE!\n")
        break