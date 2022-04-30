#!/usr/bin/env python3

class Game:
    def __init__(self):
        self.players = []
        self.places = [0] * 6 #pourquoi 6? si limité éviter crash. erreur perso?
        self.purses = [0] * 6
        self.in_penalty_box = [0] * 6

        self.pop_questions = []
        self.science_questions = []
        self.sports_questions = []
        self.rock_questions = []

        self.current_player = 0
        self.is_getting_out_of_penalty_box = False

        for i in range(50): #dépasse 50?
            self.pop_questions.append("Pop Question %s" % i)
            self.science_questions.append("Science Question %s" % i)
            self.sports_questions.append("Sports Question %s" % i)
            self.rock_questions.append("Rock Question %s" % i)

    def is_playable(self): #jamais appelé
        return self.how_many_players >= 2

    def add(self, player_name):
        self.players.append(player_name)
        self.places[self.how_many_players] = 0
        self.purses[self.how_many_players] = 0
        self.in_penalty_box[self.how_many_players] = False # à voir si vrmt obligatoire

        print(player_name + " was added")
        print(player_name + "is player number %s" % len(self.players))

        return True

    @property
    def how_many_players(self):
        return len(self.players)

    def roll(self, roll):
        print("%s is the current player" % self.players[self.current_player])
        print("He/She have rolled a %s" % roll)

        if self.in_penalty_box[self.current_player]:
            if roll % 2 != 0: #impair pour sortir!
                self.is_getting_out_of_penalty_box = True

                print("%s is getting out of the penalty box" % self.players[self.current_player])
                self.places[self.current_player] = self.places[self.current_player] + roll
                if self.places[self.current_player] > 11: #plateau taille 12, variabiliser?
                    self.places[self.current_player] = self.places[self.current_player] - 12 # si supérieur à 12???

                print(self.players[self.current_player] + \
                            '\'s new location is ' + \
                            str(self.places[self.current_player]))
                print("The category is %s" % self._current_category)
                self._ask_question()
            else:
                print("%s is not getting out of the penalty box" % self.players[self.current_player])
                self.is_getting_out_of_penalty_box = False
        else:
            self.places[self.current_player] = self.places[self.current_player] + roll ##duplication
            if self.places[self.current_player] > 11: ##duplication
                self.places[self.current_player] = self.places[self.current_player] - 12 ##duplication

            print(self.players[self.current_player] + \
                        '\'s new location is ' + \
                        str(self.places[self.current_player]))
            print("The category is %s" % self._current_category)
            self._ask_question()

    def _ask_question(self):
        if self._current_category == 'Pop': print(self.pop_questions.pop(0))
        if self._current_category == 'Science': print(self.science_questions.pop(0))
        if self._current_category == 'Sports': print(self.sports_questions.pop(0))
        if self._current_category == 'Rock': print(self.rock_questions.pop(0))

    @property
    def _current_category(self):
        if self.places[self.current_player] % 4 == 0 : return 'Pop'
        if self.places[self.current_player] % 4 == 1 : return 'Science'
        if self.places[self.current_player] % 4 == 2 : return 'Sports'
        return 'Rock'

    def was_correctly_answered(self): # changer les 2 fonctions par is_correctly_answered
        if self.in_penalty_box[self.current_player]:
            if self.is_getting_out_of_penalty_box: #nécessaire? éviter avec return dans autre fonction?
                print('Answer was correct!!!!')
                self.purses[self.current_player] += 1
                print(self.players[self.current_player] + \
                    ' now has ' + \
                    str(self.purses[self.current_player]) + \
                    ' Gold Coins.') #écriture plus propre?

                winner = self._did_player_win()
                self.current_player += 1
                if self.current_player == len(self.players): self.current_player = 0

                return winner
            else: #nécessaire?
                self.current_player += 1
                if self.current_player == len(self.players): self.current_player = 0
                return True #???



        else:

            print("Answer was corrent!!!!")
            self.purses[self.current_player] += 1
            print(self.players[self.current_player] + \
                ' now has ' + \
                str(self.purses[self.current_player]) + \
                ' Gold Coins.')

            winner = self._did_player_win()
            self.current_player += 1 #duplication
            if self.current_player == len(self.players): self.current_player = 0 #duplication

            return winner #duplication

    def wrong_answer(self):
        print('Question was incorrectly answered')
        print(self.players[self.current_player] + " was sent to the penalty box")
        self.in_penalty_box[self.current_player] = True

        self.current_player += 1 #duplication
        if self.current_player == len(self.players): self.current_player = 0 #duplication
        return True

    def _did_player_win(self):
        return not (self.purses[self.current_player] == 6) # premier à 6coins
