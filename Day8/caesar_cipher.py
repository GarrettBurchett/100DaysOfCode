from art import logo

def caesar(message:str, shift:int, direction:str) -> str:
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    coded_message = ""
    if direction == 'decode':
        shift *= -1
    for letter in message:
        if letter not in alphabet:
            coded_message += letter
        elif alphabet.index(letter) + shift > len(alphabet) - 1:
            coded_message += alphabet[(alphabet.index(letter) + shift) - len(alphabet)]
        else:
            coded_message += alphabet[alphabet.index(letter) + shift]
    
    return coded_message


done = 'yes'
print(logo)
while done == 'yes':
    operation = input("Type 'encode' to encrypt, type 'decode' to decrypt\n")
    while operation not in ['encode', 'decode']:
        print("Not a valid input. Please select a valid option.")
        operation = input("Type 'encode' to encrypt, type 'decode' to decrypt\n")
    message = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    result = caesar(message, shift % 26, operation)
    print(f"Here's the {operation}d result: {result}")
    done = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n").lower()
    
    
    
#   def encode(message:str, shift:int) -> str:
#    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
#    coded_message = ""
#    for letter in message:
#        if letter == ' ':
#            coded_message += letter
#        elif alphabet.index(letter) + shift > len(alphabet) - 1:
#            coded_message += alphabet[(alphabet.index(letter) + shift) - len(alphabet)]
#        else:
#            coded_message += alphabet[alphabet.index(letter) + shift]
#    return coded_message
#    
#def decode(message:str, shift:int) -> str:
#    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
#    coded_message = ""
#    for letter in message:
#        if letter == ' ':
#            coded_message += letter
#        else:
#            coded_message += alphabet[alphabet.index(letter) - shift]
#    return coded_message
    
    
    #if operation == 'encode':
    #    result = encode(message, shift)
    #    print(f"Here's the encoded result: {result}")
    #    done = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
    #else:
    #    result = decode(message, shift)
    #    print(f"Here's the decoded result: {result}")
    #    done = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")