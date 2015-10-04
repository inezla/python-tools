import requests

user = "596125"
passwd = "123456"
myurl = "https://smmusd.illuminatehc.com/login"
#rr = requests.get(myurl, auth = (user, passwd))
#session = requests.session
payload_login = {
#'action': 'login_check',
'username': 596125,
'password': 123456
}
with requests.Session() as ss:
	con = ss.post(myurl, data=payload_login)

print con.text

#not logging in!


#tt = requests.get(myurl, auth=('596125', '123456'))

#print tt.text


#'action': 'login_check',