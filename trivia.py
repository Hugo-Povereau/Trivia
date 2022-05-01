#!/usr/bin/env python3

class Game:
    def __init__(self):
        self.players = []
        self.players_max = 6
        self.places = [0] * self.players_max
        self.purses = [0] * self.players_max
        self.coins_to_win = 6
        self.in_penalty_box = [0] * self.players_max

        self.pop_questions = []
        self.science_questions = []
        self.sports_questions = []
        self.rock_questions = []

        self.current_player = 0

        for i in range(50):
            self.pop_questions.append("Pop Question %s" % i)
            self.science_questions.append("Science Question %s" % i)
            self.sports_questions.append("Sports Question %s" % i)
            self.rock_questions.append("Rock Question %s" % i)

    def is_playable(self):
        return 2 <= self.how_many_players <= self.players_max

    def add(self, player_name):
        if len(self.players) != 5:
            self.players.append(player_name)
            self.places[self.how_many_players] = 0
            self.purses[self.how_many_players] = 0
            self.in_penalty_box[self.how_many_players] = False
            print(player_name + " is added")
            print(player_name + " is player number %s" % len(self.players))
        else:
            print("sorry " + player_name + " the Game is already Full")

    def roll(self, roll):
        if not self.is_playable():  # ajouter callOnce
            print("sorry the amount of player isn't good")
            exit()
        print("%s is the current player" % self.players[self.current_player])
        print("He/She have rolled a %s" % roll)

        if self.in_penalty_box[self.current_player]:
            if roll % 2 != 0:
                self.in_penalty_box[self.current_player] = False
                print("%s is getting out of the penalty box" % self.players[self.current_player])
                self.player_move(roll)
            else:
                print("%s is not getting out of the penalty box" % self.players[self.current_player])
        else:
            self.player_move(roll)

    @property
    def how_many_players(self):
        return len(self.players)

    def ask_question(self):
        if self.current_category == 'Pop':
            print(self.pop_questions[0])
            self.pop_questions.append(self.pop_questions.pop(0))
        if self.current_category == 'Science':
            print(self.science_questions[0])
            self.science_questions.append(self.science_questions.pop(0))
        if self.current_category == 'Sports':
            print(self.sports_questions[0])
            self.sports_questions.append(self.sports_questions.pop(0))
        if self.current_category == 'Rock':
            print(self.rock_questions[0])
            self.rock_questions.append(self.rock_questions.pop(0))

    @property
    def current_category(self):
        if self.places[self.current_player] % 4 == 0: return 'Pop'
        if self.places[self.current_player] % 4 == 1: return 'Science'
        if self.places[self.current_player] % 4 == 2: return 'Sports'
        return 'Rock'

    def was_correctly_answered(self):
        if self.in_penalty_box[self.current_player]:
            return self.next_player()

        else:
            print("Answer is correct!!!!")
            self.purses[self.current_player] += 1
            print(self.players[self.current_player] + " now has " + str(
                self.purses[self.current_player]) + " Gold Coins.")

            winner = self.did_player_win()
            self.next_player()

            return winner

    def wrong_answer(self):
        if self.in_penalty_box[self.current_player]:
            return self.next_player()
        else:
            print('Question was incorrectly answered')
            print(self.players[self.current_player] + " was sent to the penalty box")
            self.in_penalty_box[self.current_player] = True
            return self.next_player()

    def player_move(self, roll):
        self.places[self.current_player] = self.places[self.current_player] + roll
        if self.places[self.current_player] > 11:
            self.places[self.current_player] = self.places[self.current_player] - 12

        print(self.players[self.current_player] + " new location is " + str(self.places[self.current_player]))
        print("The category is %s" % self.current_category)
        self.ask_question()

    def next_player(self):
        self.current_player += 1
        if self.current_player == len(self.players): self.current_player = 0
        return False

    def did_player_win(self):
        return self.purses[self.current_player] == self.coins_to_win
