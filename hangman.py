import random


def split(ord):
    return [char for char in ord]

def start_game():
    global word, gissade_bok, index_list, liv, right_bokstav, ord_längd
    word_list = ['words', 'of', 'your', 'choice', 'go', 'here']

    word = {}
    bok = split(random.choice(word_list).casefold())
    for x in range(len(bok)):
        word[str(x)] = bok[x]

    ord_längd = []

    for bokstav in list(word.keys()):
        ord_längd.append('_')

    gissade_bok = []

    index_list = []

    liv = 5
    right_bokstav = False

started_game = False
while True:
    global gissade_bok, ord_längd, word, index_list, liv
    if not started_game:
        start_game()
        started_game = True


    print(*gissade_bok)
    print(*ord_längd)
    svar = input('Gissa en bokstav: ')
    if len(split(svar)) > 1:
        print('Skriv in en bokstav....')
    else:
        if gissade_bok.count(svar) == 1:
            print('Du har redan skrivit in den bokstaven.....')
        else:

            gissade_bok.append(svar)

            for index in range(len(word.keys())):
                if word[str(index)] == svar:
                    index_list.append(index)
                    for bokstav in index_list:
                        ord_längd.pop(bokstav)
                        ord_längd.insert(bokstav, word[str(bokstav)])

            if ord_längd.count(svar) >= 1:
                right_bokstav = True
            else:
                right_bokstav = False

            if not right_bokstav:
                liv -= 1
                print('Fel bokstav du har:', liv, 'liv kvar')
                if liv == 0:
                    print('Du förlorade')
                    break
                right_bokstav = True

    if ord_längd == list(word.values()):
        print(*ord_längd)
        print('Du vann')
        go_agian = input('Vill du köra igen? (ja/nej)')
        if go_agian == 'ja':
            started_game = False
        if go_agian == 'nej':
            break

