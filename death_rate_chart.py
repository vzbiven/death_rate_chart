import csv

import pygal

filename = 'death_rates.csv'
with open(filename) as f:
    reader = csv.reader(f)
    for i in range(0, 4):
        next(reader)
    header_row = next(reader)
    years = header_row[-43:-2]
    
    death_rates = {
                   'Russian Federation':[],
                   'Kazakhstan':[],
                   'Ukraine':[],
                   'India':[],
                   'Brazil':[],
                   'China':[],
                   'Japan':[],
                   'United States':[],
                   'Uganda':[],
                   'Finland':[],
                   }

    for country in death_rates.keys():
        f.seek(0)
        for i in range(0, 4):
            next(reader)
        deaths = []
        for row in reader:
            if row[0] == country:
                deaths = row[-43:-2]
        deaths = list(map(float, deaths))
        death_rates[country] = deaths

line_chart = pygal.Line(width=1200, interpolate='cubic',legend_at_bottom=True,
                        legend_at_bottom_columns=5,)
line_chart.title = 'Death rate, crude (per 1,000 people)'
line_chart.x_labels = map(str, years)
for country, deaths in death_rates.items():
    line_chart.add(country, deaths)

line_chart.render_to_file('death_chart.svg')

