import urllib2
import csv
import sched, time
from threading import Timer
from datetime import datetime
from bs4 import BeautifulSoup


#same links from newegg the script will crawl through these links looking for product links to then copy data
mainUrls = ["https://www.newegg.com/Product/ProductList.aspx?Submit=ENE&N=100007709%2050001312%2050001314%2050001315%2050001402%2050001419%2050001471%2050001561%2050001944%2050012150%204814%20601201888%20601204369%20601301599%20601296379%20601296377%204023&IsNodeId=1&bop=And&PageSize=96&order=BESTMATCH",
		   "https://www.newegg.com/Product/ProductList.aspx?Submit=ENE&N=100007709%2050001312%2050001314%2050001315%2050001402%2050001419%2050001471%2050001561%2050001944%2050012150%204814%20601201888%20601204369%20601301599%20601296379%20601296377%204022&IsNodeId=1&bop=And&PageSize=96&order=BESTMATCH"]

#what values to add to the rows
keys = ['price','Brand','GPU','GPU Series', 'Model','Chipset Manufacturer','Memory Size']



def copyDataForURL(URL,price):
	URL = URL + "&recaptcha=pass"
	page = urllib2.urlopen(URL)
	data = {"price":price}
	soup = BeautifulSoup(page,"html.parser")
	details = soup.find('div', attrs={'id':'detailSpecContent'})

	try:
		 plinks = details.find('div',attrs={'id':'Specs'}).find_all('fieldset')
	except:
		print "didnt work"
		return
	for field in plinks:
		for dl in field.find_all('dl'):
			 index = 0
			 insert = dl.find_all('dd')
			 for dt in dl.find_all('dt'):
			 	data[dt.text] = insert[index].text
			 	index = index +1 
			
	print("copying data for url"+URL)
	saveRowForData(data)
	time.sleep(5)

def saveRowForData(data):
	dataValues = []
	for key in keys:
		try:
			dataValues.append(data[key])
		except:
			dataValues.append("NA")
	with open('index1.csv', 'a') as csv_file:
 		writer = csv.writer(csv_file)
 		writer.writerow(dataValues)
 		print "ADD CARD TO CSV.."


def run():
	for i,mainUrl in enumerate(mainUrls):
		print("copying more urls "+str(i) +"/"+str(mainUrls))
		mainpage = urllib2.urlopen(mainUrl)
		soup1 = BeautifulSoup(mainpage,"html.parser")
		urls = soup1.find_all('div',attrs={'class':'item-container'})

		timeDelay = 0
		index = 0
 		for x in urls:
 			url = urls[index].find('a',attrs={'class':'item-title'})['href']
 			price = urls[index].find('li',attrs={'class':'price-current'}).find('strong').text
 			print price +"-------------"
 			copyDataForURL(url,price)
 			timeDelay = timeDelay + 3
 			print str(timeDelay/3) + " / "+ str(len(urls))
 			index = index + 1
 		
run()

