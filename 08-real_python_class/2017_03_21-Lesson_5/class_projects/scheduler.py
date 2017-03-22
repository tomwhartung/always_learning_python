import schedule
import time

from data import get_rates, add_data


def test():
    print( 'getting data...' )
    data = get_rates()
    if data:
        add_data(data)
        print('...got data, len(data):', len(data))


schedule.every().minute.do(test)

while True:
    schedule.run_pending()
    time.sleep(1)
