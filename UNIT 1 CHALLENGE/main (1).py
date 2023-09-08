def print_leap_year(year):
    if(year % 4==0):
        print(year,"is a leap year")
    else:
        print(year," is not a leap year")
year=int(input("enter the  year"))
print_leap_year(year)