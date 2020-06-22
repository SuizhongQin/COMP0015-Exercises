class Critter:
    # Constants for attacks, directions
    ATTACK_POUNCE = 0
    ATTACK_ROAR = 1
    ATTACK_SCRATCH = 2
    ATTACK_FORFEIT = 3
    DIRECTION_NORTH = 0
    DIRECTION_SOUTH = 1
    DIRECTION_EAST = 2
    DIRECTION_WEST = 3
    DIRECTION_CENTER = 4

    # There is no constructor in this class because there are no attributes
    def eat(self):
        return False

    def fight(self, opponent):
        return Critter.ATTACK_FORFEIT

    def colour(self):
        return "grey"

    def move(self):
        return Critter.DIRECTION_CENTER

    def __str__(self):
        return "I am a Critter."



        if self.getx() <= rect.getx() and self.gety() >= rect.gety():
            x = self.getx()
            y = self.gety()
            if self.get_width() >= rect.get_width() + (rect.getx() - self.getx()):
                w = self.get_width()
            else:
                w = self.get_width() + (rect.get_width() - (self.get_width() - (rect.getx() - self.getx())))
            if self.get_height() >= rect.get_height() + (self.gety() - rect.gety()):
                h = self.get_height()
            else:
                h = (self.gety() - rect.gety()) + rect.get_height()
        return Rectangle(x, y, w, h)