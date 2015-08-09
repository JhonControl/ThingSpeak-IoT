import httplib, urllib,time
from random import randint

apikey = "xxxxxxxxxxxxxxxxx"  # your api --- tu API de thingspeak


while True:


    #https://api.thingspeak.com/update?key=TXBSGLTWSRF63NPZ&field1=0
   
	ran01 =  randint (0 ,10)	
	print ran01
	params = urllib.urlencode({'field1': ran01,'key': apikey})
	#params = urllib.urlencode({'field1': ran01, 'field2': 11,'key':apikey'})
	headers = {"Content-type": "application/x-www-form-urlencoded","Accept": "text/plain"}
	conn = httplib.HTTPConnection("api.thingspeak.com:80")
	conn.request("POST", "/update", params, headers)
	response = conn.getresponse()
	

	
	print response.status, response.reason
	data = response.read()
	conn.close()
	print data	
	
	  
	time.sleep(40)	# 40 segundos