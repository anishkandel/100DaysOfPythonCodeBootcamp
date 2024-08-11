alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def decrypt(original_text, shift_amount):
    decrypt_text=""
    for letter in original_text:
        shifted_position=alphabet.index(letter) -shift_amount
        print(shifted_position)
        decrypt_text+=alphabet[shifted_position]
    print(decrypt_text)    
        
decrypt(original_text=text, shift_amount=shift)     