#!/usr/bin/python

import boto3

client = boto3.client('autoscaling')
data = open("/home/moosa/userdata.sh","r")

launch_config= client.create_launch_configuration( 
	LaunchConfigurationName='boto3-test', 
	ImageId='ami-b04e92d0',
	KeyName='moosa', 
	SecurityGroups=['sg-8810acf0',],
	InstanceType='t2.micro', 
	AssociatePublicIpAddress=True,
	UserData= data.read()
	)
