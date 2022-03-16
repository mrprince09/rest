import requests
import json

URL="http://127.0.0.1:8000"

def student(id = None):
	# import pdb; pdb.set_trace()
	data={}
	if id is not None:
		data={"id":id}
	json_data = json.dumps(data)
	header={'Content-type':'application/json'}
	r= requests.get(url = URL,params=data)

	data = r.json()
	print(data)

# student(2)

def student1():
	data={'name': 'kam', 'roll': 4, 'city': 'khopal'}
	json_data = json.dumps(data)
	r= requests.post(url = URL,data=json_data)
	data=r.json()
	print(data)

student1() 

