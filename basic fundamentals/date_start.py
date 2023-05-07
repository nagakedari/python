from datetime import date
from datetime import time
from datetime import datetime
from datetime import timedelta #to work with span of time. To perform mathametical operations on times
import calendar

def main() :
    today = date.today()
    print(today)

    print("Date Components: ", today.day, today.month, today. year)

    print("Week Day: ", today.weekday())

    todayTime = datetime.now()

    print(todayTime)

    time = datetime.time(datetime.now())

    print(time)

    #formatting
    print(todayTime.strftime("The current year is: %Y"))
    print(todayTime.strftime("%a, %d %B, %y"))
    #locale format
    print(todayTime.strftime("Local date and time: %c"))
    print(todayTime.strftime("Local date: %x"))
    print(todayTime.strftime("Local time: %X"))
    #Time formating
    print(todayTime.strftime("Current time: %I:%M:%S %p"))
    print(todayTime.strftime("24- hour time: %H:%M"))

    #time delta
    print(timedelta(days=365, hours=5, minutes=1))

    print("one year from now it will be: "+str(todayTime + timedelta(days=365)))
    print("In 2 days and 3 weeks, it will be: "+str(todayTime + timedelta(days=2, weeks=3)))
    print("one week ago it was " + (todayTime - timedelta(weeks=1)).strftime("%A %B %d, %Y"))
    afd = date(today.year, 4, 1)
    print(afd)
    if afd < today :
        print("April fool's day already went by %d days ago "% ((today-afd).days))
        afd = afd.replace(year=today.year+1)
    time_to_afd = afd-today
    print("It's just ", time_to_afd.days, " days until April Fool's Day")

    # #calendars

    c= calendar.TextCalendar(calendar.SATURDAY)
    textStream = c.formatmonth(2020, 1, 0, 0)
    print(textStream)

    hc = calendar.HTMLCalendar(calendar.SUNDAY)
    ht = hc.formatmonth(2020, 1)
    print(ht)

    # #loop over the days of month

    for i in c.itermonthdays(2020, 6) :
        print(i)
    for name in calendar.month_name :
        print(name)
    for day in calendar.day_name :
        print (day)
    
    print("Team Meetings will be on: ")

    for m in range(1,13):
        cal = calendar.monthcalendar(2021, m)
        weekOne = cal[0]
        weekTwo = cal[1]

        if weekOne[calendar.FRIDAY] != 0 :
            meetDay = weekOne[calendar.FRIDAY]
        else:
            meetDay = weekTwo[calendar.FRIDAY]
        print("%10s %2d" % (calendar.month_name[m], meetDay))
main()