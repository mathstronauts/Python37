import random
from .words import words

data = words

def randomword():
    random_word = random.choice(data)
    return random_word

# make word mask function - Mathstronauts library
def wordmask(word):
    #TODO: allow user to specify number of mask letters
    a = random.randint(0, len(word)-1)
    b = random.randint(0, len(word)-1)
    while(a==b):
        b = random.randint(0, len(word)-1)
    wordmask = ""
    for i in range(len(word)):
        if i == a or i == b:
            wordmask += "_"
        else:
            wordmask += word[i]
    return wordmask

