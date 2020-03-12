import schedule
import logging

def print_hello_world():
  logging.debug('I am debug')
  print('Hello World')
  
schedule.every(1).minute.do(print_hello_world)

while True:
    schedule.run_pending()
