#Web Scrapping Program to know live cricket scores using Python and BeautifulSoup
import requests
import tables
from bs4 import BeautifulSoup
import csv
#URL of Cricbuzz Website.
URL = "http://www.cricbuzz.com/cricket-match/live-scores"
r = requests.get(URL)
soup = BeautifulSoup(r.content, 'html5lib')
p=1
scores=[]
url_store=[]
#storing content of live-score page.
table=soup.find('div', attrs = {'class':'cb-bg-white cb-col-100 cb-col'})
#Retriving only required information
for row in table.findAll('div', attrs = {'class':'cb-col cb-col-100 cb-lv-main'}):
    quote1= {}
    quote1['url']=row.a['href']
    name= row.a['title']
    print("      {0}.{1}".format(p,name))
    p=p+1
    url_store.append(quote1)
#storing URLs of live matches in a file.    
filename_url = 'current_matches_url.csv'
with open(filename_url, 'wb') as f:
    w = csv.DictWriter(f,['url'])
    w.writeheader()
    for quote1 in url_store:
        w.writerow(quote1)     
match_no=0
while match_no!=-1:       
	match_no=input("Enter the Match number (Enter -1 to exit):")
	if match_no!=-1 and match_no<=p:
		file = open(filename_url, 'r')
		t=1
		#Retriving the required match's live score URL.
		req_url="http://www.cricbuzz.com"
		for each in file:
			break
		for each in file:
			if t==match_no:
				req_url=req_url+each
				break
			t=t+1	
		print("Click on this link to go to website:")	
		print(req_url)	
		#requesting URL
		r = requests.get(req_url)
		soup = BeautifulSoup(r.content, 'html5lib')
		#storing page content in table.
		table=soup.find('div', attrs = {'class':'page'})
		team1=0
		team2=0
		#Retriving only required data.
		#print(table.prettify())
		for row in table.findAll('div',attrs={'class':'cb-col cb-col-100 cb-min-tm cb-text-gray'}):
			team1=1
			print(row.text)
		for row in table.findAll('div',attrs={'class':'cb-col cb-col-100 cb-min-tm'}):
			team2=1
			print(row.text)
		for row in table.findAll('div',attrs={'class':'cb-text-rain'}):
			print(row.text+". Stay tuned!")	
		if team2==1 and team1==1:
			for row in table.findAll('div',attrs={'class':'cb-col cb-col-100 cb-min-stts cb-text-mom'}):
				print(row.text)
			for row in table.findAll('div',attrs={'class':'cb-col cb-col-100 cb-min-stts cb-text-complete'}):
				print(row.text)	
		if team1==0 and team2==0:
			for row in table.findAll('div',attrs={'class':'cb-text-gray cb-font-16'}):
				team1=1
				print(row.text)	
			for row in table.findAll('span',attrs={'class':'cb-font-20 text-bold'}):
				team2=1
				print(row.text)	
			for row in table.findAll('div',attrs={'class':'cb-text-stump'}):
				print(row.text)
		#if match not yet started,		
		if team1==0 and team2==0:
			print("Match not yet started! Stay tuned!")
	else:
		if match_no>p:
			print("Select a valid match number!")
		elif match_no==-1:
			print("Good Bye!")
			break			
	print("")		