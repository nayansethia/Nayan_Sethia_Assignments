
import json                                                                   #importing modules
import boto3

pinpoint = boto3.client('pinpoint')                                            #pinpoint object is initialised to send sms


def lambda_handler(event, context):                                            #lambda function
    messages = "Hi this is Nayan"
    pinpoint.send_messages(
        MessageRequest={
            'Addresses': {
                'BOSS_PHONE_NUMBER': {'ChannelType': 'SMS'}                    #destination no.and the channel type
            },
            'MessageConfiguration': {
                'SMSMessage': {
                    'Body': messages,                           # defining the SMSMessage which is going to be sent
                    'MessageType': 'PROMOTIONAL'
                }
            }
        }
    )
