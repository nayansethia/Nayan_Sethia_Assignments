import boto3
s3 = boto3.resource('s3')
print("Enter the name of bucket")
my_bucket = s3.Bucket(input())                        #to get bucket name as input from user

print("Enter the name of object")
obj=input()                                           #to get object name as input from user



l= s3.list_object_versions(Bucket=my_bucket, Prefix=obj)      #l will be the dictionary that will contain information about all the versions of object having prefix obj from bucket specified by user

objver= l['Versions']                                 #objver will contain list of information about versions of object

objversorted=sorted(objver, key='LastModified')       #sorting the list according to the time last modified

desiredobj=objversorted(-2)                           #second last version of object will get placed at -2 index position that is at second last position
objid=desiredobj['VersionId']                         #objid will contain version id of the desiredobj, this desiredobj is actually a dictionary

s3.download_file(bucket, file, file, ExtraArgs={'VersionId': objid})   #to download the desired version of the object
