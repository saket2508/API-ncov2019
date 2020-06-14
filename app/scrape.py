from bs4 import BeautifulSoup
import requests
from bs4 import BeautifulSoup
import requests
import json

url='https://www.worldometers.info/coronavirus/'

source= requests.get(url).text

soup= BeautifulSoup(source,'html.parser')

data= [{"Code": "AF", "Name": "Afghanistan"},{"Code": "AX", "Name": "\u00c5land Islands"},{"Code": "AL", "Name": "Albania"},{"Code": "DZ", "Name": "Algeria"},{"Code": "AS", "Name": "American Samoa"},{"Code": "AD", "Name": "Andorra"},{"Code": "AO", "Name": "Angola"},{"Code": "AI", "Name": "Anguilla"},{"Code": "AQ", "Name": "Antarctica"},{"Code": "AG", "Name": "Antigua and Barbuda"},{"Code": "AR", "Name": "Argentina"},{"Code": "AM", "Name": "Armenia"},{"Code": "AW", "Name": "Aruba"},{"Code": "AU", "Name": "Australia"},{"Code": "AT", "Name": "Austria"},{"Code": "AZ", "Name": "Azerbaijan"},{"Code": "BS", "Name": "Bahamas"},{"Code": "BH", "Name": "Bahrain"},{"Code": "BD", "Name": "Bangladesh"},{"Code": "BB", "Name": "Barbados"},{"Code": "BY", "Name": "Belarus"},{"Code": "BE", "Name": "Belgium"},{"Code": "BZ", "Name": "Belize"},{"Code": "BJ", "Name": "Benin"},{"Code": "BM", "Name": "Bermuda"},{"Code": "BT", "Name": "Bhutan"},{"Code": "BO", "Name": "Bolivia, Plurinational State of"},{"Code": "BQ", "Name": "Bonaire, Sint Eustatius and Saba"},{"Code": "BA", "Name": "Bosnia and Herzegovina"},{"Code": "BW", "Name": "Botswana"},{"Code": "BV", "Name": "Bouvet Island"},{"Code": "BR", "Name": "Brazil"},{"Code": "IO", "Name": "British Indian Ocean Territory"},{"Code": "BN", "Name": "Brunei Darussalam"},{"Code": "BG", "Name": "Bulgaria"},{"Code": "BF", "Name": "Burkina Faso"},{"Code": "BI", "Name": "Burundi"},{"Code": "KH", "Name": "Cambodia"},{"Code": "CM", "Name": "Cameroon"},{"Code": "CA", "Name": "Canada"},{"Code": "CV", "Name": "Cabo Verde"},{"Code": "KY", "Name": "Cayman Islands"},{"Code": "CF", "Name": "CAR"},{"Code": "TD", "Name": "Chad"},{"Code": "CL", "Name": "Chile"},{"Code": "CN", "Name": "China"},{"Code": "CX", "Name": "Christmas Island"},{"Code": "CC", "Name": "Cocos (Keeling) Islands"},{"Code": "CO", "Name": "Colombia"},{"Code": "KM", "Name": "Comoros"},{"Code": "CG", "Name": "Congo"},{"Code": "CD", "Name": "DRC"},{"Code": "CK", "Name": "Cook Islands"},{"Code": "CR", "Name": "Costa Rica"},{"Code": "CI", "Name": "Ivory Coast"},{"Code": "HR", "Name": "Croatia"},{"Code": "CU", "Name": "Cuba"},{"Code": "CW", "Name": "Cura\u00e7ao"},{"Code": "CY", "Name": "Cyprus"},{"Code": "CZ", "Name": "Czechia"},{"Code": "DK", "Name": "Denmark"},{"Code": "DJ", "Name": "Djibouti"},{"Code": "DM", "Name": "Dominica"},{"Code": "DO", "Name": "Dominican Republic"},{"Code": "EC", "Name": "Ecuador"},{"Code": "EG", "Name": "Egypt"},{"Code": "SV", "Name": "El Salvador"},{"Code": "GQ", "Name": "Equatorial Guinea"},{"Code": "ER", "Name": "Eritrea"},{"Code": "EE", "Name": "Estonia"},{"Code": "ET", "Name": "Ethiopia"},{"Code": "FK", "Name": "Falkland Islands (Malvinas)"},{"Code": "FO", "Name": "Faeroe Islands"},{"Code": "FJ", "Name": "Fiji"},{"Code": "FI", "Name": "Finland"},{"Code": "FR", "Name": "France"},{"Code": "GF", "Name": "French Guiana"},{"Code": "PF", "Name": "French Polynesia"},{"Code": "TF", "Name": "French Southern Territories"},{"Code": "GA", "Name": "Gabon"},{"Code": "GM", "Name": "Gambia"},{"Code": "GE", "Name": "Georgia"},{"Code": "DE", "Name": "Germany"},{"Code": "GH", "Name": "Ghana"},{"Code": "GI", "Name": "Gibraltar"},{"Code": "GR", "Name": "Greece"},{"Code": "GL", "Name": "Greenland"},{"Code": "GD", "Name": "Grenada"},{"Code": "GP", "Name": "Guadeloupe"},{"Code": "GU", "Name": "Guam"},{"Code": "GT", "Name": "Guatemala"},{"Code": "GG", "Name": "Guernsey"},{"Code": "GN", "Name": "Guinea"},{"Code": "GW", "Name": "Guinea-Bissau"},{"Code": "GY", "Name": "Guyana"},{"Code": "HT", "Name": "Haiti"},{"Code": "HM", "Name": "Heard Island and McDonald Islands"},{"Code": "VA", "Name": "Holy See (Vatican City State)"},{"Code": "HN", "Name": "Honduras"},{"Code": "HK", "Name": "Hong Kong"},{"Code": "HU", "Name": "Hungary"},{"Code": "IS", "Name": "Iceland"},{"Code": "IN", "Name": "India"},{"Code": "ID", "Name": "Indonesia"},{"Code": "IR", "Name": "Iran, Islamic Republic of"},{"Code": "IQ", "Name": "Iraq"},{"Code": "IE", "Name": "Ireland"},{"Code": "IM", "Name": "Isle of Man"},{"Code": "IL", "Name": "Israel"},{"Code": "IT", "Name": "Italy"},{"Code": "JM", "Name": "Jamaica"},{"Code": "JP", "Name": "Japan"},{"Code": "JE", "Name": "Jersey"},{"Code": "JO", "Name": "Jordan"},{"Code": "KZ", "Name": "Kazakhstan"},{"Code": "KE", "Name": "Kenya"},{"Code": "KI", "Name": "Kiribati"},{"Code": "KP", "Name": "Korea, Democratic People's Republic of"},{"Code": "KR", "Name": "South Korea"},{"Code": "KW", "Name": "Kuwait"},{"Code": "KG", "Name": "Kyrgyzstan"},{"Code": "LA", "Name": "Laos"},{"Code": "LV", "Name": "Latvia"},{"Code": "LB", "Name": "Lebanon"},{"Code": "LS", "Name": "Lesotho"},{"Code": "LR", "Name": "Liberia"},{"Code": "LY", "Name": "Libya"},{"Code": "LI", "Name": "Liechtenstein"},{"Code": "LT", "Name": "Lithuania"},{"Code": "LU", "Name": "Luxembourg"},{"Code": "MO", "Name": "Macao"},{"Code": "MK", "Name": "North Macedonia"},{"Code": "MG", "Name": "Madagascar"},{"Code": "MW", "Name": "Malawi"},{"Code": "MY", "Name": "Malaysia"},{"Code": "MV", "Name": "Maldives"},{"Code": "ML", "Name": "Mali"},{"Code": "MT", "Name": "Malta"},{"Code": "MH", "Name": "Marshall Islands"},{"Code": "MQ", "Name": "Martinique"},{"Code": "MR", "Name": "Mauritania"},{"Code": "MU", "Name": "Mauritius"},{"Code": "YT", "Name": "Mayotte"},{"Code": "MX", "Name": "Mexico"},{"Code": "FM", "Name": "Micronesia, Federated States of"},{"Code": "MD", "Name": "Moldova, Republic of"},{"Code": "MC", "Name": "Monaco"},{"Code": "MN", "Name": "Mongolia"},{"Code": "ME", "Name": "Montenegro"},{"Code": "MS", "Name": "Montserrat"},{"Code": "MA", "Name": "Morocco"},{"Code": "MZ", "Name": "Mozambique"},{"Code": "MM", "Name": "Myanmar"},{"Code": "NA", "Name": "Namibia"},{"Code": "NR", "Name": "Nauru"},{"Code": "NP", "Name": "Nepal"},{"Code": "NL", "Name": "Netherlands"},{"Code": "NC", "Name": "New Caledonia"},{"Code": "NZ", "Name": "New Zealand"},{"Code": "NI", "Name": "Nicaragua"},{"Code": "NE", "Name": "Niger"},{"Code": "NG", "Name": "Nigeria"},{"Code": "NU", "Name": "Niue"},{"Code": "NF", "Name": "Norfolk Island"},{"Code": "MP", "Name": "Northern Mariana Islands"},{"Code": "NO", "Name": "Norway"},{"Code": "OM", "Name": "Oman"},{"Code": "PK", "Name": "Pakistan"},{"Code": "PW", "Name": "Palau"},{"Code": "PS", "Name": "Palestine, State of"},{"Code": "PA", "Name": "Panama"},{"Code": "PG", "Name": "Papua New Guinea"},{"Code": "PY", "Name": "Paraguay"},{"Code": "PE", "Name": "Peru"},{"Code": "PH", "Name": "Philippines"},{"Code": "PN", "Name": "Pitcairn"},{"Code": "PL", "Name": "Poland"},{"Code": "PT", "Name": "Portugal"},{"Code": "PR", "Name": "Puerto Rico"},{"Code": "QA", "Name": "Qatar"},{"Code": "RE", "Name": "R\u00e9union"},{"Code": "RO", "Name": "Romania"},{"Code": "RU", "Name": "Russian Federation"},{"Code": "RW", "Name": "Rwanda"},{"Code": "BL", "Name": "St. Barth"},{"Code": "SH", "Name": "Saint Helena, Ascension and Tristan da Cunha"},{"Code": "KN", "Name": "Saint Kitts and Nevis"},{"Code": "LC", "Name": "Saint Lucia"},{"Code": "MF", "Name": "Saint Martin (French part)"},{"Code": "PM", "Name": "Saint Pierre Miquelon"},{"Code": "VC", "Name": "St. Vincent Grenadines"},{"Code": "WS", "Name": "Samoa"},{"Code": "SM", "Name": "San Marino"},{"Code": "ST", "Name": "Sao Tome and Principe"},{"Code": "SA", "Name": "Saudi Arabia"},{"Code": "SN", "Name": "Senegal"},{"Code": "RS", "Name": "Serbia"},{"Code": "SC", "Name": "Seychelles"},{"Code": "SL", "Name": "Sierra Leone"},{"Code": "SG", "Name": "Singapore"},{"Code": "SX", "Name": "Sint Maarten (Dutch part)"},{"Code": "SK", "Name": "Slovakia"},{"Code": "SI", "Name": "Slovenia"},{"Code": "SB", "Name": "Solomon Islands"},{"Code": "SO", "Name": "Somalia"},{"Code": "ZA", "Name": "South Africa"},{"Code": "GS", "Name": "South Georgia and the South Sandwich Islands"},{"Code": "SS", "Name": "South Sudan"},{"Code": "ES", "Name": "Spain"},{"Code": "LK", "Name": "Sri Lanka"},{"Code": "SD", "Name": "Sudan"},{"Code": "SR", "Name": "Suriname"},{"Code": "SJ", "Name": "Svalbard and Jan Mayen"},{"Code": "SZ", "Name": "Eswatini"},{"Code": "SE", "Name": "Sweden"},{"Code": "CH", "Name": "Switzerland"},{"Code": "SY", "Name": "Syrian Arab Republic"},{"Code": "TW", "Name": "Taiwan, Province of China"},{"Code": "TJ", "Name": "Tajikistan"},{"Code": "TZ", "Name": "Tanzania, United Republic of"},{"Code": "TH", "Name": "Thailand"},{"Code": "TL", "Name": "Timor-Leste"},{"Code": "TG", "Name": "Togo"},{"Code": "TK", "Name": "Tokelau"},{"Code": "TO", "Name": "Tonga"},{"Code": "TT", "Name": "Trinidad and Tobago"},{"Code": "TN", "Name": "Tunisia"},{"Code": "TR", "Name": "Turkey"},{"Code": "TM", "Name": "Turkmenistan"},{"Code": "TC", "Name": "Turks and Caicos Islands"},{"Code": "TV", "Name": "Tuvalu"},{"Code": "UG", "Name": "Uganda"},{"Code": "UA", "Name": "Ukraine"},{"Code": "AE", "Name": "United Arab Emirates"},{"Code": "GB", "Name": "United Kingdom"},{"Code": "US", "Name": "United States"},{"Code": "UM", "Name": "United States Minor Outlying Islands"},{"Code": "UY", "Name": "Uruguay"},{"Code": "UZ", "Name": "Uzbekistan"},{"Code": "VU", "Name": "Vanuatu"},{"Code": "VE", "Name": "Venezuela, Bolivarian Republic of"},{"Code": "VN", "Name": "Vietnam"},{"Code": "VG", "Name": "British Virgin Islands"},{"Code": "VI", "Name": "Virgin Islands, U.S."},{"Code": "WF", "Name": "Wallis and Futuna"},{"Code": "EH", "Name": "Western Sahara"},{"Code": "YE", "Name": "Yemen"},{"Code": "ZM", "Name": "Zambia"},{"Code": "ZW", "Name": "Zimbabwe"}]


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
            name="United States"
        if(name=="UK"):
            name="United Kingdom"
        if(name=="S. Korea"):
            name="South Korea"
        if(name=="UAE"):
            name="United Arab Emirates"
        
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
            'name':name,
            'code':code,
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

