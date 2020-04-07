from plotter import Plotter
import matplotlib.pyplot as plt
from main_from_file import ReadFile
from main_from_file import locate_point

if __name__ == "__main__":

    shape_x = []
    shape_y = []
    point_coordinates = []
    category = [None] * 1  

    # Additional feature to ask user if they would like to use the default polygon, or another polygon.
    answer = input("Would you like to test the default polygon? (yes/no): ")
    if answer == None: 
        ReadFile.access_csv_file("polygon.csv", shape_x, shape_y)
        shape_coordinates = ReadFile.generate_coordinates("polygon.csv", shape_x, shape_y)
    # If yes is given, the default polygon is used    
    if answer == "yes":
        ReadFile.access_csv_file("polygon.csv", shape_x, shape_y)  
        shape_coordinates = ReadFile.generate_coordinates("polygon.csv", shape_x, shape_y)
    # if no is given, a path is requested from the user
    elif answer == "no":                                           
        x = ReadFile.access_csv_file(str(input("Ok, type in the csv path of your polygon: ")), shape_x, shape_y)
        shape_coordinates = ReadFile.generate_coordinates(x, shape_x, shape_y)
    else:
        print("Please enter yes or no.")  

    # Request user input for each x and y coordinate
    point_x = float(input("Input an x coordinate: "))
    point_y = float(input("Input a y coordinate: "))
    point_coordinates = (point_x, point_y)

    # Call the function to locate a single point
    locate_point(point_x, point_y, shape_x, shape_y, point_coordinates, shape_coordinates, category)

    # Prints a line of text with details of the input and the result
    print("The point you have selected was", str(point_coordinates), "This sits on the", (str(category)[1:-1]))

    # Points plotted with locations
    plotter = Plotter()
    plotter.add_point(point_x, point_y, category[0])
    plotter.add_polygon(shape_x, shape_y)
    plt.plot(shape_x, shape_y)
    plt.xlabel("x")
    plt.ylabel("y")
    plt.title("Point in Polygon Test")
    plotter.show()
