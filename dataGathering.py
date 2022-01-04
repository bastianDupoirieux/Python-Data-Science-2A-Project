# -*- coding: utf-8 -*-
"""

@author: bastd

This is a .py file with the information in the largestStations.ipynb file
"""

import urllib
import bs4

import ssl
ssl._create_default_https_context = ssl._create_unverified_context



def gather(url, start=0):
    '''A method that gathers the information on a similar info
    @param url: the url of the website to scrap, of type string
    @param start: the value of the first row in the table. Sometimes, the first row is the heading. Of type int
    @return stations: a dictionary, with key the name of the station, and with the interesting information'''
    request = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})

    request_text = urllib.request.urlopen(request).read()

    page = bs4.BeautifulSoup(request_text, 'lxml') #open and bs4 the webpage

    table = page.find('table') #find the only table on the page
    
    # get the useful information in the table
    
    tableBody = table.find('tbody')

    rows = tableBody.find_all('tr')
    
    stations = dict() #create a new dictionary

    for i in range (len(rows)-start):
        row = rows[i+start]
        values = row.find_all('td')
        stations[values[0].text.strip()]= [values[1].text.strip(), values[2].text.strip()]
    
    return (stations)
    



    
    



