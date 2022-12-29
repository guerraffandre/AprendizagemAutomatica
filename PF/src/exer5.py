from exer2 import ImportData, ReadJson
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
import warnings
warnings.filterwarnings("ignore")
"""
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
    elif carga == "Desligada":
        return 2
    elif carga == "Intermitente":
        return 3
    else:
        return "UNKOW"

def ConvertTipoPiso(carga):
    if carga == "Betuminoso":
        return 0
    elif carga == "Betão de cimento":
        return 1
    elif carga == "Calçada":
        return 2
    elif carga == "Terra batida":
        return 3
    else:
        return "UNKOW"

def ConvertTipoVias(carga):
    if carga == "A  - Auto-Estrada":
        return 0
    elif carga == "Arruamento":
        return 1
    elif carga == "EF - Estrada Florestal":
        return 2
    elif carga == "EM - Estrada Municipal":
        return 3
    elif carga == "EN - Estrada Nacional":
        return 4
    elif carga == "ER - Estrada Regional":
        return 5
    elif carga == "IC - Itinerário Complementar":
        return 6
    elif carga == "IP- Itinerário Principal":
        return 7
    elif carga == "PNT - Ponte":
        return 8
    elif carga == "VAR - Variante":
        return 9
    else:
        return "UNKOW"

def ConvertDiaDaSemana(carga):
    if carga == "Domingo":
        return 0
    elif carga == "Segunda-Feira":
        return 1
    elif carga == "Terça-Feira":
        return 2
    elif carga == "Quarta-Feira":
        return 3
    elif carga == "Quinta-Feira":
        return 4
    elif carga == "Sexta-Feira":
        return 5
    elif carga == "Sábado":
        return 6
    else:
        return "UNKOW"

def ConvertCaracteristicasTecnicas(carga):
    if carga == "Estrada sem separador":
        return 0
    elif carga == "Auto-estrada":
        return 1
    else:
        return 2

def ConvertConducaoAderencia(carga):
    if carga == "Com água acumulada na faixa de rodagem":
        return 0
    elif carga == "Com gelo, geada ou neve":
        return 1
    elif carga == "Com gravilha ou areia":
        return 2
    elif carga == "Com lama":
        return 3
    elif carga == "Com óleo":
        return 4
    elif carga == "Húmido":
        return 5
    elif carga == "Seco e limpo":
        return 6
    elif carga == "Molhado":
        return 7
    else:
        return "UNKNOW"

def ConvertFactoresAtmosfericos(carga):
    if carga == "Bom tempo":
        return 0
    elif carga == "Chuva":
        return 1
    elif carga == "Granizo":
        return 2
    elif carga == "Neve":
        return 3
    elif carga == "Nevoeiro":
        return 4
    elif carga == "Nuvem de fumo":
        return 5
    elif carga == "Vento forte":
        return 6
    else:
        return "UNKNOW"

def ConvertNatureza(carga):
    if carga == "Atropelamento com fuga":
        return 0
    elif carga == "Atropelamento de animais":
        return 1
    elif carga == "Atropelamento de peões":
        return 2
    elif carga == "Colisão choque em cadeia":
        return 3
    elif carga == "Colisão com fuga":
        return 4
    elif carga == "Colisão com outras situações":
        return 5
    elif carga == "Colisão com veiculo ou obstáculo na faixa de rodagem":
        return 6
    elif carga == "Colisão frontal":
        return 7
    elif carga == "Colisão lateral com outro veículo em movimento":
        return 8
    elif carga == "Colisão traseira com outro veículo em movimento":
        return 9
    elif carga == "Despiste com capotamento":
        return 10
    elif carga == "Despiste com colisão com veículo imobil. ou obstáculo":
        return 11
    elif carga == "Despiste com dispositivo de retenção":
        return 12
    elif carga == "Despiste com fuga":
        return 13
    elif carga == "Despiste com transposição do dispositivo de retenção lateral":
        return 14
    elif carga == "Despiste sem dispositivo de retenção":
        return 15
    elif carga == "Despiste simples":
        return 16
    else:
        return "UNKNOW"

def ConvertAcessorioPassageiros(carga):
    if carga == "C/ capacete/ cinto segurança":
        return 0
    elif carga == "C/ sistema retenção de crianças":
        return 1
    elif carga == "S/ sistema retenção de crianças":
        return 3
    elif carga == "S/ uso capacete/cinto segurança":
        return 4
    else:
        return "UNKNOW"

def ConvertLesoes30Dias(carga):
    if carga == "Ferido leve":
        return 0
    elif carga == "Morto":
        return 1
    elif carga == "Ferido grave":
        return 3
    elif carga == "Ileso":
        return 4
    else:
        return "UNKNOW"



regAcidentes = ReadJson()
csvStr = "cvAnomatricula,aVelocidadelocal,aVelocidadegeral,cvSexo,cvIdade,aSinaisLuminosos,aDiadaSemana,aTipoPiso,aTipoVias,aNumFeridosgravesa30dias,aNumFeridosligeirosa30dia,aCaracterísticasTecnicas1,aCondAderência,aNumMortosa30dias,aFactoresAtmosféricos,aNatureza,pAcessóriosPassageiro,pLesõesa30dias\n"
for dado in regAcidentes:
    try:
        x = str(int(dado.condutoresVeiculos[0].Anomatricula)) + "," + str(int(dado.acidentes[0].Velocidadelocal)) + "," + str(int(dado.acidentes[0].Velocidadegeral)) + "," + str(int(ConvertSexoToNum(dado.condutoresVeiculos[0].Sexo))) + ","+ str(int(ConvertIdadeToNum(dado.condutoresVeiculos[0].Idade))) + "," + str(int(ConvertDiaDaSemana(dado.acidentes[0].DiadaSemana))) + "," + str(int(ConvertSinaisLuminosos(dado.acidentes[0].SinaisLuminosos))) + "," + str(int(ConvertTipoPiso(dado.acidentes[0].TipoPiso))) + ","+ str(int(ConvertTipoVias(dado.acidentes[0].TiposVias)))+ "," + str(int(dado.acidentes[0].NumFeridosgravesa30dias)) + ","  + str(int(dado.acidentes[0].NumFeridosligeirosa30dias)) + ","+ str(int(ConvertCaracteristicasTecnicas(dado.acidentes[0].CaracterísticasTecnicas1))) + ","  + str(int(ConvertConducaoAderencia(dado.acidentes[0].CondAderência))) + ","+ str(int(dado.acidentes[0].NumMortosa30dias))+ ","+ str(int(ConvertFactoresAtmosfericos(dado.acidentes[0].FactoresAtmosféricos)))+","+ str(int(ConvertNatureza(dado.acidentes[0].Natureza)))+","+ str(int(ConvertAcessorioPassageiros(dado.passageiros[0].AcessóriosPassageiro)))+","+ str(int(ConvertLesoes30Dias(dado.passageiros[0].Lesõesa30dias))) +"\n"
        csvStr += x  
    except:
        a=0

with open(os.getcwd()  + "\PF\src\data\DataJson5000.csv", "w", encoding='utf-8') as file:
    file.write(csvStr)
"""

df = pd.read_csv(os.getcwd()  + "\PF\src\data\DataJson5000.csv")

correlations = df.corr()
sns.heatmap(correlations)
plt.show()
        
