from pygameextra.mouse import pos, clicked
from pygameextra.rect import Rect
from pygameextra.math import dist


def space_to_rect(x: int, y: int, width: int = 1, height: int = 1) -> Rect:
    width_half: float = width * .5
    height_half: float = height * .5
    return Rect(x-width_half, y-height_half, width, height)


class Point:
    x: int = 0
    y: int = 0
    separation: int = 1

    rect: Rect = None
    space: tuple[int, int] = None

    drag: dict

    def __init__(self, x: int = 0, y: int = 0, separation: int = 1):
        self.x = x
        self.y = y
        self.separation = separation
        self.drag = {
            'dragging' : False,
            'offset' : (0, 0),
        }

    def get_space(self) -> tuple[int, int]:
        return self.space or (
            self.x * self.separation,
            self.y * self.separation
        )

    def set_position(self, x: int, y: int) -> None:
        self.x = x
        self.y = y
        del self.rect
        del self.space
        self.rect = None
        self.space = None

    def compute(self) -> None:
        space = self.get_space()
        if self.drag['dragging']: self.handle_drag()
        if clicked()[0] and  \
        space_to_rect( *( position := pos() ) )  \
            .colliderect(
                self.rect or ( rect := space_to_rect(*space, 15, 15) )
        ):
            if not self.rect: self.rect = rect
            self.drag['offset'] = (
                space[0] - position[0],
                space[1] - position[1]
            )
            self.drag['dragging'] = True

    def handle_drag(self) -> None:
        position = pos()
        self.space = (
            position[0] + self.drag['offset'][0],
            position[1] + self.drag['offset'][1]
        )
        if not clicked()[0]:
            self.set_position(
                self.space[0] // self.separation,
                self.space[1] // self.separation
            )
            self.drag['dragging'] = False

    def find_nearest_space_node(self, *nodes) -> int:
        nearest = [9999, 0]
        for i, node in enumerate(nodes):
            if (distance := dist(self.get_space(), node)) < nearest[0]:
                nearest = [distance, i]
        return nearest[1]