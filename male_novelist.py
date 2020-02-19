#!/usr/bin/env python


"""Creates a sentence emulating a stereotypically bad author writing about women."""


import random


__author__ = "Nickolaus Dekay"
__version__ = "1.0"
__email__ = "nickolaus.dekay@gmail.com"


def pick(t):
    return random.choice(t)


def main():
    a = ('boobs', 'a bust', 'a butt', 'lips', 'an ass', 'breasts', 'hair', 'eyes', 'a voice', 'curves', 'a rump', 'legs', 'a rear end', 'mammaries', 'jugs', 'calves', 'a badonkadonk', 'gams', 'knockers', 'a complexion', 'a pout', 'hooters', 'a booty', 'cheeks', 'thighs', 'tresses')
    b = ('silken', 'creamy', 'shiny', 'ripe', 'juicy', 'middle-aged', 'rippling', 'wrinkled', 'luscious', 'frigid', 'voluptuous', 'expensive', 'plump', 'bountiful', 'tempestuous', 'withered', 'haughty', 'shrill', 'fat', 'dewy', 'soft', 'wiry', 'gleaming', 'withholding', 'bulbous', 'brittle')
    c = ('kitten', 'mountain', 'pillow', 'ice cream cone', 'tulip', 'lake', 'fortress', 'lemon', 'popsicle', 'librarian', 'python', 'pony', 'melon', 'bedsheet', 'muffin', 'bunny rabbit', 'fish', 'princess', 'ghost', 'waterfall', 'mango', 'harpy', 'ship', 'nun', 'berry', 'car')
    d = ('longed', 'lusted', 'wished', 'wanted', 'resolved', 'dared', 'detested', 'trembled', 'thirsted', 'expected', 'planned', 'deigned', 'proposed', 'shuddered', 'refused', 'hated', 'scorned', 'dreaded', 'did not care', 'ached', 'intended', 'hungered', 'craved', 'hankered', 'needed', 'pined')
    e = ('ravish', 'climb', 'invade', 'grope', 'marry', 'raw dog it with', 'caress', 'proposition', 'correct', 'emotionally manipulate', 'spar with', 'compliment', 'hire', 'booty call', 'mansplain to', 'insult', 'date', 'teabag', 'ignore', 'fondle', 'worship', 'examine', 'manhandle', 'touch', 'admire', 'demand things from')

    sentence = "She had {} like a {} {} and I {} to {} her.".format(pick(a), pick(b), pick(c), pick(d), pick(e))
    print(sentence)


if __name__ == "__main__":
    main()
