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



def minimum_bound(p_x, p_y, a_x, a_y):
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

def ray_casting(p, s):
    n = len(s)-1
    counter = 0
    for i in range(n):
        if (s[i][1] <= p[1] and s[i+1][1] > point[1]) or (s[i][1] > point[1] and s[i+1][1] <= p[1]):
            vt = (p[1] - s[i][1]) / (s[i+1][1] - s[i][1])
        if p[0] < (s[i][0] + vt * (s[i+1][0] - s[i][0])):
            counter += 1
        i += 1
    return counter


def compute_y(x, x1, y1, x2, y2):
    return (x - x1) / (x2 - x1) * (y2 - y1) + y1

def is_on_the_line(p_x, p_y, a_x, a_y, b_x, b_y):
    if not ((a_y <= p_y <= b_y or b_y <= p_y <= a_y) and (a_x <= p_x <= b_x or b_x <= p_x <= a_x)):
        return False
    elif a_x == b_x and p_x == a_x:
        return True
    elif a_x != b_x and compute_y(p_x, a_x, a_y, b_x, b_y) == p_y:
        return True
    else:
        return False

box = [(1,1),(1,5),(5,5),(5,1)]
point = [0,1]

if ray_casting(point, box) %2:
    print("inside")
else:
    print("outside")







class File_reader:

    def read_points(filename):
        with open(filename, 'r') as f:
            lines = f.readlines()[1:]
            for line in lines:
                line = line.strip().split(',')
                point_x.append(float(line[1]))
                point_y.append(float(line[2]))


    def read_polygon(filename):
        with open(filename, 'r') as f:
            lines = f.readlines()[1:]
            for line in lines:
                line = line.strip().split(',')
                shape_x.append(float(line[1]))  # values added to the empty point list.
                shape_y.append(float(line[2]))

#maybe try to put the merge function outside of create coordinates - then call it from within.


    def create_polygon_coordinates(filename):
         with open(filename, 'r') as f:
             lines = f.readlines()[1:]
             for line in lines:
                 line = line.strip().split(',')
                 shape_x.append(float(line[1]))
                 shape_y.append(float(line[2]))


    def create_point_coordinates(filename):
          with open(filename, 'r') as f:
              lines = f.readlines()[1:]
              for line in lines:
                  line = line.strip().split(',')
                  point_x.append(float(line[1]))  # values added to the empty shape list.
                  point_y.append(float(line[2]))
                  point_coordinates = [(point_x[i], point_y[i]) for i in range(0, len(point_x))]
                  return point_coordinates




if __name__ == "__main__":

    point_x = []
    point_y = []
    shape_x = []
    shape_y = []
    point_on_line = []
    polygon_coordinates = []
    point_coordinates = []
    out = []

    File_reader.read_polygon("polygon.csv")
    File_reader.read_points("input.csv")
    File_reader.create_polygon_coordinates("polygon.csv")
    File_reader.create_point_coordinates("input.csv")





    print(polygon_coordinates)

    # plotter = Plotter()
    # plotter.add_point()
    # plotter.add_polygon(shape_x, shape_y)
    # plotter.show()