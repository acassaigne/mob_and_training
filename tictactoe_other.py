class Position:

    def __init__(self, row, column):
        self.row = row
        self.column = column


class PositionAlreadyTaken(Exception):
    pass


class InvalidPosition(Exception):
    pass


class Mark:
    def __eq__(self, other):
        return type(self) == type(other)


class MarkEmpty(Mark):
    pass


class MarkX(Mark):
    pass


class MarkO(Mark):
    pass


class Player:
    def __eq__(self, other):
        return type(self) == type(other)


class PlayerO(Player):
    pass


class PlayerX(Player):
    pass

class Nobody(Player):
    pass

class Draw(Player):
    pass

