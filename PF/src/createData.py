from models.regAcidente import RegAcidente
from models.acidente import Acidente
from models.condutorVeiculo import CondutorVeiculo
from models.passageiro import Passageiro
from models.peao import Peao
from models.AuxImportData import AuxImportData

from random import randrange
from multiprocessing import Pool, Manager
import openpyxl
import os
import jsonpickle
import json

withFullData = True #onde há peoes, passageiros e acidentes nas outra sheets
maxRows = 2
yearsToImport=["2010","2011","2012","2013","2014","2015","2016","2017","2018","2019"]#,"2011","2012","2013","2014","2015","2016","2017","2018","2019"

def ReadJson():
    with open( "D:/tudo/Mestrado/IAA/Final/AprendizagemAutomatica/PF/src/data/DataJson.json", 'r') as file:
        json_str = file.read()
        return jsonpickle.decode(json_str)
        
def CreateJson(list):
    with open(os.getcwd()  + "\PF\src\data\DataJsonFull.json", "w") as file:
        jsonpickle.set_encoder_options('json', sort_keys=True, indent=4)
        frozen = jsonpickle.encode(list, file)
        file.write(frozen)
        
def ImportData():        
    regAcidentes = []
    data_inputs = []
    for year in yearsToImport:
        data_inputs.append(year)
    pool = Pool()
    regAcidentes = pool.map(ReadExcel, data_inputs)
    regAcidentes = [ent for sublist in regAcidentes for ent in sublist]    
    CreateJson(regAcidentes)
    print("READER ENDED.")        
        
def ReadExcel(year):
    print("Excel " + str(year) + " started...")
    regAcidentes = []
    book = openpyxl.load_workbook(os.getcwd()  + "\PF\IAA_Project\ISCTE_" + str(year) + "\ISCTE_" + str(year) + ".xlsx")
    sheet0 = book.worksheets[0]
    sheet1 = book.worksheets[1]
    sheet2 = book.worksheets[2]
    sheet3 = book.worksheets[3]
    auxI = 0

    print("Building matrix's " + str(year) + " ...")
    matrixSheet1 = []
    matrixSheet2 = []
    matrixSheet3 = []
    matrixSheet4 = []
    auxRowIndex1 = 0
    auxRowIndex2 = 0
    auxRowIndex3 = 0
    auxRowIndex4 = 0
    for row in sheet0:
        aux = AuxImportData()
        aux.id = row[0].value
        aux.rowIndex = auxRowIndex1
        matrixSheet1.append(aux)
        auxRowIndex1 += 1
    for row in sheet1:
        aux = AuxImportData()
        aux.id = row[0].value
        aux.rowIndex = auxRowIndex2
        matrixSheet2.append(aux)
        auxRowIndex2 += 1
    for row in sheet2:
        aux = AuxImportData()
        aux.id = row[0].value
        aux.rowIndex = auxRowIndex3
        matrixSheet3.append(aux)
        auxRowIndex3 += 1
    for row in sheet3:
        aux = AuxImportData()
        aux.id = row[0].value
        aux.rowIndex = auxRowIndex4
        matrixSheet4.append(aux)
        auxRowIndex4 += 1
    print("Building matrix's finished " + str(year) + " .")

    idsToRemove = []
    if withFullData == True:
        for m in matrixSheet1:
            if any(x.id == m.id for x in matrixSheet2) == False or any(x.id == m.id for x in matrixSheet3) == False or any(x.id == m.id for x in matrixSheet4) == False:
                idsToRemove.append(m.id)
        for id in idsToRemove:
            matrixSheet1 = list(filter(lambda item: item.id != id, matrixSheet1))
            matrixSheet2 = list(filter(lambda item: item.id != id, matrixSheet2))
            matrixSheet3 = list(filter(lambda item: item.id != id, matrixSheet3))
            matrixSheet4 = list(filter(lambda item: item.id != id, matrixSheet4))
        matrixSheet1.pop(0)
        matrixSheet2.pop(0)
        matrixSheet3.pop(0)
        matrixSheet4.pop(0)
    print("len matrix " + str(year) + " to build => " + str(len(matrixSheet1)))

    while auxI < maxRows or len(matrixSheet1) == 0:
        print(str(year) + " len matrix remaining => " + str(len(matrixSheet1)))
        rowIndexx = randrange(2, len(matrixSheet1))
        row = sheet0[matrixSheet1[rowIndexx].rowIndex]
                
        print(str(year) + " adding id => " + str(row[0].value))
        aux1 = GetCondutoresVeiculo(row[0].value, matrixSheet1, sheet0)
        aux2 = GetPassageiros(row[0].value, matrixSheet2, sheet1)
        aux3 = GetAcidentes(row[0].value, matrixSheet3, sheet2)
        aux4 = GetPeoes(row[0].value, matrixSheet4, sheet3)
        reg = RegAcidente(
            row[0].value,
            aux1,
            aux2,
            aux3,
            aux4
        )
        regAcidentes.append(reg)        
        auxI += 1

        matrixSheet1 = list(filter(lambda item: item.id != row[0].value, matrixSheet1))
        matrixSheet2 = list(filter(lambda item: item.id != row[0].value, matrixSheet2))
        matrixSheet3 = list(filter(lambda item: item.id != row[0].value, matrixSheet3))
        matrixSheet4 = list(filter(lambda item: item.id != row[0].value, matrixSheet4))
        sheet0.delete_rows(matrixSheet1[rowIndexx].rowIndex, 1)
    print("Excel " + str(year) + " finished.")
    return regAcidentes
            
def GetCondutoresVeiculo(idAcidente, matrix, sheet):
    #print("GetCondutoresVeiculo started...")
    cvs = []
    indexMatrixToDelete = []
    auxI = 0
    matrixxx = list(filter(lambda item: item.id != idAcidente, matrix))
    for m in matrixxx:
        if m.id == idAcidente:
            r = sheet[m.rowIndex]            
            cv = CondutorVeiculo(
                r[0].value,
                r[1].value,
                r[2].value,
                r[3].value,
                r[4].value,
                r[5].value,
                r[6].value,
                r[7].value,
                r[8].value,
                r[9].value,
                r[10].value,
                r[11].value,
                r[12].value,
                r[13].value,
                r[14].value,
                r[15].value,
                r[16].value,
                r[17].value,
                r[18].value,
                r[19].value,
                r[20].value,
                r[21].value,
                r[22].value,
                GetIdade(sheet[1], r, 40))
            cvs.append(cv)
            indexMatrixToDelete.append(auxI)
            auxI += 1
    for i in indexMatrixToDelete:
        matrix.pop(i)
    return cvs
    #print("GetCondutoresVeiculo ended.")

def GetPassageiros(idAcidente, matrix, sheet):
    #print("GetPassageiros started...")
    cvs = []
    indexMatrixToDelete = []
    auxI = 0
    matrixxx = list(filter(lambda item: item.id != idAcidente, matrix))
    for m in matrixxx:
        if m.id == idAcidente:
            r = sheet[m.rowIndex]             
            p = Passageiro(
                r[0].value,
                r[1].value,
                r[2].value,
                r[4].value,
                r[5].value,
                r[6].value,
                r[7].value,
                r[8].value,
                r[9].value,
                GetIdade(sheet[1], r, 28))
            cvs.append(p)
            indexMatrixToDelete.append(auxI)
            auxI += 1
    for i in indexMatrixToDelete:
        matrix.pop(i)
    return cvs
    #print("GetPassageiros ended.")

def GetAcidentes(idAcidente, matrix, sheet):
    #print("GetAcidentes started...")
    cvs = []
    indexMatrixToDelete = []
    auxI = 0
    matrixxx = list(filter(lambda item: item.id != idAcidente, matrix))
    for m in matrixxx:
        if m.id == idAcidente:
            r = sheet[m.rowIndex]      
            p = Acidente(
                r[0].value,
                r[1].value,
                r[5].value,
                r[6].value,
                r[7].value,
                r[8].value,
                r[9].value,
                r[10].value,
                r[11].value,
                r[12].value,
                r[13].value,
                r[14].value,
                r[15].value,
                r[16].value,
                r[17].value,
                r[18].value,
                r[19].value,
                r[20].value,
                r[21].value,
                r[22].value,
                r[23].value,
                r[24].value,
                r[25].value,
                r[26].value,
                r[27].value,
                r[28].value,
                r[29].value,
                r[30].value,
                r[31].value,
                r[32].value,
                r[33].value,
                r[34].value,
                r[35].value,
                r[36].value,
                r[37].value,
                r[38].value,
                r[39].value,
                r[40].value,
                r[41].value,
                r[42].value)
            cvs.append(p)
            indexMatrixToDelete.append(auxI)
            auxI += 1
    for i in indexMatrixToDelete:
        matrix.pop(i)
    return cvs
    #print("GetAcidentes ended.")

def GetPeoes(idAcidente, matrix, sheet):
    #print("GetPeoes started...")
    cvs = []
    indexMatrixToDelete = []
    auxI = 0
    matrixxx = list(filter(lambda item: item.id != idAcidente, matrix))
    for m in matrixxx:
        if m.id == idAcidente:
            r = sheet[m.rowIndex]      
            p = Peao(
                r[0].value,
                r[1].value,
                r[2].value,
                r[3].value,
                r[4].value,
                r[5].value,
                r[7].value,
                r[8].value,
                r[9].value,
                r[10].value,
                r[11].value,
                GetIdade(sheet[1], r, 30))
            cvs.append(p)
            indexMatrixToDelete.append(auxI)
            auxI += 1
    for i in indexMatrixToDelete:
        matrix.pop(i)
    return cvs
    #print("GetPeoes ended.")

def GetIdade(header, row, numCols):
    for c in range(numCols):
        if header[c].value.__contains__("Gr.Etario"):
            if row[c].value > 0:
                return header[c].value.split("(")[1].split(")")[0]