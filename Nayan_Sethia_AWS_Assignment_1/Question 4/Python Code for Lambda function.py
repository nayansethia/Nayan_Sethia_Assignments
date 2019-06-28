import json
import os                                                              #importing modules

def ns_lambda(event, context):                                         #two parameters event and context are passed, event is an object used to pass an event to lamda handler, context for runtime information
    message = "The user is: "+event['first_name]'+event['last_name']   #concatenation of strings, normal one and those two fetched from event     
    return { 
        'message' : message                                            #returning message
    }  