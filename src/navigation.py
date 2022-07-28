from enum import Enum

UNIT_ANGLE = 90
COMPLETE_ANGLE = 360

EAST_ANGLE = 0
WEST_ANGLE = 180
NORTH_ANGLE = 90
SOUTH_ANGLE = 270


class COORDINATE(Enum):
    EAST = EAST_ANGLE
    NORTH = NORTH_ANGLE
    WEST = WEST_ANGLE
    SOUTH = SOUTH_ANGLE

    @property
    def angle(self):
        return self.value


DIRECTION_SWITCH = {
    "E": COORDINATE.EAST,
    "N": COORDINATE.NORTH,
    "W": COORDINATE.WEST,
    "S": COORDINATE.SOUTH,
}

UP_RIGHT_PATH = [
    COORDINATE.EAST,
    COORDINATE.NORTH,
]

UP_LEFT_PATH = [
    COORDINATE.WEST,
    COORDINATE.NORTH,
]

DOWN_LEFT_PATH = [
    COORDINATE.WEST,
    COORDINATE.SOUTH,
]

DOWN_RIGHT_PATH = [
    COORDINATE.EAST,
    COORDINATE.SOUTH,
]


class Compass:
    @classmethod
    def get_angle(cls, direction_string):
        direction = DIRECTION_SWITCH[direction_string]
        return direction.angle

    @classmethod
    def get_directions(cls, dx: int, dy: int):
        if dx == 0 or dy == 0:
            directions = [cls.get_normal_direction(dx, dy)]
        else:
            directions = cls.get_Lshaped_directions(dx, dy)

        return directions

    @staticmethod
    def get_normal_direction(dx: int, dy: int):
        if dx == 0 and dy > 0:
            return COORDINATE.NORTH
        if dx > 0 and dy == 0:
            return COORDINATE.EAST
        if dx == 0 and dy < 0:
            return COORDINATE.SOUTH
        else:
            return COORDINATE.WEST

    @staticmethod
    def get_Lshaped_directions(dx: int, dy: int):
        if dx > 0 and dy > 0:
            return UP_RIGHT_PATH
        if dx < 0 and dy > 0:
            return UP_LEFT_PATH
        if dx < 0 and dy < 0:
            return DOWN_LEFT_PATH
        else:
            return DOWN_RIGHT_PATH


class Position2D:
    def __init__(self, x: float, y: float):
        self.x = float(x)
        self.y = float(y)

    @property
    def coordinates(self):
        return self.x, self.y

    def difference(self, other):
        diff_x = self.x - other.x
        diff_y = self.y - other.y
        return Position2D(diff_x, diff_y)

    def offset(self, other):
        offset = self.difference(other)
        dx, dy = offset.coordinates
        return dx, dy

    def distance(self, dest):
        dx, dy = self.offset(dest)
        return abs(dx) + abs(dy)


class Direction:
    def __init__(self, id_string: str):
        self.id_string = id_string
        self.angle = Compass.get_angle(id_string)

    def difference(self, target_direction):
        target_angle = target_direction.angle

        angle_difference = target_angle - self.angle

        left_difference = abs(angle_difference)
        right_difference = abs(COMPLETE_ANGLE - angle_difference)

        minimal_difference = min(left_difference, right_difference)

        return minimal_difference // UNIT_ANGLE

    def estimate_turns(self, source, dest):
        dx, dy = source.offset(dest)

        if dx == 0 and dy == 0:
            return 0

        directions = Compass.get_directions(dx, dy)

        min_turns = None
        n = len(directions)

        min_turns = COMPLETE_ANGLE
        for direction in directions:
            turns = self.difference(direction)
            if turns < min_turns:
                min_turns = turns

        additional_turns = n - 1

        total_turns = min_turns + additional_turns

        return total_turns
