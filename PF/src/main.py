from createData import ImportData, ReadJson
import time
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
        
#if __name__ == '__main__':
regAcidentes = ReadJson()

dataToGraphMain = []        
maxRowsToReadAux = 0
for regAcidente in regAcidentes:
    for condutoresVeiculo in regAcidente.condutoresVeiculos:
        dataToGraphHasType = False
        maxRowsToReadAux += 1
        #if maxRowsToReadAux == 100:
        #    break
        
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
        
    
    #print(dado.condutoresVeiculos[0].InfCompaAcçõeseManobras)
    #dataToGraph.sort(key=lambda x: x.condutoresVeiculos[0].InfCompaAcçõeseManobras, reverse=True)
    #Datahora
# Gráfico sobre notas de 3 alunos nas provas do semestre
#1-inverno 2-primavera 3-verao 4-outono
notas_pedro = [8, 9, 7, 8]
notas_maria = [5, 10, 6, 9]
notas_jose  = [7, 7, 5, 8]

print()

# Definindo a largura das barras
barWidth = 0.25

# Aumentando o gráfico
plt.figure(figsize=(10,5))

# Definindo a posição das barras
r1 = np.arange(4)
r2 = [x + barWidth for x in r1]
r3 = [x + barWidth for x in r2]

# Criando as barras leva o tipo de acidente
plt.bar(r1, notas_pedro, color='#6A5ACD', width=barWidth, label='Pedro')
plt.bar(r2, notas_maria, color='#6495ED', width=barWidth, label='Maria')
plt.bar(r3, notas_jose, color='#00BFFF', width=barWidth, label='José')

# Adiciando legendas as barras
plt.xlabel('Estacoes')
plt.xticks([r + barWidth for r in range(len(notas_pedro))], ['Inverno', 'Primavera', 'Verao', 'Outono'])
plt.ylabel('Acidentes')
plt.title('Representação dos acidentes por estaçoes')

# Criando a legenda e exibindo o gráfico
plt.legend()
plt.show()
    