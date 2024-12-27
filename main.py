def caesar(text, shift, direction):
  
  def encrypt(plain_text, shift_amount):
    cipher_text = ""
    for letter in plain_text:
      if letter in alphabet:
        position = alphabet.index(letter)
        new_position = position + shift_amount
        cipher_text += alphabet[new_position]
      else:
        cipher_text += letter
    print(f"The encoded text is {cipher_text}")

  def decrypt(cipher_text, shift_amount):
    plain_text = ""
    for letter in cipher_text:
      if letter in alphabet:
        position = alphabet.index(letter)
        new_position = position - shift_amount
        plain_text += alphabet[new_position]
      else:
        plain_text += letter
    print(f"The decoded text is {plain_text}")
  
  if direction == "encode":
    encrypt(plain_text=text, shift_amount=shift)
  elif direction == "decode":
    decrypt(cipher_text=text, shift_amount=shift)
  else:
    print("Please choose an appropriate command!")



from art import logo
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

should_continue = True
while should_continue:
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))
  shift = shift % 26
  caesar(text=text, shift=shift, direction=direction)
  restart = input("Type 'yes' if you want to go again. Otherwise type 'no'.")
  if restart == "no":
    should_continue = False
    print("GoodBye!")