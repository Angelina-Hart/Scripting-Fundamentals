# Write your code here
inp = int(input("Days you have been driving:"))
years=inp//365
remyear=inp%365
weeks=remyear//7
remweek=remyear%7
print("You have been driving for:")
print("Years:", years)
print("Weeks:", weeks)
print("Days:", remweek)
