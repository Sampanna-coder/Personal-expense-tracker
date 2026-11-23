print("============================")
print("  PERSONAL EXPENSE TRACKER")
print("============================")

#Get user information
name= input("Enter your name: ")

#Get expense information

item=input("\n What did you purchase? ")
amount = float(input("Enter the expense amount (NPR): "))

#Display expense details

print("\n================EXPENSE RECORDED================")

print("User: ",name)
print("Purchased Item:",item)
print("Amount: NPR",amount)


print("=================================")
print("Thank you for using the Personal Expense Tracker!")