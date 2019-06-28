import boto3                                          #importing boto3 module
from botocore.config import Config                    # importing Config function

boto_config = Config(retries=dict(max_attempts=20))   
client = boto3.client(                                 #specifying the client details as rds in us-east-1 region 
    'rds', region_name='us-east-1', config=boto_config
)
db_name=input("Enter the name of the database you want to use: ")     #here in order to create mysql rds instance, user will supply MySQL
instance_name=input("Enter the instance name: " )
a_s=int(input("Enter the allocated storage: "))                 #Specifies the allocated storage size specified in gibibytes.
db_ic=input("Enter the db instance storage class: ")       #Contains the name of the compute and memory capacity class of the DB instance.
eng=input("Enter the engine you want to use: ")            #Provides the name of the database engine to be used for this DB instance.
usr=input("Enter the master user name: ")                  #Contains the master username for the DB instance.

p=input("Enter the master user passworrd: ")               #Contains the master password for the DB instance.
sg_id=input("Enter the vpc security group ids: ").split()  #Contains the id of vpc security group, a list input, user will separate the names by space

subnet_gname=input("Enter the subnet group name: ")        #Contains the subnet group name

pg_name=input("Enter the parameter group name: ")          #Contains the parameter group name for the DB instance.
per=int(input("Enter the backup retention period: "))      #Contains the backup retention period, interger.
access=input("Enter True to allow public access else False") 
stype=input("Enter the storage type: ")

ns-db = {                                           #a dictionary to contain all the parameters as keys and their values
    "DBName": db_name,
    "DBInstanceIdentifier": instance_name,
    "AllocatedStorage": a_s,
    "DBInstanceClass": db_ic,
    "Engine": eng,
    "MasterUsername": usr,
    "MasterUserPassword": p,
    "VpcSecurityGroupIds": sg_id,
    "DBSubnetGroupName": subnet_gname,
    "DBParameterGroupName": pg_name,
    "BackupRetentionPeriod": per,
    "MultiAZ": True,
    "EngineVersion": "10.0.1",
    "PubliclyAccessible": access
    "StorageType": stype
}
client.create_db_instance(**ns-db)            #function to create rds instance on the basis of the parameters defined in ns-db dictionary above