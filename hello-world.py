import schedule
import logging
import sys

print('I am deployed')
logging.error('I am error')
logging.debug('I am debug')


def print_hello_world():
  logging.debug('I am debug')
  print('Hello World')
  sys.stdout.flush()
  
schedule.every(1).minute.do(print_hello_world)

while True:
    schedule.run_pending()
