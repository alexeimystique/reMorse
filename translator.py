def process(translate_input):
    translate_input = translate_input.upper()
    # Open localization file
    translated_output = ""
    for char in translate_input:
        alphabet = open("alphabet.txt", "r")
        for line in alphabet:
            if f"{char} = " in line:
                translated_char = line.replace(f"{char} = ", "")
                translated_char = translated_char.replace("\n", " ")
                translated_output = translated_output + translated_char

    print(translated_output)


translate = input("Write message: ")
process(translate)
