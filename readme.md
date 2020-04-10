# COVID-19 Data Visualization Repository for ODI
Glenn Abastillas | April 7, 2020 | Description of this Repository

Contents
  * [End-User Files](#end-user-files)
    * [Data visualization files](#data-visualization-files)
  * [Developer Files](#developer-files)
    * [Data](#data)
      * [Data Dictionaries](#data-dictionaries)
    * [Jupyter Notebooks](#jupyter-notebooks)
    * [Requirements Files](#requirements-files)

---
<a id='end-user'></a>
## End-User Files

Data products intended for end-user usage are located in the `visualizations` folder.

###### Sample
  1. [index.html](./visualizations/demographics/index.html)

<a id='data-visualization-files'></a>
#### Data Visualization Files

The `visualizations` folder contains interactive HTML files for dissemination. These HTML files are ready to use immediately upon download.

**Requirements** : The only software required is a browser that can render SVG and JavaScript enabled. Most modern browsers are able to do this except for Internet Explorer, which may result in unpredictable rendering of visualizations and interaction capability.

**Recommended Browsers**
  - Chrome
  - Safari
  - FireFox

<a id='developer'></a>
## Developer Files

These files are open for further changes from any developer who wishes to do so.

<a id='data'></a>
#### Data

Various types of data were used to generate the visualizations in `visualizations`. These include geoshape, census, and disease data. This section provides an inventory and references for the data included in this repository.

  1. Inventory of Data
  2. Data Dictionaries


<a id='data-dictionaries'></a>
##### Data Dictionaries

###### Gridded Population of the World (GPW) ([Source](https://sedac.ciesin.columbia.edu/downloads/docs/gpw-v4/gpw-v4-documentation-rev11.pdf))
Column | Description
--- | ---
GUBID | Unique random (text) id
ISOALPHA | Three-letter country/state code
COUNTRYNM | English country/state name
NAME1 | First administrative level name
NAME2 | Second administrative level name
NAME3 | Third administrative level name
NAME4 | Fourth administrative level name
NAME5 | Fifth administrative level name
NAME6 | Sixth administrative level name
CENTROID_X | Centroid coordinates for this shape
CENTROID_Y | Centroid coordinates for this shape
INSIDE_X | Longitude of the administrative unit inside center point in decimal degrees
INSIDE_Y | Latitude of the administrative unit inside center point in decimal degrees
CONTEXT | Data context value
CONTEXT_NM | Data context category
WATER_CODE | Unit type code (L = Land unit, IW = Inland Water unit)
TOTAL_A_KM | Total area of the administrative unit in square km
WATER_A_KM | Water area of the administrative unit in square km
LAND_A_KM | Land area of the administrative unit in square km; this area field is used to calculate population density
UN_2000_E | UN WPP-adjusted population estimates (2000)
UN_2005_E | UN WPP-adjusted population estimates (2005)
UN_2010_E | UN WPP-adjusted population estimates (2010)
UN_2015_E | UN WPP-adjusted population estimates (2015)
UN_2020_E | UN WPP-adjusted population estimates (2020)
UN_2000_DS | UN WPP-adjusted population density (2000)
UN_2005_DS | UN WPP-adjusted population density (2005)
UN_2010_DS | UN WPP-adjusted population density (2010)
UN_2015_DS | UN WPP-adjusted population density (2015)
UN_2020_DS | UN WPP-adjusted population density (2020)
B_2010_E | 2010 Estimate (Both)
F_2010_E | 2010 Estimate (Female)
M_2010_E | 2010 Estimate (Male)
A00_04B | Age 00 to 04 (Both)
A05_09B | Age 05 to 09 (Both)
A10_14B | Age 10 to 14 (Both)
A15_19B | Age 15 to 19 (Both)
A20_24B | Age 20 to 24 (Both)
A25_29B | Age 25 to 29 (Both)
A30_34B | Age 30 to 34 (Both)
A35_39B | Age 35 to 39 (Both)
A40_44B | Age 40 to 44 (Both)
A45_49B | Age 45 to 49 (Both)
A50_54B | Age 50 to 54 (Both)
A55_59B | Age 55 to 59 (Both)
A60_64B | Age 60 to 64 (Both)
A65PLUSB | Age 65 and older (Both)
A65_69B | Age 65 to 69 (Both)
A70PLUSB | Age 70 and older (Both)
A70_74B | Age 70 to 74 (Both)
A75PLUSB | Age 75 and older (Both)
A75_79B | Age 75 to 79 (Both)
A80PLUSB | Age 80 and older (Both)
A80_84B | Age 80 to 84 (Both)
A85PLUSB | Age 85 and older (Both)
A00_04F | Age 00 to 04 (Females)
A05_09F | Age 05 to 09 (Females)
A10_14F | Age 10 to 14 (Females)
A15_19F | Age 15 to 19 (Females)
A20_24F | Age 20 to 24 (Females)
A25_29F | Age 25 to 29 (Females)
A30_34F | Age 30 to 34 (Females)
A35_39F | Age 35 to 39 (Females)
A40_44F | Age 40 to 44 (Females)
A45_49F | Age 45 to 49 (Females)
A50_54F | Age 50 to 54 (Females)
A55_59F | Age 55 to 59 (Females)
A60_64F | Age 60 to 64 (Females)
A65PLUSF | Age 65 and older (Females)
A65_69F | Age 65 to 69 (Females)
A70PLUSF | Age 70 and older (Female)
A70_74F | Age 70 to 74 (Females)
A75PLUSF | Age 75 and older (Female)
A75_79F | Age 75 to 79 (Females)
A80PLUSF | Age 80 and older (Female)
A80_84F | Age 80 to 84 (Females)
A85PLUSF | Age 85 and older (Female)
A00_04M | Age 00 to 04 (Males)
A05_09M | Age 05 to 09 (Males)
A10_14M | Age 10 to 14 (Males)
A15_19M | Age 15 to 19 (Males)
A20_24M | Age 20 to 24 (Males)
A25_29M | Age 25 to 29 (Males)
A30_34M | Age 30 to 34 (Males)
A35_39M | Age 35 to 39 (Males)
A40_44M | Age 40 to 44 (Males)
A45_49M | Age 45 to 49 (Males)
A50_54M | Age 50 to 54 (Males)
A55_59M | Age 55 to 59 (Males)
A60_64M | Age 60 to 64 (Males)
A65PLUSM | Age 65 and older (Males)
A65_69M | Age 65 to 69 (Males)
A70PLUSM | Age 70 and older (Males)
A70_74M | Age 70 to 74 (Males)
A75PLUSM | Age 75 and older (Males)
A75_79M | Age 75 to 79 (Males)
A80PLUSM | Age 80 and older (Males)
A80_84M | Age 80 to 84 (Males)
A85PLUSM | Age 85 and older (Males)

<a id='jupyter-notebooks'></a>
#### Jupyter Notebooks

Final visualizations are made in `jupyter` and published as interactive pages by the `nbinteract` package. Both were developed in the Python programming language.

<a id='requirements-files'></a>
#### Requirements Files