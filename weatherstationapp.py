print("Welcome to the Weather Station Project!")

import random

# Function to generate simulated weather data
def generate_weather_data():
    temperature = round(random.uniform(-10, 40), 2)  # Random temperature between -10°C and 40°C
    humidity = round(random.uniform(0, 100), 2)       # Random humidity between 0% and 100%
    wind_speed = round(random.uniform(0, 20), 2)     # Random wind speed between 0 and 20 km/h

    # Return the simulated weather data as a dictionary
    weather_data = {
        "temperature": temperature,
        "humidity": humidity,
        "wind_speed": wind_speed
    }

    return weather_data

# Example usage of the function
if __name__ == "__main__":
    data = generate_weather_data()
    print("Generated Weather Data:")
    print(f"Temperature: {data['temperature']}°C")
    print(f"Humidity: {data['humidity']}%")
    print(f"Wind Speed: {data['wind_speed']} km/h")
