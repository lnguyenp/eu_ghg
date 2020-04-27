# Greenhouse Emission Patterns in EU Member States

## Overview
***
This project explore data on greenhouse gas (GhG) air pollution in 28 Member States of the European Union within 10 years of operation under Emission Trading System (EU ETS). Emission Trading System was introduced in 2005 as the mechanism to reduce carbon production and consumption in Europe.

EU ETS is a 'cap and trade' system, which combines the elements of administrative restriction on overall production GhG (cap) and market circulation of emission allowances (trade).

Each EU Member State annualy receives a number of emission allowances (EUAs). Each EUA serves as the permission to emit 1 ton of greenhouse gases. Once given to a country, national governments distribute the allowances among industry polluters through mechanism of free allowance and auctioning. At the end of the year, industry polluters must surrender emission allowances equal to the amount of the produced emissions.

EU Allowances are tradeable and excess permits can be also reserved for the next reporting period.   

The purposes of this analysis are:
- to conduct a basic analysis of the greenhouse emission patterns across Europe at the beginning of II Phase of the Emission Trading System and the most recent data from III Phase of Emission Trading System (ETS);
- to define emission reduction trends across industries and EU Member States within the given timeseries.
- to assess the rates of emission reduction in II Phase (2008-2013) and III Phases (2013-2020) of ETS;

## Data
***
This project uses data from the [Eurostat, the statistical office of the European Union](https://ec.europa.eu/eurostat/web/environment/data/database). Use direct link to the Data Explorer for convenience: [Air emissions accounts by NACE Rev. 2 activity](https://appsso.eurostat.ec.europa.eu/nui/show.do?dataset=env_ac_ainah_r2&lang=en).

**NB:** Before downloading the data, make sure: (1) to add `2008` as a reference year in *'TIME'* tab; (2) to pick `GHG` in *'AIRPOL'* tab.	   

*Include a screenshot here*

This data set will report the aggregated level of greenhouse gases (GhG) emissions across all EU Member States, broken down by 21 industries (classified according to NACE Rev. 2) plus households. The document `env_ac_ainah_r2` will have five necessary fields:

1. `TIME` - year of emission; **2008-2018**
2. `GEO` - location of GhG emission; **28 EU Member States plus Iceland, Norway, Switzerland, Serbia, and Turkey**  
3. `AIRPOL` - Greenhouse gas emissions; **Aggregated data of emissions from CO2, NO2, Methane and its **
4. `NACE_R2` - type of industry emitting the Greenhouse gas; **64 categories** and total for EU area, *find the revised description for all categories [here.](https://ec.europa.eu/eurostat/ramon/nomenclatures/index.cfm?TargetUrl=DSP_NOM_DTL_VIEW&StrNom=NACE_REV2&StrLanguageCode=EN&IntPcKey=&IntKey=18506834&StrLayoutCode=HIERARCHIC&IntCurrentPage=1)*
5. `Values` - level of recorded emission in **TONNS**

## Installations
___
1. Install [Anaconda](https://www.anaconda.com/products/individual)
- Select a destination folder to install Anaconda and click the Next button
- Install Anaconda to a directory path that does not contain spaces or unicode characters.
- Do not install as Administrator unless administrator privileges are required.
- Choose an option to start Anaconda software by opening Anaconda Navigator or the Anaconda Prompt from the Start Menu

2. Set up a working folder
- Clone the content of the repository to the folder
- Update the data (above) if necessary

3. Install Spyder
- From the Start menu, search for the Anaconda Prompt desktop app
- Download Spyder
- Open the provided scripts clean.py and analyze.py from the cloned repository
- Make sure to set the working console to the folder of the project

# Analysis
___
clean.py is the script that cleans the data for further analysis.

analyze.py is a script that identifies:
- the trend line for GhG total emissions over 10 year period (2008-2018);
- top 10 country polluters in the EU on the benchmark year of 2008 and the most recent data from year 2018, graphs the comparative bar plot of the emission difference;  
- biggest 10 polluting industries in the EU on the benchmark year of 2008 and the most recent data from year 2018, graphs the comparative bar plot of the emission difference;
- proportion of each emission contributing industry every year from 2008 to 2018, graphs a heatmap
