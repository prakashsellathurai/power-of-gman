from enum import Enum
from collections import deque
from dataclasses import dataclass

from src.navigation import Position2D, Direction
from src.config import Config



class GManPlayer:
    def __init__(self, s_pos: Position2D, s_dir: Direction, power: int):
        self.pos = s_pos
        self.dir = s_dir
        self.power = power

    def move_to(self, new_pos: Position2D, cost: int):
        remaining_power = self.power - cost
        self.pos = new_pos
        self.power = remaining_power
        return self.__init__(self.pos, self.dir, self.power)

    @property
    def angle(self):
        return self.dir.angle

    def cost_to_reach(self, destination, unit_move_cost, unit_turn_cost):
        moves = destination.dist_from(self.pos)
        move_cost = unit_move_cost * moves

        turns = self.dir.estimate_angular_dist(destination, self.pos)
        turn_cost = unit_turn_cost * turns

        total_cost = move_cost + turn_cost
        return total_cost


class GManGame:
    def __init__(self):
        self.m = self.n = Config.GRID_SIZE

        self.unit_turn_cost = Config.TURN_COST
        self.unit_move_cost = Config.MOVE_COST
        self.init_power = Config.INIT_POWER

    def init_player(self, sX, sY, sdir):
        source = Position2D(sX, sY)
        player_dir = Direction.from_string(sdir)

        self.player = GManPlayer(source, player_dir, self.init_power)

    def move_player_to(self, dX, dY):
        destination = Position2D(dX, dY)

        total_cost = self.player.cost_to_reach(
            destination, self.unit_move_cost, self.unit_turn_cost
        )

        self.player.move_to(destination, total_cost)

    def calculate_power(self):
        return int(self.player.power)
