from critter import Critter
import random


class Quoll(Critter):
    DAY = 0
    NIGHT = 1

    # constructor body
    def __init__(self):
        self._eaten = 0
        self._steps = 0
        self._direction = 0
        self._trip_length = random.randint(1, 2) * 10

    def eat(self):
        if self.get_time_of_day() == 1:
            self._eaten += 1
            return True
        else:
            return False

    def get_time_of_day(self):
        return random.randint(0, 1)

    def move(self):
        self._steps += random.randint(1, 2) * 10
        if self._direction == 0:
            self._trip_length = random.randint(1, 2) * 10
        self._direction = (self._direction - 1 + 4) % 4

    def __str__(self):
        return 'I am a Critter. Type: Quoll, eaten: %d, current direction: %d, trip length: %d, steps: %d' % \
               (self._eaten, self._direction, self._trip_length, self._steps)


# test part
if __name__ == '__main__':
    q = Quoll()
    print(q)
    q.move()
    q.eat()
    print(q)
    q.move()
    q.eat()
    print(q)
    q.move()
    print(q)
    q.move()
    print(q)
    q.move()
    print(q)
