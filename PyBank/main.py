import os
import csv

csvpath = os.path.join('..', 'Resources', 'budget_data.csv')
totalmonths=0
netprofitloss=0
profitlosschange=[]


with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader)
    for row in csvreader:
        if totalmonths==0:
            totalmonths+=1
            netprofitloss=netprofitloss+int(row[1])
            previousprofitloss=int(row[1])
        else:
            totalmonths+=1
            netprofitloss=netprofitloss+int(row[1])
            currprofitloss=int(row[1])
            change=currprofitloss-previousprofitloss
            profitlosschange.append(change)
            previousprofitloss=int(row[1])
"""
print("Financial Analysis")
print("-----------------------------------------")
print(f"Total Months : {totalmonths}")
print(f"Total : ${netprofitloss}")
print("Average Change : $", round(sum(profitlosschange)/len(profitlosschange),2))

"""
print(f"Total Months = {totalmonths}")
print(f"Net Profit Loss = {netprofitloss}")
print("Lenght of list ",len(profitlosschange))
print("Sum of values in a list ",sum(profitlosschange))
print("Max value in a list ",max(profitlosschange))
print("Min value in a list ",min(profitlosschange))
print(profitlosschange)

            
        
        
        