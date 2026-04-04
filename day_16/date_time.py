from datetime import datetime

# Question 1
now = datetime.now()
day = now.day
month = now.month
year = now.year
minute = now.minute
timestamp = now.timestamp()
print(f'{day}/{month}/{year}')

# Question 2
t = now.strftime('%m/%d/%Y,%H:%M:%S')
print(t)

# Question 3
datestr = '5 December 2019'
date_given = datetime.strptime(datestr,'%d %B %Y')
print(date_given)

# Question 4
new_year_time = datetime(year=2027,month=1,day=1,hour=0,minute=0,second=0)
time_diff = new_year_time - datetime.now()
print(time_diff)

# Question 5
initial_day = datetime(year=1970, month=1, day=1)

time_difference =  now - initial_day
print('Time difference between 1970 to now is:',time_difference)

# Question 6
''' We can use date time to set a deadline for any task, for example:
Book return deadline for library'''