hangman_pics = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
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
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

def choose_pics(number_array: int) -> str:
    """
    This function returns an ascii art of the hangman game.

    :param number_array: Number of the ascii in the array. It isn't necessary to type the ascii number from the number zero because the function already subtracts one to the item number.

    :return: An ascii art of the hangman game.
    """
    return hangman_pics[number_array - 1]