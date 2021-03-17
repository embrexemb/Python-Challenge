import os
import csv
import numpy


Results = []
TotalVotes = 0
print(f'----------------------')
print(f'Election Results')
print(f'----------------------')
PyPoll_csv=os.path.join('Resources','election_data.csv')
with open(PyPoll_csv,'r')as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)
    #get a unique list of candidates
    unique_list = []
    for row in csvreader:
        candidate = row[2]
        TotalVotes +=1
        if candidate not in unique_list:
            unique_list.append(candidate)
print(f'Total Votes: {round(TotalVotes,2)}')
print(f'----------------------')


csvfile.close()

PyPoll_csv=os.path.join('Resources','election_data.csv')
#debug line
#for x in unique_list:
         # print(x)

UListlength = len(unique_list)
#debug line
#print(UListlength)

Votes = [0] * UListlength
VotelistLength = len(Votes)
#print (VotelistLength)


with open(PyPoll_csv,'r')as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)
    
    for row in csvreader:
      for i in range(len(unique_list)):
          if unique_list[i]==row[2]:
              Votes[i] +=1

  

for i in range(len(unique_list)):
    Percentage = ((Votes[i]/TotalVotes)*100)
    print(f'{unique_list[i]}: {round(Percentage,2)}%  ({Votes[i]})')
    
    # create a record list
    Results.append(
        {"Candidate":unique_list[i],
        "WinningPercent":Percentage,
        "VoteCount":Votes[i]
        }
    )
    
print(f'----------------------')



output_path = os.path.join("Resources","Vote_Data.csv")
with open(output_path, 'w',newline='') as csvfile:
    csvwriter=csv.writer(csvfile,delimiter=',')
    csvwriter.writerow(["Election Results"])
    csvwriter.writerow(["Total Votes", (TotalVotes)])
    csvwriter.writerow(["Candidate","Percentage Votes","Votes Cast"])

#for x in Results:
  #  print(x)

#dict.get 
#dict.values




        


         

    
    




