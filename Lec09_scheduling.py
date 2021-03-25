"""
import sched, time

s = sched.scheduler(time.time, time.sleep)

def do_something(sc):
    print('timer executed')
    s.enter(5, 3, do_something, (sc,)) # enter(delay, priority, action, argument=(), kwargs=_sentinel):

s.enter(5, 3, do_something, (s,))
s.run()

"""

##################################################################
# Selenium 실습 - https://sacko.tistory.com/14?category=643535
##################################################################
import time
import datetime
import threading


count = 0
init_time = time.time()


def timer_routine(interval):
    global count
    count += 1
    print('\n{} times - {:.1f} elapsed'.format(count, time.time()-init_time))

    timer = threading.Timer(interval, timer_routine, (interval,))   # iterable data type

    if count < 5:
        timer.start()

t1 = datetime.now()
delay_time = (60 - (t1.minute)) * 60
threading.Timer(5, timer_routine, (3,)).start()
for i in range(1,30):
    print(i, end=' ')
    time.sleep(1)

