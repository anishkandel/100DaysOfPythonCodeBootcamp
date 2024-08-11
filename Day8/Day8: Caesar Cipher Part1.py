alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
alphabet_length=int(len(alphabet))
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))
# TODO-1: Create a function called 'encrypt()' that takes 'original_text' and 'shift_amount' as 2 inputs.
def encrypt(original_text, shift_amount):
    cipher_text=""
    for letter in original_text:
#         print(letter)
        shifted_position=alphabet.index(letter) + shift_amount #user le deko original letter ko alphabetical position thaa pauna lai. + shift_amount chai , orginal index
#         print (shifted_position)
        shifted_position=shifted_position%len(alphabet)
        
        cipher_text+=alphabet[shifted_position]
        
    print(f" your encoded message is {cipher_text}")
        
       

encrypt(original_text=text, shift_amount=shift)
# TODO-2: Inside the 'encrypt()' function, shift each letter of the 'original_text' forwards in the alphabet
#  by the shift amount and print the encrypted text.

# TODO-4: What happens if you try to shift z forwards by 9? Can you fix the code?

# TODO-3: Call the 'encrypt()' function and pass in the user inputs. You should be able to test the code and encrypt a
#  message.



