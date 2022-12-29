from Funcs import ImportData, ReadJson
import time
import random
from datetime import date, datetime
import numpy as np
import matplotlib.pyplot as plt
from models.DataToShow import DataToShow

Y = 2000
seasons = [('winter', (date(Y,  1,  1),  date(Y,  3, 20))),
           ('spring', (date(Y,  3, 21),  date(Y,  6, 20))),
           ('summer', (date(Y,  6, 21),  date(Y,  9, 22))),
           ('autumn', (date(Y,  9, 23),  date(Y, 12, 20))),
           ('winter', (date(Y, 12, 21),  date(Y, 12, 31)))]

def get_season(now):
    if isinstance(now, datetime):
        now = now.date()
    now = now.replace(year=Y)
    return next(season for season, (start, end) in seasons if start <= now <= end)

maxRowsToRead = 100
        
regAcidentes = ReadJson()

dataToGraphMain = []        
maxRowsToReadAux = 0
for regAcidente in regAcidentes:
    for condutoresVeiculo in regAcidente.condutoresVeiculos:
        dataToGraphHasType = False
        maxRowsToReadAux += 1
        
        for typeDataAux2 in dataToGraphMain:
            if typeDataAux2.tipoAcidente == condutoresVeiculo.InfCompaAcçõeseManobras:
                dataToGraphHasType = True
                    
        if dataToGraphHasType == False:
            aux = DataToShow()
            aux.tipoAcidente = condutoresVeiculo.InfCompaAcçõeseManobras
            if get_season(datetime.strptime(condutoresVeiculo.Datahora, '%Y:%m:%d %H:%M:%S')) == "winter":
                aux.countEstacoes[0] = aux.countEstacoes[0] + 1
                aux.inverno += 1                
            elif get_season(datetime.strptime(condutoresVeiculo.Datahora, '%Y:%m:%d %H:%M:%S')) == "spring":
                aux.countEstacoes[1] = aux.countEstacoes[1] + 1
                aux.primavera += 1
            elif get_season(datetime.strptime(condutoresVeiculo.Datahora, '%Y:%m:%d %H:%M:%S')) == "summer":
                aux.countEstacoes[2] = aux.countEstacoes[2] + 1
                aux.verao += 1
            elif get_season(datetime.strptime(condutoresVeiculo.Datahora, '%Y:%m:%d %H:%M:%S')) == "autumn":
                aux.countEstacoes[3] = aux.countEstacoes[3] + 1
                aux.outono += 1
            dataToGraphMain.append(aux)
        else:            
            for typeDataAux in dataToGraphMain:                
                if typeDataAux.tipoAcidente == condutoresVeiculo.InfCompaAcçõeseManobras:
                    if get_season(datetime.strptime(condutoresVeiculo.Datahora, '%Y:%m:%d %H:%M:%S')) == "winter":
                        typeDataAux.countEstacoes[0] = typeDataAux.countEstacoes[0] + 1
                        typeDataAux.inverno += 1                
                    elif get_season(datetime.strptime(condutoresVeiculo.Datahora, '%Y:%m:%d %H:%M:%S')) == "spring":
                        typeDataAux.countEstacoes[1] = typeDataAux.countEstacoes[1] + 1
                        typeDataAux.primavera += 1
                    elif get_season(datetime.strptime(condutoresVeiculo.Datahora, '%Y:%m:%d %H:%M:%S')) == "summer":
                        typeDataAux.countEstacoes[2] = typeDataAux.countEstacoes[2] + 1
                        typeDataAux.verao += 1
                    elif get_season(datetime.strptime(condutoresVeiculo.Datahora, '%Y:%m:%d %H:%M:%S')) == "autumn":
                        typeDataAux.countEstacoes[3] = typeDataAux.countEstacoes[3] + 1
                        typeDataAux.outono += 1
    
plt.figure(figsize=(10,8))
barWidth = 0.25
tiposAcidente = []
inverno = []
primavera = []
verao = []
outono = []
for dado in dataToGraphMain:
    if dado.tipoAcidente == "Não identificada":
        continue
    tiposAcidente.append(dado.tipoAcidente)
    
    inverno.append(dado.countEstacoes[0])
    primavera.append(dado.countEstacoes[1])
    verao.append(dado.countEstacoes[2])
    outono.append(dado.countEstacoes[3])
 
r1 = np.arange(len(tiposAcidente))
r2 = [x + barWidth for x in r1]
r3 = [x + barWidth for x in r2]
r4 = [x + barWidth for x in r3]

plt.bar(r1, inverno, color="#ff0000", width=barWidth, label="inverno")
plt.bar(r2, primavera, color="#0000ff", width=barWidth, label="primavera")
plt.bar(r3, verao, color="#666666", width=barWidth, label="verao")
plt.bar(r4, outono, color="#000000", width=barWidth, label="outono")
    
plt.xlabel('Tipos acidentes')
plt.xticks([r + barWidth for r in range(len(tiposAcidente))], tiposAcidente,rotation='vertical')
plt.ylabel('Numero de acidentes')
plt.title('Representação do numero de acidentes por estações')
plt.legend()
plt.show()

"""
valor tratado foi o valor não definido porque é irrelevante

tendo em conta os dados fornecidos que so vão de janeiro a maio, apenas demostra 2 barras, sendo estas do inverno e primavera

concluir os resultados do grafico
"""