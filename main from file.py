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

    # work out a way to input the values of max and min to a method - To give a bounding of ay box
    # def point_location_generator:
    class plotdecider:
        def minimumbound(x_min, x_max, y_min, y_max):
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

    plotdecider.minimumbound(0, 4, 0, 7)


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

    # list = []
    # def polyboardercheck2(b):
    #     for i in range(19):
    #         if shapey[i] <= coordinatey[b] <= shapey[i+1]:
    #             if coordinatex[b] == shapex[i] or coordinatex[b] == shapex[i+1]:
    #                 list.append("boundary")
    #                 break
    #         elif shapex[i] <= coordinatex[b] <= shapex[i+1]:
    #             if coordinatey[b] == shapey[i] or coordinatey[b] == shapey[i+1]:
    #                 list.append("boundary")
    #                 break
    #         else:
    #             list.append("unclassified")
    #             break
    #
    # for n in range(len(coordinatex)):
    #     polyboardercheck2(n)
    #
    # print(list)


 # Plots visualised through the matplotlib module
    plotter = Plotter()
    plotter.add_point(coordinatex[59], coordinatey[59], boundbox_output[59])
    plotter.add_point(coordinatex[55], coordinatey[55], boundbox_output[55])
    plotter.add_point(coordinatex[91], coordinatey[91], boundbox_output[91])
    plotter.add_point(coordinatex[52], coordinatey[52], boundbox_output[52])
    plotter.add_point(coordinatex[5], coordinatey[5], boundbox_output[5])
    plotter.add_point(coordinatex[6], coordinatey[6], boundbox_output[6])
    plotter.add_point(coordinatex[7], coordinatey[7], boundbox_output[7])
    plotter.add_point(coordinatex[8], coordinatey[8], boundbox_output[8])
    plotter.add_point(coordinatex[34], coordinatey[34], boundbox_output[34])
    plotter.add_point(coordinatex[15], coordinatey[15], boundbox_output[15])
    plotter.add_point(coordinatex[28], coordinatey[28], boundbox_output[28])
    plotter.add_point(coordinatex[14], coordinatey[14], boundbox_output[14])
    plotter.add_point(coordinatex[85], coordinatey[85], boundbox_output[85])
    plotter.add_point(coordinatex[97], coordinatey[97], boundbox_output[97])
    plotter.add_point(coordinatex[30], coordinatey[30], boundbox_output[30])
    plotter.add_point(coordinatex[27], coordinatey[27], boundbox_output[27])

    plotter.add_boarder(boundboxx, boundboxy)
    plotter.add_polygon(shapex, shapey)
    plotter.show()

    # import math
    list = []
    # Identify boundry points on the north direction
    # def parallel_to_x_north(a):
    #     for i in range(19):
    #         if coordinatex[a] == shapex[i]:
    #             if shapey[i+1] > shapey[i] and shapey[i+1] > coordinatey[a] > shapey[i]:
    #                 list.append("boundary")
    #                 break
    #             else:
    #                 continue
    #
    # def parallel_to_x_south(a):
    #     for i in range(19):
    #         if coordinatex[a] == shapex[i]:
    #             if shapey[i] > shapey[i+1] and shapey[i] > coordinatey[a] > shapey[i+1]:
    #                 list.append("boundary")
    #                 break
    #             else:
    #                 continue
    #
    # def parallel_to_y_east(a):
    #     for i in range(19):
    #         if coordinatey[a] == shapey[i]:
    #             if shapex[i+1] > shapex[i] and shapex[i] < coordinatex[a] < shapex[i+1]:
    #                 list.append("boundary")
    #                 break
    #             else:
    #                 continue
    #
    # def parallel_to_y_west(a):
    #     for i in range(19):
    #         if coordinatey[a] == shapey[i]:
    #             if shapex[i+1] < shapex[i] and shapex[i] > coordinatex[a] > shapex[i+1]:
    #                 list.append("boundary")
    #                 break
    #             else:
    #                 continue
        # for i in range(99):
        #     # parallel_to_x_north(i)
        #     # parallel_to_x_south(i)
        #     # parallel_to_y_east(i)
        #     # parallel_to_y_west(i)
        #     # nonparalellline(i)
        #
        #
        # print(list)                               #


    #
    # def nonparalellline(a):
    #     for i in range(19):
    #         if (shapex[i+1] - shapex[i]) > 0:
    #             if coordinatey[a] == (coordinatex[a] - shapex[i]) / (shapex[i+1] - shapex[i]) * (shapey[i+1] - shapey[i]) + shapey[i]:
    #                 list.append('boundary')
    #             elif (shapey[i+1] - shapey[i]) > 0:
    #                 if coordinatex[a] == (coordinatey[a] - shapey[i]) / (shapey[i+1] - shapey[i]) * (shapex[i+1] - shapex[i]) + shapex[i]:
    #                     list.append('boundary')
    #             else:
    #                 continue
    #
    # nonparalellline()
    # print(list)

















