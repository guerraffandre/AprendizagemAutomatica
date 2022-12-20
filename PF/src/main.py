from createData import ImportData, ReadJson
import time
import numpy as np
import matplotlib.pyplot as plt
from models.DataToShow import DataToShow

maxRowsToRead = 100
        
if __name__ == '__main__':
    
    data = ReadJson()
    
    dataToGraph = []
    maxRowsToReadAux = 0
    for dado in data:
        dataToGraphHasType = False
        maxRowsToReadAux += 1
        if maxRowsToReadAux == 100:
            break
        
        for dataToGrap in dataToGraph:
            if dataToGrap.tipoAcidente == dado.condutoresVeiculos[0].InfCompaAcçõeseManobras:
                dataToGraphHasType = True
                    
        if dataToGraphHasType == False:
            dts = DataToShow()
            dts.tipoAcidente = dado.condutoresVeiculos[0].InfCompaAcçõeseManobras
            #inverno
            if "1000:12:22 00:00:00" < dado.condutoresVeiculos[0].Datahora < "3000:03:21 23:59:59":
                dts.count[0] += 1
            #primavera  
            elif "1000:03:22 00:00:00" < dado.condutoresVeiculos[0].Datahora < "3000:06:21 23:59:59":
                dts.count[1] += 1
            #verao  
            elif "1000:06:22 00:00:00" < dado.condutoresVeiculos[0].Datahora < "3000:09:22 23:59:59":
                dts.count[2] += 1
            #outono  
            elif "1000:09:23 00:00:00" < dado.condutoresVeiculos[0].Datahora < "3000:12:21 23:59:59":
                dts.count[3] += 1
            dataToGraph.append(dts)
        else:            
            for dataToGrap in dataToGraph:                
                if dataToGrap.tipoAcidente == dado.condutoresVeiculos[0].InfCompaAcçõeseManobras:
                    #inverno
                    if "1000:12:22 00:00:00" < dado.condutoresVeiculos[0].Datahora < "3000:03:21 23:59:59":
                        dataToGrap.count[0] += 1
                    #primavera  
                    elif "1000:03:22 00:00:00" < dado.condutoresVeiculos[0].Datahora < "3000:06:21 23:59:59":
                        dataToGrap.count[1] += 1
                    #verao  
                    elif "1000:06:22 00:00:00" < dado.condutoresVeiculos[0].Datahora < "3000:09:22 23:59:59":
                        dataToGrap.count[2] += 1
                    #outono  
                    elif "1000:09:23 00:00:00" < dado.condutoresVeiculos[0].Datahora < "3000:12:21 23:59:59":
                        dataToGrap.count[3] += 1
            
        
        #print(dado.condutoresVeiculos[0].InfCompaAcçõeseManobras)
        #dataToGraph.sort(key=lambda x: x.condutoresVeiculos[0].InfCompaAcçõeseManobras, reverse=True)
        #Datahora
    
    # Gráfico sobre notas de 3 alunos nas provas do semestre
    #1-inverno 2-primavera 3-verao 4-outono
    notas_pedro = [8, 9, 7, 8]
    notas_maria = [5, 10, 6, 9]
    notas_jose  = [7, 7, 5, 8]
    

    # Definindo a largura das barras
    barWidth = 0.25

    # Aumentando o gráfico
    plt.figure(figsize=(10,5))

    # Definindo a posição das barras
    r1 = np.arange(4)
    r2 = [x + barWidth for x in r1]
    r3 = [x + barWidth for x in r2]
    
    # Criando as barras
    plt.bar(r1, notas_pedro, color='#6A5ACD', width=barWidth, label='Pedro')
    plt.bar(r2, notas_maria, color='#6495ED', width=barWidth, label='Maria')
    plt.bar(r3, notas_jose, color='#00BFFF', width=barWidth, label='José')
    
    # Adiciando legendas as barras
    plt.xlabel('Provas')
    plt.xticks([r + barWidth for r in range(len(notas_pedro))], ['Prova 1', 'Prova 2', 'Prova 3', 'Prova 4'])
    plt.ylabel('Notas')
    plt.title('Representação das notas de 3 alunos em 4 provas do semestre')
    
    # Criando a legenda e exibindo o gráfico
    plt.legend()
    plt.show()
    