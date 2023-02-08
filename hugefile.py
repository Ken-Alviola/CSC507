import multiprocessing
import time
import os

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

    # Creates x number of processes
    p1 = multiprocessing.Process(target=total("hugefile1_500M-1.txt","hugefile2_500M-1.txt"))
    p2 = multiprocessing.Process(target=total("hugefile1_500M-2.txt","hugefile2_500M-2.txt"))
    
    process_list = [p1,p2]
    
    # Starts all processes
    for p in process_list:
        p.start()
        
    # Forces all processes to finish before finish timer executes
    for p in process_list:
        p.join()
 
    finish_time = time.perf_counter()
 
    print(f"Program finished in {round(finish_time-start_time,3)} seconds")