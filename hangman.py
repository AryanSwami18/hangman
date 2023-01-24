
import random
##game loop and player lives
game_loop = 0
player_lives = 6
##stages of hangman
stages = [
  '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
'''
]

##WORD_LIST
word_list = ["cat", "easter", "milk", "book", "woman", "hello"]
##generating a random word and display "_"
choosen_word = random.choice(word_list)
##generating a empty display list
display_list = []
## adding the same number of _ to display list
for l in choosen_word:
  display_list += "_"

##game loop
while game_loop == 0:
  ##user guesing the letter
  user_word = input("guess a letter:").lower()
  ##clear screen
  
  ##checking if the letter is there
  for position in range(len(choosen_word)):
    letter = choosen_word[position]
    if user_word == letter:
      display_list[position] = letter
  ##printing the display list after every update
  print(display_list)
  ##to reduce lives
  if user_word not in choosen_word:
    print("word not found")
    player_lives -= 1
    print(stages[player_lives])
    ##to check if player lives are 0 or not
    if player_lives == 0:
      print("sorry you lost the game ")
      print(f"the word was {choosen_word}")
      game_loop = 1
  ##cheking if all the blanks are gone
  elif "_" not in display_list:
    print("congrates you won")
    game_loop = 1
