import os
import csv

TotalVotes = 0.0

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
print(TotalVotes)

csvfile.close()

PyPoll_csv=os.path.join('Resources','election_data.csv')
#debug line
for x in unique_list:
          print(x)

UListlength = len(unique_list)
#debug line
print(UListlength)

Votes = [0] * UListlength
VotelistLength = len(Votes)
print (VotelistLength)


with open(PyPoll_csv,'r')as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)
    
    for row in csvreader:
      for i in range(len(unique_list)):
          if unique_list[i]==row[2]:
              Votes[i] +=1

for i in range(len(unique_list)):
    print(f'{unique_list[i]} Votes: {Votes[i]}')



        


         

    
    




