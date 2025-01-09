# CAR-SELECTION-TOOL

INTRODUCTION

The car selection tool is a comprehensive and user-friendly application designed to help users find their ideal car based on specific preferences. By inputting criteria such as budget, car segment, fuel type, and desired features, users can filter through a detailed dataset of cars to match their needs. The tool displays the filtered results in the terminal, providing extensive information about each car. Additionally, it offers an interactive scatter plot visualization, allowing users to select criteria such as horsepower, torque, top speed, or mileage to compare against price. Clicking on points in the scatter plot reveals the car names and details, making it easy for users to explore and select the best options. This tool combines powerful data filtering with interactive visualization, enhancing the car selection process for users. 

Purpose:
•	The car selection tool aims to help users filter, select, and visualize cars based on their preferences. The tool provides both terminal output and interactive scatter plots, offering a comprehensive way to explore car options.

Key Features:
1.	User Input Interface:
o	Users can specify their preferences, including minimum and maximum budget, preferred car segment (Exotic, Luxury, Mid-Range, Common), preferred fuel type (Petrol, Diesel, Hybrid), and required features (e.g., sunroof, automatic transmission).
o	Users have the flexibility to leave any field blank if they don't have specific preferences, allowing the tool to consider a wider range of options.
2.	Filtering and Matching:
o	The tool filters the car data based on the user-provided preferences. It ensures that only the cars meeting the specified criteria are considered.
o	The filtered data includes detailed information about each matching car, such as brand, model, price, fuel type, features, safety rating, horsepower, torque, RPM, top speed, and mileage.
3.	Displaying Results:
o	The tool displays the list of matching cars along with their details in the terminal. Users can view comprehensive information about each car, making it easier to compare options.
4.	Interactive Scatter Plot Visualization:
o	Users can select a specific attribute (e.g., horsepower, torque, top speed, mileage) to create a scatter plot showing the relationship between price and the chosen attribute.
o	The scatter plot uses color gradients to represent the values of the selected attribute, providing a clear visual representation of the data.
5.	Click-to-Show Car Details:
o	The scatter plot is interactive, allowing users to click on any point (representing a car) to display the car's name in a black annotation box.
o	Clicking on a point also prints the full details of the selected car in the terminal, providing an in-depth view of its specifications.

Implementation:
1.	Data Loading and Preparation:
o	The tool uses the pandas library to load and manipulate car data stored in a CSV file (car_data.csv).
2.	User Input Collection:
o	The get_user_preferences function collects user input through command-line prompts. It handles blank inputs by setting corresponding values to None, allowing for flexible filtering.
4.	Car Data Filtering:
o	The filter_cars function filters the car data based on user preferences. It applies conditions for price range, car segment, fuel type, and required features to obtain a subset of matching cars.
5.	Displaying Car Details:
o	The display_cars function prints the details of each matching car in the terminal, making it easy for users to review their options.
6.	Creating Scatter Plots:
o	The plot_scatter function generates scatter plots using matplotlib. Users select an attribute to plot against price, and the scatter plot visualizes the relationship using color gradients.
o	The tool employs matplotlib events to enable interactive annotations. Clicking on a scatter plot point displays the car name in a black box and prints the car's details in the terminal.

Example Interaction:
•	User Input:
o	Minimum Budget: 20000
o	Maximum Budget: 50000
o	Preferred Segment: Mid-Range
o	Preferred Fuel Type: Hybrid
o	Required Features: sunroof, automatic_transmission
•	Filtered Results:
o	The tool displays a list of cars that match the specified criteria, providing detailed information about each car.
•	Scatter Plot:
o	The user selects "horsepower" as the scatter plot criteria.
o	The scatter plot shows price vs. horsepower, with different colors representing horsepower values.
•	Click Interaction:
o	Clicking on a dot in the scatter plot displays the car name in a black box and prints the car's full details in the terminal.

This tool offers a powerful and user-friendly way to explore car options based on personal preferences, combining data filtering, comprehensive display, and interactive visualization.


