cdef tuple lerp(tuple a, tuple b, double t):
    cdef double x = (1 - t) * a[0] + t * b[0]
    cdef double y = (1 - t) * a[1] + t * b[1]
    cdef tuple r = (x, y)
    return r

cdef list spline(list positions, double seperate):
    cdef double increment = 1 / seperate
    cdef list points = []
    cdef double t = 0.0
    cdef list placehold = []
    cdef list new_positions = []
    while t <= 1+increment:
        placehold = positions.copy()
        while len(placehold) > 1:
            new_positions = [] # []
            for i in range(len(placehold)-1):
                new_positions.append(lerp(placehold[i], placehold[i+1], t))
            placehold = new_positions
        points.append(placehold[0])

        t += increment

    return points

cpdef list[tuple] spline_curve(list positions, double seperate):
    return spline(positions, seperate)

# cpdef void test_lerp(double x1, double y1, double x2, double y2, int times):
#     before = time.time()
#     for _ in range(times):
#         lerp(x1, y1, x2, y2, 0.3)
#     print(f'cython time: {time.time()-before}')