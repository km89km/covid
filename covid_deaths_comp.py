#! python3
# covid_deaths_comp.py - creates a data visualisation of
# the cumulative covid-19 deaths per 1 million population
# of Colombia, Mexico and the UK.
# data downloaded from https://github.com/owid/covid-19-data/blob/master/
# public/data/owid-covid-data.csv

import csv
import matplotlib.pyplot as plt
from datetime import datetime

# list of countries to plot
countries = ['colombia', 'mexico', 'uk']
# initialise dictionary to store data for each country
country_data = {}
for country in countries:
    # initialise separate sub-dictionary to store relevant data.
    country_data[country] = {}
    # open each countries .csv file.
    filename = f'{country}_data.csv'
    with open(filename) as f:
        # create reader object to parse data.
        reader = csv.reader(f)
        # move beyond row of headings.
        next(reader)
        # initialise lists to store the relevant data of each country.
        country_data[country]["dates"] = []
        country_data[country]["total_deaths"] = []
        for row in reader:
            # create datetime object of the date for easier plotting.
            current_date = datetime.strptime(row[3], '%Y-%m-%d')
            # skip any missing data entries.
            try:
                # round the cases figure to 3 decimals.
                new_deaths = round(float(row[13]), 3)
            except ValueError:
                pass
            else:
                # add to dates list for current country.
                country_data[country]["dates"].append(current_date)
                # add to total_cases list for that country.
                country_data[country]["total_deaths"].append(new_deaths)

# set the style of the plot.
plt.style.use('seaborn-poster')
fig, ax = plt.subplots()
# plot each of the countries data with a colour code.
ax.plot(country_data['colombia']['dates'],
        country_data['colombia']['total_deaths'], c='yellow', label='Colombia')
ax.plot(country_data['mexico']['dates'],
        country_data['mexico']['total_deaths'], c='green', label='Mexico')
ax.plot(country_data['uk']['dates'],
        country_data['uk']['total_deaths'], c='red', label='UK')
# set the legend of the colour codes to appear in the top left corner.
plt.legend(loc="upper left")
# et Title and axes labels
ax.set_title('Cumulative Total Covid-19 Deaths per 1 million people', fontsize=18)
ax.set_xlabel('Date', fontsize=16)
# auto format the date ticks to avoid clashing.
fig.autofmt_xdate()
ax.set_ylabel('Number of Deaths per 1 million people', fontsize=16)
ax.tick_params(axis='both', which='minor', labelsize=16)
# set the y-axis to start at zero.
ax.set_ylim(bottom=0)
# limit the y-axis ticks to 15 to avoid overlapping.
ax.yaxis.set_major_locator(plt.MaxNLocator(15))
# plot the data.
plt.show()
