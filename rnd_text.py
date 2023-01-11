import random
import time
import datetime
import pandas as pd

def file2_write():
    "CSC507 Milestone 2. creates/opens file2.txt and writes 1000 integers on a new line"
    
    count = 0
    file = open("file2.txt", "w")
    
    while count <= 999999:
        file.write(str(random.randint(0,1_000_000)))
        print("",file=file)
        count += 1
        
    file.close()

def timed_file2_write():
    '''CSC507 Milestone 3. Prints start and end times as well as execution time'''
    
    current_time = datetime.datetime.now()
    print(f'Start time: {current_time}')
    
    start_time = time.time()
    
    file2_write()
    
    current_time = datetime.datetime.now()
    print(f'End time: {current_time}')
    print("--- %s seconds execution time ---" % round((time.time()- start_time),3))
    
def pandas_newfile1():
    '''CSC507 Milestone 4. Loads file1.txt into a dataframe, multiplies each line by 2, and outputs to new text file'''
    
    current_time = datetime.datetime.now()
    print(f'Start time: {current_time}')
    
    start_time = time.time()
    
    df = pd.read_csv("file1.txt", sep=" ", header=None)
    double_df = df * 2
    double_df[0].to_csv("newfile1_pandas.txt", index = False, header= None)
    
    current_time = datetime.datetime.now()
    print(f'End time: {current_time}')
    print("--- %s seconds execution time ---" % round((time.time()- start_time),3))
    
def line_by_line_newfile1():
    '''CSC507 Milestone 4. Reads file1.txt line by line, multiplies each line by 2, and outputs to new text file'''
    
    current_time = datetime.datetime.now()
    print(f'Start time: {current_time}')
    
    start_time = time.time()
    
    count = 0
    file = open("file1.txt", "r")
    newfile = open("newfile1_lines.txt", "w")
    
    for line in file:
        line = int(line) * 2
        newfile.write(str(line))
        print("",file=newfile)
        
    file.close()
    newfile.close()
    
    current_time = datetime.datetime.now()
    print(f'End time: {current_time}')
    print("--- %s seconds execution time ---" % round((time.time()- start_time),3))
    
    
def split():
    '''CSC507 Milestone 4. Splits file1.txt evenly into 2 files'''
    lines_per_file = 500000
    smallfile = None
    with open('file1.txt') as bigfile:
        for lineno, line in enumerate(bigfile):
            if lineno % lines_per_file == 0:
                if smallfile:
                    smallfile.close()
                small_filename = 'small_file_{}.txt'.format(lineno + lines_per_file)
                smallfile = open(small_filename, "w")
            smallfile.write(line)
        if smallfile:
            smallfile.close()
            
def split_newfile1():
    '''CSC507 Milestone 4. Splits file1.txt into 2, creates dataframes for each,
    multiplies each line by 2, and outputs to new text file. 2nd half of file is appended'''
    
    current_time = datetime.datetime.now()
    print(f'Start time: {current_time}')
    
    start_time = time.time()
    
    split()
    
    df1 = pd.read_csv("small_file_500000.txt", sep=" ", header=None)
    double_df1 = df1 * 2
    double_df1[0].to_csv("newfile1_split.txt", index = False, header= None)
    
    df2 = pd.read_csv("small_file_1000000.txt", sep=" ", header=None)
    double_df2 = df2 * 2
    double_df2[0].to_csv("newfile1_split.txt", mode = 'a', index = False, header= None)
    
    current_time = datetime.datetime.now()
    print(f'End time: {current_time}')
    print("--- %s seconds execution time ---" % round((time.time()- start_time),3))
