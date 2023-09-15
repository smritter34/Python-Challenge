import csv
file_to_load = 'Python-challenge/PyPoll/Resources/election_data.csv'
total_votes_list = []
candidate_set = set()

vote = []
candidate_votes_dict= {}
stockham_vote = 0
Doane_vote = 0
DeGette_vote = 0
# Read the csv file
with open(file_to_load) as election_data:
    csv_reader = csv.reader(election_data)

    # reading the header
    next(csv_reader)


    for row in csv_reader:
        total_votes_list.append(row[0])
        candidate_set.add(row[2])
        
        if row[2] == 'Charles Casper Stockham':
            stockham_vote += 1
        elif row[2] == 'Raymon Anthony Doane':
            Doane_vote += 1
        elif row[2] == 'Diana DeGette':
            DeGette_vote += 1



x = round((stockham_vote/len(total_votes_list))* 100, 3)
y = round((Doane_vote/len(total_votes_list))* 100, 3)
z = round((DeGette_vote/len(total_votes_list))* 100,3)

candidate_list = list(candidate_set)

print(candidate_set)

candidate_Stockham = ''
candidate_Doane = ''
candidate_DeGette = ''

for item in candidate_set:
    
    if item == 'Charles Casper Stockham':
        candidate_Stockham = item
    elif item == 'Raymon Anthony Doane':
        candidate_Doane = item
    elif item == 'Diana DeGette':
        candidate_DeGette = item

output = (
"Election results \n------------------------------------------\n"
f"Total Votes: {len(total_votes_list)} \n------------------------------------------\n"
f"{candidate_Stockham}: {x}% ({stockham_vote}) \n{candidate_Doane}: {y}% ({Doane_vote}) \n{candidate_DeGette}: {z}% ({DeGette_vote}) \n------------------------------------------\n"
f"Winner: {candidate_DeGette}"
)


print(output)

with open("Python-challenge/PyPoll/Analysis/output.txt", "w") as f:
    print(output,file=f)