import random

from logo import stages, logo

from replit import clear

import words12

word_list = words12.word_list
word = random.choice(word_list)
display = []

for _ in word:
  display.append('_')

lives = 6

end_of_game = False

print(logo)
while not end_of_game:
  user_letter = input('Guess a letter: ').lower()

  clear()
  if user_letter in display:
    print(f"You've already guessed {user_letter}")

  for position in range(len(word)):
    letter = word[position]
    if letter == user_letter:
      display[position] = user_letter

  if user_letter not in word:
    print(
      f"You guessed {user_letter}, that's not in the word. You lose a life.")
    lives -= 1
    if lives == 0:
      end_of_game = True
      print('You lose.')

  print(stages[lives])
  print(f"{' '.join(display)}")

  if '_' not in display:
    end_of_game = True
    print('You win.')
