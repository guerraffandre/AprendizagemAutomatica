import time
from datetime import date, datetime
import numpy as np
import matplotlib.pyplot as plt
from models.DataToShow import DataToShow
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

#DataJson2
#DataJsonFullData
#DataJsonNoLightInjures

maxRows = 5000
yearsToImport=["2010","2011","2012","2013","2014","2015","2016","2017","2018","2019"]#,"2011","2012","2013","2014","2015","2016","2017","2018","2019"

def ReadJson():
    with open( os.getcwd()  + "\src\data\DataJson5000.json", 'r') as file:
        json_str = file.read()
        return jsonpickle.decode(json_str)
        
def CreateJson(list):
    with open(os.getcwd()  + "\src\data\DataJson5000.json", "w") as file:
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
    book = openpyxl.load_workbook(os.getcwd()  + "\PF\excel\ISCTE_" + str(year) + "\ISCTE_" + str(year) + ".xlsx")
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
    auxRowIndex1 = 1
    auxRowIndex2 = 1
    auxRowIndex3 = 1
    auxRowIndex4 = 1
    for row in sheet0:
        aux = AuxImportData(
        row[0].value,
        auxRowIndex1)
        matrixSheet1.append(aux)
        auxRowIndex1 += 1
    for row in sheet1:
        aux = AuxImportData(
        row[0].value,
        auxRowIndex2)
        matrixSheet2.append(aux)
        auxRowIndex2 += 1
    for row in sheet2:
        aux = AuxImportData(
        row[0].value,
        auxRowIndex3)
        matrixSheet3.append(aux)
        auxRowIndex3 += 1
    for row in sheet3:
        aux = AuxImportData(
        row[0].value,
        auxRowIndex4)
        matrixSheet4.append(aux)
        auxRowIndex4 += 1
    matrixSheet1.pop(0)
    matrixSheet2.pop(0)
    matrixSheet3.pop(0)
    matrixSheet4.pop(0)
    print("Building matrix's finished " + str(year) + ".")
    print("len matrix " + str(year) + " to build => " + str(len(matrixSheet3)))

    while auxI < maxRows or len(matrixSheet3) == 0:
        if len(matrixSheet3) == 0:
            break
        print(str(year) + ": " + str(auxI/maxRows*100))
        #print(str(year) + " len matrix remaining => " + str(len(matrixSheet1)))
        rowIndexx = randrange(0, len(matrixSheet3))
        row = sheet0[matrixSheet3[rowIndexx].rowIndex]
                
        #print(str(year) + " adding id => " + str(row[0].value))
        reg = RegAcidente(
            row[0].value,
            GetCondutoresVeiculo(row[0].value, matrixSheet1, sheet0),
            GetPassageiros(row[0].value, matrixSheet2, sheet1),
            GetAcidentes(row[0].value, matrixSheet3, sheet2),
            GetPeoes(row[0].value, matrixSheet4, sheet3)
        )
        regAcidentes.append(reg)
        auxI += 1

        matrixSheet1 = list(filter(lambda item: item.id != row[0].value, matrixSheet1))
        matrixSheet2 = list(filter(lambda item: item.id != row[0].value, matrixSheet2))
        matrixSheet3 = list(filter(lambda item: item.id != row[0].value, matrixSheet3))
        matrixSheet4 = list(filter(lambda item: item.id != row[0].value, matrixSheet4))

    print("Excel " + str(year) + " finished.")
    return regAcidentes
            
def GetCondutoresVeiculo(idAcidente, matrix, sheet):
    #print("GetCondutoresVeiculo started...")
    cvs = []
    matrixxx = list(filter(lambda item: item.id == idAcidente, matrix))
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
    return cvs
    #print("GetCondutoresVeiculo ended.")

def GetPassageiros(idAcidente, matrix, sheet):
    #print("GetPassageiros started...")
    cvs = []
    matrixxx = list(filter(lambda item: item.id == idAcidente, matrix))
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
    return cvs
    #print("GetPassageiros ended.")

def GetAcidentes(idAcidente, matrix, sheet):
    #print("GetAcidentes started...")
    cvs = []
    matrixxx = list(filter(lambda item: item.id == idAcidente, matrix))
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
    return cvs
    #print("GetAcidentes ended.")

def GetPeoes(idAcidente, matrix, sheet):
    #print("GetPeoes started...")
    cvs = []
    matrixxx = list(filter(lambda item: item.id == idAcidente, matrix))
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
    return cvs
    #print("GetPeoes ended.")

def GetIdade(header, row, numCols):
    for c in range(numCols):
        if header[c].value.__contains__("Gr.Etario"):
            if row[c].value is not None and row[c].value > 0:
                return header[c].value.split("(")[1].split(")")[0]
