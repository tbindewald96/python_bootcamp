from art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
done = False
encrypted_list =  []
decrypted_list = []

print(logo)

while not done: 
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = list(input("Type your message:\n").lower())
    shift = int(input("Type the shift number:\n"))

    def caesar(original_text, shift_amount):
        if direction == "encode":
            for i in original_text:
                if i in alphabet:
                    location = alphabet.index(i)
                    new_location = location + shift
                    if new_location > 25: 
                        new_location = new_location % 26
                    encrypted_list.append(alphabet[new_location])
                else: 
                    encrypted_list.append(i)
            encrypted_word = ''.join(encrypted_list)
            return f"The encrypted word is: {encrypted_word}"
        elif direction == "decode":
            for i in original_text:
                if i in alphabet:
                    location = alphabet.index(i)
                    new_location = location - shift
                    if new_location < 0:
                        new_location = 26 - (-new_location % 26)
                    decrypted_list.append(alphabet[new_location])
                else:
                    decrypted_list.append(i)
            decrypted_word = ''.join(decrypted_list)
            return f"The decrypted word is: {decrypted_word}"
    print(caesar(text, shift))
    proceed = input('Do you want to continue? Type "yes" or "no".\n').lower()
    if proceed == "no":
        done = True