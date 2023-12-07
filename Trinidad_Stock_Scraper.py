
HEADER = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36'



import datetime
import os
from uuid import uuid4
import base64
import warnings

# def try_install_module(module_name):
#   """Try to install the specified module and import it."""
#   try:
#     return importlib.import_module(module_name)
#   except ImportError:
#     pip.install(module_name)
#     return importlib.import_module(module_name)


# # Try to install the following modules
# modules_to_install = ['requests', 'bs4', 'pandas', 'base64', 'js2py', 'sqlalchemy']

# for module_name in modules_to_install:
#   module = try_install_module(module_name)
#   print(f'Successfully installed {module_name}')


import js2py
import requests
from bs4 import BeautifulSoup as bs
import pandas as pd

# SQL DATABASE Libraries
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine, Column, Integer, String, Float, Date, ForeignKey, CheckConstraint, DateTime
# from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy import desc


warnings.simplefilter(action='ignore', category=FutureWarning)

#Database Name :

cwd = os.getcwd()


Location = r''
Database = os.path.join(Location,  'STOCK_DATABASE.db')

# Export Database
db_path        = Location

# # Initialize Method
Base = declarative_base()

class Stock_Data(Base):
    __tablename__       = 'stock_data'
    id                  = Column(Integer, primary_key=True)
    stock_Name          = Column(String)
    stock_Code          = Column(String)
    OPEN                = Column(Float)
    CLOSE               = Column(Float)
    VOLUME_TRADED       = Column(Float)
    OPEN                = Column(Float)
    stock_date           = Column(Date)


    # Utility Variable
    uniqueId = Column(String)
    date_created = Column(Date)
    last_updated = Column(Date)

    def __init__(self, stock_Name, stock_Code, CLOSE, VOLUME_TRADED, OPEN, stock_date):
        self.stock_Name     = stock_Name
        self.stock_Code     = stock_Code
        self.CLOSE          = CLOSE
        self.VOLUME_TRADED  = VOLUME_TRADED
        self.OPEN           = OPEN
        self.stock_date     = stock_date

        if self.uniqueId is None:
            self.uniqueId = str(uuid4()).split('-')[4]
        if self.date_created is None:
            self.date_created = datetime.datetime.now()


        self.last_updated = datetime.datetime.now()

    def __repr__(self):
        return f"<Stock_Data(stock_Code='{self.stock_Code}')>"

class CBTT_Rates(Base):
    __tablename__       = 'cbtt_rates'
    id                  = Column(Integer, primary_key=True)
    Canadian_Buy        = Column(Float)
    Canadian_Sell       = Column(Float)
    US_Buy              = Column(Float)
    US_Sell             = Column(Float)
    CBDate                = Column(Date)


    # Utility Variable
    uniqueId = Column(String)
    date_created = Column(Date)
    last_updated = Column(Date)

    def __init__(self, Canadian_Buy, Canadian_Sell, US_Buy, US_Sell, CBDate):
        self.Canadian_Buy   = Canadian_Buy
        self.Canadian_Sell  = Canadian_Sell
        self.US_Buy         = US_Buy
        self.US_Sell        = US_Sell
        self.CBDate           = CBDate

        if self.uniqueId is None:
            self.uniqueId = str(uuid4()).split('-')[4]
        if self.date_created is None:
            self.date_created = datetime.datetime.now()


        self.last_updated = datetime.datetime.now()

    def __repr__(self):
        return f"<CBTT_Rates(Date='{self.CBDate}')>"

############################################
#               FUNCTIONS
############################################

# Scrape CBTT
def getCBTTRATES():
    headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
    }
    parameters = {
        'sEcho': '1',
        'iColumns': '21',
        'sColumns': ',,,,,,,,,,,,,,,,,,,,',
        'iDisplayStart': '1',
        'iDisplayLength': '15000',
        'mDataProp_0': '0',
        'sSearch_0': '',
        'bRegex_0': 'false',
        'bSearchable_0': 'true',
        'bSortable_0': 'true',
        'mDataProp_1': '1',
        'sSearch_1': '',
        'bRegex_1': 'false',
        'bSearchable_1': 'true',
        'bSortable_1': 'false',
        'mDataProp_2': '2',
        'sSearch_2': '',
        'bRegex_2': 'false',
        'bSearchable_2': 'true',
        'bSortable_2': 'false',
        'mDataProp_3': '3',
        'sSearch_3': '',
        'bRegex_3': 'false',
        'bSearchable_3': 'true',
        'bSortable_3': 'false',
        'mDataProp_4': '4',
        'sSearch_4': '',
        'bRegex_4': 'false',
        'bSearchable_4': 'true',
        'bSortable_4': 'false',
        'mDataProp_5': '5',
        'sSearch_5': '',
        'bRegex_5': 'false',
        'bSearchable_5': 'true',
        'bSortable_5': 'false',
        'mDataProp_6': '6',
        'sSearch_6': '',
        'bRegex_6': 'false',
        'bSearchable_6': 'true',
        'bSortable_6': 'false',
        'mDataProp_7': '7',
        'sSearch_7': '',
        'bRegex_7': 'false',
        'bSearchable_7': 'true',
        'bSortable_7': 'false',
        'mDataProp_8': '8',
        'sSearch_8': '',
        'bRegex_8': 'false',
        'bSearchable_8': 'true',
        'bSortable_8': 'false',
        'mDataProp_9': '9',
        'sSearch_9': '',
        'bRegex_9': 'false',
        'bSearchable_9': 'true',
        'bSortable_9': 'false',
        'mDataProp_10': '10',
        'sSearch_10': '',
        'bRegex_10': 'false',
        'bSearchable_10': 'true',
        'bSortable_10': 'false',
        'mDataProp_11': '11',
        'sSearch_11': '',
        'bRegex_11': 'false',
        'bSearchable_11': 'true',
        'bSortable_11': 'false',
        'mDataProp_12': '12',
        'sSearch_12': '',
        'bRegex_12': 'false',
        'bSearchable_12': 'true',
        'bSortable_12': 'false',
        'mDataProp_13': '13',
        'sSearch_13': '',
        'bRegex_13': 'false',
        'bSearchable_13': 'true',
        'bSortable_13': 'false',
        'mDataProp_14': '14',
        'sSearch_14': '',
        'bRegex_14': 'false',
        'bSearchable_14': 'true',
        'bSortable_14': 'false',
        'mDataProp_15': '15',
        'sSearch_15': '',
        'bRegex_15': 'false',
        'bSearchable_15': 'true',
        'bSortable_15': 'false',
        'mDataProp_16': '16',
        'sSearch_16': '',
        'bRegex_16': 'false',
        'bSearchable_16': 'true',
        'bSortable_16': 'false',
        'mDataProp_17': '17',
        'sSearch_17': '',
        'bRegex_17': 'false',
        'bSearchable_17': 'true',
        'bSortable_17': 'false',
        'mDataProp_18': '18',
        'sSearch_18': '',
        'bRegex_18': 'false',
        'bSearchable_18': 'true',
        'bSortable_18': 'false',
        'mDataProp_19': '19',
        'sSearch_19': '',
        'bRegex_19': 'false',
        'bSearchable_19': 'true',
        'bSortable_19': 'false',
        'mDataProp_20': '20',
        'sSearch_20': '',
        'bRegex_20': 'false',
        'bSearchable_20': 'true',
        'bSortable_20': 'false',
        'sSearch': '',
        'bRegex': 'false',

    }

    URL = f'https://www.central-bank.org.tt/static/erdDataTable.php'

    response = requests.get(URL, headers =headers, params=parameters)
    if response.status_code == 200 :
        df = pd.DataFrame(response.json()['aaData'], columns=['Date','BBD Buying Rate','BBD Selling Rate','CAN Buying Rate','CAN Selling Rate','CHF Buying Rate','CHF Selling Rate','ECD Buying Rate','ECD Selling Rate','EURO Buying Rate','EURO Selling Rate','GBP Buying Rate','GBP Selling Rate','GYD Buying Rate','GYD Selling Rate','JMD Buying Rate','JMD Selling Rate','JPY Buying Rate','JPY Selling Rate','USD Buying Rate','USD Selling Rate'])[['Date','CAN Buying Rate','CAN Selling Rate','USD Buying Rate','USD Selling Rate']]
        fin_DF = df.dropna(subset=['Date','CAN Buying Rate','CAN Selling Rate','USD Buying Rate','USD Selling Rate'])
        fin_DF['Date'] = pd.to_datetime(fin_DF['Date'])
        return fin_DF

    return None

def add_to_db(session, df, codeName, code ):
    print('#'*50)
    stock_Name                = codeName
    Stock_Code                 = code

    print('[*] Stock Name           : ', stock_Name)
    print('[*] Stock Code           : ', Stock_Code)

    for index, pol_data in df.iterrows():
        try:

            try:
                OPEN      = float(pol_data['Open'])
            except:
                OPEN      = 0
            try:
                CLOSE      = float(pol_data['Close'])
            except:
                CLOSE      = 0
            try:
                VOLUME_TRADED      = float(pol_data['Volume Traded'])
            except:
                VOLUME_TRADED      = 0

            stock_date      = pol_data['Date']
            if pd.isna(stock_date):
                stock_date = None



            print('[*] MARKET DATE          : ', str(stock_date))
            # print('[*] Issue Date           : ', EffDate)
            # print('[*] REFUND Amt           : ', REFUND)

            stockdata = Stock_Data(
                stock_Name =  stock_Name,
                stock_Code =  Stock_Code,
                OPEN =  OPEN,
                CLOSE =  CLOSE,
                VOLUME_TRADED =  VOLUME_TRADED,
                stock_date =  stock_date
            )

            session.add(stockdata)
                # commit every 1000 objects to the database
            print('[*] Added to Database : ', stockdata)

            if index % 2000 == 0:
                session.commit()

            print('*'*50)
        except IndentationError as e:
            print('[*] Error : ', e)

    # commit any remaining objects to the database
    session.commit()

def add_to_db_CBTT(session, df):
    print('#'*50)
    for index, pol_data in df.iterrows():
        try:
            try:
                Canadian_Buy      = float(pol_data['CAN Buying Rate'])
            except:
                Canadian_Buy      = 0
            try:
                Canadian_Sell      = float(pol_data['CAN Selling Rate'])
            except:
                Canadian_Sell      = 0
            try:
                US_Buy      = float(pol_data['USD Buying Rate'])
            except:
                US_Buy      = 0
            try:
                US_Sell      = float(pol_data['USD Selling Rate'])
            except:
                US_Sell      = 0

            CBDate      = pol_data['Date']
            if pd.isna(CBDate):
                CBDate = None



            print('[*] MARKET DATE          : ', str(CBDate))
            # print('[*] Issue Date           : ', EffDate)
            # print('[*] REFUND Amt           : ', REFUND)

            cbttdata = CBTT_Rates(
                Canadian_Buy =  Canadian_Buy,
                Canadian_Sell =  Canadian_Sell,
                US_Buy =  US_Buy,
                US_Sell =  US_Sell,
                CBDate =  CBDate
            )

            session.add(cbttdata)
                # commit every 1000 objects to the database
            print('[*] Added to Database : ', cbttdata)

            if index % 2000 == 0:
                session.commit()

            print('*'*50)
        except IndentationError as e:
            print('[*] Error : ', e)

    # commit any remaining objects to the database
    session.commit()

def get_variable(encoded_script):

    decoded_script = base64.b64decode(encoded_script).decode('latin-1')

    js_code = decoded_script.replace('document.cookie','COOKIE').replace("location.reload();","")
    # print('[*] print : ', js_code)
    py_code = js2py.eval_js(js_code)
    result = py_code
    # print('[*] Cookie Code : ', result)
    return result


try:
    engine = create_engine(f'sqlite:///{Database}',  echo=False) # Echo = True means that it shows the logs
    Base.metadata.create_all(engine)

    # # Create a session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Scrape Market Watch

    StockCode = ['RY','SFC']
    countrycode = ['','ca']


    StockName = ['Royal Bank of Canada','Sagicor Financial Corporation']

    headers = {
        'User-Agent': HEADER
    }
    print('[*] Scraping : Market Watch')
    today = str(datetime.datetime.now().strftime("%m/%d/%Y"))
    for count in range(0,len(StockName)):

        code = StockCode[count]
        codeName = StockName[count]
        cc = countrycode[count]
        try:
            last_date = session.query(Stock_Data).filter(Stock_Data.stock_Code == f'{code}').order_by(desc(Stock_Data.stock_date)).first().__dict__['stock_date']
        except:
            last_date = datetime.date(2015,12,31)

        if last_date >= datetime.datetime.now().date() :
            pass
        else:
            datadf = []
            counter = 0
            df = None
            while True:

                URL = f'https://www.marketwatch.com/investing/stock/{code}/downloaddatapartial?'
                payload = {
                    'partial': 'true',
                    'index': counter,
                    'countryCode': cc,
                    'iso': '',
                    'startDate': '12/31/2021 00:00:00',
                    'endDate': f'{today} 00:00:00',
                    'frequency': 'P1D',
                    'downloadPartial': 'true',
                    'csvDownload': 'false',
                    'newDates': 'false',
                }


                response = requests.get(URL, headers = headers, params =  payload)

                if response.status_code == 200 :

                    try:
                        df = pd.read_html(response.content)[0]
                        df['Date'] = df['Date  Date'].apply(lambda row: row.split(' ')[0])
                        df['Date'] = pd.to_datetime(df['Date'], dayfirst=False)
                        df['Open'] = df['Open'].apply(lambda row: row.replace('$',''))
                        df['High'] = df['High'].apply(lambda row: row.replace('$',''))
                        df['Close'] = df['Close'].apply(lambda row: row.replace('$',''))
                        df['Low'] = df['Low'].apply(lambda row: row.replace('$',''))
                        datadf.append(df)
                    except ValueError :
                        break

                else:
                    print(f'[*] Error in {code} Code : {str(response.status_code)}')
                counter = counter + 1
            df = pd.concat(datadf)
            df = df[df['Date'].dt.date > last_date]
            add_to_db(session, df, codeName, code )

    print('[*] Scraping : TTSE')

    # Scrape TTSE

    StockCode = ['RFHL','NCBFG','FCGFH','SBTT','AGL','GHL','NEL','NFM','MASSY','PLD','PHL','UCL','NGL', 'FCI', 'GML']

    StockName = ['Republic Bank of Trinidad and Tobago Limited','NCB Financial Group','First Citizens Bank Ltd ','Scotiabank Ltd ','Agostinis Limited balance after sale','Guardian Holdings Limited balance after sale','National Enterprises Limited','National Flour Mills Limited','Massy Holdings Ltd Balance at 30.09.2017','Point Lisas Industrial Develop.','Prestige Holdings Limited','Unilever Caribbean Limited','TT NGL Limited', 'First Caribbean International Bank', 'Trinidad Publishing Company - Guardian Media Limited' ]

    headers = {
        'Authority':'www.stockex.co.tt',
        'Method':'GET',
        'Scheme':'https',
        'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'Accept-Encoding':'gzip, deflate, br',
        'Accept-Language':'en-US,en;q=0.9,de;q=0.8',
        'Cache-Control':'no-cache',

        'Cookie':"""sucuri_cloudproxy_uuid_2bf554b18=d8450e5c0a1eb7b610118d5c1a1f5305""".strip(),
        'Pragma':'no-cache',
        'Sec-Ch-Ua-Mobile':'?0',
        'Sec-Ch-Ua-Platform':'"Windows"',
        'Sec-Fetch-Dest':'document',
        'Sec-Fetch-Mode':'navigate',
        'Sec-Fetch-Site':'cross-site',
        'Sec-Fetch-User':'?1',
        'Upgrade-Insecure-Requests':'1',
        'User-Agent' : HEADER,
    }

    df = None
    count = 0

    for count in range(0,len(StockName)):
        code = StockCode[count]
        codeName = StockName[count]
        print('[*] Scraping : ',codeName, code)
        URL = f'https://www.stockex.co.tt/manage-stock/{code}/'

        try:
            last_date = session.query(Stock_Data).filter(Stock_Data.stock_Code == f'{code}').order_by(desc(Stock_Data.stock_date)).first().__dict__['stock_date']
        except:
            last_date = datetime.date(2015,12,31)
        if last_date >= datetime.datetime.now().date() :
            pass
        else:
            response = requests.get(URL, headers =headers)

            # get_variable(str(response.text))
            soup = bs(response.content, 'lxml')
            scpt = soup.find('script')
            string_of_characters = scpt.text.split('S=')[1].split(';')[0]
            string_of_characters = string_of_characters

            # print(string_of_characters)
            print('*'*50)
            try:
                decodedCode = get_variable(str(string_of_characters)).split(";")[0]
            except Exception as e:
                print(f'[*] Error : {e}')
            print('[*] Decoded Security Code : ', decodedCode)
            print('*'*50)
                                                                #  sucuri_cloudproxy_uuid_39a6883fc=9f489ca8bd4da156a5bbe93c14eeac82
            response = requests.get(URL, headers = {'Cookie':f"""{decodedCode};""".strip(),'User-Agent':HEADER})

            if 'redirected' in str(response.content):
                soup = bs(response.content, 'lxml')

                scpt = soup.find('script')
                coded = scpt.text.split('S=')[1].split(';')[0]
                decoded = base64.b64decode(coded).decode('latin-1')

                js_code = decoded.replace('\n','').replace("location.reload();","").replace("document.cookie","DecodedCode")
                py_code = js2py.eval_js(js_code)
                decodedCode = py_code.split(";")[0]

                response = requests.get(URL, headers = {'Cookie':f"""{decodedCode};""".strip(),'User-Agent':HEADER})


            # response = requests.get(URL, headers = {'Cookie':f"""sucuricp_tfca_6e453141ae697f9f78b18427b4c54df1=1;{decodedCode};""".strip(),'User-Agent': HEADER})
            if response.status_code == 200 :
                try:
                    df = pd.read_html(response.content)[2]
                    print(df)
                    df['Date'] = pd.to_datetime(df['Date'], dayfirst=True, format='mixed')
                    df = df[df['Date'].dt.date > last_date]
                    add_to_db(session, df, codeName, code )
                except KeyError :
                    print(f'[*] Error in {code} Code')
            else:
                print(f'[*] Error in {code} Code : {str(response.status_code)}')


    df = getCBTTRATES()
    try:
        last_date = session.query(CBTT_Rates).filter(CBTT_Rates.CBDate).order_by(desc(CBTT_Rates.CBDate)).first().__dict__['CBDate']
    except:
        last_date = datetime.date(2015,12,31)

    df = df[df['Date'].dt.date > last_date]

    add_to_db_CBTT(session, df)

    session.close()
    print('[*] PROGRAM ENDED')
    print('*'*50)

except IndentationError as e:
    pass