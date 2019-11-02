from collections import OrderedDict
import matplotlib.pyplot as plt

class Plotter:

    def __init__(self):
        plt.figure()

    def add_polygon(self, xs, ys):
        plt.fill(xs, ys, 'lightgray', label='Polygon')

    def add_boarder(self, xs, ys):
        plt.plot(xs, ys, 'salmon', label = 'boarder')

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

# Create a function that takes a CSV file and creates a list of points.
# This may be reused also to read the list of testing points.
if __name__ == "__main__":

    #Empty lists for coordinates of points and polygons to go into
    coordinatex = []
    coordinatey = []
    shapex = []
    shapey = []
    coordinates = []
    xinside = []
    sample_output =[]
    boundbox_output = []

    #Class containing a selection of methods

    class File_reader:

        #Method to read coordinates
        def read_points(filename):
            with open(filename, 'r') as f:
                lines = f.readlines()[1:]
                for line in lines:
                    line = line.strip().split(',')
                    coordinatex.append(float(line[1]))
                    coordinatey.append(float(line[2]))

        def read_polygon(filename):
            with open(filename, 'r') as f:
                lines = f.readlines()[1:]
                for line in lines:
                    line = line.strip().split(',')
                    shapex.append(float(line[1]))
                    shapey.append(float(line[2]))

        def create_coordinates(filename):
            with open(filename, 'r') as f:
                lines = f.readlines()[1:]
                for line in lines:
                    line = line.strip().split(',')
                    coordinates.append(line[1:3])

        def read_sample_output(filename):
            with open(filename, 'r') as f:
               lines = f.readlines()[1:]
            for line in lines:
                line = line.strip().split(',')
                sample_output.append(str(line[1]))

    # Read the files
    File_reader.read_points("input.csv")
    File_reader.read_polygon("polygon.csv")
    File_reader.create_coordinates("input.csv")
    File_reader.read_sample_output("sample_output.csv")


    # Convert strings to floats
    coordinates = [[float(float(j)) for j in i] for i in coordinates]



    # values to define a minimum and maximum to draw the boundry box in plotter .
    boundboxx = [0, 0, 4, 4, 0]
    boundboxy = [0, 7, 7, 0, 0]

    # Values to define the min/max boundries of the maximum boundry box
    x_min = 0
    x_max = 4
    y_min = 0
    y_max = 7


    # def point_location_generator:
    for i in range(len(coordinates)):
        if x_min < (coordinatex[i]) < x_max and y_min < (coordinatey[i]) < y_max:
            boundbox_output.append("inside")
        elif x_min == coordinatex[i] and y_min < coordinatey[i] < y_max:
            boundbox_output.append("boundary")
        elif x_max == coordinatex[i] and y_min < coordinatey[i] < y_max:
            boundbox_output.append("boundary")
        elif y_min == coordinatey[i] and x_min < coordinatex[i] < x_max:
            boundbox_output.append("boundary")
        elif y_max == coordinatey[i] and x_min < coordinatex[i] < x_max:
            boundbox_output.append("boundary")
        else:
            boundbox_output.append("outside")

    # Create a list from 1 - 100, that can be used for indexing of the
    count = 1
    id = []
    idstring = []
    while (count < 101):
        id.append(count)
        count = count + 1

    # Write the
    output_file = open("mbr_output.csv", "w")
    for i in boundbox_output:
        output_file.write(i + "\n")



    # # Plots visualised through the matplotlib module
    # plotter = Plotter()
    # plotter.add_point(coordinatex[1:100], coordinatey[1:100], boundbox_output[1:100])
    # plotter.add_point(coordinatex[2], coordinatey[2], boundbox_output[2])
    # plotter.add_point(coordinatex[89], coordinatey[89], boundbox_output[89])
    # plotter.add_point(coordinatex[73], coordinatey[73], boundbox_output[73])
    # plotter.add_boarder(boundboxx, boundboxy)
    # plotter.add_polygon(shapex, shapey)
    # plotter.show()

    # SET counting to 0
    counting = 0

    # Check to see if point lies each side of polygon:

    # polygon_boarder = []
    # # for i in range(len(coordinates)):
    # #     if shapex[i] == (coordinatex[i]):
    # #         polygon_boarder.append("boundary")
    # #     else:
    # #         break
    # print(polygon_boarder)

    import math
    point_on_line = []
    # Does the point cross the line parallel to the x axis?
    for i in range(len(coordinates)):
        if coordinatex[i] == 0 and 1 > coordinatey[i] < 6:
            point_on_line.append("boundary")
        elif coordinatex[i] == 1 and 2 > coordinatey[i] < 5:
            point_on_line.append("boundary")
        elif coordinatex[i] == 2 and 2 > coordinatey[i] < 3:
            point_on_line.append("boundary")
        elif coordinatex[i] == 3 and 4 > coordinatey[i] < 5:
            point_on_line.append("boundary")
        elif coordinatex[i] == 4 and 1 > coordinatey[i] < 3:
            point_on_line.append("boundary")
        elif coordinatex[i] == 4 and 4 > coordinatey[i] < 6:
            point_on_line.append("boundary")
        elif coordinatey[i] == 0 and 1 > coordinatex[i] < 3:
            point_on_line.append("boundary")
        elif coordinatey[i] == 2 and 2 > coordinatex[i] < 3:
            point_on_line.append("boundary")
        elif coordinatey[i] == 3 and 2 > coordinatex[i] < 4:
            point_on_line.append("boundary")
        elif coordinatey[i] == 4 and 3 > coordinatex[i] < 4:
            point_on_line.append("boundary")
        elif coordinatey[i] == 7 and 1 > coordinatex[i] < 3:
            point_on_line.append("boundary")
        elif coordinatey[i] == (coordinatex[i]/-1)*(1-0):
            point_on_line.append("boundary")
        print(point_on_line)



















    # Algorithm to check whether a point crosses any line.
    #     IF ray crosses the line then its outside the polygon:





    #         THEN INC counting by 1
    # if counting %2 == 0:
    #     print ("outside")
    # else:
    #     print ("inside")

