
import os
import sys
import csv
import argparse

#Add input arguments for command prompt
parser = argparse.ArgumentParser()
parser.add_argument("sub", help="subject number")
#parser.add_argument("ses_s", help="input starting session number - input 2 digit format'XX'")
#parser.add_argument("ses_e", help="input ending session number - input 2 digit format'XX'")
args, unknown = parser.parse_known_args()


#Define subject and session label
subject_label = args.sub
session_start = 1
session_end = 1

#etract cumilative reward from the .csv file
#counter = '01'
#while counter <= session_end:
 #   if counter < 10:
  #      session_label = f"0{counter}"
   # else:
    #    session_label = str(counter)
files = os.listdir(f"loki_GitRepo/data/BIDS/sub-0790/ses-01/func")
for file in files:
    if(file.find('.tsv')>0):
        os.rename(f'loki_GitRepo/data/BIDS/sub-0790/ses-01/func/{file}.tsv',f'loki_GitRepo/data/BIDS/sub-0790/ses-01/func/{file}')
    #counter = counter + 1
