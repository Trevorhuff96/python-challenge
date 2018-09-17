import csv
import os
from collections import defaultdict

path=r'C:\Users\trevo\Desktop\python-challenge\PyPoll\election_data.csv'

with open(path, newline='') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',') 
    # Read the header row first 
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    num_of_voters=0

    # this will create a dictionary that dynamically stores candidate stats
    # the default dictionary will make it dynamic because it will allow an unkown amount of candidates
    # the key will be the Candidate name and the value will be a counter of how many votes they received
    cand_dict=defaultdict(int)
    for row in csvreader:
        cand_dict[row[2]]+=1
        num_of_voters+=1
    
    out_file=open("out_file.txt","w")

    print("ELECTION RESULTS")
    print("\n ---------------------------------")
    print(f" \n {num_of_voters}")
    print("\n ---------------------------------")

    out_file.write("ELECTION RESULTS")
    out_file.write("\n ---------------------------------")
    out_file.write(f" \n {num_of_voters}")
    out_file.write("\n ---------------------------------")

    # performs calculations on the dictionary
    max_perc=0
    winner=""
    for k,v in cand_dict.items():
        #for each candidate find the percentage of votes they recieved
        perc_votes=(v/num_of_voters)*100
        print(f"{k}: {round(perc_votes,3)}% ({v})")
        out_file.write(f" \n {k}: {round(perc_votes,3)}% ({v})")

        #find the maximum percentage and winner of election
        if(perc_votes>max_perc):
            winner=k
            max_perc=perc_votes

    print("\n ---------------------------------")
    print(f"\n Winner: {winner}")
    print("\n ---------------------------------")

    out_file.write("\n ---------------------------------")
    out_file.write(f"\n Winner: {winner}")
    out_file.write("\n ---------------------------------")
    
