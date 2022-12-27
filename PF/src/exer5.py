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
import os
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

def ConvertSinaisLuminosos(carga):
    if carga == "Inexistentes":
        return 0
    elif carga == "A funcionar normalmente":
        return 1
    else:
        return "UNKOW"

def ConvertTipoPiso(carga):
    if carga == "Betuminoso":
        return 0
    elif len(carga) == 7: #calçada
        return 1
    elif carga == "Terra batida":
        return 2
    else:
        return "UNKOW"

def ConvertTipoVias(carga):
    if carga == "A  - Auto-Estrada":
        return 0
    elif len(carga) > 20 : #IC - Itinerário Complementar
        return 1
    elif carga == "Arruamento":
        return 2
    elif carga == "EM - Estrada Municipal":
        return 3
    elif carga == "EN - Estrada Nacional":
        return 4
    elif carga == "EF - Estrada Florestal":
        return 5
    elif carga == "Outra Via":
        return 6
    else:
        return "UNKOW"

def ConvertDiaDaSemana(carga):
    if carga == "Domingo      ":
        return 0
    elif carga == "Quinta-Feira ":
        return 1
    elif carga == "Quinta-Feira ":
        return 2
    elif len(carga) == 5:  #terca
        return 3
    elif len(carga) == 6:  #sabado
        return 4
    elif carga == "Segunda-Feira":
        return 5
    elif carga == "Sexta-Feira  ":
        return 6
    else:
        return "UNKOW"

regAcidentes = ReadJson()
csvStr = "cvAnomatricula,aVelocidadelocal,aVelocidadegeral,cvSexo,cvIdade,aSinaisLuminosos,aDiadaSemana,aTipoPiso,aTipoVias,aNumFeridosgravesa30dias,aNumFeridosligeirosa30dia\n"
for dado in regAcidentes:
    try:
        x = str(int(dado.condutoresVeiculos[0].Anomatricula)) + "," + str(int(dado.acidentes[0].Velocidadelocal)) + "," + str(int(dado.acidentes[0].Velocidadegeral)) + "," + str(int(ConvertSexoToNum(dado.condutoresVeiculos[0].Sexo))) + "," + str(int(ConvertIdadeToNum(dado.condutoresVeiculos[0].Idade))) + "," + str(int(ConvertSinaisLuminosos(dado.acidentes[0].SinaisLuminosos))) + "," + str(int(ConvertDiaDaSemana(dado.acidentes[0].DiadaSemana))) + "," + str(int(ConvertTipoPiso(dado.acidentes[0].TipoPiso))) + "," + str(int(ConvertTipoVias(dado.acidentes[0].TiposVias)))+ "," + str(int(dado.acidentes[0].Velocidadelocal)) + "," + str(int(dado.acidentes[0].NumFeridosgravesa30dias)) + "," + str(int(dado.acidentes[0].NumFeridosligeirosa30dias)) +"\n"
        csvStr += x  
    except:
        a=0

with open(os.getcwd()  + "\PF\exer5Data.txt", "w", encoding='utf-8') as file:
    file.write(csvStr)

df = pd.read_csv(os.getcwd()  + "\PF\exer5Data.txt")

correlations = df.corr()
sns.heatmap(correlations)
plt.show()
        
