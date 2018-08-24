#!/usr/bin/python
#coding=utf-8
import os
import sys
import json
import csv
import pickle
from slackclient import SlackClient

#arguments and declaration
prof = sys.argv[1]
line = Instance Under Maintenance
SLACK_API_TOKEN = "************"
sc = SlackClient(SLACK_API_TOKEN)

#Slack Module
def slack_msg(message):
    sc.api_call("chat.postMessage",channel="#test",text=message)

#main function of check instance under maintenance
ec2_event_report = os.system("aws ec2 describe-instance-status --profile %(prof)s --output json --region eu-west-1 > /tmp/ec2_event_metadata.json" % locals())
with open('/tmp/ec2_event_metadata.json') as ec2_event_data_file:
    ec2_event_data = json.load(ec2_event_data_file)
    length = len(ec2_event_data['InstanceStatuses'])
    for ec2_event_index in range(len(ec2_eveta['InstanceStatuses'])):
        try:
            Instance_id = ec2_event_data['InstanceStatuses'][ec2_event_index]['InstanceId']
            ec2_event_status = os.system("aws ec2 describe-instance-status --profile %(prof)s --output json --instance-ids %(Instance_id)s --region region > /tmp/ec2_event_status.json" % locals())
            with open('/tmp/ec2_event_status1.json') as ec2_event_status_file:
                status_file = json.load(ec2_event_status_file)
                status = status_file['InstanceStatuses'][0]['Events'][0]['Code']
                comp = status_file['InstanceStatuses'][0]['Events'][0]['Description']
                s = statuInstans_file['InstanceStatuses'][0]['InstanceStatus']['Status']
                if "[Completed]" in comp:
                        pass
                else:
                    a="Instance maintenance : %s " %(Instance_id)
                    b="Status :%s" %(status)
                    c="In the Account :  %s" %(prof)
                    ec2_instance_details = os.system("aws ec2 describe-instances --profile %(prof)s --output json --instance-ids %(Instance_id)s --region eu-west-1 > /tmp/ec2_details.json" % locals())
                    with open('/tmp/ec2_details.json') as ec2_details_file:
                            ec2_details_data = json.load(ec2_details_file)
                            for ec2_detail_index in range(len(ec2_details_data['Reservations'][0]['Instances'][0]['Tags'])):
                                try :
                                    val = ec2_details_data['Reservations'][0]['Instances'][0]['Tags'][ec2_detail_index]['Key']
                                    if val == "Hostname":
                                        host = ec2_details_data['Reservations'][0]['Instances'][0]['Tags'][ec2_detail_index]['Value']
                                    else:
                                        pass
                                except (KeyError,IndexError):
                                    pass
                                    s = " "
                                    hostname = " Hostname : %s" %host
                                    msg=a+s+b+s+c+s+hostname
                                    slack_msg(msg)
            except (KeyError,IndexError):
                sts.append("ok")
            finally :
                    if length = len(sts)
                        print " No EC2 maintenance"
                    else :
                        pass
slack_msg(line)
slack_msg(prof)
