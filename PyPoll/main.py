import os
import csv
import sys

csvpath = os.path.join('Resources', 'election_data.csv') #create path for the file to be analyzed
totalvotes=0 #Intialize variable to hold total votes,set it to 0.
candidatevotes={} # Intiaize dictionary to capture candidate and votes. With Candidate as Key and Votes as Value.

with open(csvpath) as csvfile: # open the file in the path
    csvreader = csv.reader(csvfile, delimiter=',') #Read csv with ',' as delimiter
    next(csvreader) #skip header row
    for row in csvreader: # Loop through all rows in the file
        if row[2] not in candidatevotes.keys(): # if Candidate does not exists in dictionary key
            candidatevotes.update({row[2]:int(0)}) #Adds Candidate to the dictonary as Key with Value of 0,Update method of dictionary updates value if exists else adds it.
        totalvotes=totalvotes+1 # Increment Vote count by 1
        # For the candidate i.e. row[2] (which is a key in dictionary), it updates the votes i.e. candidatevotes[row[2]] (which is the value in dictionary) by incrementing current value by 1
        #Update uses ({key,value}) syntax. Here it finds row[2] i.e candidate and increments the votes i.e.candidatevotes[row[2]] by 1
        candidatevotes.update({row[2]:candidatevotes[row[2]]+1}) 

# This sorts dictionary items (contents) by descending order of  values (i.e Votes)
# Reference, https://careerkarma.com/blog/python-sort-a-dictionary-by-value/
candidatevotes=sorted(candidatevotes.items(),key=lambda item:item[1],reverse=True)


# Print to terminal
print("\nElection Results\n")
print("---------------------------------\n")
print(f"Total Votes: {totalvotes}\n")
print("---------------------------------\n")
for k,v in candidatevotes: # For key, value i.e Candidate, votes 
    # prints Candidate (i.e Key) name and % Votes,calculated using (Value(i.e Votes)/Total Votes)*100.
    #Format function formats given float value upto 3 decimal places (using '.3f' parameter)
    print(f"{k}: {format((v/totalvotes)*100,'.3f')}% ({v})") 
print("\n---------------------------------")
# Since we Sorted out dictionary(candidatevotes) by descending order of votes the winner is the first key in the dictionary
# To get the first key, Convert the dictionary to a list, which converts it into a list of lists i.e array of lists.
# Then get the first value [0](which is key of the original dictionary) of the first list [0].
print(f"\nWinner: {list(candidatevotes)[0][0]}\n")
print("---------------------------------")

#Print to file
# Reference to print to a file instead of terminal,https://stackabuse.com/writing-to-a-file-with-pythons-print-function/
filepath = os.path.join('Analysis', 'PyPollAnalysis.txt') #create path for the file to be written
sys.stdout=open(filepath,"w") #Open file in write mode and set sys.stdout as file handler, this will print to a file instead of terminal
print("\nElection Results")
print("---------------------------------\n")
print(f"Total Votes: {totalvotes}\n")
print("---------------------------------\n")
for k,v in candidatevotes:
    print(f"{k}: {format((v/totalvotes)*100,'.3f')}% ({v})")
print("\n---------------------------------")
print(f"\nWinner: {list(candidatevotes)[0][0]}\n")
print("---------------------------------")
sys.stdout.close() # Close the file handler, so that print can happen on the terminal.
