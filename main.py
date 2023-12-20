import datetime as dt
from datetime import date as date_n
def calcage(d):
    no_of_days=d
    years=no_of_days//365
    months=(no_of_days-years*365)//30
    days=(no_of_days-years*365-months*30)
    print(years,"years",months,"months",days,"days")

def calcdays(date1,date2):
    days=(date1-date2).days
    return calcage(days)

d1=date_n(2023,12,12)
d2=date_n(2022,6,13)
calcdays(d1,d2)