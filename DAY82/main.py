MORSE_CODE_DICT = {'A': '.-', 'B': '-...',
                   'C': '-.-.', 'D': '-..', 'E': '.',
                   'F': '..-.', 'G': '--.', 'H': '....',
                   'I': '..', 'J': '.---', 'K': '-.-',
                   'L': '.-..', 'M': '--', 'N': '-.',
                   'O': '---', 'P': '.--.', 'Q': '--.-',
                   'R': '.-.', 'S': '...', 'T': '-',
                   'U': '..-', 'V': '...-', 'W': '.--',
                   'X': '-..-', 'Y': '-.--', 'Z': '--..',
                   '1': '.----', '2': '..---', '3': '...--',
                   '4': '....-', '5': '.....', '6': '-....',
                   '7': '--...', '8': '---..', '9': '----.',
                   '0': '-----', ', ': '--..--', '.': '.-.-.-',
                   '?': '..--..', '/': '-..-.', '-': '-....-',
                   '(': '-.--.', ')': '-.--.-'}

sentence = input("Please input a word or sentence to be encrypted in morse code: ")
sentence = sentence.upper()
morse_list = []

for char in sentence:
    if char == " ":
        morse_list.append("  ")
    elif char in MORSE_CODE_DICT.keys():
        morse_list.append(MORSE_CODE_DICT[char])
    else:
        print("One of the Characters does not have a Morse code. Please ensure you input you didn't input special "
              "charaters such as '$,%,#'")

sentence_in_morse = "".join([str(item) for item in morse_list])

print(f"The morse code for {sentence} is {sentence_in_morse}")
