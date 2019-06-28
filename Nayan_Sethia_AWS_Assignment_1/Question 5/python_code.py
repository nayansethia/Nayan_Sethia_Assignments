import json                        #importing modules
import boto3
import urllib

s3=boto3.client('s3')

def ns_lambda_func(event,context):
     source_buc=event['Records'][0]['s3']['bucket']['name']               #to get the name of source bucket
     key=urlib.unquote_plus(event['Records'][0]['s3']['object']['key']    #to get the key   
     print("Enter the name of destination bucket")                        
     target_buc=input()                     #user input gives name of target bucket
     cp={'Bucket':source_buc,'key':key}      
     k=s3.copy_object(Bucket=target_buc, key=key, CopySource=cp)               #copy function
     if k==1:                                    # if the object has been copied successfully the variable k will be equal to 1
         
        return {
        'statusCode': 200,                      # if copy operation is success then the status returned is 200
        'body': json.dumps('Copying Done')      
          }
     else:
         if Bucket==None:                        # if error occurs due to non existance of target bucket
             return {
             'body':json.dumps('Target bucket doesn't exist....error')   
               }
         else:
              if cp['Bucket']==None:            #if error occurs due to non existance of source bucket
                  return {
                  'body':json.dumps("Source bucket doesn't exist")
                    }
              
              return {                          #if the error is none of the above...
                   'body':json.dumps("Check either key is not correct!!")
                   }
