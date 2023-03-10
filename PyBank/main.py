import csv
import os

input_file = os.path.join("Resources","budget_data.csv")
output_file = os.path.join("Analysis","budget_analysis.txt")

total_months = 0
net_total = 0
month_lists = []
net_change_list = []
greatest_increase = ["",0]
greatest_decrease = ["",9999999999]

with open(input_file) as file:
    csvreader = csv.reader(file)
    # file has a header, code below to exclude 
    header = next(csvreader)
    # first_row is now what represents the data
    first_row = next(csvreader)
    total_months += 1
    # same as : total_months=total_months+1
    # [1] means the data in the second column, [0] would be the date in this case
    net_total += int(first_row[1])
    previous_net = int(first_row[1])

    for line in csvreader:
        total_months += 1
        # instead of "first_row", its now "line"
        net_total += int(line[1])
        # difference between two columns after each other
        net_change = int(line[1]) - previous_net
        previous_net = int(line[1])
        # append will have a list of the differences
        net_change_list.append(net_change)
        month_lists.append(line[0])

        if net_change > greatest_increase[1]:
            greatest_increase[1] = net_change
            greatest_increase[0] = line[0]
        if net_change < greatest_decrease[1]:
            greatest_decrease[1] = net_change
            greatest_decrease[0] = line[0]

avg = sum(net_change_list) / len(net_change_list)

text = (f"""
Financial Analysis
----------------------------
Total Months: {total_months}
Total: ${net_total:,.2f}
Average Change: ${avg:,.2f}
Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]:,.2f})
Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]:,.2f})
""")

print(text)
# w mean write
with open(output_file, 'w') as file:
    file.write(text)