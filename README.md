# API-ncov2019
An easy to use RESTFUL API that gives real time COVID-19 info. Data is obtained from Worldmeter's coronavirus page through a python web scraper. 

#### Latest data available at(JSON with full data): https://ncov2019api.herokuapp.com/latest
#### Data from the previous day(JSON with full data): https://ncov2019api.herokuapp.com/yesterday

#### For continent-wise data: https://ncov2019api.herokuapp.com/latest/continents
```
{
  "data": {
    "Africa": {
      "active_cases": 125845, 
      "critical_cases": 515, 
      "id": 5, 
      "new_cases": 0, 
      "new_deaths": 0, 
      "new_recoveries": 0, 
      "total_cases": 244578, 
      "total_deaths": 6490, 
      "total_recovered": 112243
    }, 
    "Asia": {
      "active_cases": 586510, 
      "critical_cases": 15516, 
      "id": 3, 
      "new_cases": 49, 
      "new_deaths": 0, 
      "new_recoveries": 1, 
      "total_cases": 1617233, 
      "total_deaths": 40248, 
      "total_recovered": 990475
    }, 
    "Europe": {
      "active_cases": 855314, 
      "critical_cases": 6592, 
      "id": 2, 
      "new_cases": 0, 
      "new_deaths": 0, 
      "new_recoveries": 0, 
      "total_cases": 2205848, 
      "total_deaths": 182868, 
      "total_recovered": 1167666
    }, 
    "North America": {
      "active_cases": 1266406, 
      "critical_cases": 19418, 
      "id": 1, 
      "new_cases": 2, 
      "new_deaths": 0, 
      "new_recoveries": 0, 
      "total_cases": 2481351, 
      "total_deaths": 144974, 
      "total_recovered": 1069971
    }, 
    "Oceania": {
      "active_cases": 381, 
      "critical_cases": 3, 
      "id": 6, 
      "new_cases": 0, 
      "new_deaths": 0, 
      "new_recoveries": 0, 
      "total_cases": 8931, 
      "total_deaths": 124, 
      "total_recovered": 8426
    }, 
    "South America": {
      "active_cases": 610371, 
      "critical_cases": 12074, 
      "id": 4, 
      "new_cases": 74, 
      "new_deaths": 1, 
      "new_recoveries": 348, 
      "total_cases": 1425770, 
      "total_deaths": 60458, 
      "total_recovered": 754941
    }
  }
}
```


#### For country-wise data: https://ncov2019api.herokuapp.com/latest/countries
```
{
  "data": {
    "Afghanistan": {
      "active_cases": 19570, 
      "cases_pm": 637.0, 
      "code": "AF", 
      "continent": "Asia", 
      "critical_cases": 19, 
      "deaths_pm": 12.0, 
      "id": 40, 
      "new_cases": 0, 
      "new_deaths": 0, 
      "new_recoveries": 0, 
      "population": 38882182, 
      "tests_pm": 1440.0, 
      "total_cases": 24766, 
      "total_deaths": 471, 
      "total_recovered": 4725, 
      "total_tests": 55981
    }, 
    "Albania": {
      "active_cases": 441, 
      "cases_pm": 529.0, 
      "code": "AL", 
      "continent": "Europe", 
      "critical_cases": 7, 
      "deaths_pm": 13.0, 
      "id": 108, 
      "new_cases": 0, 
      "new_deaths": 0, 
      "new_recoveries": 0, 
      "population": 2877924, 
      "tests_pm": 6341.0, 
      "total_cases": 1521, 
      "total_deaths": 36, 
      "total_recovered": 1044, 
      "total_tests": 18250
    }, 
    "Algeria": {
      "active_cases": 2546, 
      "cases_pm": 249.0, 
      "code": "DZ", 
      "continent": "Africa", 
      "critical_cases": 39, 
      "deaths_pm": 18.0, 
      "id": 59, 
      "new_cases": 0, 
      "new_deaths": 0, 
      "new_recoveries": 0, 
      "population": 43811264, 
      "tests_pm": 0.0, 
      "total_cases": 10919, 
      "total_deaths": 767, 
      "total_recovered": 7606, 
      "total_tests": 0
    }, 
    ...
```
#### To get data of a specific country use: https://ncov2019api.herokuapp.com/latest/countries/{country_name}

#### Calling https://ncov2019api.herokuapp.com/latest/countries/India will give you:

```
{
  "data": {
    "active_cases": 153799, 
    "cases_pm": 241.0, 
    "code": "IN", 
    "continent": "Asia", 
    "critical_cases": 8944, 
    "deaths_pm": 7.0, 
    "id": 4, 
    "new_cases": 0, 
    "new_deaths": 0, 
    "new_recoveries": 0, 
    "population": 1379381861, 
    "tests_pm": 4102.0, 
    "total_cases": 333008, 
    "total_deaths": 9520, 
    "total_recovered": 169689, 
    "total_tests": 5658614
  }
}
```

#### To get data of a specific continent use: https://ncov2019api.herokuapp.com/latest/continents/{continent_name}

#### Calling https://ncov2019api.herokuapp.com/latest/continents/Asia will give you:

```
{
  "data": {
    "active_cases": 586510, 
    "critical_cases": 15516, 
    "id": 3, 
    "new_cases": 49, 
    "new_deaths": 0, 
    "new_recoveries": 1, 
    "total_cases": 1617233, 
    "total_deaths": 40248, 
    "total_recovered": 990475
  }
}
```

