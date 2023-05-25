import sys
def is_leap_year(year):
    if year%100==0 and year %400==0:
        return 1
    elif year%100!=0 and year%4==0:
        return 1
    else:
        return 0
def date_validator(date:list):
    if len(date[2])==4:
        if int(date[1]) in [1,3,5,7,8,10,12]:
            if int(date[0])<=31:
                return 1
        elif int(date[1]) ==2:
            if is_leap_year(int(date[2])):
                if int(date[0]) <= 29:
                    return 1
                else:
                    return 0
            else:
                if int(date[0]) <=28:
                    return 1
                else:
                    return 0
        elif int(date[1]) in [4,6,9,11]:
            if int(date[0]) <= 30:
                return 1
            else:
                return 0
        else:
            return 0
    else:
        return 0

if __name__ =="__main__":
    print("WELCOME TO DATE CHECKER .")
    print("\n\n for exit enter 0")
    while True:
        date_check = input("enter a date[dd/mm/yy]: ").split("/")
        if date_check==["0"]:
            sys.exit(0)
        elif date_validator(date_check):
            print("input date is correct.")
        else:
            print("!invalid date .i can check any date format and tell if given date is right or not.")
            
