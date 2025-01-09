import pandas as pd
import matplotlib.pyplot as plt

# Load the car data
car_data = pd.read_csv('car_data.csv')

# Function to get user preferences
def get_user_preferences():
    budget_min_input = input("Enter your minimum budget or leave blank: ")
    budget_max_input = input("Enter your maximum budget or leave blank: ")
    budget_min = int(budget_min_input) if budget_min_input else None
    budget_max = int(budget_max_input) if budget_max_input else None
    preferred_segment = input("Enter preferred car segment (Exotic, Luxury, Mid-Range, Common) or leave blank: ")
    fuel_type = input("Enter preferred fuel type (Petrol, Diesel, Electric, Hybrid) or leave blank: ")
    features_input = input("Enter required features (comma separated: sunroof, automatic_transmission) or leave blank: ")
    features = features_input.split(',') if features_input else []
    
    return {
        "budget_min": budget_min,
        "budget_max": budget_max,
        "preferred_segment": preferred_segment,
        "fuel_type": fuel_type,
        "features": features
    }

# Function to filter cars based on preferences
def filter_cars(data, preferences):
    filtered_data = data.copy()
    
    if preferences['budget_min'] is not None:
        filtered_data = filtered_data[filtered_data['price'] >= preferences['budget_min']]
    if preferences['budget_max'] is not None:
        filtered_data = filtered_data[filtered_data['price'] <= preferences['budget_max']]
    if preferences['preferred_segment']:
        filtered_data = filtered_data[filtered_data['segment'] == preferences['preferred_segment']]
    if preferences['fuel_type']:
        filtered_data = filtered_data[filtered_data['fuel_type'] == preferences['fuel_type']]
    
    for feature in preferences['features']:
        if feature:
            filtered_data = filtered_data[filtered_data[feature] == True]
    
    return filtered_data

# Function to display matching cars
def display_cars(filtered_data):
    if filtered_data.empty:
        print("No cars match your preferences.")
    else:
        for index, car in filtered_data.iterrows():
            print(f"{car['brand']} {car['model']}")
            print(f"Price: ${car['price']}")
            print(f"Fuel Type: {car['fuel_type']}")
            print(f"Sunroof: {'Yes' if car['sunroof'] else 'No'}")
            print(f"Automatic Transmission: {'Yes' if car['automatic_transmission'] else 'No'}")
            print(f"Safety Rating: {car['safety_rating']} stars")
            print(f"Horsepower: {car['horsepower']} hp")
            print(f"Torque: {car['torque']} Nm")
            print(f"RPM: {car['rpm']}")
            print(f"Top Speed: {car['top_speed']} km/h")
            print(f"Mileage: {car['mileage']} km/l")
            print()

# Function to plot scatter plot based on user-selected criteria
def plot_scatter(filtered_data):
    if filtered_data.empty:
        print("No data to plot.")
        return
    
    criteria = input("Enter the criteria for scatter plot (e.g., horsepower, torque, top_speed, mileage): ")
    
    if criteria not in filtered_data.columns:
        print("Invalid criteria. Please try again.")
        return
    
    fig, ax = plt.subplots(figsize=(10, 6))
    scatter = ax.scatter(filtered_data['price'], filtered_data[criteria], c=filtered_data[criteria], cmap='viridis', edgecolor='black')
    plt.title(f'Price vs. {criteria.capitalize()}')
    plt.xlabel('Price')
    plt.ylabel(criteria.capitalize())
    plt.colorbar(scatter, label=criteria.capitalize())

    annot = ax.annotate("", xy=(0,0), xytext=(20,20), textcoords="offset points",
                        bbox=dict(boxstyle="round", fc="black", ec="white", lw=2),
                        arrowprops=dict(arrowstyle="->"))
    annot.set_visible(False)

    def update_annot(ind):
        pos = scatter.get_offsets()[ind["ind"][0]]
        annot.xy = pos
        car = filtered_data.iloc[ind['ind'][0]]
        text = f"{car['brand']} {car['model']}"
        annot.set_text(text)
        annot.get_bbox_patch().set_facecolor('black')
        annot.get_bbox_patch().set_alpha(0.7)
        annot.get_bbox_patch().set_edgecolor('white')
        show_car_details(car)

    def show_car_details(car):
        print(f"\nClicked on: {car['brand']} {car['model']}")
        print(f"Price: ${car['price']}")
        print(f"Fuel Type: {car['fuel_type']}")
        print(f"Sunroof: {'Yes' if car['sunroof'] else 'No'}")
        print(f"Automatic Transmission: {'Yes' if car['automatic_transmission'] else 'No'}")
        print(f"Safety Rating: {car['safety_rating']} stars")
        print(f"Horsepower: {car['horsepower']} hp")
        print(f"Torque: {car['torque']} Nm")
        print(f"RPM: {car['rpm']}")
        print(f"Top Speed: {car['top_speed']} km/h")
        print(f"Mileage: {car['mileage']} km/l")

    def on_click(event):
        if event.inaxes == ax:
            cont, ind = scatter.contains(event)
            if cont:
                update_annot(ind)
                annot.set_visible(True)
                fig.canvas.draw_idle()
            else:
                annot.set_visible(False)
                fig.canvas.draw_idle()

    fig.canvas.mpl_connect("button_press_event", on_click)
    plt.show()

# Main function to run the car selection tool
def main():
    preferences = get_user_preferences()
    filtered_cars = filter_cars(car_data, preferences)
    display_cars(filtered_cars)
    plot_scatter(filtered_cars)

if __name__ == "__main__":
    main()
