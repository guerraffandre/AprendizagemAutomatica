from createData import ImportData, ReadJson
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.pyplot as plt
import pandas as pd
import os
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import cross_val_score
import warnings
warnings.filterwarnings("ignore")

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
        return "UNKNOW"

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



regAcidentes = ReadJson()
csvStr = "cvAnomatricula,aVelocidadelocal,aVelocidadegeral,cvSexo,cvIdade,aSinaisLuminosos,aDiadaSemana,aTipoPiso,aTipoVias,aNumFeridosgravesa30dias,aNumFeridosligeirosa30dia,aCaracterísticasTecnicas1,aCondAderência,aNumMortosa30dias\n"
for dado in regAcidentes:
    try:
        x = str(int(dado.condutoresVeiculos[0].Anomatricula)) + "," + str(int(dado.acidentes[0].Velocidadelocal)) + "," + str(int(dado.acidentes[0].Velocidadegeral)) + "," + str(int(ConvertSexoToNum(dado.condutoresVeiculos[0].Sexo))) + ","+ str(int(ConvertIdadeToNum(dado.condutoresVeiculos[0].Idade))) + "," + str(int(ConvertDiaDaSemana(dado.acidentes[0].DiadaSemana))) + "," + str(int(ConvertSinaisLuminosos(dado.acidentes[0].SinaisLuminosos))) + "," + str(int(ConvertTipoPiso(dado.acidentes[0].TipoPiso))) + ","+ str(int(ConvertTipoVias(dado.acidentes[0].TiposVias)))+ "," + str(int(dado.acidentes[0].NumFeridosgravesa30dias)) + ","  + str(int(dado.acidentes[0].NumFeridosligeirosa30dias)) + ","+ str(int(ConvertCaracteristicasTecnicas(dado.acidentes[0].CaracterísticasTecnicas1))) + ","  + str(int(ConvertConducaoAderencia(dado.acidentes[0].CondAderência))) + ","+ str(int(dado.acidentes[0].NumMortosa30dias)) +"\n"
        csvStr += x  
    except:
        a=0

with open("D:/tudo/Mestrado/IAA/Final/AprendizagemAutomatica/PF/src/data/exer8Data.csv", "w", encoding='utf-8') as file:
    file.write(csvStr)

df = pd.read_csv("D:/tudo/Mestrado/IAA/Final/AprendizagemAutomatica/PF/src/data/exer8Data.csv")

X_train, X_test, y_train, y_test = train_test_split(df.iloc[:, :-1], df.iloc[:,-1], test_size=0.3, random_state=1)
        
X_train.shape, X_test.shape, y_train.shape, y_test.shape

pipeline = make_pipeline(StandardScaler(), RandomForestClassifier(n_estimators=1, max_depth=100))

pipeline.fit(X_train, y_train)

print('Model Accuracy Test: %.2f' % pipeline.score(X_test, y_test))
print('Model Accuracy Train: %.2f' % pipeline.score(X_train, y_train))

scores = cross_val_score(pipeline, X=X_train, y=y_train, cv=2, n_jobs=1)

print('CV accuracy scores: %s' % scores)
print('CV accuracy: %.3f +/- %.3f' % (np.mean(scores),np.std(scores)))

from sklearn.model_selection import StratifiedKFold

kfold = StratifiedKFold(n_splits=8).split(X_train, y_train)
scores = []

'''
for k, (train, test) in enumerate(kfold):
    print(k, train, test)
'''