import csv
import os

path=r'C:\Users\trevo\Desktop\python-challenge\PyBank\budget_data.csv'

with open(path, newline='') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',') 
    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")
    num_of_months=0
    net_value=0

    #variables to assist in finding average change
    list_of_changes=[]
    last_value=0
    current_value=0
    

    #variables to assist in finding max profit
    maximum_profit=0
    current_profit=0
    profit_key=0
    profit_counter=0

    #variables to assist in finding max loss
    max_loss=0
    current_net_loss=0
    loss_key=0

    for row in csvreader:
        #counts how many months
        print(int(row[1]))
        net_value=net_value+int(row[1]) 
        num_of_months+=1

        #creates a variable that holds the change of revenue from month to month
        last_value=current_value
        current_value=int(row[1])
        current_net_revenue=current_value-last_value
        list_of_changes.append(current_net_revenue)

        #finds the greatest increase in revenue
        if(current_net_revenue>maximum_profit):
            maximum_profit=current_net_revenue
            profit_key=row[0]
        
        #finds the greatest decrease in revenue
        if(current_net_revenue<max_loss):
            max_loss=current_net_revenue
            loss_key=row[0]
        

   
    print(f"List {list_of_changes}")
    sum_of_change=0
    counter=0
    for value in list_of_changes:
        sum_of_change=sum_of_change+value
        counter+=1

    average_change= (sum_of_change/(len(list_of_changes)))
    print("ANALYSIS")
    print(" ----------------------------")
    print(f"Total Number of Months {num_of_months}")
    print(f"Total : ${net_value}")
    print(f"Average Change: {average_change}")
    print(f"Greatest Increase in Profits: {profit_key} with {maximum_profit}" )
    print(f"Greatest Decrease in Revenue: {loss_key} with {max_loss}")

    out_file=open("out_file.txt","w")

    out_file.write("ANALYSIS")
    out_file.write("\n ----------------------------")
    out_file.write(f"\n Total Number of Months {num_of_months}")
    out_file.write(f"\n Total : ${net_value}")
    out_file.write(f"\n Average Change: {average_change}")
    out_file.write(f"\n Greatest Increase in Profits: {profit_key} with {maximum_profit}" )
    out_file.write(f"\n Greatest Decrease in Revenue: {loss_key} with {max_loss}")
    


