from models.regAcidente import RegAcidente
from models.acidente import Acidente
from models.condutorVeiculo import CondutorVeiculo
from models.passageiro import Passageiro
from models.peao import Peao
from models.AuxImportData import AuxImportData
from random import randrange
from multiprocessing import Pool
import openpyxl
import os
import jsonpickle

maxRows = 2000
yearsToImport=["2010","2011","2012","2013","2014","2015","2016","2017","2018","2019"]#,"2011","2012","2013","2014","2015","2016","2017","2018","2019"

def ReadJson():
    with open( os.getcwd()  + "\src\data\Data2000.json", 'r') as file:
        json_str = file.read()
        return jsonpickle.decode(json_str)
        
def CreateJson(list):
    with open(os.getcwd()  + "\src\data\Data2000.json", "w") as file:
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
    book = openpyxl.load_workbook(os.getcwd()  + "\excel\ISCTE_" + str(year) + "\ISCTE_" + str(year) + ".xlsx")
    sheet0 = book.worksheets[0]
    sheet1 = book.worksheets[1]
    sheet2 = book.worksheets[2]
    sheet3 = book.worksheets[3]
    auxI = 0

    print("Building matrix's " + str(year) + " ...")
    arraySheet1 = []
    arraySheet2 = []
    arraySheet3 = []
    arraySheet4 = []
    for row in sheet0:
        aux = AuxImportData(
        row[0].value,
        row[0].row)
        arraySheet1.append(aux)
    for row in sheet1:
        aux = AuxImportData(
        row[0].value,
        row[0].row)
        arraySheet2.append(aux)
    for row in sheet2:
        aux = AuxImportData(
        row[0].value,
        row[0].row)
        arraySheet3.append(aux)
    for row in sheet3:
        aux = AuxImportData(
        row[0].value,
        row[0].row)
        arraySheet4.append(aux)
    arraySheet1.pop(0)
    arraySheet2.pop(0)
    arraySheet3.pop(0)
    arraySheet4.pop(0)
    print("Building matrix's finished " + str(year) + ".")
    print("len matrix " + str(year) + " to build => " + str(len(arraySheet3)))

    while auxI < maxRows or len(arraySheet3) == 0:
        if len(arraySheet3) == 0:
            break
        print(str(year) + ": " + str(auxI/maxRows*100))
        #print(str(year) + " len array remaining => " + str(len(arraySheet3)))
        rowIndexx = randrange(0, len(arraySheet3))
        row = sheet0[arraySheet3[rowIndexx].rowIndex]
        #print("row index => " + str(rowIndexx) + " - " + str(row[1].value))
                
        #print(str(year) + " adding id => " + str(row[0].value))
        reg = RegAcidente(
            row[0].value,
            GetCondutoresVeiculo(row[0].value, arraySheet1, sheet0),
            GetPassageiros(row[0].value, arraySheet2, sheet1),
            GetAcidentes(row[0].value, arraySheet3, sheet2),
            GetPeoes(row[0].value, arraySheet4, sheet3)
        )
        regAcidentes.append(reg)
        auxI += 1

        arraySheet1 = list(filter(lambda item: item.id != row[0].value, arraySheet1))
        arraySheet2 = list(filter(lambda item: item.id != row[0].value, arraySheet2))
        arraySheet3 = list(filter(lambda item: item.id != row[0].value, arraySheet3))
        arraySheet4 = list(filter(lambda item: item.id != row[0].value, arraySheet4))

    print("Excel " + str(year) + " finished.")
    return regAcidentes
            
def GetCondutoresVeiculo(idAcidente, array, sheet):
    #print("GetCondutoresVeiculo started...")
    cvs = []
    arrayy = list(filter(lambda item: item.id == idAcidente, array))
    for m in arrayy:
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

def GetPassageiros(idAcidente, array, sheet):
    #print("GetPassageiros started...")
    cvs = []
    arrayy = list(filter(lambda item: item.id == idAcidente, array))
    for m in arrayy:
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

def GetAcidentes(idAcidente, array, sheet):
    #print("GetAcidentes started...")
    cvs = []
    arrayy = list(filter(lambda item: item.id == idAcidente, array))
    for m in arrayy:
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

def GetPeoes(idAcidente, array, sheet):
    #print("GetPeoes started...")
    cvs = []
    arrayy = list(filter(lambda item: item.id == idAcidente, array))
    for m in arrayy:
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
