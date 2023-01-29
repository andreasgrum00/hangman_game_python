from random import choice

words = ["Estudante", "Elefante", "Computador", "Fotografia", "Caminhao", "Pneu", "Cisne", "Cadeira", "Astronauta", "Fantasia"]

def choose_random_word() -> str:
    """
    This function choose a random word given by OpenAI's ChatGPT. P.S. Those previous words are written in brazilian portuguese.
    """
    return choice(words).lower()