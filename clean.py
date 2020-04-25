import pandas as pd 
import numpy as np

#Preparing 'VALUE' column for math computation

a = pd.read_csv('env_ac_ainah_r2_1_Data.csv', thousands = ",").drop(
    columns=["Flag and Footnotes", "UNIT","AIRPOL"])

a['Value'] = pd.to_numeric(a['Value'].str.replace(
    ",","").str.replace(":",""))

#Filtering 28 EU Member States

a = a[(a['GEO']!= "European Union - 27 countries (from 2020)") & (
    a['GEO']!= "Switzerland") & (
    a['GEO']!= "Iceland") & (a['GEO']!= "Norway") & (
    a['GEO']!= "Turkey") & (a['GEO']!= "Serbia")]

#Shortening the name of entities for further analysis        
a['GEO'] = a['GEO'].str.replace(
    " \(until 1990 former territory of the FRG\)","")

a['GEO'] = a['GEO'].str.replace(
    "European Union - 28 countries \(2013-2020\)","European Union")

#Renaming emission level column
a.rename(columns = {'Value':'Emissions'}, inplace=True)
a.reset_index().drop(columns='index')

#Technical note for check
print("\b")
print("Technical note:")
print("\b")
print("(1).Total number of georgraphic entities:", a['GEO'].nunique())
print("Including 28 EU Member States and seperate entry for",
      "the European Union as a whole")
print("\b")
print("(2).Time frame of the dataset include:", a['TIME'].unique().tolist())
print("\b")
print("(3).Total number of economic categories contributing to the emission:", 
      a['NACE_R2'].nunique())
print("Including 21 relevant industries and seperate entry for",
      "total emission from all economic categories")

a.to_csv('sum_10y.csv', index = False)
