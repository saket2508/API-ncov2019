from bs4 import BeautifulSoup
import requests
import json

with open('app\codes.json') as f:
    data= json.load(f)

url='https://www.worldometers.info/coronavirus/'

source= requests.get(url).text

soup= BeautifulSoup(source,'html.parser')


def getTableData(rawdata_table):
    table_body= rawdata_table.find_all('tbody')
    rows= table_body[0].find_all('tr')

    data_scraped={}

    continents=[]
    world={}
    countries=[]

    for row in rows[:6]:
        row_data= row.find_all('td')

        c_name= row_data[1].text.strip('\n')
        if(c_name!=''):
            name= c_name

        total_cases= int(row_data[2].text.replace(',',''))

        new_cases= row_data[3].text.strip('+').replace(',','')
        if(new_cases==''):
            new_cases=0
        new_cases= int(new_cases)

        total_deaths= int(row_data[4].text.replace(',',''))
    
        new_deaths= row_data[5].text.strip('+').replace(',','')
        if(new_deaths==''):
            new_deaths=0
        new_deaths= int(new_deaths)

        total_recovered= int(row_data[6].text.replace(',',''))

        new_recoveries= row_data[7].text.strip('+').replace(',','')
        if(new_recoveries==''):
            new_recoveries=0
        new_recoveries= int(new_recoveries)

        active_cases= int(row_data[8].text.replace(',',''))
        
        critical_cases= int(row_data[9].text.replace(',',''))

        code=""

        c_data= {
        'name':name,
        'total_cases':total_cases,
        'new_cases':new_cases,
        'total_deaths':total_deaths,
        'new_deaths':new_deaths,
        'total_recovered':total_recovered,
        'new_recoveries':new_recoveries,
        'active_cases':active_cases,
        'critical_cases':critical_cases}
        continents.append(c_data)
        
    continents.sort(key=lambda x: x['total_cases'], reverse=True)

    for item in continents:
        item["id"]= continents.index(item)+1

    data_scraped['continents']= continents

    world_data= rows[7].find_all('td')
    total_cases_world= int(world_data[2].text.strip('\n').replace(',',''))
    new_cases_world= int(world_data[3].text.strip('+').replace(',',''))
    total_deaths_world= int(world_data[4].text.strip('\n').replace(',',''))
    new_deaths_world= int(world_data[5].text.strip('+').replace(',',''))
    total_recovered_world= int(world_data[6].text.strip('\n').replace(',',''))
    new_recoveries_world= int(world_data[7].text.strip('+').replace(',',''))
    active_cases_world= int(world_data[8].text.strip('\n').replace(',',''))
    critical_cases_world= int(world_data[9].text.strip('\n').replace(',',''))

    w_data= {
        'total_cases':total_cases_world,
        'new_cases':new_cases_world,
        'total_deaths':total_deaths_world,
        'new_deaths':new_deaths_world,
        'total_recovered':total_recovered_world,
        'new_recoveries':new_recoveries_world,
        'active_cases':active_cases_world,
        'critical_cases':critical_cases_world}
    data_scraped['world']= w_data



    for row in rows[8:]:
        row_data= row.find_all('td')
        c_id= int(row_data[0].text)

        name= row_data[1].text

        if(name=="USA"):
            name= "United States"
        if(name=="UK"):
            name="United Kingdom"
        if(name=="UAE"):
            name="United Arab Emirates"
        if(name=="S. Korea"):
            name="South Korea"
        
        code=""

        for element in data:
            if name in element["Name"]:
                code= element["Code"]
                break
        
        if(name=="Caribbean Netherlands"):
            code="NL"
        
        if(name=="India"):
            code="IN"
        
        if(name=="Channel Islands"):
            code= "JE"

        total_cases= int(row_data[2].text.replace(',',''))

        new_cases= row_data[3].text.strip('+').replace(',','')
        if(new_cases==''):
            new_cases=0
        else:
            new_cases= int(new_cases)

        total_deaths= row_data[4].text.replace(',','')
        if(total_deaths=="" or total_deaths=='' or total_deaths==' '):
            total_deaths=0
        total_deaths= int(total_deaths)
        
        new_deaths= row_data[5].text.strip('+').replace(',','')
        if(new_deaths=="" or new_deaths==' '):
            new_deaths=0
        new_deaths= int(new_deaths)

        total_recovered= row_data[6].text.replace(',','')
        if(total_recovered=="" or total_recovered==" " or total_recovered=="N/A"):
            total_recovered=0
        total_recovered= int(total_recovered)

        new_recoveries= row_data[7].text.strip('+').replace(',','')
        if(new_recoveries=="" or new_recoveries==" " or new_recoveries=="N/A"):
            new_recoveries=0
        new_recoveries= int(new_recoveries)

        active_cases= row_data[8].text.replace(',','')
        if(active_cases=="" or active_cases==" " or active_cases=="N/A"):
            active_cases=0
        active_cases= int(active_cases)

        critical_cases= row_data[9].text.replace(',','')
        if(critical_cases=="" or critical_cases==" " or critical_cases=="N/A"):
            critical_cases=0
        critical_cases= int(critical_cases)

        cases_pm= row_data[10].text.replace(',','')
        if(cases_pm=="" or cases_pm==" " or cases_pm=="N/A"):
            cases_pm=0
        cases_pm= float(cases_pm)

        deaths_pm= row_data[11].text.replace(',','')
        if(deaths_pm=="" or deaths_pm==" " or deaths_pm=="N/A"):
            deaths_pm=0
        deaths_pm= float(deaths_pm)

        total_tests= row_data[12].text.replace(',','')
        if(total_tests=="" or total_tests==" " or total_tests=="N/A"):
            total_tests=0
        total_tests= int(total_tests)

        tests_pm= row_data[13].text.replace(',','')
        if(tests_pm=="" or tests_pm==" " or tests_pm=="N/A"):
            tests_pm=0
        tests_pm= float(tests_pm)

        population= row_data[14].text.replace(',','')
        if(population=="" or population==" "):
            population=0
        population= int(population)

        continent= row_data[15].text



        country={
            'id':c_id,
            'code':code,
            'name':name,
            'total_cases':total_cases,
            'new_cases':new_cases,
            'total_deaths':total_deaths,
            'new_deaths':new_deaths,
            'total_recovered':total_recovered,
            'new_recoveries':new_recoveries,
            'active_cases':active_cases,
            'critical_cases':critical_cases,
            'cases_pm':cases_pm,
            'deaths_pm':deaths_pm,
            'total_tests':total_tests,
            'tests_pm':tests_pm,
            'population':population,
            'continent':continent
        }
        countries.append(country)
    countries.sort(key=lambda x: x['total_cases'], reverse=True)

    for item in countries:
        item["id"]= countries.index(item)+1
    
    data_scraped['countries']= countries


    return data_scraped



def getCurrentData():

    #labels={0:'id',1:'name',2:'total_cases',3:'new_cases',4:'total_deaths',5:'new_deaths',6:'total_recovered',7:'new_recovered',8:'active_cases',9:'critical_cases',10:'cases_pm',11:'deaths_pm',12:'total_tests',13:'tests_pm',14:'population',15:'continent'}
    table= soup.find_all('table',{'id':'main_table_countries_today'})[0]
    
    data_current= getTableData(table)

    return data_current

def getPreviousDayData():
    table= soup.find_all('table',{'id':'main_table_countries_yesterday'})[0]

    data_previous_day= getTableData(table)

    return data_previous_day

getCurrentData()

