import random
import time
import datetime

def file2_write():
    "creates/opens file2.txt and writes 1000 integers on a new line"
    
    count = 0
    file = open("file2.txt", "w")
    
    while count <= 999999:
        file.write(str(random.randint(0,1_000_000)))
        print("",file=file)
        count += 1
        
    file.close()

def timed_file2_write():
    '''Prints start and end times as well as execution time'''
    
    current_time = datetime.datetime.now()
    print(f'Start time: {current_time}')
    
    start_time = time.time()
    
    file2_write()
    
    current_time = datetime.datetime.now()
    print(f'End time: {current_time}')
    print("--- %s seconds execution time ---" % round((time.time()- start_time),3))