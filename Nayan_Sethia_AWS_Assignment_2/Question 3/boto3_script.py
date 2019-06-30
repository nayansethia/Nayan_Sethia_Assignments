import boto3                                                                         #importing modules
ec2 = boto3.resource('ec2')                  
                 
vpc = ec2.create_vpc(CidrBlock='192.168.0.0/16')                                  #creating vpc in default region here it is us-east-1

vpc.create_tags(Tags=[{"Key": "Name", "Value": "ns-vpc"}])                    #name of vpc will be ns-vpc
vpc.wait_until_available()


                                                                               # create then attach internet gateway to vpc this is will allow the interaction with systems outside vpc
ig = ec2.create_internet_gateway()
vpc.attach_internet_gateway(InternetGatewayId=ig.id)


                                                                                  # create a route table and a public route  
route_table = vpc.create_route_table()
route = route_table.create_route(                                                #creation of public route
    DestinationCidrBlock='0.0.0.0/0',
    GatewayId=ig.id
)


# create subnet
public_subnet1 = ec2.create_subnet(CidrBlock='192.168.1.0/24', VpcId=vpc.id, AvailabiltyZone="us-east-1a")            #creation of subnet in us-east-1a

public_subnet2 = ec2.create_subnet(CidrBlock='192.168.2.0/24', VpcId=vpc.id, AvailabiltyZone="us-east-1b")        #creation of subnet in us-east-1b

public_subnet3 = ec2.create_subnet(CidrBlock='192.168.3.0/24', VpcId=vpc.id, AvailabiltyZone="us-east-1c")     #creation of subnet in us-east-1c

private_subnet1 = ec2.create_subnet(CidrBlock='192.168.4.0/24', VpcId=vpc.id, AvailabiltyZone="us-east-1a")          #creation of subnet in us-east-1a
private+subnet2=ec2.create_subnet(CidrBlock='192.168.5.0/24', VpcId=vpc.id, AvailabiltyZone="us-east-1b")            #creation of subnet in us-east-1b

private_subnet3=ec2.create_subnet(CidrBlock='192.168.6.0/24', VpcId=vpc.id, AvailabiltyZone="us-east-1c")          #creation of subnet in us-east-1c

# associate the route table with the subnet
route_table.associate_with_subnet(SubnetId=public_subnet1.id)                     #the created route table is associated with the subnets which we want to make public
route_table.associate_with_subnet(SubnetId=public_subnet2.id)            
route_table.associate_with_subnet(SubnetId=public_subnet3.id)

# Create sec group
sec_group = ec2.create_security_group(                             #security group associated with vpc
    GroupName='ns-security', VpcId=vpc.id)
sec_group.authorize_ingress(
    CidrIp='0.0.0.0/0',
    IpProtocol='icmp',
    FromPort=-1,
    ToPort=-1
)


