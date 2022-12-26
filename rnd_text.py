import random

def file2_write():
    "creates/opens file2.txt and writes 1000 integers on a new line"
    
    count = 0
    file = open("file2.txt", "w")
    
    while count <= 999:
        file.write(str(random.randint(0,1_000_000)))
        print("",file=file)
        count += 1
        
    file.close()