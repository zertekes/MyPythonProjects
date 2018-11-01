import datetime
from datetime import date

def main():
    calc_days()
    
def in_start_dates():
    f_year = int(input('Please enter the start year: '))
    f_month = int(input('Please enter the start month: '))
    f_day = int(input('Please enter the start day: '))
    f_d = datetime.date(f_year, f_month, f_day)
    return f_d

def in_ending_dates():
    l_year = int(input('Please enter the ending year: '))
    l_month = int(input('Please enter the ending month: '))
    l_day = int(input('Please enter the ending day: '))
    l_d = datetime.date(l_year, l_month, l_day)
    return l_d

def calc_days():
    f = in_start_dates()
    l = in_ending_dates()
    d = l - f
    print('Between the entered dates ' , d.days, ' days different.')

if __name__ == '__main__': main() 