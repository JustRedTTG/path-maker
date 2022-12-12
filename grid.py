class Grid:
    width: int
    height: int
    separation: int
    size: tuple[int, int]

    def __init__(self, width: int, height: int, separation: int):
        self.width = width
        self.height = height
        self.separation = separation
        self.size = self.get_size()

    def get_size(self) -> tuple[int, int]:
        return (
            (self.width - 1) * self.separation,
            (self.height - 1) * self.separation
        )

    def get_point(self, x: int, y: int) -> tuple[int, int]:
        return (
            x * self.separation,
            y * self.separation
        )
