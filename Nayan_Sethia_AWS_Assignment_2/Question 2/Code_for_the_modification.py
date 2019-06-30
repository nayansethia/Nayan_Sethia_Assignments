import boto3                                                                                            #importing required modules
import json
import pymysql
def update(att):                                                                                        # update function is defined to update the required entries of gender and date attributes
    a=att['gender']                      #variable to store the entry of gender attribute
    b=att['date']                        #variable to store the entry of date attribute

    if a=='M':                           #M is converted to Male and F is converted to female
        att['gender']="Male"
    elif a=='F':
        att['gender']="Female"

    b=b.split('/')                      #to convert the entry of date attribute into the list so as to process it easily
    m=b[0]
    d=b[1]
    y=b[2]
    if int(y)>19:                      #if the year is given greater than 19 then the prefix 19 will be added for example if it is 97 then the entry will be updated as 1997
        y=str(19)+y               
    else:                             #else 20 is added as prefix ex- if yy is 14 then the updation will be 2014
        y=str(20)+y
    att['date']=d+'/'+m+'/'+y
    return att


                                     
def lambda_handler(event,context):             #lamda function
    db=boto3.resource('dynamodb')            
    tb=db.Table('ns-aws2')                    #tb is variable storing fetched table
    reply=tb.scan(AttributesToGet=["gender","date"])           #scanning the table 
    att=reply['items']                                                            #to store the items of table

    updated=update(att)                                 #att is passed as parameter to update function 

    connection = pymysql.connect(host='***********.us-east-1.rds.amazonaws.com',             #to establish connection for commiting the updated entries
                                 user='*******',
                                 password='*********',
                                 db='ns-aws')
    with connection.cursor() as cursor:
         sql="INSERT INTO ns-aws(gender,date) VALUES(%s,%s)"
         cursor.execute(sql, (updated['date'], updated['gender']))

         connection.commit()


    for record in event['Records']:                  #reading the dynamodb table and conversion is done so as to insert it into firehose
        logger.info(record)
        ddbRecord = record['dynamodb']
        logger.info('DDB Record: ' + json.dumps(ddbRecord))
        
        firehoseRecord = converttoredshift(ddbRecord)
        logger.info('Firehose Record: ' + firehoseRecord)
        
        firehose.put_record(DeliveryStreamName=deliveryStreamName, Record={ 'Data': firehoseRecord}) #the updated entries are then stored into firehose i.e redshift
    return 'processed {} records.'.format(len(event['Records']))
def converttoredshift(ddbRecord):
    firehoseRecord = ''
                                                                                          # Parse the NewImage json element
    newImage = ddbRecord['NewImage']
                                                                                          # construct firehose record from NewImage
    firehoseRecord = '{},{},{},{}'.format(newImage['productCode']['S'],
    newImage['MfgDate']['N'],
    newImage['BestByDate']['N'],
    newImage['upc']['S']) + '\n'
    return firehoseRecord 



