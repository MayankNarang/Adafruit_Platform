import requests ,  json 
header={"x-aio-key":"aio_zcFu02aQkMz3np84kIhtjZKzFhbT"}
username="Mayank_124"
feed_key="slider"
url="https://io.adafruit.com/api/v2/{}/feeds/{}/data".format(username,feed_key)
while 1:
	response=requests.get(url=url,headers=header)
	data=json.loads(response.content)
	print(data[0]["value"])