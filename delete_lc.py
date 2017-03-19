#!/usr/bin/python


import boto3

client = boto3.client('autoscaling')

lc=raw_input("Please enter name of launch-configuration to delete:")


if client.delete_launch_configuration(LaunchConfigurationName=lc):
	print "Configuration " + lc + " deleted."
else:
	print "Unable to delete provided launch configuration"

