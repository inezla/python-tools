#this script will allow me to automatically scrape (get info) my grades from the illuminate website
import requests

user = "596125"
passwd = "123456"
myurl = "https://smmusd.illuminatehc.com/login"
#rr = requests.get(myurl, auth = (user, passwd))
#session = requests.session
payload_login = {
'username': 596125,
'password': 123456
}
with requests.Session() as ss:
	con = ss.post("https://smmusd.illuminatehc.com/login")

#go to https://smmusd.illuminatehc.com/login
#under username type 596125
#under password type 123456
#scrape grades
#print to screen


#in further use, try to send text of grades