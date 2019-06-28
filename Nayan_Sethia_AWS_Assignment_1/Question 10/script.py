import boto3                                       #inporting boto3
from boto3 import resource
from boto3.dynamodb.conditions import Key         #importing key

# The boto3 dynamoDB resource           
dynamodb_resource = resource('dynamodb')                  #a variable that will contain this resource

table = dynamodb_resource.Table("ns-aws-games")    # table is a variable that will contain ns-aws-games table of dynamano db

def qt(table_name, filter_key, filter_value):        # a function to perform querry operation
    
    table = dynamodb_resource.Table(table_name)      

    if filter_key and filter_value:                  # condition that if filter key and its value is matched at any point
        filtering_exp = Key(filter_key).eq(filter_value)
        response = table.query(KeyConditionExpression=filtering_exp)  #querry out that row and send as a reply
        return reply

rep=qt("ns-aws-2", gid, 2)        #reply stored will be in dictionary form

print(rep['gname'])            #to fetch the value of gname and rating attribute from that dictionary
print(rep['rating'])