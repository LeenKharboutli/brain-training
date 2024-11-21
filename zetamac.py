

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


multiplication_range_factor_1 = [2, 12]
multiplication_range_factor_2 = [2, 100]

def generate_multiplication_problem():
    factor_1 = randint(multiplication_range_factor_1[0], multiplication_range_factor_1[1])
    factor_2 = randint(multiplication_range_factor_2[0], multiplication_range_factor_2[1])
    ans = factor_1 * factor_2
    return factor_1, factor_2, ans

while time() <= end_time:
    factor_1, factor_2, ans = generate_multiplication_problem()
    print(f"{factor_1} x {factor_2} = ")
    while input() != str(ans):
        pass


    

    
