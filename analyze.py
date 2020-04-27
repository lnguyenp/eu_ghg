# -*- coding: utf-8 -*-
"""
Created on Fri Apr 24 16:45:31 2020

@author: Linh Nguyen
"""

import pandas as pd 
import numpy as np 
import seaborn as sns
import matplotlib.pyplot as plt

a = pd.read_csv('sum_10y.csv')

#Yearly total of GhG emissions in the EU
b = a[(a['NACE_R2'] == "Total - all NACE activities") & (
    a['GEO']=="European Union")].reset_index().drop(columns=['index'])

b.to_csv('total_GhG.csv', index = False)

# # Graph lineplot of total GhG emissions in the EU across years
sns.set(style="darkgrid")
f, ax = plt.subplots(figsize=(14, 6))
sns.set_color_codes("pastel")
ax = sns.lineplot(x="TIME", y="Emissions", data=b)
ax.set_ylabel('Year, 2008-2018')    
ax.set_xlabel('Level of Emission')


#Finding the EU member country that contributed the most in 2009
c = a[(a['NACE_R2'] == "Total - all NACE activities") & (
    a['TIME'] == 2008) & (a['GEO'].str.contains(
        "European Union") == False)]

max2008 = c.groupby(['GEO'],as_index=False).sum().sort_values(
    by = 'Emissions', ascending = False)[0:10]

c.set_index(['GEO'],inplace=True)


#Draw a barplot of top 10 country-emittents in 2008
sns.set(style="darkgrid")
f, bx = plt.subplots(figsize=(12, 6))

bx = sns.barplot(x="Emissions", y="GEO",
                 palette="rocket", data=max2008, 
                 label = "Emission severity",
                 color="c")

bx.legend(ncol=2, loc="lower right", frameon=True)
bx.set(xlim = (0,9*1e8), ylabel= "", xlabel= "")
sns.despine(left=True, bottom=True)

bx.set_title('Top 10 country-polluters in 2008')


#Finding EU member countries that contributed the most in 2018

e = a[(a['NACE_R2'] == "Total - all NACE activities") & (
    a['TIME'] == 2018) & (a['GEO'].str.contains("European Union") == False)]

max2018 = e.groupby(['GEO'],as_index = False).sum().sort_values(
    by = 'Emissions', ascending = False)[0:10]
print(max2018)

#Draw a barplot of top 10 country-emittents in 2018
sns.set(style="darkgrid")
f, ex = plt.subplots(figsize=(12, 6))

ex = sns.barplot(x="Emissions", y="GEO",
                 palette="rocket", data=max2018, 
                 label = "Emission severity",
                 color="c")

ex.legend(ncol=2, loc="lower right", frameon=True)
ex.set(xlim = (0,9*1e8), ylabel="", xlabel="")
sns.despine(left=True, bottom=True)

ex.set_title('Top 10 country-emmitents polluters in 2018')

#Combine plots to see the difference by top polluters
comb_cntr = a[(a['NACE_R2'] == "Total - all NACE activities") & 
              ((a['TIME'] == 2018)| (a['TIME'] == 2008)) &
              (a['GEO'].str.contains("European Union") == False)]

comb_cntr_sorted = comb_cntr.sort_values(
    by = 'Emissions', ascending = False)[0:14]

print(comb_cntr_sorted.head(20))

sns.set(style="darkgrid")
comp1 = sns.catplot(x="Emissions", y="GEO", hue="TIME", 
                    data=comb_cntr_sorted,
                    kind="bar", palette="rocket")

comp1.set(xlim = (0,10*1e8), xlabel = "", ylabel = "")
comp1.despine(left=True, bottom=True)

plt.subplots_adjust(top=0.9, left = 0.01, right = 0.81)
comp1.fig.suptitle('Emission difference by country, 2008-2018', fontsize=18, va = 'top')


#Finding industry that contributed the most in 2009 

d = a[(a['GEO']=="European Union") & (
    a['TIME'] == 2008) & (a['NACE_R2'] != "Total - all NACE activities")]

ind_2008 = d.groupby(['NACE_R2'],as_index=False).sum().sort_values(
    by = 'Emissions', ascending = False)[0:10]

print(ind_2008)

#Finding industry that contributed the most in 2009 

f = a[(a['GEO']=="European Union") & (
    a['TIME'] == 2018) & (a['NACE_R2'] != "Total - all NACE activities")]

ind_2018 = f.groupby(['NACE_R2']).sum().sort_values(
    by = 'Emissions', ascending = False)[0:10]

print(ind_2018)

#Combine plots to see the difference between top polluting industries
comb_ind = a[(a['NACE_R2'] != "Total - all NACE activities") & 
              ((a['TIME'] == 2018)| (a['TIME'] == 2008)) &
              (a['GEO'] == "European Union")]

comb_ind_sorted = comb_ind.sort_values(
    by = 'Emissions', ascending = False)[0:14]

print(comb_cntr_sorted.head(20))

sns.set(style="darkgrid")
comp2 = sns.catplot(x="Emissions", y="NACE_R2", hue="TIME", 
                    data=comb_ind_sorted,
                    kind="bar", palette="rocket")

comp2.set(xlim = (0,17.5*1e8), xlabel = "", ylabel = "")
comp2.despine(left=True, bottom=True)

plt.subplots_adjust(top=0.9)
comp2.fig.suptitle('Emission difference by industry, 2008-2018', fontsize=16.5, va = 'top')


#Creating the accumulative table of GhG emissions per industry per year
summ_tab = a[(a['NACE_R2'] != "Total - all NACE activities") & (
    a['GEO'] == "European Union")]

summ_tab = pd.pivot_table(summ_tab, values = 'Emissions', 
                          index = 'NACE_R2', columns = 'TIME', 
                          aggfunc=np.sum, fill_value=0)

# Draw a heatmap with the numeric values in each cell
sns.set(style="darkgrid")
comp3 = sns.heatmap(summ_tab, annot=True,fmt = {0:f}, 
                    linewidths=0.1, square = True)

comp3.set_ylabel('')    
comp3.set_xlabel('')
plt.xticks(rotation=0) 