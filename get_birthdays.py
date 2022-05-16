
from datetime import datetime, timedelta, date


users = [
        {
            "name": "Kate",
            "birthday": datetime(1988, 5, 16)
        },
        {
            "name": "Olesia",
            "birthday": datetime(1966, 5, 22)
        },
         {
            "name": "Katia",
            "birthday": datetime(1966, 5, 22)
        },
        {
            "name": "Sophia",
            "birthday": datetime(1988, 5, 18)
        },
        {
            "name": "Eduard",
            "birthday": datetime(1966, 5, 25)
        },
         {
            "name": "Yevhen",
            "birthday": datetime(1966, 5, 25)
        },
        {
            "name": "Sergii",
            "birthday": datetime(1988, 5, 23)
        },
        {
            "name": "Kyrylo",
            "birthday": datetime(1966, 5, 24)
        },
         {
            "name": "Anna",
            "birthday": datetime(1966, 4, 15)
        }
    ]

for dict in users:
    dict['day'] = ''

# we define the current day and day of week
current_datetime=datetime.now()
current_date = current_datetime.date()
day_of_week_today=current_datetime.weekday()

# we create a list of dates next week saturday to friday
weekdays = []
x = 5
while x < 12:
    weekdays.append(current_date + timedelta(days=x-day_of_week_today))
    x = x + 1

# we create a list of days and month strings to match with the database info on birthdays sat to sun
i = 0
birthday_dates_next_week = []
while i <= 6:
    birthday_dates_next_week.append(weekdays[i].strftime('%d %B'))
    i = i + 1



# we find the bdays that are celebrated next week

output = {"Monday": '',
"Tuesday": '',
'Wednesday': "",
"Thursday": "",
"Friday": ""

}

monday_bday = []
tuesday_bday = []
wednesday_bday = []
thursday_bday = []
friday_bday = []

#we're creatingnew out put dict to store the bdays next week
for dict in users:
    for key, value in dict.items():
        if key == "birthday":
            day_of_week = value.strftime('%A')
            if day_of_week == "Saturday" or day_of_week == "Sunday":
                day_of_week = "Monday"
            dict['day'] = day_of_week
            bday = value.strftime('%d %B')
             
            if bday in birthday_dates_next_week and day_of_week == 'Monday':
                monday_bday.append(dict['name'])
                output["Monday"]=monday_bday

            if bday in birthday_dates_next_week and day_of_week == 'Tuesday':
                tuesday_bday.append(dict['name'])
                output["Tuesday"]=tuesday_bday
            if bday in birthday_dates_next_week and day_of_week == 'Wednesday':
                wednesday_bday.append(dict['name'])
                output["Wednesday"]=wednesday_bday
            if bday in birthday_dates_next_week and day_of_week == 'Thursday':
                thursday_bday.append(dict['name'])
                output["Thursday"]=thursday_bday
            if bday in birthday_dates_next_week and day_of_week == 'Friday':
                friday_bday.append(dict['name'])
                output["Friday"]=friday_bday
                

# we're printing out the values for every key
for k, v in output.items():
    print(k+": "+", ".join(v))
