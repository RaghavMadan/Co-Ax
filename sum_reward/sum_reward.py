
import os
import sys
import csv
import argparse

#Add input arguments for command prompt
parser = argparse.ArgumentParser()
parser.add_argument("sub", help="subject number")
parser.add_argument("ses", help="session number - input 2 digit format'XX'")
#parser.add_argument("ses_start", help="input starting session number - input 2 digit format'XX'")
#parser.add_argument("ses_end", help="input ending session number - input 2 digit format'XX'")
args, unknown = parser.parse_known_args()


#Define subject and session label
subject_label = args.sub
session_label = f"ses-{args.ses}"
#session_start = f"ses-{args.ses_start}"
#session_end = f"ses-{args.ses_end}"

#etract cumilative reward from the .csv file
files = os.listdir(f"loki_GitRepo/data/BIDS/sub-0{subject_label}/{session_label}/beh")
for file in files:
    if(file.find('.csv')>0):
        with open(f"loki_GitRepo/data/BIDS/sub-0{subject_label}/{session_label}/beh/{file}") as csvDataFile:
            csvReader = csv.reader(csvDataFile)
            data = []
            for row in csvReader:
                data.append(row)
            session_reward= data[-1][4][0:4]
            total = 30.0 + float(session_reward)
            print (f"Total reward for this session = {total}")

