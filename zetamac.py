

# # NOTE: we want a timer, automatically set to 120 seconds, but can be configured
# # NOTE: we also want to be able to configure the types of questions
# # NOTE: 4 types of questions (addition, subtraction, multiplication, division)

# # NOTE: while the timer is going, you should be able to keep getting new randomized questions 
# # NOTE: we only get a new question if we answer correctly
import datetime

from time import time
from random import randint
# import tkinter

start_time = time()
print(datetime.datetime.fromtimestamp(start_time))

time_limit = 60
end_time = start_time + time_limit
print(datetime.datetime.fromtimestamp(end_time))

multiplication_factor_1_range = (2, 12)
multiplication_factor_2_range = (2, 100)

def generate_multiplication_problem():
    factor_1 = randint(*multiplication_factor_1_range)
    factor_2 = randint(*multiplication_factor_2_range)
    ans = factor_1 * factor_2
    return factor_1, factor_2, ans

score = 0
# while time() <= end_time:
#     factor_1, factor_2, ans = generate_multiplication_problem()
#     print(f"{factor_1} x {factor_2} = ")
#     while input() != str(ans):
#         if time() >= end_time: 
#             print("Game over!")
#             break
    
#         # pass




# # root = tkinter.Tk()
# # tkinter.Widget(root, "Timer")


import sys
import threading
import queue


def get_user_input(timeout=5):
    # print(prompt, end="", flush=True)

    result_queue = queue.Queue()

    def read_input():

        try:
            user_input = sys.stdin.readline().rstrip("\n")
            result_queue.put(user_input)
        except Exception as e:
            result_queue.put(e)

    input_thread = threading.Thread(target=read_input)
    input_thread.daemon = True
    input_thread.start()

    input_thread.join(timeout)
    if input_thread.is_alive():
        return result_queue.get()
    else:
        return None


while time() <= end_time:
    # Step 1: generate the new problem
    factor_1, factor_2, ans = generate_multiplication_problem()
    print(f"{factor_1} x {factor_2} = ")
    user_input = None
    # Step 2: receive user input 
    while user_input != str(ans):
        time_left = end_time-time()
        print(f"{time_left=}, {end_time=}")
        if time_left <= 0:
            print('game over')
            break
        user_input = get_user_input(timeout=time_left)

        if user_input == ans:
            print("\nInput cancelled due to timeout.")
        else:
            print("You entered:", user_input)
    score +=1

    # Step 3: check user input against answer, 

print(f"Your score: {score}")



    

    
