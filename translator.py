def to_morse(original_message):
    # Processing input
    original_message = original_message.upper()
    original_message = original_message.split()

    # Starting conversion
    morse_message = ""
    for word in original_message:
        char_count = 1
        for char in word:
            alphabet = open("alphabet.txt", "r")
            for line in alphabet:
                if f"{char} = " in line:
                    translated_char = line.replace(f"{char} = ", "")
                    translated_char = translated_char.replace("\n", "")

                    if len(word) == char_count:
                        morse_message = morse_message + translated_char + " / "
                    else:
                        morse_message = morse_message + translated_char + " "
                        char_count += 1

    print(morse_message)


def translate(morse_code):
    # Processing input
    morse_message = morse_code.replace("/", " / ")
    morse_message = morse_message.split()

    # Starting translation
    translated_message = ""

    for item in morse_message:
        alphabet = open("alphabet.txt", "r")
        for line in alphabet:
            if f" = {item}" in line and len(line) == (len(item) + 5):
                character = line[:1]
                translated_message = translated_message + character
            if item == "/":
                translated_message = translated_message + " "
                break

    print(translated_message)


while True:
    print("Choose 1 for text to morse, choose 2 for morse to text.")
    answer = input()
    if answer == "1":
        message = input("What is your message: ")
        to_morse(message)
    if answer == "2":
        message = input("What is your morse code: ")
        translate(message)
