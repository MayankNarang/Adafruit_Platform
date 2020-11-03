import requests ,  json 
header={"x-aio-key":"aio_zcFu02aQkMz3np84kIhtjZKzFhbT"}
username="Mayank_124"
feed_key="temperature"
data={"value":"40"}
url="https://io.adafruit.com/api/v2/{}/feeds/{}/data".format(username,feed_key)
response=requests.post(url=url,headers=header,data=data)
print(response.content)