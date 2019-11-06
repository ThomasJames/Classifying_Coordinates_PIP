from collections import OrderedDict
import matplotlib.pyplot as plt


class Plotter:

    def __init__(self):
        plt.figure()

    def add_polygon(self, xs, ys):
        plt.fill(xs, ys, 'lightgray', label='Polygon')

    def add_boarder(self, xs, ys):
        plt.plot(xs, ys, 'salmon', label='boarder')

    def add_point(self, x, y, kind=None):
        if kind == "outside":
            plt.plot(x, y, "ro", label='Outside')
        elif kind == "boundary":
            plt.plot(x, y, "bo", label='Boundary')
        elif kind == "inside":
            plt.plot(x, y, "go", label='Inside')
        else:
            plt.plot(x, y, "ko", label='Unclassified')

    def show(self):
        handles, labels = plt.gca().get_legend_handles_labels()
        by_label = OrderedDict(zip(labels, handles))
        plt.legend(by_label.values(), by_label.keys())
        plt.show()


def compute_y(x, x1, y1, x2, y2):  # The auguments for the equation for a point on a line.
    return (x - x1) / (x2 - x1) * (y2 - y1) + y1  # The auguments for a equation.


# Function to test parameters and return whether the point is on a line True / False
def is_on_the_line(p_x, p_y, a_x, a_y, b_x, b_y):
    if not ((a_y <= p_y <= b_y or b_y <= p_y <= a_y) and (a_x <= p_x <= b_x or b_x <= p_x <= a_x)):
        return False
    elif a_x == b_x and p_x == a_x:
        return True
    elif a_x != b_x and compute_y(p_x, a_x, a_y, b_x, b_y) == p_y:
        return True
    else:
        return False


# cn_PnPoly(): crossing number test for a point in a polygon
#      Input:   P = a point,
#               V[] = vertex points of a polygon V[n+1] with V[n]=V[0]
#      Return:  0 = outside, 1 = inside
# This code is patterned after [Franklin, 2000]
# Taken from: http://geomalgorithms.com/a03-_inclusion.html
def ray_casting_algorthim(point, polygon): # Tuples containing
  n = len(polygon)-1
  cn = 0    # the  crossing number counter

  # loop through all edges of the polygon
  i = 0
  # while i<n: # edge from V[i]  to V[i+1]
  for i in range(n):
    # upward crossing or downward crossing
    if (polygon[i][1] <= point[1] and polygon[i+1][1] > point[1]) or (polygon[i][1] > point[1] and V[i+1][1] <= point[1]):
      # compute  the actual edge-ray intersect x-coordinate
      vt = (point[1]  - polygon[i][1]) / (polygon[i+1][1] - polygon[i][1])
      # if P[0] > (V[i][0] + vt * (V[i+1][0] - V[i][0])): # P.x > intersect - ray toward left
      if point[0] < (polygon[i][0] + vt * (polygon[i+1][0] - polygon[i][0])): # P.x < intersect - ray toward right - original
        cn += 1   # a valid crossing of y=P[1] right of P.x

    i += 1


  #print str(cn)
  return (cn&1)    # 0 if even (out), and 1 if  odd (in)


# box = [(1,1),(1,2),(2,2),(2,1)]
# point_1 = (1.25, 1.95)
# point_2 = (1.5, 3)
#
# print(cn_PnPoly(point_1, box))












def is_point_outside_minimum_bound(p_x, p_y, a_x, a_y):
    if min(a_x) < p_x < max(a_x) and min(a_y) < p_y < max(a_y):  # is the point within the bounds of the box
        out.append("inside")
    elif min(a_x) == p_x and min(a_y) <= p_y <= max(a_y):  # is the point.x on the min x axis and within the y
        out.append("boundary")
    elif max(a_x) == p_x and min(a_y) <= p_y <= max(a_y):  # is the point.x on the max x axis and within the y
        out.append("boundary")
    elif min(a_y) == p_y and min(a_x) <= p_x <= max(a_x):  # is the point.y on the min y axis within the x
        out.append("boundary")
    elif max(a_y) == p_y and min(a_x) <= p_x <= max(a_x):  # is the point.y on the max y axis within the x
        out.append("boundary")
    else:
        out.append("outside")  # else the point cant be inside or on boundry, therefore its outside


# Class containing methods to read files
class File_reader:

    # Method to read the points from a csv file and create lists from the second and third col
    def read_points(filename):
        with open(filename, 'r') as f:
            lines = f.readlines()[1:]
            for line in lines:
                line = line.strip().split(',')
                point_x.append(float(line[1]))  # values added to the empty shape list.
                point_y.append(float(line[2]))

                # Method to read the points from a csv file and create lists from the

    def read_polygon(filename):
        with open(filename, 'r') as f:
            lines = f.readlines()[1:]
            for line in lines:
                line = line.strip().split(',')
                shape_x.append(float(line[1]))  # values added to the empty point list.
                shape_y.append(float(line[2]))




if __name__ == "__main__":

    point_x = []
    point_y = []
    shape_x = []
    shape_y = []
    point_on_line = []
    polygon_coordinates = []
    point_coordinates = []

    File_reader.read_polygon("polygon.csv")
    File_reader.read_points("input.csv")

    def create_polygon_coordinates(shape, point_y):

        polygon_coordinates = [(shape_x[i], shape_y[i]) for i in range(0, len(shape_y))]
        return polygon_coordinates

    def create_point_coordinates(point_x, point_y):

        point_coordinates = [(point_x[i], point_y[i]) for i in range(0, len(point_x))]
        return point_coordinates

    print(create_point_coordinates(point_x, point_y))
    print(create_polygon_coordinates(shape_x,shape_y))
    
    point = [(1.0, 5.5), (-1.0, 0.5), (2.5, 3.5), (1.5, 5.5), (0.5, 5.5), (2.5, 0.0), (0.5, 1.0), (3.5, 0.0), (4.0, 7.5), (-1.0, 5.5), (2.5, 6.0), (-0.5, 4.5), (2.0, 4.0), (1.5, 2.0), (0.0, 3.5), (3.0, 1.5), (1.0, -1.0), (3.0, 0.5), (3.0, -1.0), (5.0, 1.0), (4.0, 2.5), (4.0, 2.0), (2.5, 2.0), (3.0, 2.0), (5.0, 6.0), (3.5, 2.5), (-0.5, 6.5), (0.0, 1.0), (4.0, 6.5), (-1.0, 1.5), (0.0, 6.0), (3.5, 5.0), (1.5, -1.0), (-0.5, 0.0), (0.0, 2.0), (0.0, 4.0), (-0.5, 1.5), (0.5, 5.0), (2.0, 8.0), (1.5, 2.5), (2.0, 4.5), (0.5, 8.0), (4.5, -1.0), (3.0, 3.5), (5.0, 0.5), (-0.5, 3.0), (-0.5, -0.5), (4.0, 0.0), (4.5, 2.5), (4.5, 5.5), (5.0, 4.0), (4.0, 8.0), (2.5, 3.0), (2.0, 7.5), (5.0, 7.5), (1.5, 0.0), (1.0, 7.5), (0.0, 0.5), (2.0, 0.5), (0.0, 5.0), (5.0, 5.5), (1.5, 4.0), (3.5, -0.5), (-0.5, 2.0), (5.0, 6.5), (1.5, 1.5), (4.0, 0.5), (1.5, 5.0), (2.5, 8.0), (0.0, -1.0), (2.5, -0.5), (4.0, 4.0), (0.0, 0.0), (-1.0, 2.0), (3.0, 8.0), (2.0, 6.5), (1.0, 0.0), (-1.0, 7.0), (1.5, 6.0), (4.0, 6.0), (4.5, 7.5), (0.0, 7.5), (4.5, 0.0), (2.5, -1.0), (3.5, 4.0), (0.0, 4.5), (1.0, 8.0), (1.5, 3.5), (3.5, 2.0), (4.0, 1.0), (5.0, 1.5), (1.0, 4.5), (2.5, 6.5), (-1.0, 6.0), (2.0, 1.0), (3.0, 1.0), (5.0, 4.5), (4.0, 5.5), (-1.0, -1.0), (1.5, 4.5)]
    polygon = [(0.0, 1.0), (0.0, 6.0), (1.0, 7.0), (3.0, 7.0), (4.0, 6.0), (4.0, 4.0), (3.0, 4.0), (3.0, 5.0), (2.0, 6.0), (1.0, 5.0), (1.0, 2.0), (2.0, 1.0), (3.0, 2.0), (2.0, 2.0), (2.0, 3.0), (4.0, 3.0), (4.0, 1.0), (3.0, 0.0), (1.0, 0.0), (0.0, 1.0)]
    



    print(cn_PnPoly(point[6], polygon))



    # plotter = Plotter()
    # plotter.add_point(point_x[14], point_y[14], is_point_on_line(14))
    # plotter.add_polygon(shape_x, shape_y)
    # plotter.show()