import pandas as pd
import urllib.request
from bs4 import BeautifulSoup

requests_text = urllib.request.urlopen('https://en.wikipedia.org/wiki/List_of_European_countries_by_population').read()
page = BeautifulSoup(requests_text, "lxml")

list0 = []
list_country = []
list_population = []

for table in page.findAll('', { 'class' : "client-nojs"}) :
  for item in page.findAll({'tr'}) :
    list0.append(item.getText().replace("\n\xa0", "").replace("\u202f*", "$").replace("\n\n", "@"))

del list0[:2]
del list0[52:]

for k in range(len(list0)):
  temp = list0[k].find('$')
  list_country.append(list0[k][:temp])
  temp2 = list0[k].find('@') +1
  temp3 = list0[k].find('\n')
  list_population.append(list0[k][temp2:temp3])

countries = pd.DataFrame.from_dict( {'Countries' : list_country, 'Population' : list_population})
countries