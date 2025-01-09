import pandas as pd
import random

# Define car brands and their specific models for each segment
car_segments = {   
    'Exotic': {
        'Ferrari': ['488', '812', 'Portofino', 'F8', 'Roma'],
        'Lamborghini': ['Huracan', 'Aventador', 'Urus', 'Gallardo', 'Murcielago'],
        'Bugatti': ['Veyron', 'Chiron', 'Divo', 'Centodieci', 'Bolide'],
        'McLaren': ['720S', '600LT', 'GT', 'Senna', 'Artura'],
        'Aston Martin': ['DB11', 'Vantage', 'DBS', 'Rapide', 'Vanquish']
    },
    'Luxury': {
        'Rolls-Royce': ['Phantom', 'Ghost', 'Wraith', 'Dawn', 'Cullinan'],
        'Bentley': ['Continental', 'Flying Spur', 'Bentayga', 'Mulsanne', 'Arnage'],
        'Porsche': ['911', 'Cayenne', 'Panamera', 'Macan', 'Taycan'],
        'Lexus': ['IS', 'ES', 'GS', 'LS', 'NX'],
        'Jaguar': ['XE', 'XF', 'XJ', 'F-Pace', 'E-Pace']
    },
    'Mid-Range': {
        'BMW': ['1 Series', '2 Series', '3 Series', '4 Series', '5 Series'],
        'Mercedes-Benz': ['A-Class', 'C-Class', 'E-Class', 'G-Class', 'S-Class'],
        'Audi': ['A3', 'A4', 'A5', 'A6', 'A7'],
        'Volvo': ['S60', 'S90', 'XC40', 'XC60', 'XC90'],
        'Genesis': ['G70', 'G80', 'G90', 'GV70', 'GV80'],
        'Cadillac': ['ATS', 'CTS', 'XT4', 'XT5', 'Escalade'],
        'Infiniti': ['Q50', 'Q60', 'Q70', 'QX50', 'QX60'],
        'Lincoln': ['MKC', 'MKZ', 'Nautilus', 'Aviator', 'Navigator'],
        'Acura': ['ILX', 'TLX', 'RLX', 'MDX', 'RDX'],
        'Alfa Romeo': ['Giulia', 'Stelvio', '4C', 'GTV', 'Spider']
    },
    'Common': {
        'Toyota': ['Corolla', 'Camry', 'Prius', 'RAV4', 'Highlander'],
        'Honda': ['Civic', 'Accord', 'CR-V', 'Pilot', 'Fit'],
        'Ford': ['Focus', 'Fiesta', 'Mustang', 'Explorer', 'F-150'],
        'Nissan': ['Altima', 'Sentra', 'Maxima', 'Rogue', 'Murano'],
        'Hyundai': ['Elantra', 'Sonata', 'Tucson', 'Santa Fe', 'Kona'],
        'Kia': ['Optima', 'Soul', 'Sportage', 'Sorento', 'Stinger'],
        'Chevrolet': ['Malibu', 'Impala', 'Cruze', 'Equinox', 'Tahoe'],
        'Volkswagen': ['Golf', 'Jetta', 'Passat', 'Tiguan', 'Atlas'],
        'Mazda': ['Mazda3', 'Mazda6', 'CX-3', 'CX-5', 'CX-9'],
        'Subaru': ['Impreza', 'Legacy', 'Outback', 'Forester', 'Ascent'],
        'Renault': ['Clio', 'Megane', 'Kadjar', 'Captur', 'Zoe'],
        'Peugeot': ['208', '308', '508', '2008', '3008'],
        'Citroën': ['C3', 'C4', 'C5', 'Berlingo', 'SpaceTourer'],
        'Seat': ['Ibiza', 'Leon', 'Arona', 'Ateca', 'Tarraco'],
        'Skoda': ['Fabia', 'Octavia', 'Superb', 'Kodiaq', 'Karoq'],
        'Suzuki': ['Swift', 'Baleno', 'Vitara', 'S-Cross', 'Jimny'],
        'Dacia': ['Sandero', 'Duster', 'Logan', 'Lodgy', 'Dokker'],
        'Jeep': ['Wrangler', 'Cherokee', 'Grand Cherokee', 'Compass', 'Renegade'],
        'Land Rover': ['Range Rover', 'Discovery', 'Evoque', 'Defender', 'Freelander']
    }
}

# Define attribute ranges based on segments
attribute_ranges = {
    'Exotic': {
        'price': (150000, 300000),
        'horsepower': (500, 1000),
        'torque': (500, 1000),
        'rpm': (8000, 12000),
        'top_speed': (250, 350),
        'mileage': (5, 10),
        'safety_rating': (5)
    },
    'Luxury': {
        'price': (60000, 150000),
        'horsepower': (300, 500),
        'torque': (400, 600),
        'rpm': (7000, 9000),
        'top_speed': (200, 250),
        'mileage': (10, 15),
        'safety_ratings': (5)
    },
    'Mid-Range': {
        'price': (30000, 60000),
        'horsepower': (200, 300),
        'torque': (200, 400),
        'rpm': (6000, 8000),
        'top_speed': (160, 200),
        'mileage': (15, 20),
        'safety_rating': (4, 5)
    },
    'Common': {
        'price': (15000, 30000),
        'horsepower': (100, 200),
        'torque': (100, 200),
        'rpm': (5000, 7000),
        'top_speed': (120, 160),
        'mileage': (20, 30),
        'safety_rating': (3, 4)
    }
}

# Define other car attributes
fuel_types = ['Petrol', 'Diesel', 'Hybrid']
safety_ratings = [3, 4, 5]

# Function to generate car data
def generate_car_data(car_segments, attribute_ranges):
    data = {
        'segment': [],
        'brand': [],
        'model': [],
        'price': [],
        'fuel_type': [],
        'sunroof': [],
        'automatic_transmission': [],
        'safety_rating': [],
        'horsepower': [],
        'torque': [],
        'rpm': [],
        'top_speed': [],
        'mileage': []
    }

    for segment, brands in car_segments.items():
        for brand, models in brands.items():
            for model in models:
                price = random.randint(*attribute_ranges[segment]['price'])
                horsepower = random.randint(*attribute_ranges[segment]['horsepower'])
                torque = random.randint(*attribute_ranges[segment]['torque'])
                rpm = random.randint(*attribute_ranges[segment]['rpm'])
                top_speed = random.randint(*attribute_ranges[segment]['top_speed'])
                mileage = round(random.uniform(*attribute_ranges[segment]['mileage']), 2)
                fuel_type = random.choice(fuel_types)
                sunroof = random.choice([True, False])
                automatic_transmission = random.choice([True, False])
                safety_rating = random.choice(safety_ratings)

                data['segment'].append(segment)
                data['brand'].append(brand)
                data['model'].append(model)
                data['price'].append(price)
                data['fuel_type'].append(fuel_type)
                data['sunroof'].append(sunroof)
                data['automatic_transmission'].append(automatic_transmission)
                data['safety_rating'].append(safety_rating)
                data['horsepower'].append(horsepower)
                data['torque'].append(torque)
                data['rpm'].append(rpm)
                data['top_speed'].append(top_speed)
                data['mileage'].append(mileage)
    
    return pd.DataFrame(data)

# Generate car data for the defined brands and models
car_data = generate_car_data(car_segments, attribute_ranges)

# Save to CSV
car_data.to_csv('car_data.csv', index=False)

print("Car data CSV with additional attributes based on segments has been created!")
