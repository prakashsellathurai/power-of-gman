from dataclasses import dataclass

from src.config import CONFIGURATION


class Position2D:
    def __init__(self, x: float, y: float):
        self.x = float(x)
        self.y = float(y)

    def __eq__(self, other):
        if isinstance(other, Position2D):
            return self.x == other.x and self.y == other.y
        return NotImplemented

    def __sub__(self, other):
        if isinstance(other, Position2D):
            diff_x = self.x - other.x
            diff_y = self.y - other.y
            return Position2D(diff_x, diff_y)

    @property
    def coords(self):
        return self.x, self.y

    def offset_to(self, other):
        offset = self - other
        dx, dy = offset.coords
        return dx, dy

    def __hash__(self):
        return hash((self.x, self.y))

    def dist_from(self, dest):
        dx, dy = self.offset_to(dest)
        return abs(dx) + abs(dy)


@dataclass
class Direction:
    id_string: str
    angle: float

    @classmethod
    def from_string(cls, id_string):
        angle = CONFIGURATION.QUADRANT_ANGLE[id_string]
        return cls(id_string=id_string, angle=angle)

    @classmethod
    def from_angle(cls, angle):
        id_string = list(CONFIGURATION.QUADRANT_ANGLE.keys())[
            list(CONFIGURATION.QUADRANT_ANGLE.values()).index(angle)
        ]
        return cls(id_string, angle)

    def rotate(self, target_angle):
        clock_rot = abs(target_angle - self.angle)
        anti_clock_rot = abs(CONFIGURATION.COMPLETE_ANGLE - (target_angle - self.angle))
        return min(clock_rot, anti_clock_rot) // CONFIGURATION.UNIT_ANGLE

    def estimate_angular_dist(self, source, dest):
        dx, dy = source.offset_to(dest)
        if dx == 0 and dy == 0:
            return 0

        if dx > 0 and dy > 0:
            target_angles = [
                CONFIGURATION.QUADRANT_ANGLE["E"],
                CONFIGURATION.QUADRANT_ANGLE["N"],
            ]
        elif dx < 0 and dy > 0:
            target_angles = [
                CONFIGURATION.QUADRANT_ANGLE["N"],
                CONFIGURATION.QUADRANT_ANGLE["W"],
            ]
        elif dx < 0 and dy < 0:
            target_angles = [
                CONFIGURATION.QUADRANT_ANGLE["W"],
                CONFIGURATION.QUADRANT_ANGLE["S"],
            ]
        elif dx > 0 and dy < 0:
            target_angles = [
                CONFIGURATION.QUADRANT_ANGLE["S"],
                CONFIGURATION.QUADRANT_ANGLE["E"],
            ]
        elif dx == 0 and dy > 0:
            target_angles = [CONFIGURATION.QUADRANT_ANGLE["N"]]
        elif dx > 0 and dy == 0:
            target_angles = [CONFIGURATION.QUADRANT_ANGLE["E"]]
        elif dx == 0 and dy < 0:
            target_angles = [CONFIGURATION.QUADRANT_ANGLE["S"]]
        elif dx < 0 and dy == 0:
            target_angles = [CONFIGURATION.QUADRANT_ANGLE["W"]]

        angular_rotations = (
            len(target_angles)
            - 1
            + min([self.rotate(target_angle) for target_angle in target_angles])
        )
        return angular_rotations
