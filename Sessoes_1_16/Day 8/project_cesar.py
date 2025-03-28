alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
keeping=True

def cesar_message(code_decode, message_text, shift_move):
    result = '' 
    #inside the for loop cause a bug
    if code_decode == 'decode':
        shift_move *= -1

    for letter in message_text:
        if letter in alphabet:
            index = alphabet.index(letter)
            new_index = (index + shift_move) % len(alphabet)
            result += alphabet[new_index]
        else:
            result += letter  # no alphabetics

    print(f"The message is: {result}")

while keeping:
    choice = input('Type "code" to encrypt or "decode" to decrypt: \n').lower()
    message = input('Write the message: \n').lower()
    shift = int(input('How many shifts? \n'))
    
    cesar_message(choice, message, shift)
    
    question=input("Type 'yes' to continue and 'no' to exit: \n").lower()

    if question == 'no':
        print('Ok, Thank you')
        keeping = False

