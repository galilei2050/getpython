# Include datetime module
import datetime

# Timepoint of program start
now = datetime.datetime.now()

# Get today week day
weekday = now.weekday()

# Is today friday
# Here we make a comparison by operator == and assignment result to variable is_today_friday
# Why friday is 4th day?
is_today_friday = weekday == 4

# Try it
# print(type(is_today_friday))
# And this
# print(type(weekday))

if not is_today_friday:
   print("Nope today is not Friday")
   exit(1)

# Same for day of month
today_is_13 = now.day == 13

if not today_is_13:
   print("Today is not 13")
   exit(1)

print("Today is Friday 13!")
