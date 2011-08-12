
# How many Sundays on the first of the month during the twentieth century?

from datetime import datetime, timedelta
 
count = 0
date = datetime(1901, 1, 1)
delta = timedelta(days=1)
while date < datetime(2001, 1, 1):
  if date.day == 1 and date.weekday() == 6:  count += 1
  date += delta
print 'count: ', count