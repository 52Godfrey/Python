import os
import csv

list = []
candidate = []
count = []
percent = []

total_votes = 0


csvpath = os.path.join('PyPoll', 'Resources', 'election_data.csv')


with open(csvpath, "r") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    print(csvreader)

    csv_header = next(csvreader)

    for row in csvreader:
        total_votes = total_votes + 1

        list.append(row[2])
    
    for x in set(list):
        candidate.append(x)
        i = list.count(x)
        count.append(i)
        j = (i/total_votes)*100
        percent.append(j)

winner_tally = max(count)
winner_candidate = candidate[count.index(winner_tally)]


print("-"*64)
print(f"ELECTION RESULTS")
print("-"*64)
print(f"Total Votes: {total_votes}")
print("-"*64)
for i in range(len(candidate)):
        print(candidate[i] + ": " + str(round(percent[i], 4)) + "% (" + str(count[i]) + ")")
print("-"*64)
print("The winner is: " + winner_candidate)
print("-"*64)

with open('Analysis.txt', 'w') as text:
    text.write("----------------------------------------------\n")
    text.write(f"ELECTION RESULTS\n")
    text.write("----------------------------------------------\n")
    text.write(f"Total Votes: {total_votes}\n")
    text.write("----------------------------------------------\n")
    for i in range(len(candidate)):
            text.write(candidate[i] + ": " + str(round(percent[i], 4)) + "% (" + str(count[i]) + ")\n")
    text.write("----------------------------------------------\n")
    text.write("The winner is: " + winner_candidate+ "\n")
    text.write("----------------------------------------------\n")