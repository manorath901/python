import datetime
import pytz


t_now = pytz.timezone('Asia/Kolkata')
now = datetime.datetime.now(t_now)
format = now.strftime("%a %B %d %H:%M:%S %Z %Y")
print(format)