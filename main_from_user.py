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


    answer = input("Would you like to test the default polygon? (yes/no): ")
    if answer == None:
        print("please answer the question (yes/no) ")
    if answer == "yes":
        ReadFile.access_csv_file("polygon.csv", shape_x, shape_y)
        shape_coordinates = generate_coordinates(shape_x, shape_y)
    elif answer == "no":
        ReadFile.access_csv_file(str(input("Ok, type in the csv path of your polygon: ")), shape_x, shape_y)
        shape_coordinates = generate_coordinates(shape_x, shape_y)
    else:
        print("Please enter yes or no.")

    point_x = float(input("Input an x coordinate: "))
    point_y = float(input("Input a y coordinate: "))
    point_coordinates = (point_x, point_y)



    locate_point(point_x, point_y, shape_x, shape_y, point_coordinates, shape_coordinates, location)

    print("The point you have selected was", str(point_coordinates), "This sits on the", (str(location)[1:-1]))



    # Points plotted with locations
    plotter = Plotter()
    plotter.add_point(point_x, point_y, location[0])
    plotter.add_polygon(shape_x, shape_y)
    plt.xlabel("(x)")
    plt.ylabel("(y)")
    plt.title("what is the point?")
    plotter.show()

