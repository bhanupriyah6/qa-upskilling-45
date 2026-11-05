bill=float(input("Enter the total bill amount: "))
tip_percentage=float(input("Enter the tip percentage you want to give: "))  
people=int(input("Enter the number of people to split the bill: "))
tip_amount=(bill*tip_percentage)/100
total_amount=bill+tip_amount
share=total_amount/people
print("The total amount is:", total_amount)
print("Each person should pay:", share)