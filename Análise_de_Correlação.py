#!/usr/bin/env python
# coding: utf-8

# In[5]:


#Importando bibliotecas e abrindo arquivos necessários
import pandas as pd
import numpy as np
df= pd.read_excel("input_acoes_NotasFundamentei_20200517.xlsx")
abas= pd.ExcelFile("input_planilhaCanalHolder_20200211.xlsx")
MA=abas.parse('Múltiplos Ações')
FA=abas.parse('Fundamentos Ações')


# In[18]:


#Função usada para realizar a analise de correlação entre uma coluna e as demais de um dataFrame
def analiseCorr(nomeColuna,dataFrame):
    analise=dataFrame.corrwith(dataFrame[nomeColuna]).sort_values(ascending=False)
    count=0
    for a in analise.values:
        analise.values[count]=round(a,3)
        count+=1
    return analise
""" Paramêtros:
        nomeColuna:String utilizada para localizar a coluna que será analisada em relação as demais
        dataFrame: DataFrame usado para a analise de correlação
    Return: Serie contendo os valores da analise de correlação"""


# In[6]:


#Fazendo alterações no arquivo, removendo espaços nos nomes das colunas
MA.columns = [str(c).replace(' ', '_') for c in MA.columns]
df.columns = [str(c).replace(' ', '_') for c in df.columns]


# In[7]:


#Join das tabelas "Fundamentos ações" e "NotasCanalFundamentei" e um merge entre as duas primeiras abas do arquivo input_planilhaCanalHolder_20200211.xlsx
MA=MA.join(df.set_index("Código_de_Neg."),on="Código_de_Neg.")
uniaoAbas = pd.merge(MA, FA, on="Nome", how='outer', suffixes=('', '_y'))
uniaoAbas = uniaoAbas.drop(list(uniaoAbas.filter(regex='_y$')), axis=1)


# In[8]:


#Removendo registros com dados incompletos, tais dados foram ignorados para a analise de correlação
uniaoAbas.replace('-', np.nan,inplace=True)
uniaoAbas.dropna(inplace=True)


# In[14]:


#Chamando a função principal
analiseCorrelação=analiseCorr("NotaFundamentei20200201",uniaoAbas)


# In[19]:


#Exibindo o resultado da análise, sendo mostrado os valores a partir do terceiro elemento, pois os dois primeiros não interessam
print(analiseCorrelação[2:])


# In[20]:





# In[ ]:




