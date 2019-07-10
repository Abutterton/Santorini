
class Action():
    def __init__(self, player, start, to, build):
        self.player = player
        self.start = start
        self.to = to
        self.build = build

    def __str__(self):
        return (str(self.start) + str(self.to) +str(self.build))

    def __repr__(self):
        return str(self)

    def __eq__(self, other):
        return self.__class__ == other.__class__ and self.start == other.start and self.to == other.to and self.player == other.player and self.build == other.build

    def __hash__(self):
        return hash((self.start, self.to, self.build, self.player))