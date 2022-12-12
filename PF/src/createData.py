from models.regAcidente import RegAcidente
from models.acidente import Acidente
from models.condutorVeiculo import CondutorVeiculo
from models.passageiro import Passageiro
from models.peao import Peao

from random import randrange
from multiprocessing import Pool, Manager
import openpyxl
import os
import jsonpickle
import json

maxRows = 1100
yearsToImport=["2010","2011","2012","2013","2014","2015","2016","2017","2018","2019"]#,"2011","2012","2013","2014","2015","2016","2017","2018","2019"

def ReadJson():
    with open(os.getcwd()  + "\PF\data.txt", 'r') as file:
        json_str = file.read()
        return jsonpickle.decode(json_str)
        
def CreateJson(list):
    with open(os.getcwd()  + "\PF\data.txt", "w") as file:
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
    print("Excel started...")
    regAcidentes = []
    book = openpyxl.load_workbook(os.getcwd()  + "\PF\IAA_Project\ISCTE_" + str(year) + "\ISCTE_" + str(year) + ".xlsx")
    sheet0 = book.worksheets[0]
    sheet1 = book.worksheets[1]
    sheet2 = book.worksheets[2]
    sheet3 = book.worksheets[3]
    auxI = 0
    while auxI < maxRows:
        row = sheet0[randrange(2, sheet0.max_row)]
        print(str(row[0].value))
        reg = RegAcidente(
            row[0].value,
            GetCondutoresVeiculo(row[0].value, sheet0),
            GetPassageiros(row[0].value, sheet1),
            GetAcidentes(row[0].value, sheet2),
            GetPeoes(row[0].value, sheet3)
        )        
        regAcidentes.append(reg)        
        auxI += 1             
    print("Excel finished.")
    return regAcidentes
            
def GetCondutoresVeiculo(idAcidente, sheet):
    #print("GetCondutoresVeiculo started...")
    cvs = []
    auxI = 0
    rowsToDelete = []
    for r in sheet.iter_rows():
        auxI += 1
        if r[0].value == idAcidente:
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
            rowsToDelete.append(auxI)
    
    for i in rowsToDelete:
        sheet.delete_rows(i, 1)
    return cvs
    #print("GetCondutoresVeiculo ended.")

def GetPassageiros(idAcidente, sheet):
    #print("GetPassageiros started...")
    cvs = []
    auxI = 0
    rowsToDelete = []
    for r in sheet.iter_rows():
        auxI += 1
        if r[0].value == idAcidente:
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
            rowsToDelete.append(auxI)
    
    for i in rowsToDelete:
        sheet.delete_rows(i, 1)
    return cvs
    #print("GetPassageiros ended.")

def GetAcidentes(idAcidente, sheet):
    #print("GetAcidentes started...")
    cvs = []
    auxI = 0
    rowsToDelete = []
    for r in sheet.iter_rows():
        auxI += 1
        if r[0].value == idAcidente:
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
            rowsToDelete.append(auxI)
    
    for i in rowsToDelete:
        sheet.delete_rows(i, 1)
    return cvs
    #print("GetAcidentes ended.")

def GetPeoes(idAcidente, sheet):
    #print("GetPeoes started...")
    cvs = []
    auxI = 0
    rowsToDelete = []
    for r in sheet.iter_rows():
        auxI += 1
        if r[0].value == idAcidente:
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
            rowsToDelete.append(auxI)
    
    for i in rowsToDelete:
        sheet.delete_rows(i, 1)
    
    return cvs
    #print("GetPeoes ended.")

def GetIdade(header, row, numCols):
    for c in range(numCols):
        if header[c].value.__contains__("Gr.Etario"):
            if row[c].value > 0:
                return header[c].value.split("(")[1].split(")")[0]