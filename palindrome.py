# function to identify a palindrome
def is_palindrome():
  word_or_phrase = input('Please write a word or a phrase: ')
  characters = word_or_phrase.lower() # convert to lower case
  characters = characters.replace(' ','').strip() # replace function with  ' ','' as paremeters, remove spaces between characters and split function removes spaces at the beginning and at the end
  # evaluates if is a palindrome
  if characters == characters[::-1]: # choose all characters and sort in reverse order
    print(f"Congrats! The submitted word(s): '{word_or_phrase}' is a palindrome")
  else:
    print(f"Sorry! The submitted word(s): '{word_or_phrase}' is NOT a palindrome")

def run():
  is_palindrome()  

if __name__ == "__main__":
  run()
