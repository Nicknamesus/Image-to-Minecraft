import time
import random
from block_to_color import find_closest_color_in_json

def json_color_finder():
    sum_time = 0
    tests = 10
    for i in range(tests):
        start_time = time.perf_counter()

        find_closest_color_in_json((random.randint(0,255),random.randint(0,255),random.randint(0,255)))

        end_time = time.perf_counter()

        sum_time += end_time - start_time
    
    avg_time = sum_time / tests
    print("Average time:", avg_time)
    print("for 124x124 picture:", avg_time*124*124)

json_color_finder()