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
route=route_table.create_route(
     DestinationCidrBlock=


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


sec_group2 = ec2.create_security_group(                             #security group designed for the bastion host
    GroupName='ns-security-2', VpcId=vpc.id)


ec2.authorize_security_group_ingress(
        GroupId=security_group_id,                                  #this is defined so as to allow bastion host to get connected to the ip ranges of my organization
        IpPermissions=[
            
            {'IpProtocol': 'tcp',
             'FromPort': 22,
             'ToPort': 22,
             'IpRanges': [***************]}                        #here each star will represent one ip address to which I want my bastion host to get connected, here these IPs are our organization's IP which I am not supposed to disclose
        ])



bastionhost=ec2.create_instances(                                     #bastion host is created in public_subnet1 and the security group defined above
    ImageId='ami-835b4efa', InstanceType='t2.micro', MaxCount=1, MinCount=1,
    NetworkInterfaces=[{'SubnetId': public_subnet1.id, 'DeviceIndex': 0, 'AssociatePublicIpAddress': True, 'Groups': [sec_group2.group_id]}])



# Create sec group
sec_group = ec2.create_security_group(                             #security group for the instances in the private subnets
    GroupName='ns-security-1', VpcId=vpc.id)




ec2.authorize_security_group_ingress(
        GroupId=security_group_id,                        #this is defined so as to make access of instances into private subnets to bastion host
        IpPermissions=[
            
            {'IpProtocol': 'tcp',
             'FromPort': 22,
             'ToPort': 22,
             'IpRanges': ['bastionhost[unicode('PublicIpAddress')]']}        #here bastion host's ip is given 
        ])



instance1 = ec2.create_instances(                                                # three instances in three private subnets are created and with security group defined above.
    ImageId='ami-835b4efa', InstanceType='t2.micro', MaxCount=1, MinCount=1,
    NetworkInterfaces=[{'SubnetId': private_subnet1.id, 'DeviceIndex': 0, 'AssociatePublicIpAddress': True, 'Groups': [sec_group.group_id]}])


instance2 = ec2.create_instances(
    ImageId='ami-835b4efa', InstanceType='t2.micro', MaxCount=1, MinCount=1,
    NetworkInterfaces=[{'SubnetId': private_subnet2.id, 'DeviceIndex': 0, 'AssociatePublicIpAddress': True, 'Groups': [sec_group.group_id]}])



instance3 = ec2.create_instances(
    ImageId='ami-835b4efa', InstanceType='t2.micro', MaxCount=1, MinCount=1,
    NetworkInterfaces=[{'SubnetId': private_subnet3.id, 'DeviceIndex': 0, 'AssociatePublicIpAddress': True, 'Groups': [sec_group.group_id]}])








