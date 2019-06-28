import boto3
                                                                                                  # create a boto3 client
client = boto3.client('sqs')
                                                                                                  # create the test queue

client.create_queue(QueueName='ns_queue')
                                                                                                   # get a list of queues, we get back a dict with 'QueueUrls' as a key with a list of queue URLs
queues = client.list_queues(QueueNamePrefix='ns_queue')                                            # we filter to narrow down the list
ns_queue_url = queues['QueueUrls'][0]

for i in range(0,100):
      enqueue_response = client.send_message(QueueUrl=ns_queue_url, MessageBody='Hello please copy jenkins from ns-1 to ns-2")
                                                                                                   # the response contains MD5 of the body, a message Id, MD5 of message attributes, and a sequence number (for FIFO queues)
    print('Message ID : ',enqueue_response['MessageId'])
                                                                                                   # next, we dequeue these messages - 10 messages at a time (SQS max limit) till the queue is exhausted.
                                                                                                   # in production/real setup, I suggest using long polling as you get billed for each request, regardless of an empty response
while True:
    messages = client.receive_message(QueueUrl=test_queue_url,MaxNumberOfMessages=10)              # adjust MaxNumberOfMessages if needed
    if 'Messages' in messages:                                                                     # when the queue is exhausted, the response dict contains no 'Messages' key
        for message in messages['Messages']:                                                       # 'Messages' is a list
                                                                                                   # process the messages
            print(message['Body'])
                                                                                                   # next, we delete the message from the queue so no one else will process it again
            client.delete_message(QueueUrl=test_queue_url,ReceiptHandle=message['ReceiptHandle'])
    else:
        print('Queue is now empty')
        break