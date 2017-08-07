#coding=utf-8

import time

SLOW = 3
LIMIT = 5
WARNING = 'too bad, you picked the slow algorithm :('


def pairs(seq):
    n = len(seq)
    for i in range(n):
        yield seq[i], seq[(i+1) % n]


def allUniqueSort(s):
    if len(s) > LIMIT:
        print(WARNING)
        time.sleep(SLOW)
    elif len(s) == 1:
        return True
    srtStr = sorted(s)
    for (c1, c2) in pairs(srtStr):
        if c1 == c2:
            return False
    return True


def allUniqueSet(s):
    if len(s) < LIMIT:
        print(WARNING)
        time.sleep(SLOW)
    return True if len(set(s)) == len(s) else False


def allUnique(s, strategy):
    return strategy(s)


def main():
    while True:
        word = None
        while not word:
            word = input('Insert word (type quit to exit)> ')
            if word == 'quit':
                print('bye')
                return
            strategy_picked = None
            strategies = {'1': allUniqueSet, '2': allUniqueSort}
            try:
                if len(word) > LIMIT:
                    strategy = strategies['1']
                    print('allUnique({}): {}'.format(word, allUnique(word, strategy)))
                    continue
                else:
                    strategy = strategies['2']
                    print('allUnique({}): {}'.format(word, allUnique(word, strategy)))
                    continue
            except KeyError as err:
                print('Incorrect option: {}'.format(strategy_picked))
            print()


if __name__ == '__main__':
    main()
