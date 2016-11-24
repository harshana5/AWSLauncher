import boto3
import time

client = boto3.client('ec2',region_name='ap-southeast-2')
ec2 = boto3.resource('ec2',region_name='ap-southeast-2')

security_group = ec2.SecurityGroup('sg-a0e6f0c4')
launch = ec2.create_instances(DryRun=False,
                     ImageId='ami-d97e40ba',
                     InstanceType='t2.micro',
                     MinCount=1,
                     MaxCount=1)

time.sleep(30)

response = client.describe_instance_status( InstanceIds=[launch[0].id,])
privateip = ec2.Instance(launch[0].id).private_ip_address


hostfile = open('host','w')
hostfile.write("[windows] \n")
hostfile.write(privateip)






