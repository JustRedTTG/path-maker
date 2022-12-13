from grid import Grid

wire_gauge = .5

def path_points(point_a: tuple[int, int], point_b: tuple[int, int], grid: Grid) -> list[tuple[int, int], ...]:
    x, y = point_a
    x_diff = (x-point_b[0])
    y_diff = (y-point_b[1])
    xp, yp = 0, 0 # the usage of separation

    path: list[tuple[int, int], ...] = [point_a]

    if abs(x_diff) < abs(y_diff):
        if y_diff < 0:
            while y < point_a[1] - y_diff * wire_gauge:
                y += grid.separation
                path.append((x, y))
            yp = 1
        else:
            while y > point_a[1] - y_diff * wire_gauge:
                y -= grid.separation
                path.append((x, y))
            yp = -1

        if x < point_b[0]:
            while x < point_a[0] - x_diff:
                x += grid.separation
                path.append((x, y))
            xp = 1
        else:
            while x > point_a[0] - x_diff:
                x -= grid.separation
                path.append((x, y))
            xp = -1
                
        if y_diff < 0:
            while y < point_a[1] - y_diff:
                y += grid.separation
                path.append((x, y))
        else:
            while y > point_a[1] - y_diff:
                y -= grid.separation
                path.append((x, y))
    else:
        if x_diff < 0:
            while x < point_a[0] - x_diff * wire_gauge:
                x += grid.separation
                path.append((x, y))
            xp = 1
        else:
            while x > point_a[0] - x_diff * wire_gauge:
                x -= grid.separation
                path.append((x, y))
            xp = -1

        if y < point_b[1]:
            while y < point_a[1] - y_diff:
                y += grid.separation
                path.append((x, y))
            yp = 1
        else:
            while y > point_a[1] - y_diff:
                y -= grid.separation
                path.append((x, y))
            yp = -1

        if x_diff < 0:
            while x < point_a[0] - x_diff:
                x += grid.separation
                path.append((x, y))
        else:
            while x > point_a[0] - x_diff:
                x -= grid.separation
                path.append((x, y))

    path.append(point_b)
    path = [(int(x), int(y)) for x, y in path]
    return path, xp, yp