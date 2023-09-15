import csv
file_to_load = "Resources/budget_data.csv"

# Initialize variables / placeholders
netchangelist=[]
months_of_change=[]
total_months = 0
total_profit=0
greatest_increase=['',0]
greatest_decrease=['',0]

# Read the csv file
with open(file_to_load) as financial_data:
    csv_reader = csv.reader(financial_data)

    # reading the header
    next(csv_reader)

    # reading the first row
    first_row=next(csv_reader)

    # process first row data
    total_months+=1 # total_months = total_months + 1
    total_profit+=int(first_row[1])
    previousnet=int(first_row[1])

    for row in csv_reader:
        total_months=total_months+1
        total_profit+=int(row[1])

        # calculate net change from previous month
        netchange=int(row[1])-previousnet
        previousnet=int(row[1])
        netchangelist +=[netchange]
        months_of_change.append(row[0])
        
        # calculate increase
        if netchange > greatest_increase[1]:
            greatest_increase[0] = row[0] # replace month name
            greatest_increase[1] = netchange # replace greatest diff.

        # calculate decrease
        if netchange < greatest_decrease[1]:
            greatest_decrease[0] = row[0]
            greatest_decrease[1] = netchange


# calculate average profit/loss
avg_change = sum(netchangelist) / len(netchangelist)
output = (
    f"total months: {total_months}\n"
    f"total_profit: ${total_profit}\n"
    f"average change in profit: ${avg_change:.2f}\n" # format to keep 2 decimals
    f"Greatest Increase in Profits: {greatest_increase[0]} ${greatest_increase[1]}\n"
    f"Greatest Decrease in Profits: {greatest_decrease[0]} ${greatest_decrease[1]}\n"
)
print(output)

with open("Analysis/output.txt", "w") as f:
    print(output,file=f)


