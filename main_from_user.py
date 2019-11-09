from plotter import Plotter
import matplotlib.pyplot as plt
from main_from_file import ReadFile
from main_from_file import generate_coordinates
from main_from_file import locate_point

if __name__ == "__main__":
    shape_x = []
    shape_y = []
    point_coordinates = []
    location = [None] * 1
    point_x = float(input("Input an x coordinate: "))
    point_y = float(input("Input a y coordinate: "))
    point_coordinates = (point_x, point_y)
    print(point_coordinates)

    answer = input("Would you like to test the default polygon?: ")
    if answer == "yes":
        ReadFile.access_csv_file("polygon.csv", shape_x, shape_y)
        shape_coordinates = generate_coordinates(shape_x, shape_y)
    elif answer == "no":
        print('no')
    else:
        print("Please enter yes or no.")




    locate_point(point_x, point_y, shape_x, shape_y, point_coordinates, shape_coordinates, location)




    # Points plotted with locations
    plotter = Plotter()
    plotter.add_point(point_x, point_y, location[0])
    plotter.add_polygon(shape_x, shape_y)
    plt.xlabel("(x)")
    plt.ylabel("(y)")
    plt.title("what is the point?")
    plotter.show()

    print("The point you have selected was", str(point_coordinates), "This sits on the", (str(location)[1:-1]))
