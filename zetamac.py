

# NOTE: we want a timer, automatically set to 120 seconds, but can be configured
# NOTE: we also want to be able to configure the types of questions
# NOTE: 4 types of questions (addition, subtraction, multiplication, division)

# NOTE: while the timer is going, you should be able to keep getting new randomized questions 
# NOTE: we only get a new question if we answer correctly


from time import time
from random import randint


start_time = time()

time_limit = 120
end_time = start_time + time_limit

multiplication_factor_1_range = (2, 12)
multiplication_factor_2_range = (2, 100)

def generate_multiplication_problem():
    factor_1 = randint(*multiplication_factor_1_range)
    factor_2 = randint(*multiplication_factor_2_range)
    ans = factor_1 * factor_2
    return factor_1, factor_2, ans

while time() <= end_time:
    factor_1, factor_2, ans = generate_multiplication_problem()
    print(f"{factor_1} x {factor_2} = ")
    while input() != str(ans):
        pass


    

    
