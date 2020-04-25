# Greenhouse Emission Patterns in EU Member States

## Overview
___
This project explore data on greenhouse gas (GhG) air pollution in 28 Member States of the European Union within 10 years of operation under Emission Trading System (EU ETS). Emission Trading System was introduced in 2005 as the mechanism to reduce carbon production and consumption in Europe.

EU ETS is a 'cap and trade' system, which combines the elements of administrative restriction on overall production GhG (cap) and free market circulation of excess emission allowance (trade). Each EU Member State receives a number of emission allowances, which is a permission to

The purposes of this analysis are:
- to conduct a basic analysis of the greenhouse emission patterns across Europe before II Phase of the Emission Trading System and after the conclusion of III Phase of Emission Trading System (ETS);
- to assess the rates of emission reduction in II Phase (2008-2013) and III Phases (2013-2020) of ETS;
- to define emission reduction trends across industries and EU Member States within the given timeseries.

## Data
___
This project uses data from the [Eurostat, the statistical office of the European Union](https://ec.europa.eu/eurostat/web/environment/data/database). Use direct link to the Data Explorer for convenience: [Air emissions accounts by NACE Rev. 2 activity](https://appsso.eurostat.ec.europa.eu/nui/show.do?dataset=env_ac_ainah_r2&lang=en).

**NB:** Before downloading the data, make sure: (1) to add `2008` as a reference year in *'TIME'* tab; (2) to pick `GHG` in *'AIRPOL'* tab.	   

*Include a screenshot here*

This data set will report the aggregated level of greenhouse gases (GhG) emissions across all EU Member States, broken down by 21 industries (classified according to NACE Rev. 2) plus households. The document `env_ac_ainah_r2` will have five necessary fields:

1. `TIME` - year of emission; **2008-2018**
2. `GEO` - location of GhG emission; **28 EU Member States plus Iceland, Norway, Switzerland, Serbia, and Turkey**  
3. `AIRPOL` - Greenhouse gas emissions; **Aggregated data of emissions from CO2, NO2, Methane and its **
4. `NACE_R2` - type of industry emitting the Greenhouse gas; **64 categories** and total for EU area, *find the revised description for all categories [here.](https://ec.europa.eu/eurostat/ramon/nomenclatures/index.cfm?TargetUrl=DSP_NOM_DTL_VIEW&StrNom=NACE_REV2&StrLanguageCode=EN&IntPcKey=&IntKey=18506834&StrLayoutCode=HIERARCHIC&IntCurrentPage=1)*
5. `Values` - level of recorded emission in **TONNS**

*Add the table scroll*


## Installations
___


# Analysis
___
This project

## Limitations
