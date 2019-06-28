import json                            #importing modules
import boto3

from __future__ import print_function

def lambda_handler(event, context):                             #defining lamda function
    
       
    payload=event["Records"][0]["body"]                         #getting message from the queue in variable payload
    if payload=="Copy":                                         #if the message is Copy then the desired file will be copied from source to destination folder in ns-jenkins-bucket
       s3 = boto3.resource('s3')
       s3.meta.client.upload_file('ns-jenkins-bucket/folder1/jenkins', 'ns-jenkins-bucket', '/folder2/')
       