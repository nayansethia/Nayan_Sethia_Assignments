import boto3                                             #importing boto3 module

db = boto3.resource('dynamodb')                          #accesing dynamodb as db here

table = db.create_table(                                #creating table with db.create_table
    TableName=input("Enter the name of the table: "),         #Specifying the tablename, taking user input
    KeySchema=[                                          #defining keyschema for the table
        { 
            'AttributeName': 'gid',                      #game id                      
            'KeyType': 'HASH'                            # primary key
        },
    ],
    AttributeDefinitions=[                               #defining attribute definitions
        {
            'AttributeName': 'gid',                      #game id
            'AttributeType': 'N'                         #integer type
        }, 
        { 'AttributeName': 'gname',              #name of game
            'AttributeType': 'S'                 #string type
       },
       
       {
            'AttributeName': 'publisher',       #publisher attribute
            'AttributeType': 'S'                #string type
        },
        {
            'AttributeName': 'rating',         #rating attribute
            'AttributeType': 'N'               #string type
        },
        {
            'AttributeName': 'release_date',   #release date of game
            'AttributeType': 'S'               #stirng type
        },

       {
            'AttributeName': 'genere',           #genere of game
            'AttributeType': 'S'                 #string type
        },
          
    ],
    ProvisionedThroughput={                      #read and write operations per unit second for the table
        'ReadCapacityUnits': 2,    
        'WriteCapacityUnits': 2
    }
)

table.meta.client.get_waiter('table_exists').wait(TableName='ns-aws-games')

table = db.Table('ns-aws-games')        #table is the variable storing ns-aws-games
l=[]                                    # a list used to store the values given as input by the user for each row

print("Enter how many rows do you want for the creation of table:")
n=int(input())                       # n will store the no. of entries user want to add

for i in range(n):
    print("Enter the entries for row %d", (i+1))
    print("Enter Game ID:")
    l.append(int(input()))
    print("Enter the name of the game")
    l.append(input())
    print("Enter the publisher of the game:")
    l.append(input())
    print("Enter the rating of the game:")
    l.append(int(input())
    print("Enter the release date of the game:")
    l.append(input())

    print("Enter the genere of the game:")
    l.append(input())                    #after this l will have the following structure:  [gid, gname, publisher, rating, relase_date, genere]

    table.put_item(                      #to put entries into the table
        Item={
            'gid':l[0]
            'gname':l[1]
            'publisher':l[2]
            'rating':l[3]
            'release_date':l[4]
            'genre':l[5]
            }
        )
    l=[]                       # l list is emptied to be reused again
    
    
   

