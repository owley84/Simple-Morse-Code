decode_morse_code_dict = {
    '.-': 'A', 
    '-...': 'B', 
    '-.-.': 'C', 
    '-..': 'D', 
    '.': 'E',
    '..-.': 'F', 
    '--.': 'G', 
    '....': 'H', 
    '..': 'I', 
    '.---': 'J',
    '-.-': 'K', 
    '.-..': 'L', 
    '--': 'M', 
    '-.': 'N', 
    '---': 'O',
    '.--.': 'P', 
    '--.-': 'Q', 
    '.-.': 'R', 
    '...': 'S', 
    '-': 'T',
    '..-': 'U', 
    '...-': 'V', 
    '.--': 'W', 
    '-..-': 'X', 
    '-.--': 'Y',
    '--..': 'Z', 
    '-----': '0', 
    '.----': '1', 
    '..---': '2', 
    '...--': '3',
    '....-': '4', 
    '.....': '5', 
    '-....': '6', 
    '--...': '7', 
    '---..': '8',
    '----.': '9'
}

encode_morse_code_dict = {
    'A': '.-', 
    'B': '-...', 
    'C': '-.-.', 
    'D': '-..', 
    'E': '.',
    'F': '..-.', 
    'G': '--.', 
    'H': '....', 
    'I': '..', 
    'J': '.---',
    'K': '-.-', 
    'L': '.-..', 
    'M': '--', 
    'N': '-.', 
    'O': '---',
    'P': '.--.', 
    'Q': '--.-', 
    'R': '.-.', 
    'S': '...', 
    'T': '-',
    'U': '..-', 
    'V': '...-', 
    'W': '.--', 
    'X': '-..-', 
    'Y': '-.--',
    'Z': '--..', 
    '0': '-----', 
    '1': '.----', 
    '2': '..---', 
    '3': '...--',
    '4': '....-', 
    '5': '.....', 
    '6': '-....', 
    '7': '--...', 
    '8': '---..',
    '9': '----.',
    ' ': '/'
}

def decode_morse_code(morse_code):
    words = morse_code.split(' / ')
    decoded_message = ''
    for word in words:
        letters = word.split(' ')
        for letter in letters:
            if letter in decode_morse_code_dict:
                decoded_message += decode_morse_code_dict[letter]
        decoded_message += ' '
    return decoded_message.strip()

def encode_morse_code(message):
    encoded_message = ''
    for char in message:
        if char.upper() in encode_morse_code_dict:
            encoded_message += encode_morse_code_dict[char.upper()] + ' '
    return encoded_message.strip()

# Main program loop
while True:
    print("\n----- Morse Code Converter -----\n")
    choice = input("Choose an option:\n 1. Decode Morse code into message\n 2. Encode message into Morse code\n 3. Exit\nEnter your choice: ")
    
    if choice == '1':
        morse_code = input("Enter Morse code: ")
        decoded_message = decode_morse_code(morse_code)
        print("Decoded message:", decoded_message)
    elif choice == '2':
        message = input("Enter a message: ")
        encoded_message = encode_morse_code(message)
        print("Encoded message:", encoded_message)
    elif choice == '3':
        print("Exiting the program...")
        break
    else:
        print("Invalid choice. Please try again.")