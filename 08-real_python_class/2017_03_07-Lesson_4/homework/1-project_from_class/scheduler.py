##
#  Python scheduler (like a crontab but easier to understand)
#
import schedule
import time
from data import get_data, add_data

def test_job():
   print( 'Working.' )

def job():
   data = get_data()
   if data:
      add_data( data )
      print( 'Added some data, presumably successfully.' )

## schedule.every(10).minutes.do( job )
## schedule.every(10).seconds.do( test_job )
## schedule.every(10).seconds.do( job )
schedule.every().hour.do( job )

while True:
   schedule.run_pending()
   time.sleep( 1 )
