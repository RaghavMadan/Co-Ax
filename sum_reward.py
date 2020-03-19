
import os
import sys
import csv
import argparse

#for FW CLI path
#fw_path = open("fw_file_path.txt")
#sys.path.insert(0,fw_path)


#Initiate argparse for user input
parser = argparse.ArgumentParser()
parser.add_argument("sub", help="subject number")
parser.add_argument("ses_s", help="input starting session number - input 2 digit format'XX'")
parser.add_argument("ses_e", help="input ending session number - input 2 digit format'XX'")
parser.add_argument("n_hours", help="input total number of hours in half hour increments 'eg-1, 1.5, 2..'")
args, unknown = parser.parse_known_args()

#initialize and check user arguments
subject_label = args.sub
session_start = int(args.ses_s)
session_end = int(args.ses_e)
total_hours = float(args.n_hours)
if total_hours % 0.5 != 0:
    print ("n_hours can only take multiple of 0.5")
    quit() 

#loop through session files and extract reward value from individual files
counter = session_start
reward_counter = 0 
session_reward = 0
while counter <= session_end:
    if counter < 10:
        session_label = f"0{counter}"
    else:
        session_label = str(counter)
    files = os.listdir(f"loki_GitRepo/data/BIDS/sub-0{subject_label}/ses-{session_label}/beh")
    for file in files:
        if(file.find('.csv')>0):
            with open(f"loki_GitRepo/data/BIDS/sub-0{subject_label}/ses-{session_label}/beh/{file}") as csvDataFile:
                csvReader = csv.reader(csvDataFile)
                data = []
                for row in csvReader:
                    data.append(row)
                    session_reward= data[-1][4][0:4]
    print (f"reward for session {session_label} = {session_reward}")
    reward_counter = reward_counter + float(session_reward)
    counter = counter + 1
total = total_hours*30 + reward_counter
print (f"Total reward for this session = {total}")

