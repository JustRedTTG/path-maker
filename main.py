from grid import Grid
from point import Point
from path import path_points
from curve import spline_curve
import pygameextra as pe
pe.init()

grid = Grid(20, 20, 25)
points = [
    Point(1, 1, grid.separation),
    Point(4, 2, grid.separation)
]
pe.display.make(grid.size, 'path maker')
width, height = pe.display.get_size()

while True:
    [pe.event.quitCheckAuto() for pe.event.c in pe.event.get()]
    pe.fill.full(pe.colors.verydarkgray)

    # Draw the grid
    for i in range(grid.width):
        x = i * grid.separation
        pe.draw.line(pe.colors.darkgray, (x, 0), (x, height), 3)
        pe.draw.line(pe.colors.darkgray, (0, x), (width, x), 3)

    # Draw the path
    path_points_result: list[tuple[int, int], ...] = path_points(points[0].get_space(), points[1].get_space(), grid)
    pe.pygame.draw.lines(pe.display.display_reference.surface, pe.colors.green, False,
                         spline_curve(path_points_result, 40), 4)
    for path_point in path_points_result:
        pe.draw.circle(pe.colors.red, path_point, 4, 1)

    # Draw the points
    for point in points:
        point.compute()
        pe.draw.circle(pe.colors.white, point.get_space(), 3, 0)


    pe.display.update(60)