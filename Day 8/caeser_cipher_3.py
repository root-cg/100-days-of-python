alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

#TODO-1: Combine the encrypt() and decrypt() functions into a single function called caesar(). 


def caesar(text, shift, direction):
  plain_text = ""
  for letter in text:
    position = alphabet.index(letter)
    if direction == "decode":
        new_position = position - shift
    elif direction == "encode":
        new_position = position + shift
    plain_text += alphabet[new_position]
  print(f"The {direction}ed text is {plain_text}")


#TODO-2: Call the caesar() function, passing over the 'text', 'shift' and 'direction' values.

caesar(text, shift, direction)