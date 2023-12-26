import random

def choose_random_word(file_name):
  words = read_words(file_name)
  word = '' 
  desc = ''
  if len(words) == 0:
    print(f"No words exists in the file {file_name}")
  parts = random.choice(words).split(':')
  if len(parts) == 2:
    word = parts[0].strip().lower()
    desc = parts[1].strip()
    
  return word, desc
  

def read_words(file_name):
  try: 
    with open(file=file_name, mode='r') as file:
      words = file.read().splitlines()
      return words
  except FileNotFoundError:
    print(f"Words file not found: {file_name}")
    return []
  

def get_main_word(word, guessmade):
  main = ""
  for letter in word:
    if letter in guessmade:
      main = main + letter
    else:
      main = main + "_" + " "
  return main
