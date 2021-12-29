# -*- coding: utf-8 -*-
"""
@author: bastianDupoirieux
"""

import urllib
import bs4


countries = dict()

def countryPopulation(country):
    '''A method that computes the population of a certain country, using the worldomters.info webiste
    @param country: a variable of type string, the name of the country we want to gather the information from
    @return the population of the given country'''
    
    '''Right now, this method only works for single name countries'''
    #TODO: write method for multi-name countries using regex
    
    assert type(country) == str, "the variable must a be a string, it's a country name"
    
    if country.str.contains(' ') == True:
        raise ValueError("This method can't handle countries with multiple names right now. Sry :-(")
    
    country = country[0].upper() + country[1:].lower() #transform the text so that it is understandable for the webiste
    url= 'https://www.worldometers.info/world-population/population-by-country/'
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    request_text = urllib.request.urlopen(req).read()
    
    page = bs4.BeautifulSoup(request_text, 'lxml')
    
    table = page.find('div', {"style": "font-size:14px; width:100%",}, {"class": "table-responsive"})
    
    countriesInfo = table.find("table", {"id" : "example2"})
    countriesInfoBody = countriesInfo.find('tbody') #take the table's body
    rows = countriesInfoBody.find_all('tr')
    population= 0
    
    for row in rows:
        workCountry = row.find('td', {"style": "font-weight: bold; font-size:15px; text-align:left"}).text.strip()
        if workCountry != country: #if the country we are currently looking at is not the country we are working on
            pass
        else:
            population = int(row.find('td', {"style": "font-weight: bold;"}).text.strip().replace(",", ""))
     
    if population == 0:
        raise ValueError("Population is null, country probably not found, check again")
        
    return(population)


def numberOfCities(population, convention = 5000000):
    '''A method that computes the number of cities we want to look at, given a specific population.
    We use the rule that one city is counted for a certain number of inhabitants (i.e. 10 million inhabitants is 10//convention +1 cities), whilst rounding up the number of cities
    @param population: a variable of type int, with the population of the country
    @param convention: a variable of type int, representing a set parameter to compute the number of cities. We set it at 5,000,000
    @return the number of cities we will be working on'''
    return((population//convention) + 1)

def listCities(country):
    '''A method that finds a list of the largest cities in a given country
    @param country: a variable of type string, the country worked on
    @return a list of the largest cities, the amount of cities depending on the numberOfCities function'''
    assert type(country) == str, "the variable must be a string, it's a country name"
    country = country.replace(' ', '-')
    country = country.lower()
   
    
    citiesList = []
    
    population = countryPopulation(country)
    citiesNumber = numberOfCities(population)
    
    url = 'https://population.mongabay.com/population/' + str(country) +'/'
    
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    request_text = urllib.request.urlopen(req).read()
    
    page = bs4.BeautifulSoup(request_text, 'lxml')
    
    table = page.find('div', {"class":"datatable"})
    
    tableCities = table.find('table')
     
    rows = tableCities.find_all('tr')[1:] # the first row in the table is each column's title, dismiss this column
    
    for i in range(citiesNumber):
        row = rows[i]
        city = row.find('td').text.strip()
        citiesList.append(city)

    return(citiesList)