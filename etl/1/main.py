import connections as conne
import pandas as pd
from common import config
import os

source = conne.database()
parameters = config()['destination']

sqlmaxtl = 'SELECT DimD.FullDateAlternateKey,DimO.OrganizationName,Ds.ScenarioName,DiA.AccountDescription, Facf.Amount \
FROM FactFinance Facf INNER JOIN DimDate DimD ON Facf.DateKey = DimD.DateKey INNER JOIN DimOrganization DimO ON Facf.OrganizationKey = DimO.OrganizationKey INNER JOIN DimScenario Ds ON Facf.ScenarioKey = Ds.ScenarioKey INNER JOIN DimAccount DiA ON Facf.AccountKey = DiA.AccountKey WHERE YEAR(DimD.FullDateAlternateKey) = 2010'

df = source.__execute__(sqlmaxtl)

#print(type(df))
#print(df.columns)
#print(df.head())
#print(df.shape)
#print(df.ndim)
#print(df.tail())
#print(df.dtypes)

print(parameters['path'])

df.to_csv(parameters['path'])