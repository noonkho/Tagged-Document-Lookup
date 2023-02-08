import timeit
# import random
# import math

# from basic import Doc, initalize_basic, brute_force
# from smart import SmartDoc, prime, historic, initalize_smart, smart

# compute basic solution time
def basic_time(n):
    setup_code = '''
import random
from basic import Doc, initalize_basic, brute_force
problem = initalize_basic()
q = random.sample(problem[1], random.randint(10,40))
    '''

    test_code = '''
brute_force(problem[0], problem[1], q)
    '''

    times = timeit.repeat(setup = setup_code,
                          stmt = test_code,
                          repeat = 5,
                          number = n)

    # printing minimum exec. time
    print('Basic solution time: {}'.format(min(times)))


# compute smart solution time
def smart_time(n):
    setup_code = '''
import random
import math
from smart import SmartDoc, prime, historic, initalize_smart, smart
problem = initalize_smart()
q = random.sample(problem[1], random.randint(10,40))
    '''

    test_code = '''
smart(problem[0], problem[1], q)
    '''

    times = timeit.repeat(setup = setup_code,
                          stmt = test_code,
                          repeat = 5,
                          number = n)

    # printing minimum exec. time
    print('Smart solution time: {}'.format(min(times)))


n_list = [100, 200, 500, 1000]
for n in n_list:
    print("When n is: " + str(n))
    basic_time(n)
    smart_time(n)