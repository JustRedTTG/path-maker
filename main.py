from grid import Grid
from point import Point
from path import path_points
from curve import spline_curve
import pygameextra as pe
from pygameextra.fpslogger import Logger
pe.init()

grid = Grid(20, 20, 25)
fps = Logger()
points = [
    Point(1, 1, grid.separation),
    Point(8, 7, grid.separation),
    Point(6, 7, grid.separation),
]
pe.display.make(grid.size, 'path maker')
width, height = pe.display.get_size()
dragging = False
backup_lines = None

while True:
    [pe.event.quitCheckAuto() for pe.event.c in pe.event.get()]
    pe.fill.full(pe.colors.verydarkgray)

    # Draw the grid
    for i in range(grid.width):
        x = i * grid.separation
        pe.draw.line(pe.colors.darkgray, (x, 0), (x, height), 3)
        pe.draw.line(pe.colors.darkgray, (0, x), (width, x), 3)

    # Draw the path
    if backup_lines:
        pe.pygame.draw.lines(pe.display.display_reference.surface, pe.colors.pink, False, backup_lines, 4)
    else:
        path_points_result, xp, yp = path_points(points[0].get_space(), points[1].get_space(), grid)
        pe.pygame.draw.lines(pe.display.display_reference.surface, pe.colors.green, False,
                             backup_lines := spline_curve(path_points_result, 20 if dragging else 500), 4)
        for path_point in path_points_result:
            pe.draw.circle(pe.colors.red, path_point, 4, 1)

    if dragging:
        del backup_lines
        backup_lines = None

    # Third point
    point_index = points[2].find_nearest_space_node(*path_points_result)
    temp, _, _ = path_points(path_points_result[point_index], points[2].get_space(), grid)
    temp = [v if v != path_points_result[-1] and v != path_points_result[0] else (
        v[0] + xp * grid.separation * 3,
        v[1] + yp * grid.separation * 3
    ) for v in temp]
    pe.pygame.draw.lines(pe.display.display_reference.surface, pe.colors.pink, False,
                         spline_curve([
                             *path_points_result[0:point_index],
                             *temp,
                             points[2].get_space()
                         ], 500), 4)
    if dragging:
        for pp in [*path_points_result[0:point_index], *temp, points[2].get_space()]:
            if pp in temp:
                pe.draw.circle(pe.colors.aqua, pp, 4, 4)
            else:
                pe.draw.circle(pe.colors.darkaqua, pp, 4, 2)

    dragging_off = 0
    # Draw the points
    for point in points:
        point.compute()
        dragging = dragging or point.drag['dragging']
        dragging_off += 1 if point.drag['dragging'] else 0
        if point.drag['dragging']:
            pe.draw.circle(pe.colors.white, point.get_space(), 3, 0)
        else:
            pe.draw.circle((255, 255, 255, 100), point.get_space(), 3, 0)
    if dragging_off == 0: dragging = False

    fps.render()
    pe.display.update()