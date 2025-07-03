# import threading
# import time


# start_time = time()

# time_limit = 30
# end_time = start_time + time_limit


# class KeyboardThread(threading.Thread):

#     def __init__(self, input_cbk = None, name='keyboard-input-thread'):
#         self.input_cbk = input_cbk
#         super(KeyboardThread, self).__init__(name=name, daemon=True)
#         self.start()

#     def run(self):
#         while True:
#             self.input_cbk(input()) #waits to get input + Return

# showcounter = 0 #something to demonstrate the change

# def my_callback(inp):
#     #evaluate the keyboard input
#     print('You Entered:', inp, ' Counter is at:', showcounter)

# #start the Keyboard thread
# kthread = KeyboardThread(my_callback)

# while True:
#     #the normal program executes without blocking. here just counting up
#     showcounter += 1

# https://stackoverflow.com/questions/2408560/non-blocking-console-input

import threading
from time import time
import datetime
from random import randint

multiplication_factor_1_range = (2, 12)
multiplication_factor_2_range = (2, 100)

def generate_multiplication_problem():
    factor_1 = randint(*multiplication_factor_1_range)
    factor_2 = randint(*multiplication_factor_2_range)
    ans = factor_1 * factor_2
    return factor_1, factor_2, ans

score = 0

start_time = time()

time_limit = 20
end_time = start_time + time_limit
print(datetime.datetime.fromtimestamp(start_time))
print(datetime.datetime.fromtimestamp(end_time))

class KeyboardThread(threading.Thread):

    def __init__(self, input_cbk = None, name='keyboard-input-thread'):
        self.input_cbk = input_cbk
        self.user_ans = None
        super(KeyboardThread, self).__init__(name=name, daemon=True)
        self.start()

    def run(self):
        while True:
            factor_1, factor_2, ans = generate_multiplication_problem()
            print(f"{factor_1} x {factor_2} = ")
            user_ans = self.input_cbk(input()) #waits to get input + Return
            if user_ans != str(ans):
                print('wrong!')
            else:
                print('correct')

showcounter = 0 #something to demonstrate the change

def my_callback(inp):
    #evaluate the keyboard input
    print('You Entered:', inp, ' Counter is at:', datetime.datetime.fromtimestamp(time()))

    # if inp != str(ans):
    #     print('wrong!')
    # else:
    #     print('correct')
    return inp
        # pass

#start the Keyboard thread
kthread = KeyboardThread(my_callback)

while True:
    #the normal program executes without blocking. here just counting up
    # print(kthread.user_ans) # Tried to see if there was a way to access the input from the callback
    if time() >= end_time:
        print(datetime.datetime.fromtimestamp(time()))
        print("Game over!")
        
        break
    # showcounter += 1
