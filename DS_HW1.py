#Your program should define (not prompt) for the following:
#    A value of hourly pay,
#    A percentage rate for his/her commission. (the salesperson gets a percentage of the weekly sales amount)
#Your program should compute the total pay as the sum of the pay based on the number of hours worked times the hourly rate plus the commission. 
#Your program should output the pay based on the hours worked, the commission and the total pay for the week.
#Your program should display output at the end of the program for the following:
#    the total number of hours worked for the week,
#    the weekly salary (based on hourly pay), 
#    the commission for the week (based on weekly sales amount),  
#    the total pay for the week.
#Your program should include Header comments (what the program does) and in-line comments (the major design steps).
#Document the values you chose for the value of hourly pay and percentage rate of commission in your comments as well.

#Pay Calculater

#Hourly Rate
hr=13

#Commission Rate
rate=.25

#Get inputs
hw=int(input("Please input hours worked: "))
sales=int(input("Please input sales amount: "))

#Calculate Pay
hr=hr*hw
sales=sales*rate
sales=int(sales)
total=hr+sales

#Present Results
print("Hours worked this week "+str(hw))
print("Pay for the hour worked $"+str(hr))
print("Commission earned $"+str(sales))
print("Total pay earned $"+str(total))