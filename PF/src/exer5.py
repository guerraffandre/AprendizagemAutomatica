from createData import ImportData, ReadJson
import time
import random
from datetime import date, datetime
import numpy as np
import matplotlib.pyplot as plt
from models.DataToShow import DataToShow
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import csv

def ConvertSexoToNum(sexoStr):
    if sexoStr == "Masculino":
        return 0
    elif sexoStr == "Feminino":
        return 1
    else:
        return "UNKOW"

def ConvertIdadeToNum(idadestr):
    if len(idadestr) == 3:
        return idadestr[:2]
    elif len(idadestr) == 4:# =>12
        return idadestr[2:]
    elif len(idadestr) == 5:# 12-25
        return idadestr[3:]
    else:
        return "UNKOW"

regAcidentes = ReadJson()
csvStr = "cvAnomatricula,aVelocidadelocal,cvSexo,cvIdade\n"
for dado in regAcidentes:
    try:
        x = str(int(dado.condutoresVeiculos[0].Anomatricula)) + "," + str(int(dado.acidentes[0].Velocidadelocal)) + "," + str(int(ConvertSexoToNum(dado.condutoresVeiculos[0].Sexo))) + "," + str(int(ConvertIdadeToNum(dado.condutoresVeiculos[0].Idade))) + "\n"
        csvStr += x  
    except:
        a=0

with open("C:/AAESCOLA/AprendizagemAutomática/PF/src/exer5Data.csv", "w", encoding='utf-8') as file:
    file.write(csvStr)

df = pd.read_csv(r'C:/AAESCOLA/AprendizagemAutomática/PF/src/exer5Data.csv' )

correlations = df.corr()
sns.heatmap(correlations)
plt.show()
        
