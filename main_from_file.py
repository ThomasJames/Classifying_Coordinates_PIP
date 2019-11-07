from plotter import Plotter
import matplotlib.pyplot as plt

# Function to define minimum and maximum bounds of the polygon, and provide an output that states the location of the point.
# 
def minimum_bound(p_x, p_y, a_x, a_y):
    if min(a_x) < p_x < max(a_x) and min(a_y) < p_y < max(a_y):  # is the point within the bounds of the box
        return True
    elif min(a_x) == p_x and min(a_y) <= p_y <= max(a_y):
        return 1
    elif max(a_x) == p_x and min(a_y) <= p_y <= max(a_y):
        return 1
    elif min(a_y) == p_y and min(a_x) <= p_x <= max(a_x):
        return 1
    elif max(a_y) == p_y and min(a_x) <= p_x <= max(a_x):
        return True
    else:
        return False


def ray_casting(pt, sh):
    n = len(sh) - 1
    counter = 0
    for i in range(n):
        if (sh[i][1] <= pt[1] < sh[i + 1][1]) or (sh[i][1] > pt[1] >= sh[i + 1][1]):
            vt = (pt[1] - sh[i][1]) / (sh[i + 1][1] - sh[i][1])
            if pt[0] < (sh[i][0] + vt * (sh[i + 1][0] - sh[i][0])):
                counter += 1
        i += 1
    return counter


def compute_y(x, x1, y1, x2, y2):
    return (x - x1) / (x2 - x1) * (y2 - y1) + y1


def is_on_line(p_x, p_y, a_x, a_y, b_x, b_y):
    if not ((a_y <= p_y <= b_y or b_y <= p_y <= a_y) and (a_x <= p_x <= b_x or b_x <= p_x <= a_x)):
        return False
    elif a_x == b_x and p_x == a_x:
        return True
    elif a_x != b_x and compute_y(p_x, a_x, a_y, b_x, b_y) == p_y:
        return True
    else:
        return False


class ReadFile:

    def __init__(self, filename):
        self.filename = filename

    def create_points(self):
        with open(self, 'r') as f:
            lines = f.readlines()[1:]
            for line in lines:
                line = line.strip().split(',')
                point_x.append(float(line[1]))
                point_y.append(float(line[2]))

    def create_polygon(self):
        with open(self, 'r') as f:
            lines = f.readlines()[1:]
            for line in lines:
                line = line.strip().split(',')
                shape_x.append(float(line[1]))
                shape_y.append(float(line[2]))


def generate_coordinates(p_x, p_y):
    return list(map(lambda x, y: (x, y), p_x, p_y))


def locate_points(p_x, p_y, s_x, s_y, s, p):
    for i in range(len(location)):
        if not minimum_bound(p_x[i], p_y[i], s_x, s_y):
            location[i] = "outside"
        elif (ray_casting(p[i], s)) % 2 != 0:
            location[i] = "inside"
        else:
            location[i] = "outside"
        for j in range(len(s_x) - 1):
            if is_on_line(p_x[i], p_y[i], s_x[j], s_y[j], s_x[j + 1], s_y[j + 1]):
                location[i] = "boundary"


if __name__ == "__main__":

    point_x = []
    point_y = []
    shape_x = []
    shape_y = []

    ReadFile.create_polygon("polygon.csv")
    ReadFile.create_points("input.csv")

    s = []
    p = []
    location = [None] * len(point_x)

    p = generate_coordinates(point_x, point_y)
    s = generate_coordinates(shape_x, shape_y)

    locate_points(point_x, point_y, shape_x, shape_y, s, p)

    # Write the output to a csv file called mbr_output
    output_file = open("output.csv", "w")
    for i in location:
        output_file.write(i + "\n")

    plotter = Plotter()
    for i in range(len(point_x)):
        plotter.add_point(point_x[i], point_y[i], location[i])
    plotter.add_polygon(shape_x, shape_y)
    plt.xlabel("x axis")
    plt.ylabel("y axis")
    plotter.show()
