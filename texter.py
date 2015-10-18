#twilio.py
from twilio.rest import TwilioRestClient

import requests

from bs4 import BeautifulSoup



#my first function
"""
def meeterGreeter():
	print "Hello World"
	print "nice to meet you"

def doubler(nums):
	#this function will return 2 * nums
	doubled = 2 * nums
	return doubled
"""

def textMe(mess):
	accountSID = 'AC32fa8f01f2c546e62676e56e7d436319'
	authToken = 'f76bbb65c5102ba6d354f6cdfcde550c'
	myTwilionumber = '14242522749'
	myCellPhone = '+13104633516'
	twilioCli = TwilioRestClient(accountSID, authToken)
	message = twilioCli.messages.create(body=mess, from_=myTwilionumber, to=myCellPhone)


def adminIlluminate():
	#this function logs into illuminate and returns the grade webpage
	user = "596125"
	passwd = "123456"
	cookieurl = "https://smmusd.illuminatehc.com/login"
	grade_url = "https://smmusd.illuminatehc.com/login_check"
	payload_login = {
	'_username': "596125",
	'_password': "123456"
	}

	ss = requests.Session()
	ss.get(cookieurl)
	gradepage = ss.post(grade_url, data=payload_login)

	return gradepage


def getGrades(gradepage):
	#this will gather the data from grade page using soup, and organizing them. It will return 
	#the information I want (only class, grade, and percentage) as a string.
	gradepage = adminIlluminate()
	soup = BeautifulSoup(gradepage.content)
	tables = soup.select("div table.table-responsive")
	gradedict = {} #dict to hold values
	for table in tables:
		for row in table.select("tr"):
			cells = row.select("td")
			print cells
			if len(cells):
				myclass = cells[1].getText()
				mygrade = cells[0].getText()
				gradedict[myclass] = mygrade
	grademessage = ""
	for k,v in gradedict.items():
		period = "{}: {}".format(k,v)
		grademessage = grademessage + "\n" + period
			
	return grademessage


