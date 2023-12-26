from .app_utils import choose_random_word, get_main_word
from .app_config import Configuration

def hangman():
  config = Configuration()
  word, desc = choose_random_word(config.words_file)
  validletter = config.validletter
  turns = len(word) * config.multiplier
  print(f"Try to guess it less than {turns} attempts")

  guessmade = ''
  
  while len(word) > 0:
    main = get_main_word(word, guessmade)
    
    if main == word:
      print(main)
      print("You win!")
      break
    
    print("Hint:", desc)
    guess = input(f"Guess the word: {main} : ").casefold()

    if guess in validletter:
      guessmade = guessmade + guess
    else:
      print("Enter a valid character")
      guess = input()
    
    if guess not in word:
      turns = turns - 1
      if turns == 0:    
        print("You lose")
        print(f"The word was {word}")
        break
      if turns == 1:
        print("Last breaths counting. Take care!")
      print(f"{turns} turns left")

    
    
    