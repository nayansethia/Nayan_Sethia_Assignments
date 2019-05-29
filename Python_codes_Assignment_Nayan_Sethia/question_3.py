import json
q3file = open('question3.json','r')

d=json.loads(q3file.read())
#print(d)
k=d["Records"][0]["s3"]["bucket"]["arn"]
#x=k["s3"]
print(k)
