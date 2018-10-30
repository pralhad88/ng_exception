import simplejson as json
import json

with open('keys.json') as fileObject:
	fileContents = fileObject.read()
	r = json.loads(fileContents)
def trance(formatted):
	j=0
	while True:
		a=r['values'][j]['from']
		if formatted in a:
			out=r['values'][j]['to']
			#print(r['values'][j]['to'])
			return out
			break
		j+=1