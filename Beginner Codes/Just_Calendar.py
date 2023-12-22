import calendar

yy = int(input('Enter the year for calendar: '))

q = input(' You want to show the whole calendar or a month from the calendar? (y/n): ')

if (q == 'y'):
    print(calendar.calendar(yy))
elif (q == 'n'):
    mm = int(input('Enter the month for calendar in mm format: '))
    print(calendar.month(yy, mm))