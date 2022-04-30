from random import randrange #monter
from trivia import Game

if __name__ == '__main__':
    not_a_winner = False

    game = Game()

    game.add('Chet')
    game.add('Pat')
    game.add('Sue')
    game.add('zaezaea')
    game.add('zaeaze')
    #game.add('zaeza') # limité 5j échoue si plus

    while True:
        game.roll(randrange(5) + 1)

        if randrange(9) == 7:
            not_a_winner = game.wrong_answer()
        else:
            not_a_winner = game.was_correctly_answered()

        if not not_a_winner: break
