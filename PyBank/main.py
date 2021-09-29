import os
import csv
import sys

csvpath = os.path.join('Resources', 'budget_data.csv') #create path for the file to be analyzed

totalmonths=0 # Intialize variable to get count for Total months
netprofitloss=0 # Intialize variable to capture net profit/loss
profitlosschange={} #Intialize Empty dictionary. Will be used to capture month and change


with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',') #Read csv with ',' as delimiter
    next(csvreader) #skip header row
    for row in csvreader: # Loop through all rows in the file
        if totalmonths==0: # After header, if it is the first row in the file i.e First month in the file
            totalmonths+=1 # Increment month count by 1
            netprofitloss=netprofitloss+int(row[1]) # Increment new profit/loss by the amount on the 1st row i.e 1st month on the file
            previousprofitloss=int(row[1]) # Since it is the 1st month,no chnage can be calculated yet.
            #so store this as previous month profit/loss for next months change calculation.Store it as a int
        else: # For all other rows in the file, i.e not first month in the file
            totalmonths+=1 # Increment month count by 1
            netprofitloss=netprofitloss+int(row[1]) # Increment new profit/loss by the amount for the current month (i.e row)
            currprofitloss=int(row[1]) # Store current month(i.e row) profit/loss amunt
            change=currprofitloss-previousprofitloss # Calcualte change of profit/loss for the current month
            # Add key value pair of (month,change) to dictionary. Month as key and Change as value.Update method of dictionary updates value if exists else adds it
            profitlosschange.update({row[0]:change}) 
            previousprofitloss=int(row[1]) # Store current month's (i.r row's) profit/loss to calculate next month's (i.e next row's) change.

# Calcualte Greatest Increase in Profit
maxmonth = max(profitlosschange,key=profitlosschange.get) # Gets key (i.e Month) from the dictionary with maximum value (i.e change)
GreatestProfitIncrease=profitlosschange[maxmonth] # Gets Value (i.e change) with key (i.e month) of maximum month

# Calcualte Greatest Decrease in Profit
minmonth = min(profitlosschange,key=profitlosschange.get) # Gets key (i.e Month) from the dictionary with minimum value (i.e change)
GreatestProfitDecrease=profitlosschange[minmonth] # Gets Value (i.e change) with key (i.e month) of minimum month

# calcualte average of change 
# sum of dictionary values (i.e change) divided by length of dictionary. Then round to 2 decimal places
avgchange=round(sum(profitlosschange.values())/len(profitlosschange),2) 

# Print to terminal
print("\nFinancial Analysis\n")
print("-----------------------------------------\n")
print(f"Total Months : {totalmonths}\n")
print(f"Total : ${netprofitloss}\n")
print(f"Average Change : ${avgchange}\n")
print(f"Greatest Increase in Profits: {maxmonth} (${GreatestProfitIncrease})\n")
print(f"Greatest Decrease in Profits: {minmonth} (${GreatestProfitDecrease})")

#Print to file
# Reference to print to a file instead of terminal,https://stackabuse.com/writing-to-a-file-with-pythons-print-function/
filepath = os.path.join('Analysis', 'PyBankAnalysis.txt') #create path for the file to be written
sys.stdout=open(filepath,"w") #Open file in write mode and set sys.stdout as file handler, this will print to a file instead of terminal
print("\nFinancial Analysis\n")
print("-----------------------------------------")
print(f"Total Months : {totalmonths}\n")
print(f"Total : ${netprofitloss}\n")
print(f"Average Change : ${avgchange}\n")
print(f"Greatest Increase in Profits: {maxmonth} (${GreatestProfitIncrease})\n")
print(f"Greatest Decrease in Profits: {minmonth} (${GreatestProfitDecrease})")
sys.stdout.close() # Close the file handler, so that next print can happen on the terminal.


            
        
        
        