# -*- coding: utf-8 -*-

class TennisGame1:

    def __init__(self, player1Name, player2Name):
        self.player_1_name = player1Name
        self.player_2_name = player2Name
        self.player_1_points = 0
        self.player_2_points = 0

    def won_point(self, playerName):
        if playerName == self.player_1_name:
            self.player_1_points += 1
        else:
            self.player_2_points += 1

    def is_tied(self):
        return self.player_1_points == self.player_2_points

    def one_player_upper_forty(self):
        return self.player_1_points >= 4 or self.player_2_points >= 4

    def score(self):
        if self.is_tied():
            return self.get_tied_score()
        if self.one_player_upper_forty():
            return self.advantage_or_win()
        return self.get_score_below_deuce()

    def get_score_below_deuce(self):
        return f"{self.get_player_score_name(self.player_1_points)}-{self.get_player_score_name(self.player_2_points)}"

    def get_player_score_name(self, player_points):
        return {
            0: "Love",
            1: "Fifteen",
            2: "Thirty",
            3: "Forty",
        }[player_points]

    def advantage_or_win(self):
        player_name = self.get_leading_player_name()
        if self.get_score_gap() == 1:
            return f"Advantage {player_name}"
        return f"Win for {player_name}"

    def get_leading_player_name(self):
        if self.player_1_points > self.player_2_points:
            return self.player_1_name
        return self.player_2_name

    def get_tied_score(self):
        result = {
            0: "Love-All",
            1: "Fifteen-All",
            2: "Thirty-All",
        }.get(self.player_1_points, "Deuce")
        return result

    def get_score_gap(self):
        return abs(self.player_1_points - self.player_2_points)


class TennisGame2:
    def __init__(self, player_1_name, player_2_name):
        self.player_1_name = player_1_name
        self.player_2_name = player_2_name
        self.player_1_points = 0
        self.player_2_points = 0
        self.score_dict = {0: "Love", 1: "Fifteen", 2: "Thirty", 3: "Forty"}

    def won_point(self, playerName):
        if playerName == self.player_1_name:
            self.increment_player_1_score()
        else:
            self.increment_player_2_score()

    def is_tied(self):
        return self.player_1_points == self.player_2_points

    def is_below_deuce(self):
        return self.player_2_points < 4 and self.player_1_points < 4

    def is_higher_than_deuce(self):
        return not self.is_below_deuce()

    def get_leader_name(self):
        if self.player_1_points > self.player_2_points:
            return self.player_1_name
        return self.player_2_name

    def score(self):
        if self.is_tied():
            return self.score_tied()
        return self.score_if_not_tied()

    def score_if_not_tied(self):
        if self.is_below_deuce():
            result = self.score_not_tied_below_deuce()
        if self.is_higher_than_deuce():
            result = self.score_not_tied_higher_than_deuce()
        return result

    def score_not_tied_higher_than_deuce(self):
        leader = self.get_leader_name()
        result = "Advantage " + leader
        if abs(self.player_1_points - self.player_2_points) >= 2:
            result = "Win for " + leader
        return result

    def score_not_tied_below_deuce(self):
        P1res = self.score_dict[self.player_1_points]
        P2res = self.score_dict[self.player_2_points]
        result = P1res + "-" + P2res
        return result

    def score_tied(self):
        result = ""
        if self.player_1_points < 3:
            result = self.score_dict[self.player_1_points] + "-All"
        if self.player_1_points > 2:
            result = "Deuce"
        return result

    def increment_player_1_score(self):
        self.player_1_points += 1

    def increment_player_2_score(self):
        self.player_2_points += 1


class ScoreName:
    def __init__(self):
        self.score_name = ["Love", "Fifteen", "Thirty", "Forty"]

    def __getitem__(self, player_score):
        return self.score_name[player_score]

class TennisGame3:
    def __init__(self, player_1_name, player_2_name):
        self.player_1_name = player_1_name
        self.player_1_score = 0
        self.player_2_name = player_2_name
        self.player_2_score = 0
        self.score_name = ScoreName()


    def won_point(self, n):
        if n == self.player_1_name:
            self.player_1_score += 1
        else:
            self.player_2_score += 1

    def is_deuce(self):
        return 3 <= self.player_1_score == self.player_2_score

    def score(self):
        if self.is_deuce():
            return "Deuce"
        if self.score_is_below_deuce():
            return self.score_name_below_deuce()
        return self.score_name_above_deuce()

    def score_name_above_deuce(self):
        advantage_player_name = self.get_leading_player_name()
        if abs(self.player_1_score - self.player_2_score) == 1:
            return "Advantage " + advantage_player_name
        return "Win for " + advantage_player_name

    def score_name_below_deuce(self):
        score_name = self.score_name[self.player_1_score]
        if self.player_1_score == self.player_2_score:
            return score_name + "-All"
        return score_name + "-" + self.score_name[self.player_2_score]

    def score_is_below_deuce(self):
        return self.player_1_score < 4 and self.player_2_score < 4

    def get_leading_player_name(self):
        if self.player_1_score > self.player_2_score:
            return self.player_1_name
        return self.player_2_name
