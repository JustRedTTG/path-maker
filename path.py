from grid import Grid

wire_gauge = .5

def path_points(point_a: tuple[int, int], point_b: tuple[int, int], grid: Grid) -> list[tuple[int, int], ...]:
    x, y = point_a
    x_diff = (x-point_b[0])
    y_diff = (y-point_b[1])

    path: list[tuple[int, int], ...] = [point_a]

    if abs(x_diff) < abs(y_diff):
        if x < point_b[0]:
            if y_diff < 0:
                while y < point_a[1] - y_diff * wire_gauge:
                    y += grid.separation
                    path.append((x, y))
                while x < point_a[0] - x_diff:
                    x += grid.separation
                    path.append((x, y))
                while y < point_a[1] - y_diff:
                    y += grid.separation
                    path.append((x, y))
            else:

                while y > point_a[1] - y_diff * wire_gauge:
                    y -= grid.separation
                    path.append((x, y))
                while x < point_a[0] - x_diff:
                    x += grid.separation
                    path.append((x, y))
                while y > point_a[1] - y_diff:
                    y -= grid.separation
                    path.append((x, y))
        if x > point_b[0]:
            if y_diff < 0:
                while y < point_a[1] - y_diff * wire_gauge:
                    y += grid.separation
                    path.append((x, y))
                while x > point_a[0] - x_diff:
                    x -= grid.separation
                    path.append((x, y))
                while y < point_a[1] - y_diff:
                    y += grid.separation
                    path.append((x, y))
            else:

                while y > point_a[1] - y_diff * wire_gauge:
                    y -= grid.separation
                    path.append((x, y))
                while x > point_a[0] - x_diff:
                    x -= grid.separation
                    path.append((x, y))
                while y > point_a[1] - y_diff:
                    y -= grid.separation
                    path.append((x, y))
    else:
        print('horizontal')

    path.append(point_b)
    path = [(int(x), int(y)) for x, y in path]
    return path