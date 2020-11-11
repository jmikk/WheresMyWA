import requests
from bs4 import BeautifulSoup
import csv
from time import sleep
import os
import sys

Version = 1
print("This is Version: "+str(Version))

UserAgent=input("Please enter your main nations name: ")
filename="puppet.csv"

names=[]
NewListOfIssues = 'Find_my_WA.txt'
with open("puppet.csv") as csv_file:
	csv_reader = csv.reader(csv_file)
	for row in csv_reader:
		names.append(row[0])
index=0

if os.path.exists(NewListOfIssues):
  os.remove(NewListOfIssues)
stop=0;
for every in names:
	if(stop==0):
		every=every.replace(" ", "_")	
		r = requests.get('https://www.nationstates.net/cgi-bin/api.cgi/', headers={'User-Agent': UserAgent}, params={'nation':every, 'q':'wa'})
		sleep(.8)
		#print(r.content)
		soup = BeautifulSoup(r.content, "xml")
		#print(soup)
		WAStatus=soup.find('UNSTATUS')
		with open(NewListOfIssues, 'a+') as f:
			#print(WAStatus.text)
			if(WAStatus.text == 'WA Member' or WAStatus.text == 'WA Delegate'):
				f.writelines('***************I found a WA on: '+ every+"\n")
				print('I found a WA on: '+ every)
				stop=1
			else:
				f.writelines('I did not find a WA on: '+ every+"\n")
				print(every+" is a " +WAStatus.text)      
input('Found it press enter to close')

