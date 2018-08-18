import csv
import requests
from BeautifulSoup import BeautifulSoup

url = 'http://www.showmeboone.com/sheriff/JailResidents/JailResidents.asp'
response = requests.get(url)
html = response.content

soup = BeautifulSoup(html)
table = soup.find('tbody', attrs={'class': 'stripe'})

listRows = []
for row in table.findAll('tr'):                                 #List of rows
    listCells = []
    for cell in row.findAll('td'):                              #Individual Cells
        listCells.append(cell.text.replace('&nbsp;', ''))       #To get rid of awkward &nbsp;
    listRows.append(listCells)


#Outputting to a csv format!
outfile = open("inmates.csv","wb")
writer = csv.writer(outfile)

#Writing rows
writer.writerow(["Last", "First", "Middle", "Gender", "Race", "Age", "City", "State"])
writer.writerows(listRows)
