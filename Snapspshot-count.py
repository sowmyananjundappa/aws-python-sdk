#!/usr/bin/python
#coding=utf-8
import os
import sys
import json
import csv
import pickle
import subprocess
from slackclient import SlackClient

#Arguments passed
prof = sys.argv[1]
List = []
owner = sys.argv[2]
line = "No of Snapshots in your AWS Accounts"
slack_msg(line)
SLACK_API_TOKEN = "************"
sc = SlackClient(SLACK_API_TOKEN)

#Slack module to post your output
def slack_msg(message):
    sc.api_call("chat.postMessage",channel="#test",text=message)
    
#main function 
snapshot_count_report = os.system("aws ec2 describe-snapshots --profile %(prof)s --owner-ids %(owner)s --output json  --region eu-west-1 > /tmp/snapshots_metadata.json" % globals())
with open('/tmp/snapshots_metadata.json') as snapshot_file:
    snap_data = json.load(snapshot_file)
    snap_index = len(snap_data['Snapshots'])
    print (snap_index)
    acc = "Accountname:"+ prof
    slack_msg(acc)
    slack_msg(snap_index)
    total = 0
    with open('/tmp/file.txt', 'r') as inp, open('/tmp/output.txt', 'w') as outp:
        for line in inp:
            try:
                num = float(line)
                total += num
                outp.write(line)
                slack_msg(total)
                except ValueError:
