import schedule

def print_hello_world():
  print('Hello World')
  
schedule.every(1).minute.do(print_hello_world)

while True:
    schedule.run_pending()
