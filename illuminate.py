#this script will allow me to automatically scrape (get info) my grades from the illuminate website
import requests

rr = requests.get(myurl, auth = (user, passwd))
user = "596125"
passwd = "123456"
myurl = "https://smmusd.illuminatehc.com/login"

#go to https://smmusd.illuminatehc.com/login
#under username type 596125
#under password type 123456
#scrape grades
#print to screen


#in further use, try to send text of grades