import os
import csv
import numpy 


#Path to collect the data 
PyBank_csv = os.path.join('Resources','budget_data.csv')

MinPandL = float(0)
MinPandL = 0
MaxPandL = float(0)
MaxPandL = 0
TotalPandL = float(0)
TotalPandL = 0
DifList=[]
Counter = 0
AvgPandL = 0
MaxDate = " "
MinDate = " "
SavedTotal = 0.0
#Function for printing
def print_budget_data(datalisted):
   Cnt = int(datalisted["Count"])
   newlist=[]
   newlist.append(datalisted["Differences"])
   for nix in newlist:
        AvgPandL= 0.0
   
   Opens = float(datalisted["First Total"])
   print(Opens)
   AvgPandL = (sum(nix)/Opens)

   print('Financial Analysis')
   print('-------------------------------------------------------------')
   print(f'Total Months: {datalisted["Count"]}')
   print(f'Total:  ${datalisted["Grand Total"]}')
   print(f'Average Change: ${round(AvgPandL,2)}')
   print(f'Greatest Increase in Profits: {datalisted["Max Date"]}  ${datalisted["MaxAmount"]}')
   print(f'Greatest Decrease in Profits: {datalisted["Min Date"]}  ${datalisted["MinAmount"]}')
   
   output_path = os.path.join("Resources","Financial_Analysis.csv")
   with open(output_path, 'w',newline='') as csvfile:
       csvwriter = csv.writer(csvfile, delimiter=',')
       csvwriter.writerow(["Financial Analysis"])
       csvwriter.writerow(["Data Listing","Amounts","Dates"])
       csvwriter.writerow(["Total Months",datalisted["Count"],""])
       csvwriter.writerow(["Total", "${:,.2f}".format(datalisted["Grand Total"]),""])
       csvwriter.writerow(["Average Change","${:,.2f}".format(AvgPandL),""])
       csvwriter.writerow(["Greatest Increase","${:,.2f}".format(datalisted["MaxAmount"]),datalisted["Max Date"]])
       csvwriter.writerow(["Greatest Decrease","${:,.2f}".format(datalisted["MinAmount"]),datalisted["Min Date"]])
       

    #function ends here - add more

#read in the csv file
with open(PyBank_csv,'r') as csvfile:
    #split the string on commas
    csvreader = csv.reader(csvfile, delimiter=',')
    #drop header
    header = next(csvreader)
    FirstTotal = 0.0

    #for loop to read to end of file
    for row in csvreader:
       
       if row[0] != ' ':
            
            if FirstTotal == 0:
                FirstTotal = float(row[1])
            
           
            # check for date, add total, check P&L to see if < or > the current amount
            TDateHolder = row[0]
            # print(DateHolder)
            TPandL = float(row[1])
            #print(PandL)
            TotalPandL = TotalPandL + TPandL
            DifYear = TotalPandL - FirstTotal
            DifList.append(DifYear)
            Counter += 1
            
            if MaxPandL <= TPandL:
                MaxPandL = TPandL
                MaxDate = TDateHolder
                #print(MaxDate)
            if MinPandL >= TPandL:
                MinPandL = TPandL
                MinDate = TDateHolder

            PyBankData = {
                "Grand Total":TotalPandL,
                "Count":Counter,
                "MaxAmount":MaxPandL,
                "Max Date":MaxDate,
                "MinAmount":MinPandL,
                "Min Date":MinDate,
                "First Total":FirstTotal,
                "Differences":DifList

             }

            
print_budget_data(PyBankData)    

        

            
           

