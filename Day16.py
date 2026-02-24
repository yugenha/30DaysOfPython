from datetime import *
print(dir(datetime))
print("Today's date is:", datetime.now())
print("Today's date is:", datetime.now().strftime("%m/%d/%Y, %H:%M:%S"))
# Today is 5 December, 2019
date_str = "5 December, 2019"
date_object = datetime.strptime(date_str, "%d %B, %Y")
print(date_object)
new_year = datetime(2026, 1, 1)
time_to_new_year = new_year - datetime.now()
print("Time to New Year:", time_to_new_year)

past_date = datetime.strptime("1 January 1970", "%d %B %Y")
years_passed = (datetime.now() - past_date).days // 365
print("Years passed since 1 January 1970:", years_passed)
