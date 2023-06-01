"""
Exercise 2
"""

#The Weekday Function
def WeekDay():
    "This program takes a date and shows the corresponding day" 
    while True:
        print('Please enter a date in the form of "mm/dd/yyyy"')
        print('\n (Enter "quit" to end the program):')
        date = input()
        if date == 'quit':
            break
        day = int(date[3:5])
        month = int(date[:2])
        year = int(date[6:])
        Totaldays = (year - 2018 + (year - 2017)//4-(year-2001)//100+(year-2001)//400)%7
        leap=1 if (year%4==0 and year%100!=0) or year%400==0 else 0
        m = [31,28+leap,31,30,31,30,31,31,30,31,30]
        Totaldays+=sum(m[:month-1])+day
        week = ['Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday']
        print(date+' is a '+week[Totaldays%7])
            
WeekDay()   
