import datetime

data = datetime.date(2025, 11, 8)
today = datetime.date.today()

time = datetime.time(12, 30, 26)
time_now = datetime.datetime.now()
time_now = time_now.strftime("%H:%M:%S %m-%d-%Y")
# print(time_now)
#
# print(data)
# print(today)
# print(time)
# print(time_now)

target_datetime = datetime.datetime(2030,1,2,12,30,26)

current_datetime = datetime.datetime.now()


if target_datetime < current_datetime:
    print("Target date has passed")
else:
    print("Target date has not passed")