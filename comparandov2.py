import pandas as pd

import numpy as np
import openpyxl
##Local lib


df = pd.read_excel(r"C:\Users\Vladimir\PycharmProjects\comparandoarquivos\Ligação_Não atendida.xlsx")
df1 = pd.read_excel(r"C:\Users\Vladimir\PycharmProjects\comparandoarquivos\Ligação Retornada.xlsx")

df=df.merge(df1, on=['Telefone'], how='outer', suffixes=['', '_'], indicator=True)
df["Retornou?"] = None

df=df.query('_merge == "both" or _merge == "left_only"')



for i, row in df.iterrows():
    if df['_merge'][i] == 'both' and df['Hora'][i] <= df['Hora_'][i]:
        df.loc[i, 'Retornou?'] = 'Retornou'

    elif df['_merge'][i] == 'both' and df['Hora'][i] > df['Hora_'][i]:
        df.loc[i, 'Retornou?'] = 'Não Retornou'

    elif df['_merge'][i] == 'left_only':
        df.loc[i, 'Retornou?'] = 'Não Retornou'

print(df)



df.to_excel("comparativo.xlsx")



