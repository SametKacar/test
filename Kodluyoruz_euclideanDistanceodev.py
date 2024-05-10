import math

points = [(3, 0), (0, 4)]

def euclidean_distance(x1, y1, x2, y2):

  return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

x1, y1 = points[0]
x2, y2 = points[1]

print(euclidean_distance(x1, y1, x2, y2))

