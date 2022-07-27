from enum import Enum
from collections import deque
from dataclasses import dataclass

from src.navigation import Position2D, Direction
from src.config import CONFIGURATION


class Gman:
    def __init__(self, position: Position2D, direction: Direction, power: int):
        self.position = position
        self.direction = direction
        self.power = power

    @classmethod
    def init(self, sourceX, sourceY, sourcedir):
        position = Position2D(sourceX, sourceY)
        direction = Direction.from_string(sourcedir)
        power = CONFIGURATION.INIT_POWER
        return self(position, direction, power)

    def move(self, destinationX, destinationY):
        destination = Position2D(destinationX, destinationY)
        cost = self.estimate_cost(destination)
        self.position = destination
        self.power -= cost

    def estimate_cost(self, target_position):
        moves = target_position.dist_from(self.position)
        move_cost = int(CONFIGURATION.MOVE_COST * moves)

        turns = self.direction.estimate_angular_dist(target_position, self.position)
        turn_cost = int(CONFIGURATION.TURN_COST * turns)

        total_cost = move_cost + turn_cost
        return total_cost

    def print_power(self):
        print("POWER", self.power)
