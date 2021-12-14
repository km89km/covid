#! python3
# third_vaccinations.py - reads in a downloaded .json file
# containing the data for the cumulative total of people who
# have received their 3rd dose or booster vaccination. After
# storing the relevant information, a simple bar graph is plotted
# and saved.
# data downloaded from https://coronavirus.data.gov.uk/details/vaccinations

import json
from plotly.graph_objs import Bar, Layout
from plotly import offline

# use downloaded .json file containing cumulative numbers
# of people that have received 3rd Vaccination.
filename = 'uk_vac_data.json'
with open(filename) as f:
    # save data to dictionary called 'all_data'.
    all_data = json.load(f)

# initialise lists to store the nation names and number of vacs.
nations, numbers = [], []
# the desired information is stored in a list called 'data', so we iterate
# through it's sub-dictionaries to find the information for each nation.
for sub in all_data['data']:
    # find the most recent data for each nation and store it's value
    # for nation name and total of vaccinations.
    if sub['date'] == "2021-12-13":
        # the relevant keys are used to find the desired information.
        nations.append(sub["areaName"])
        numbers.append(sub["cumPeopleVaccinatedThirdInjectionByPublishDate"])

# visualise the data by creating a Bar object from plotly.
data = [Bar(x=nations, y=numbers)]

# configure the axes and layout.
x_axis_config = {'title': 'Nation'}
y_axis_config = {'title': 'Number of Vaccinations'}
my_layout = Layout(title='Total Number of 3rd Dose/Booster Vaccinations '
                         'in the UK (As of 13/12/21)',
                   xaxis=x_axis_config, yaxis=y_axis_config)
# plot the bar graph with the desired information and save offline copy.
offline.plot({'data': data, 'layout': my_layout}, filename='vacs.html')
