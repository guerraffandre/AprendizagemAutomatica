from createData import ImportData, ReadJson
import time
from datetime import date, datetime
import numpy as np
import matplotlib.pyplot as plt
from models.DataToShow import DataToShow

        
if __name__ == '__main__':
    
    st = time.time()
    ImportData()
    et = time.time()
    print(str(et - st))
    
