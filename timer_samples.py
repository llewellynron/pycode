############################################
# #Seconds to d:m:h:s
# time = float(input("Input time in seconds: "))
# day = time // (24 * 3600)
# time = time % (24 * 3600)
# hour = time // 3600
# time %= 3600
# minutes = time // 60
# time %= 60
# seconds = time
# print("d:h:m:s-> %d:%d:%d:%d" % (day, hour, minutes, seconds))

############################################
from datetime import datetime
import pytz
import calendar
from time import strptime       # Use to create a time struct

utcmoment_naive = datetime.utcnow()
utcmoment = utcmoment_naive.replace(tzinfo=pytz.utc)

# print "utcmoment_naive: {0}".format(utcmoment_naive) # python 2
print("utcmoment_naive: {0}".format(utcmoment_naive))
print("utcmoment:       {0}".format(utcmoment))

localFormat = "%Y-%m-%d %H:%M:%S"

timezones = ['US/Eastern', 'America/New_York', 'Europe/Madrid', 'America/Los_Angeles']

for tz in timezones:
    # print(pytz.timezone(tz))
    localDatetime = utcmoment.astimezone(pytz.timezone(tz))
    # print(localDatetime)
    print(f"{tz} \t\t\t {localDatetime.strftime(localFormat)}")
    # print(calendar.timegm(mytimestruct)     # will return epoch time from a time struct
    print("strptime_struct = ",strptime(localDatetime.strftime(localFormat),localFormat))

exit()

# # utcmoment_naive: 2017-05-11 17:43:30.802644
# # utcmoment:       2017-05-11 17:43:30.802644+00:00
# # 2017-05-11 10:43:30
# # 2017-05-11 19:43:30
# # 2017-05-11 13:43:30
# ############################################
# # Time Functions
# ############################################
# import time                     # Ref:  https://docs.python.org/3/library/time.html#module-time
# from datetime import datetime
# print("time.altzone : ", time.altzone)
# print("time.daylight: ", time.daylight)
# print("time.timezone: ", time.timezone)
# print("time.tzname  : ", time.tzname)
#                                                     # epoch time = secs from Jan 1, 1970
# mytime = time.time()                                # returns epoch time with decimals
# print("mytime = ", mytime)
# gmt_timestruct = time.gmtime(mytime)                # Convert epoch time to time struct in GMT
# print("gmtime = ", gmt_timestruct)
# mytime_struct = time.localtime(mytime)              # Convert epoch time to time struct in local time
# print(mytime_struct.tm_gmtoff)                      # print offset
# print(mytime_struct.tm_isdst)                       # is DST
# print("locatime(mytime) struct= ", mytime_struct)
# print("mktime =", time.mktime(mytime_struct))       # Convert time struct to epoch time with no decimals => 1616680890.0
# print("asctime =", time.asctime(mytime_struct))     # Convert time struct to asctime => Thu Mar 25 10:01:30 2021
# #Ref: https://realpython.com/python-time-module/
# print("  ctime =", time.ctime(mytime))              # Convert epoch time to ctime    => Thu Mar 25 10:01:30 2021
# dt = datetime.fromtimestamp(mytime)
# print("dt = ", dt)                                  # dt =  2021-03-25 10:14:35.987175
# # Make custom timestamp:  help(time.strftime) or https://docs.python.org/3/library/time.html#time.strftime
# myts = time.strftime("%Y%m%d-%H%M%S", gmt_timestruct)   # Create TS from Timestruct:
# print("my ts =", myts)                              # my ts = 20210325-141435
# mystr_to_timestruct = time.strptime(time.ctime(mytime), "%a %b %d %H:%M:%S %Y")
# print("my pts =", mystr_to_timestruct)
#
# mytuple=(2021,3,24,21,10,0,0,0,0)
# print(time.mktime(mytuple))
# print(time.localtime(time.mktime(mytuple)))
#
# exit()
############################################
# Time tuples
############################################
import time
time_tuple = (2021, 3, 25, 10, 44, 50, 3, 84, 1)

exit()

############################################
# File timestamps
############################################
import pathlib              # Ref:  https://www.python.org/dev/peps/pep-0428/
import time
fname = pathlib.Path('basics_refresh.py')
assert fname.exists(), f'No such file: {fname}'  # check that the file exists

print(fname.stem, fname.name)
print("stat() = ", fname.stat())
print("stat().st_ctime = ", fname.stat().st_ctime)
print("local time = ", time.asctime(time.localtime(fname.stat().st_ctime)))

exit()

print("ctime = ",fname.stat().st_ctime.asctime())

# import pathlib
# import time
# time.localtime()
from pathlib import Path        # Ref: https://www.python.org/dev/peps/pep-0428/
p = Path('.')
mylist = [ x for x in p.iterdir() if x.is_dir()]
print(mylist)
print(mylist[0])