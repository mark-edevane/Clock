def func():
    x = 1
    y = 3
    z = 14
    return z % y, z // y
#print(func(), 153 % 60)

import time
def time_convert(sec):
 #   print('1 - seconds total =', int(sec))
    mins = sec // 60
   # print('2 - min =', mins)
    sec = sec % 60
   # print('3 - seconds after getting minutes =', int(sec))
    hours = mins // 60
  #  print('4 - hours =', hours)
    mins = mins % 60
  #  print('5 - mins 2 =', mins)
  #  print("Time Lapsed = {0}:{1}:{2}".format(int(hours),int(mins),int(sec)))
    return sec, mins, hours

# input("Press Enter to start")
# start_time = time.time()
# input("Press Enter to stop")
# end_time = time.time()  
# time_lapsed = end_time - start_time
# time_convert(time_lapsed)
print(time_convert(185)[1])