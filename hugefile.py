import multiprocessing
import time
import os

def split_1B(file,num_files):
    '''for use in splitting hugefile1 and 2 into x number of files'''
    
    lines_per_file = int(1_000_000_000 / num_files)
    smallfile = None
    with open(file) as bigfile:
        for lineno, line in enumerate(bigfile):
            if lineno % lines_per_file == 0:
                if smallfile:
                    smallfile.close()
                small_filename = 'small_file_{}.txt'.format(lineno + lines_per_file)
                smallfile = open(small_filename, "w")
            smallfile.write(line)
        if smallfile:
            smallfile.close()
            
def total(file1,file2):
    '''CSC507 Mod8. Opens 2 text files, reads line by line, adds each corresponding
    line, and outputs to totalfile.txt'''
    
    newfile = open("totalfile.txt", "a")
    
    with open(file1) as textfile1, open(file2) as textfile2: 
        for x, y in zip(textfile1, textfile2):
            x = int(x.strip())
            y = int(y.strip())
            line_sum = x + y
            newfile.write(str(line_sum))
            print("",file=newfile)
             
    textfile1.close()
    textfile2.close()
    newfile.close()

if __name__ == "__main__":
    if os.path.exists("totalfile.txt"):
        os.remove("totalfile.txt") 
    
    start_time = time.perf_counter()

    #sets pool to current cpu count (10)
    pool = multiprocessing.Pool(multiprocessing.cpu_count())
    
    #runs total() function in parallel for 10 sets of input files
    pool.starmap(func=total, iterable=[("hugefile1_100M-1.txt","hugefile2_100M-1.txt"),
                                      ("hugefile1_100M-2.txt","hugefile2_100M-2.txt"),
                                      ("hugefile1_100M-3.txt","hugefile2_100M-3.txt"),
                                      ("hugefile1_100M-4.txt","hugefile2_100M-4.txt"),
                                      ("hugefile1_100M-5.txt","hugefile2_100M-5.txt"),
                                      ("hugefile1_100M-6.txt","hugefile2_100M-6.txt"),
                                      ("hugefile1_100M-7.txt","hugefile2_100M-7.txt"),
                                      ("hugefile1_100M-8.txt","hugefile2_100M-8.txt"),
                                      ("hugefile1_100M-9.txt","hugefile2_100M-9.txt"),
                                      ("hugefile1_100M-10.txt","hugefile2_100M-10.txt")])
    
    #releases resources
    pool.close()
    
    finish_time = time.perf_counter()
 
    print(f"Program finished in {round(finish_time-start_time,3)} seconds")