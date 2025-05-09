def read_weather_data(file_name):
    with open(file_name, 'r') as f:
        lines = f.readlines()
        data = [line.strip().split() for line in lines]
    return [(d, int(t)) for d, t in data]

def find_max_temp_per_year(data):
    yearly_max = {}
    for date, temp in data:
        year = date.split('-')[0]
        if year not in yearly_max or temp > yearly_max[year][1]:
            yearly_max[year] = (date, temp)
    return [yearly_max[y] for y in sorted(yearly_max)]

def write_max_temps(file_name, records):
    with open(file_name, 'w') as f:
        for date, temp in records:
            f.write(f"{date} {temp}\n")

data = read_weather_data("weather_data.txt")
max_records = find_max_temp_per_year(data)
write_max_temps("max_temp_by_year.txt", max_records)
print("Max temperature per year has been written to max_temp_by_year.txt")
