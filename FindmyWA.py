import requests
from bs4 import BeautifulSoup
import csv
from time import sleep
import os
import sys
import re

Version = 1
print("This is Version: "+str(Version))

UserAgent=input("Please enter your main nations name: ")
filename="puppet.csv"
names = set()
NewListOfIssues = 'Find_my_WA.txt'
with open("puppet.csv") as csv_file:
	csv_reader = csv.reader(csv_file)
	for row in csv_reader:
		names.add(row[0].lower().replace(" ", "_"))
index=0

if os.path.exists(NewListOfIssues):
  os.remove(NewListOfIssues)
stop=0;

if(stop==0):
	r = requests.get('https://www.nationstates.net/cgi-bin/api.cgi', headers={'User-Agent': UserAgent}, params={'wa':1,'q':'members'})
	sleep(.8)
	#print(r.content)
	soup = BeautifulSoup(r.content, "xml")
	Mem=soup.find('MEMBERS')
	#print(Mem.text)
	with open(NewListOfIssues, 'a+') as f:
		i = 0
		for i, match in enumerate(names.intersection(Mem.text.split(",")), 1):
  			print("I found a WA on: " + match)
  			f.writelines("I found a WA on: " + match)
		if not i:
  			print("I didn't find any WA puppets.")
input('Found it press enter to close')

