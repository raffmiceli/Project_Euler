import datetime

def daycalc(month,day,year):
    '''
Input date in m/d/y format, returns day of the week.
Returns "mystery" for most nonexistent dates.
    '''
    daystable = ['Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday']
    monthstable = [0,3,3,6,1,4,6,2,5,0,3,5]
    centtable = [6,4,2,0]
    y = int(str(year)[2:])
    c = int(str(year)[0:2])
            
    if year%4 == 0:
        monthstable[0:2] = [-1,2]
    if year%4 != 0 and month == 2 and day >= 29:
        return 'mystery'
    if month > 12 or day > 31:
        return 'mystery'

    w = (day%7 + monthstable[month-1] + (y+y/4)%7 + centtable[c%4])%7
    dayw = daystable[w]

    return dayw

f = 0
for m in range(1,13):
    for y in range(1901,2001):
        day = daycalc(m,1,y)
        if day == 'Sunday':
            f += 1
print f

##count = 0
##for y in range(1901,2001):
##    for m in range(1,13):
##        if datetime.datetime(y,m,1).weekday() == 6:
##            count += 1
##print count
##
##print (len([True for year in range(1901, 2001) for month in range(1,13) if datetime.datetime(year, month, 1).weekday() == 1]))

