from createData import ImportData, ReadJson
import time


if __name__ == '__main__':
    
    data = ReadJson()
    
    print(str(data[0].id))
    
    #st = time.time()
    #ImportData()
    #et = time.time()
    #print(str(et - st))
    