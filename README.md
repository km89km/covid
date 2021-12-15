This repository contains some simple visualisations of covid-19 data using python, csv and json modules
and plotly and pyplot.
covid_cases.comp.py - compares the cumulative total cases per 1 million people of three countries.
These countries have personal significance to me as they represent where I was during the initial
outbreak (Mexico), where I wanted to go but was unable due to border closures (Colombia) and where
I ended up, due to safety concerns (United Kingdom). The data used in the program was downloaded 
from https://github.com/owid/covid-19-data/blob/master/public/data/owid-covid-data.csv.

After parsing the .csv file for the whole world to isolate the desired countries and saving the data
to new .csv files (mexico_data.csv, colomobia_data.csv and uk_data.csv) each file is iterated through, 
adding the date and total cases to a separate list contained in a new dictionary called country_data.
With this information isolated and easily accessed, the next step is to plot a visualisation using
pyplot. As there are three countries to plot, each is colour coded and a legend is added to the top
left corner. As the data covers close to 2 years worth of data, the set_major_locator(plt.MaxNLocator(int))
method is applied to the y-axis (showing the number of cases), setting the ticks to 10 to avoid overlapping
and the autofmt_xdate() method is called on the x-axis to prevent the dates from overlapping.
A copy of the final visualisation is entitled 'cases_visualisation.png'.

covid_deaths_comp.py - is very similar in essence to the previous program but plots the cumulative total
deaths per 1 million people of the same countries. A copy of the final visualisation is entitled 
'deaths_visualisation.png'.

third_vaccinations.py - compares the 3rd dose/booster vaccination totals of the nations of the UK and plots
a simple bar graph to visualise the data.
The data used in this program was downloaded from https://coronavirus.data.gov.uk/details/vaccinations.

This time, the data ('uk_vac_data.json') is in the .json format rather than .csv and we save the data in a 
dictionary called 'all_data' by using json.dump(file). The main data of this file is contained in a list of
dictionaries called 'data', so we iterate through each dictionary to find the desired information. As the
data displays the cumulative total of vaccinations, the program finds the most recent total for each country
by matching the dictionary['date'] key to the most recent date and then saves the nation name and total
number of vaccinations to separate lists. These two lists are then visualised in a Bar graph using plotly.
The axes are given the appropriate titles and an offline visualisation is saved, entitled 'vacs.html'.
