#Importando bibliotecas e abrindo arquivos necessários
import pandas as pd
import numpy as np
abas= pd.ExcelFile("input_planilhaCanalHolder_20200211.xlsx")
MA=abas.parse('Múltiplos Ações')
FA=abas.parse('Fundamentos Ações')

#Função usada para realizar a inputação de dados numéricos em um dataFrame
def normalizaDf(dataFrame):
    isNumeric=dataFrame._get_numeric_data()
    return (isNumeric-isNumeric.min())/(isNumeric.max()-isNumeric.min())
""" Paramêtros:
        dataFrame: DataFrame usado para a normalização
    Return: DataFrame contendo apenas colunas numéricas, normalizadas"""

    #Merge entre as duas primeiras abas do arquivo input_planilhaCanalHolder_20200211.xlsx
uniaoAbas = pd.merge(MA, FA, on="Nome", how='outer', suffixes=('', '_y'))
uniaoAbas = uniaoAbas.drop(list(uniaoAbas.filter(regex='_y$')), axis=1)

#Removendo espaços nos nomes das colunas
uniaoAbas.columns = [str(c).replace(' ', '_') for c in uniaoAbas.columns]

colunasNumericasNormalizadas=normalizaDf(uniaoAbas)

print(colunasNumericasNormalizadas)