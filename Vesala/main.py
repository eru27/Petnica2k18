import random

LIVES = 6

def load():
    f = open('reci.txt', 'r')
    f = f.readlines()
    index = random.randint(0, len(f) - 1)
    return f[index].strip()

def getLines(word):
    lines = list('_' * len(word))
    return lines

def check(word, lines, letter):
    ok = False
    for index in range(0,len(word)):
        if word[index] == letter:
            lines[index] = letter
            ok = True
    return ok

def isGuessed(lines):
    ok = True
    for ch in lines:
        if ch == '_':
            ok = False
    return ok

def printAll(lines, lives):
    print(str(' '.join(lines)))
    print('Imate jos ' + str(lives) + ' zivot(a)')

def game():
    lives = LIVES
    word = load()
    lines = getLines(word)
    while lives > 0 and (not isGuessed(lines)):
        letter = input("Izaberite slovo: ")
        ok = check(word, lines, letter)
        if not ok:
            lives -= 1
        printAll(lines, lives)
    if lives == 0:
        print('Izgubili ste :c')
    else:
        print('Cestitam!')

game()