import datetime

# now = str(datetime.datetime.now()).split()[1]
# print(now[:5])

minute = datetime.datetime.now().minute
hour = datetime.datetime.now().hour
print(f"{hour}:{minute}")
