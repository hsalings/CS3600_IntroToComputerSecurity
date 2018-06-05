# Hanna Salings
# CS 3600 HW1
# Due 09/06/2017

import string  # used to strip punctuation from input

with open("dictionary.txt") as file:
  dictionary = file.read().split()
  # used later to check if a word is an actual word that is found in the given dictionary.txt file

def bruteforce(input_ciphertext):
  LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'  # all possible symbols that can be encrypted (don't need to worry about lowercase)
  output_plaintext = ''  # encrypted/decrypted form of the message
  input_ciphertext.strip(string.punctuation)
  cipherSplit = input_ciphertext.split()
  firstWord = cipherSplit[0]  # want just the first word for now to find out what the key is

  for key in range(0,26):  # check each key in the range of the letters
    translated = ''
    for symbol in firstWord:  # only checking the first word for this part
      if symbol in LETTERS:
        num = LETTERS.find(symbol) # gets the number of the symbol
        num = num + key
        # Range Check:
        if num >= len(LETTERS):
          num = num - len(LETTERS)
        elif num < 0:
          num = num + len(LETTERS)

        translated = translated + LETTERS[num]

      else:
        translated = translated + symbol
          
    for word in dictionary:  # check through all words in the dictionary file until a matching word is found
      if translated == word:
        break

    if translated == word:  # exit key checking for-loop once the translated word is found to be a real word
      break
            
  for symbol in input_ciphertext:  # another for-loop using the correct key for the rest of the input
    if symbol in LETTERS:
      num = LETTERS.find(symbol)
      num = num + key
      # Range Check:
      if num >= len(LETTERS):
        num = num - len(LETTERS)
      elif num < 0:
        num = num + len(LETTERS)

      translated = LETTERS[num]

      output_plaintext = output_plaintext + translated

    else:
      output_plaintext = output_plaintext + symbol
    
  # Check
  print(input_ciphertext, "\n")
  print(output_plaintext, "\n")
  print("--------------------------") # makes checking the inputs vs. outputs easier to read
  
  return output_plaintext, 12381101, "Salings"
