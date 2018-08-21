import csv

filename = 'death_rates.csv'
with open(filename) as f:
    reader = csv.reader(f)
    for i in range(0, 4):
        next(reader)
    header_row = next(reader)

years = header_row[4:-2]

print(years)
rus_deaths = {}
    for row in reader:
        if row[0] == 'Russian Federation':
            [4:]
