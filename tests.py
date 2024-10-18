from draw import line_to
assert line_to(0, 0, 4, 2) == [[0, 0], [1, 1], [2, 1], [3, 2]]
assert line_to(0, 2, 4, 0) == [[0, 1], [1, 1], [2, 0], [3, 0]]
assert line_to(4, 2, 0, 0) == [[4, 1], [3, 1], [2, 0], [1, 0]]
assert line_to(4, 0, 0, 2) == [[4, 0], [3, 1], [2, 1], [1, 2]]
