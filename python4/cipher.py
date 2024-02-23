alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']    

def caesar(text, shift):
    if direction == 'encode':
        def encrypt(plain_text, shift_amount):
            message = ""
            for letter in plain_text:
                position = alphabet.index(letter)
                new_position = position + shift_amount    
                new_letter = alphabet[new_position]
                message += new_letter
            print(f"The encoded text is {message}") 
    
    elif direction == 'decode':
        def decrypt(message, shift_amount):
            decrypted_message = ""
            for letter in message:
                position = alphabet.index(letter)
                decrypted_position = position - shift_amount
                decrypted_letter = alphabet[decrypted_position]
                decrypted_message += decrypted_letter
            print(f"the decoded text is {decrypted_message}")    
    else:
        print('pls type a valid option')

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

caesar(text, shift)

