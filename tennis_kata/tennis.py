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
        return self.player_1_points==self.player_2_points

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
                    0 : "Love",
                    1 : "Fifteen",
                    2 : "Thirty",
                    3 : "Forty",
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
        
    def won_point(self, playerName):
        if playerName == self.player_1_name:
            self.increment_player_1_score()
        else:
            self.increment_player_2_score()

    def is_tied(self):
        return self.player_1_points == self.player_2_points

    def is_below_deuce(self):
        return self.player_2_points < 4 and self.player_1_points < 4

    def score(self):
        result = ""
        score_dict = {0: "Love", 1: "Fifteen", 2: "Thirty", 3: "Forty"}
        if (self.is_tied() and self.player_1_points < 3):
            result = score_dict[self.player_1_points] + "-All"
        if (self.player_1_points==self.player_2_points and self.player_1_points>2):
            result = "Deuce"

        if (not self.is_tied() and self.is_below_deuce()):
            P1res = score_dict[self.player_1_points]
            P2res = score_dict[self.player_2_points]
            result = P1res + "-" + P2res
        
        if (self.player_1_points > self.player_2_points and self.player_2_points >= 3):
            result = "Advantage " + self.player_1_name
        
        if (self.player_2_points > self.player_1_points and self.player_1_points >= 3):
            result = "Advantage " + self.player_2_name
        
        if (self.player_1_points>=4 and self.player_2_points>=0 and (self.player_1_points - self.player_2_points)>=2):
            result = "Win for " + self.player_1_name
        if (self.player_2_points>=4 and self.player_1_points>=0 and (self.player_2_points - self.player_1_points)>=2):
            result = "Win for " + self.player_2_name
        return result
    

    def increment_player_1_score(self):
        self.player_1_points +=1

    def increment_player_2_score(self):
        self.player_2_points +=1
        
class TennisGame3:
    def __init__(self, player1Name, player2Name):
        self.p1N = player1Name
        self.p2N = player2Name
        self.p1 = 0
        self.p2 = 0
        
    def won_point(self, n):
        if n == self.p1N:
            self.p1 += 1
        else:
            self.p2 += 1
    
    def score(self):
        if (self.p1 < 4 and self.p2 < 4) and (self.p1 + self.p2 < 6):
            p = ["Love", "Fifteen", "Thirty", "Forty"]
            s = p[self.p1]
            return s + "-All" if (self.p1 == self.p2) else s + "-" + p[self.p2]
        else:
            if (self.p1 == self.p2):
                return "Deuce"
            s = self.p1N if self.p1 > self.p2 else self.p2N
            return "Advantage " + s if ((self.p1-self.p2)*(self.p1-self.p2) == 1) else "Win for " + s
