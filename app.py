
from enum import Enum, unique, auto

class Month:
    def __init__(self, numDays):
        self.numDays = numDays
    
    """
        Months of the year are stupid, here's how they work:
        if the year is divisible by 400, or it is not divisible by 100 and it is divisible by 4, then its a leap 
        year and february has 29 days, otherwise february has 28 days.
        otherwise if the month is before august and its index is odd it has 31 days, otherwise it has 30 days.
        otherwise if the month is before august and its index is event it has 30 days, otherwise it has 31 days.
    """
    @classmethod
    def set(cls, index, year):
        if index == 2: # if february
            if year % 400 == 0 or (year % 100 != 0 and year % 4 == 0): # if leap year
                return cls(29) # february has 29 days
            else:
                return cls(28) # else february has 28 days
        elif index < 8: # else if before august
            return cls(31 if index % 2 == 1 else 30) # 31 days if odd month else 30
        else:
            return cls(30 if index % 2 == 1 else 31) # 30 days if odd month else 31

SUNDAY = 1
MONDAY = 2
TUESDAY = 3
WEDNESDAY = 4
THURSDAY = 5
FRIDAY = 6
SATURDAY = 7

currentWeekDay = SATURDAY
prevThanksgivingBirthdayYear = 0

def rotateWeekDay():
    global currentWeekDay
    if currentWeekDay == SATURDAY:
        currentWeekDay = SUNDAY
    else:
        currentWeekDay += 1

def isThanksgiving(monthIndex, weekDay):
    global thursdayCounter
    if monthIndex == 11:
        if weekDay == THURSDAY:
            thursdayCounter += 1
            if thursdayCounter == 4:
                return True
    return False

for year in range(0, 4001): # iterate by year
    for monthIndex in range(1, 13): # iterate by month
        currentMonth = Month.set(monthIndex, year) # set month so we know how many days to iterate thru
        thursdayCounter = 0 # reset thursdayCounter
        for day in range(1, currentMonth.numDays + 1): # for each day in the month
            if isThanksgiving(monthIndex, currentWeekDay): # if it's thanksgiving
                if day == 23: # if its birthday
                    print("Thanksgiving birthday in " + str(year) + "! That's a change of " + str(year - prevThanksgivingBirthdayYear) + ".")
                    prevThanksgivingBirthdayYear = year
            rotateWeekDay() # change the weekday for next iteration

