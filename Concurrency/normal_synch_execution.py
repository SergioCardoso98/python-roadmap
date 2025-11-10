import time
start_time = time.time()
def do_something():
    print('Starting to do something')
    time.sleep(2)
    print('Finished doing something')

do_something()#executes this it takes 2secs
do_something()#then executes this it takes 2secs
do_something()#then executes this it takes 2secs
#total time arround 6sec
end_time = time.time()
print('All somethings were done')
print(f"Execution time: {end_time - start_time:.6f} seconds")
