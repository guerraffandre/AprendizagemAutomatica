from Funcs import ImportData
import time
import os

if __name__ == '__main__':
    
    st = time.time()
    ImportData()
    et = time.time()
    print(str(et - st))
    
    with open(os.getcwd()  + "\src\data\ktime.txt", "w", encoding='utf-8') as file:
        file.write(str(et - st))

    os.system("shutdown /s /t 1")
    
    
