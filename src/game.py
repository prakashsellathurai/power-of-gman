from dataclasses import dataclass
from src.navigation import Position2D, Direction


TURN_COST = 5
MOVE_COST = 10
INIT_POWER = 200


@dataclass
class Game:
    position: Position2D
    direction: Direction
    power: int

    @classmethod
    def initialize(cls, source_x, source_y, sourcedir):
        position = Position2D(source_x, source_y)
        direction = Direction(sourcedir)
        power = INIT_POWER
        return cls(position, direction, power)

    def move(self, destination_x, destination_y):
        destination = Position2D(destination_x, destination_y)
        cost = self.estimate_cost(destination)
        self.position = destination
        self.power -= cost

    def estimate_cost(self, target_position):
        moves = target_position.distance(self.position)
        move_cost = int(MOVE_COST * moves)

        turns = self.direction.estimate_turns(target_position, self.position)
        turn_cost = int(TURN_COST * turns)

        total_cost = move_cost + turn_cost
        return total_cost

    def print_power(self):
        print("POWER", self.power)
