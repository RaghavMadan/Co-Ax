
import os
import sys
import csv
import argparse
import re

#Add input arguments for command prompt
parser = argparse.ArgumentParser()
parser.add_argument("sub", help="subject number")
parser.add_argument("ses_s", help="input starting session number - input 2 digit format'XX'")
parser.add_argument("ses_e", help="input ending session number - input 2 digit format'XX'")
args, unknown = parser.parse_known_args()


#Define subject and session label
subject_label = args.sub
session_start = int(args.ses_s)
session_end = int(args.ses_e)

#etract cumilative reward from the .csv file
counter = session_start
while counter <= session_end:
    if counter < 10:
        session_label = f"0{counter}"
    else:
        session_label = str(counter)
    files = os.listdir(f"loki_GitRepo/data/BIDS/sub-0{subject_label}/ses-{session_label}/func")

    for file in files:
        if(file.find('.tsv')>0):
            infile = f"loki_GitRepo/data/BIDS/sub-0{subject_label}/ses-{session_label}/func/{file}"
            with open(infile,'r') as f:
            	data= f.read()
            with open(infile,'w') as f:	
            	f.write(re.sub(r"stim_duration", r"duration", data))
          
            with open(infile,'r') as f:
            	data= f.read()
            with open(infile,'w') as f:	
            	f.write(re.sub(r'stim_onset', r'onset', data))

            with open(infile,'r') as f:
            	data= f.read()
            with open(infile,'w') as f:	
            	f.write(re.sub(r',\s', r'\t', data))

            with open(infile,'r') as f:
            	data= f.read()	
            with open(infile,'w') as f:	
            	f.write(re.sub(r',', r'\t', data))
			
                
    counter = counter + 1
