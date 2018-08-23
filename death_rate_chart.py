import csv

import pygal

filename = 'death_rates.csv'
with open(filename) as f:
    reader = csv.reader(f)
    for i in range(0, 4):
        next(reader)
    header_row = next(reader)
    years = header_row[-12:-2]

    rus_deaths = {}
    deaths = []
    for row in reader:
        if row[0] == 'Russian Federation':
            deaths = row[-12:-2]
            rus_deaths = dict(zip(years, deaths))

deaths = list(map(float, deaths))
years = list(map(int, years))
print(deaths)

line_chart = pygal.Line()
line_chart.title = 'Death rate, crude (per 1,000 people)'
line_chart.x_labels = map(str, years)
line_chart.add('russia', deaths)
line_chart.render_to_file('death_chart.svg')

