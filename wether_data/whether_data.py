import random

def generate_weather_data():
    temperature = random.randint(-10, 40)
    humidity = random.randint(20, 100)
    wind_speed = random.randint(0, 20)
    conditions = random.choice(["Clear", "Cloudy", "Rainy", "Windy", "Stormy", "Snowy"])
    return temperature, humidity, wind_speed, conditions

def write_weather_to_file(file_name, temperature, humidity, wind_speed, conditions):
    with open(file_name, 'w') as f:
        f.write(f"Weather Data Report\n")
        f.write(f"Temperature: {temperature}°C\n")
        f.write(f"Humidity: {humidity}%\n")
        f.write(f"Wind Speed: {wind_speed} m/s\n")
        f.write(f"Conditions: {conditions}\n")

temperature, humidity, wind_speed, conditions = generate_weather_data()
file_name = "weather_data.txt"
write_weather_to_file(file_name, temperature, humidity, wind_speed, conditions)

print(f"Weather data has been written to {file_name}")
