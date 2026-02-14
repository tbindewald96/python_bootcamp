alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = list(input("Type your message:\n").lower())
shift = int(input("Type the shift number:\n"))
encrypted_list =  []
decrypted_list = []

if direction == "encode":
    def encrypt(original_text, shift_amount):
        for i in original_text:
            location = alphabet.index(i)
            new_location = location + shift
            if new_location > 25: 
              new_location = new_location - 26
            encrypted_list.append(alphabet[new_location])
        encrypted_word = ''.join(encrypted_list)
        return f"The encrypted word is: {encrypted_word}"
    print(encrypt(text,shift))
elif direction == "decode":
    def decrypt(original_text, shift_amount):
        for i in original_text:
            location = alphabet.index(i)
            new_location = location - shift
            decrypted_list.append(alphabet[new_location])
        decrypted_word = ''.join(decrypted_list)
        return f"The decrypted word is: {decrypted_word}"
    print(decrypt(text,shift))

  
# TODO-2: Inside the 'decrypt()' function, shift each letter of the 'original_text' *backwards* in the alphabet
#  by the shift amount and print the decrypted text.
# TODO-3: Combine the 'encrypt()' and 'decrypt()' functions into one function called 'caesar()'.
#  Use the value of the user chosen 'direction' variable to determine which functionality to use.

