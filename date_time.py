import time
from datetime import datetime
import calendar

print time.asctime( time.localtime(time.time()) ), time.timezone

print datetime.now()

cal = calendar.month(2014,8)

print cal