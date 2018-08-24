import boto3
import json
import sys
import os
import csv

#System arguments and declaration
null = os.system(">/tmp/iam.json")
prof = sys.argv[1]
region = sys.argv[2]

#main function
role_report = os.system("aws iam list-roles --profile (prof)s --region (region)s 1 >> /tmp/iam.json " % globals())
with open('/tmp/iam.json') as iam_file:
    iam_data = json.load(iam_file)
    null_files = os.system(">/tmp/iam_role.csv")
    csvfile = open("/tmp/iam_role.csv", "a")
    whileriter = csv.writer(csvfile)
    writer.writerow(['Role_Name','Trust'])
    for iam_index in range(len(iam_data['Roles'])):
        a = iam_data['Roles'][iam_index]['RoleName']
        print(a)
        writer.writerow([
            str(iam_data['Roles'][iam_index]['RoleName']),
            str(iam_data['Roles'][iam_index]['AssumeRolePolicyDocument']['Statement'][0]['Principal']['AWS'])])
