# COVID-19 Data Visualization Repository for ODI
Go to: [Visualization](https://gabastil.github.io/odi-covid-19) | [Datasets](data/datasets/) | [Map Data](data/maps/) | Versão em Português (a ser publicado)

Data visualizations for Guinea-Bissau's Ministry of Public Health through the [Overseas Development Insitute (ODI)](https://www.odi.org/).

Contents
  * [End-User Files](#end-user-files)
    * [Data visualization files](#data-visualization-files)
  * [Developer Files](#developer-files)
    * [Data](#data)
      * [Inventory of Data](#inventory-of-data)
      * [Data Dictionaries](#data-dictionaries)
    * [Jupyter Notebooks](#jupyter-notebooks)
    * [Requirements Files](#requirements-files)

---
<a id='end-user'></a>
## End-User Files

The dashboard is directly accessible via [https://gabastil.github.io/odi-covid-19](https://gabastil.github.io/odi-covid-19). Alternatively, data products intended for end-user usage are located in the `docs` folder.

For example, the index page for the dashboard is located here:
  1. [./docs/index.html](./docs/index.html)

<a id='data-visualization-files'></a>
#### Data Visualization Files

The `visualizations` folder contains interactive HTML files for dissemination. These files are immediately viewable upon download to your local device.

**Requirements** : The only software required is a browser that can render SVG and JavaScript enabled. Most modern browsers are able to do this except for Internet Explorer, which may result in unpredictable rendering of visualizations and interaction capability.

**Recommended Browsers**
  - Chrome
  - Safari
  - FireFox

<a id='developer'></a>
## Developer Files

These files are open for further changes from developers.

<a id='data'></a>
#### Data

Various types of data were used to generate the visualizations in `visualizations`. These include geoshape, census, and disease data. This section provides an inventory and references for the data included in this repository.

  1. Inventory of Data
  2. Data Dictionaries

<a id='inventory-of-data'></a>
##### 1. Inventory of Data

Data | Description | Location
--- | --- | ---
Demographics | UN population count from 2000 to 2020 | [data/datasets/demographics](data/datasets/demographics)
Health Centers | Shapefile data for health center locations in Guinea-Bissau | [data/maps/health centers](data/maps/health%20centers)
Health Regions | Shapefile data for administrative health regions in Guinea-Bissau | [data/maps/health regions](data/maps/health%20regions)
Regions | Shapefile data for regions and sectors in Guinea-Bissau | [data/maps/regions](data/maps/regions)
Roads | Shapefile data for roads in Guinea-Bissau | [data/maps/roads](data/maps/roads)
Schools | Shapefile data for schools in Guinea-Bissau | [data/maps/schools](data/maps/schools)
Sectors | Shapefile data for sectors in Guinea-Bissau (Use Regions instead) | [data/maps/sectors](data/maps/sectors)



<a id='data-dictionaries'></a>
##### 2. Data Dictionaries

Data dictionaries for each data file in the [inventory of data](#inventory-of-data) table can be found in each folder's respective `readme` files.

<a id='jupyter-notebooks'></a>
#### Jupyter Notebooks

Final visualizations are made in `jupyter` and published as interactive pages by the `nbinteract` package. Both were developed in the Python programming language.

You can directly access the current dashboard at [https://gabastil.github.io/odi-covid-19](https://gabastil.github.io/odi-covid-19/).

<a id='requirements-files'></a>
#### Requirements Files

`To be filled out`