def caesar(start_text, shift_amount, direction="encode"):
    """
    Encrypts or decrypts a given text by shifting the characters by the provided shift_amount using the ASCII character set
    """
    end_text = ""
    if direction == "decode":
        shift_amount *= -1

    for char in start_text:
        pos = ord(char)
        new_pos = pos + shift_amount
        end_text += chr(new_pos)
    return end_text


should_end = False
while not should_end:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    
    result = caesar(start_text=text, shift_amount=shift, direction=direction)
    print(result)
    
    restart = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
    if restart == "no":
        should_end = True
        print("Goodbye")












