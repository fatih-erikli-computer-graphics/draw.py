def line_to(x1, y1, x2, y2):
  dx = max(x1, x2) - min(x1, x2)
  dy = max(y1, y2) - min(y1, y2)
  pixels = []
  if dx > dy:
    if x1 < x2:
      if y1 < y2:
        y = y1
        for x in range(x1, x2):
          y = y + dy / dx
          pixels.append([x, int(y)])
      else:
        y = y1
        for x in range(x1, x2):
          y = y - dy / dx
          pixels.append([x, int(y)])
    else:
      if y1 < y2:
        y = y1
        for x in range(x1, x2, -1):
          y = y + dy / dx
          pixels.append([x, int(y)])
      else:
        y = y1
        for x in range(x1, x2, -1):
          y = y - dy / dx
          pixels.append([x, int(y)])
  else:
    if y1 < y2:
      if x1 < x2:
        x = x1
        for y in range(y1, y2):
          x = x + dx / dy
          pixels.append([int(x), y])
      else:
        x = x1
        for y in range(y1, y2):
          x = x - dx / dy
          pixels.append([int(x), y])
    else:
      if x1 < x2:
        x = x1
        for y in range(y1, y2, -1):
          x = x + dx / dy
          pixels.append([int(x), y])
      else:
        x = x1
        for y in range(y1, y2, -1):
          x = x - dx / dy
          pixels.append([int(x), y])
  return pixels

def fill_stroke(points):
  min_x = None
  max_x = None
  pixels = []
  for x, y in points:
    if min_x is None or x < min_x:
      min_x = x
    if max_x is None or x > max_x:
      max_x = x
  for x in range(min_x, max_x+1):
    min_y = None
    max_y = None
    for xx, yy in points:
      if x == xx:
        if min_y is None or yy < min_y:
          min_y = yy
        if max_y is None or yy > max_y:
          max_y = yy
    for x, y in line_to(x, min_y-1, x, max_y+1):
      pixels.append([x, y])
  return pixels
