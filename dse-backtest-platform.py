import sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from bs4                             import BeautifulSoup
from selenium                        import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options
from webdriver_manager.microsoft     import EdgeChromiumDriverManager

stocks = [
    '1JANATAMF',
    '1STPRIMFMF',
    'AAMRANET',
    'AAMRATECH',
    'ABB1STMF',
    'ABBANK',
    'ACFL',
    'ACI',
    'ACIFORMULA',
    'ACMELAB',
    'ACMEPL',
    'ACTIVEFINE',
    'ADNTEL',
    'ADVENT',
    'AFCAGRO',
    'AFTABAUTO',
    'AGNISYSL',
    'AGRANINS',
    'AIBL1STIMF',
    'AIBLPBOND',
    'AIL',
    'AL-HAJTEX',
    'ALARABANK',
    'ALIF',
    'ALLTEX',
    'AMANFEED',
    'AMBEEPHA',
    'AMCL(PRAN)',
    'ANLIMAYARN',
    'ANWARGALV',
    'AOL',
    'APEXFOODS',
    'APEXFOOT',
    'APEXSPINN',
    'APEXTANRY',
    'APOLOISPAT',
    'APSCLBOND',
    'ARAMIT',
    'ARAMITCEM',
    'ARGONDENIM',
    'ASIAINS',
    'ASIAPACINS',
    'ATCSLGF',
    'ATLASBANG',
    'AZIZPIPES',
    'BANGAS',
    'BANKASIA',
    'BARKAPOWER',
    'BATASHOE',
    'BATBC',
    'BAYLEASING',
    'BBS',
    'BBSCABLES',
    'BDAUTOCA',
    'BDCOM',
    'BDFINANCE',
    'BDLAMPS',
    'BDSERVICE',
    'BDTHAI',
    'BDTHAIFOOD',
    'BDWELDING',
    'BEACHHATCH',
    'BEACONPHAR',
    'BENGALWTL',
    'BERGERPBL',
    'BEXGSUKUK',
    'BEXIMCO',
    'BGIC',
    'BIFC',
    'BNICL',
    'BPML',
    'BPPL',
    'BRACBANK',
    'BSC',
    'BSCCL',
    'BSRMLTD',
    'BSRMSTEEL',
    'BXPHARMA',
    'BXSYNTH',
    'CAPMBDBLMF',
    'CAPMIBBLMF',
    'CENTRALINS',
    'CENTRALPHL',
    'CITYBANK',
    'CITYGENINS',
    'CNATEX',
    'CONFIDCEM',
    'CONTININS',
    'COPPERTECH',
    'CROWNCEMNT',
    'CRYSTALINS',
    'CVOPRL',
    'DACCADYE',
    'DAFODILCOM',
    'DBH',
    'DBH1STMF',
    'DEBARACEM',
    'DEBBDLUGG',
    'DEBBDWELD',
    'DEBBDZIPP',
    'DEBBXDENIM',
    'DEBBXFISH',
    'DEBBXKNI',
    'DEBBXTEX',
    'DELTALIFE',
    'DELTASPINN',
    'DESCO',
    'DESHBANDHU',
    'DGIC',
    'DHAKABANK',
    'DHAKAINS',
    'DOMINAGE',
    'DOREENPWR',
    'DSHGARME',
    'DSSL',
    'DULAMIACOT',
    'DUTCHBANGL',
    'EASTERNINS',
    'EASTLAND',
    'EASTRNLUB',
    'EBL',
    'EBL1STMF',
    'EBLNRBMF',
    'ECABLES',
    'EGEN',
    'EHL',
    'EIL',
    'EMERALDOIL',
    'ENVOYTEX',
    'EPGL',
    'ESQUIRENIT',
    'ETL',
    'EXIM1STMF',
    'EXIMBANK',
    'FAMILYTEX',
    'FARCHEM',
    'FAREASTFIN',
    'FAREASTLIF',
    'FASFIN',
    'FBFIF',
    'FEDERALINS',
    'FEKDIL',
    'FINEFOODS',
    'FIRSTFIN',
    'FIRSTSBANK',
    'FORTUNE',
    'FUWANGCER',
    'FUWANGFOOD',
    'GBBPOWER',
    'GEMINISEA',
    'GENEXIL',
    'GENNEXT',
    'GHAIL',
    'GHCL',
    'GLOBALINS',
    'GOLDENSON',
    'GP',
    'GPHISPAT',
    'GQBALLPEN',
    'GRAMEENS2',
    'GREENDELMF',
    'GREENDELT',
    'GSPFINANCE',
    'HAKKANIPUL',
    'HEIDELBCEM',
    'HFL',
    'HRTEX',
    'HWAWELLTEX',
    'IBBL2PBOND',
    'IBBLPBOND',
    'IBNSINA',
    'IBP',
    'ICB',
    'ICB3RDNRB',
    'ICBAGRANI1',
    'ICBAMCL2ND',
    'ICBEPMF1S1',
    'ICBIBANK',
    'ICBSONALI1',
    'IDLC',
    'IFADAUTOS',
    'IFIC',
    'IFIC1STMF',
    'IFILISLMF1',
    'ILFSL',
    'IMAMBUTTON',
    'INDEXAGRO',
    'INTECH',
    'INTRACO',
    'IPDC',
    'ISLAMIBANK',
    'ISLAMICFIN',
    'ISLAMIINS',
    'ISNLTD',
    'ITC',
    'JAMUNABANK',
    'JAMUNAOIL',
    'JANATAINS',
    'JHRML',
    'JMISMDL',
    'JUTESPINN',
    'KARNAPHULI',
    'KBPPWBIL',
    'KDSALTD',
    'KEYACOSMET',
    'KOHINOOR',
    'KPCL',
    'KPPL',
    'KTL',
    'LANKABAFIN',
    'LEGACYFOOT',
    'LHBL',
    'LIBRAINFU',
    'LINDEBD',
    'LOVELLO',
    'LRBDL',
    'LRGLOBMF1',
    'MAKSONSPIN',
    'MALEKSPIN',
    'MARICO',
    'MATINSPINN',
    'MBL1STMF',
    'MEGCONMILK',
    'MEGHNACEM',
    'MEGHNAINS',
    'MEGHNALIFE',
    'MEGHNAPET',
    'MERCANBANK',
    'MERCINS',
    'METROSPIN',
    'MHSML',
    'MIDASFIN',
    'MIRACLEIND',
    'MIRAKHTER',
    'MITHUNKNIT',
    'MJLBD',
    'MLDYEING',
    'MONNOAGML',
    'MONNOCERA',
    'MONNOFABR',
    'MONOSPOOL',
    'MPETROLEUM',
    'MTB',
    'NAHEEACP',
    'NATLIFEINS',
    'NAVANACNG',
    'NBL',
    'NCCBANK',
    'NCCBLMF1',
    'NEWLINE',
    'NFML',
    'NHFIL',
    'NITOLINS',
    'NLI1STMF',
    'NORTHERN',
    'NORTHRNINS',
    'NPOLYMER',
    'NRBCBANK',
    'NTC',
    'NTLTUBES',
    'NURANI',
    'OAL',
    'OIMEX',
    'OLYMPIC',
    'ONEBANKLTD',
    'ORIONINFU',
    'ORIONPHARM',
    'PADMALIFE',
    'PADMAOIL',
    'PAPERPROC',
    'PARAMOUNT',
    'PBLPBOND',
    'PDL',
    'PENINSULA',
    'PEOPLESINS',
    'PF1STMF',
    'PHARMAID',
    'PHENIXINS',
    'PHOENIXFIN',
    'PHPMF1',
    'PIONEERINS',
    'PLFSL',
    'POPULAR1MF',
    'POPULARLIF',
    'POWERGRID',
    'PRAGATIINS',
    'PRAGATILIF',
    'PREBPBOND',
    'PREMIERBAN',
    'PREMIERCEM',
    'PREMIERLEA',
    'PRIME1ICBA',
    'PRIMEBANK',
    'PRIMEFIN',
    'PRIMEINSUR',
    'PRIMELIFE',
    'PRIMETEX',
    'PROGRESLIF',
    'PROVATIINS',
    'PTL',
    'PUBALIBANK',
    'PURABIGEN',
    'QUASEMIND',
    'QUEENSOUTH',
    'RAHIMAFOOD',
    'RAHIMTEXT',
    'RAKCERAMIC',
    'RANFOUNDRY',
    'RDFOOD',
    'RECKITTBEN',
    'REGENTTEX',
    'RELIANCE1',
    'RELIANCINS',
    'RENATA',
    'RENWICKJA',
    'REPUBLIC',
    'RINGSHINE',
    'RNSPIN',
    'ROBI',
    'RSRMSTEEL',
    'RUNNERAUTO',
    'RUPALIBANK',
    'RUPALIINS',
    'RUPALILIFE',
    'SAFKOSPINN',
    'SAIFPOWER',
    'SAIHAMCOT',
    'SAIHAMTEX',
    'SALAMCRST',
    'SALVOCHEM',
    'SAMATALETH',
    'SAMORITA',
    'SANDHANINS',
    'SAPORTL',
    'SAVAREFR',
    'SBACBANK',
    'SEAPEARL',
    'SEMLFBSLGF',
    'SEMLIBBLSF',
    'SEMLLECMF',
    'SHAHJABANK',
    'SHASHADNIM',
    'SHEPHERD',
    'SHURWID',
    'SHYAMPSUG',
    'SIBL',
    'SILCOPHL',
    'SILVAPHL',
    'SIMTEX',
    'SINGERBD',
    'SINOBANGLA',
    'SJIBLPBOND',
    'SKICL',
    'SKTRIMS',
    'SONALIANSH',
    'SONALILIFE',
    'SONALIPAPR',
    'SONARBAINS',
    'SONARGAON',
    'SOUTHEASTB',
    'SPCERAMICS',
    'SPCL',
    'SQUARETEXT',
    'SQURPHARMA',
    'SSSTEEL',
    'STANCERAM',
    'STANDARINS',
    'STANDBANKL',
    'STYLECRAFT',
    'SUMITPOWER',
    'SUNLIFEINS',
    'TAKAFULINS',
    'TALLUSPIN',
    'TAMIJTEX',
    'TITASGAS',
    'TOSRIFA',
    'TRUSTB1MF',
    'TRUSTBANK',
    'TUNGHAI',
    'UCB',
    'UNILEVERCL',
    'UNIONBANK',
    'UNIONCAP',
    'UNIONINS',
    'UNIQUEHRL',
    'UNITEDFIN',
    'UNITEDINS',
    'UPGDCL',
    'USMANIAGL',
    'UTTARABANK',
    'UTTARAFIN',
    'VAMLBDMF1',
    'VAMLRBBF',
    'VFSTDL',
    'WALTONHIL',
    'WATACHEM',
    'WMSHIPYARD',
    'YPL',
    'ZAHEENSPIN',
    'ZAHINTEX',
    'ZEALBANGLA'
]

stocks_to_trade = [
    'AAMRANET',
    'AAMRATECH',
    'ABBANK',
    'ACFL',
    'ACI',
    'ACIFORMULA',
    'ACMELAB',
    'ACMEPL',
    'ACTIVEFINE',
    'ADNTEL',
    'ADVENT',
    'AFCAGRO',
    'AFTABAUTO',
    'AGNISYSL',
    'AGRANINS',
    'AIL',
    'AL-HAJTEX',
    'ALARABANK',
    'ALIF',
    'ALLTEX',
    'AMANFEED',
    'AMBEEPHA',
    'AMCL(PRAN)',
    'ANLIMAYARN',
    'ANWARGALV',
    'AOL',
    'APEXFOODS',
    'APEXFOOT',
    'APEXSPINN',
    'APEXTANRY',
    'APOLOISPAT',
    'ARAMIT',
    'ARAMITCEM',
    'ARGONDENIM',
    'ASIAINS',
    'ASIAPACINS',
    'ATCSLGF',
    'ATLASBANG',
    'AZIZPIPES',
    'BANGAS',
    'BANKASIA',
    'BARKAPOWER',
    'BATASHOE',
    'BATBC',
    'BAYLEASING',
    'BBS',
    'BBSCABLES',
    'BDAUTOCA',
    'BDCOM',
    'BDFINANCE',
    'BDLAMPS',
    'BDTHAI',
    'BDTHAIFOOD',
    'BDWELDING',
    'BEACHHATCH',
    'BEACONPHAR',
    'BENGALWTL',
    'BERGERPBL',
    'BEXGSUKUK',
    'BEXIMCO',
    'BGIC',
    'BIFC',
    'BNICL',
    'BPML',
    'BPPL',
    'BRACBANK',
    'BSC',
    'BSCCL',
    'BSRMLTD',
    'BSRMSTEEL',
    'BXPHARMA',
    'BXSYNTH',
    'CENTRALINS',
    'CENTRALPHL',
    'CITYBANK',
    'CITYGENINS',
    'CNATEX',
    'CONFIDCEM',
    'CONTININS',
    'COPPERTECH',
    'CROWNCEMNT',
    'CRYSTALINS',
    'CVOPRL',
    'DACCADYE',
    'DAFODILCOM',
    'DBH',
    'DELTALIFE',
    'DELTASPINN',
    'DESCO',
    'DESHBANDHU',
    'DGIC',
    'DHAKABANK',
    'DHAKAINS',
    'DOMINAGE',
    'DOREENPWR',
    'DSHGARME',
    'DSSL',
    'DULAMIACOT',
    'DUTCHBANGL',
    'EASTERNINS',
    'EASTLAND',
    'EASTRNLUB',
    'EBL',
    'ECABLES',
    'EGEN',
    'EHL',
    'EIL',
    'EMERALDOIL',
    'ENVOYTEX',
    'EPGL',
    'ESQUIRENIT',
    'ETL',
    'EXIMBANK',
    'FAMILYTEX',
    'FARCHEM',
    'FAREASTFIN',
    'FAREASTLIF',
    'FASFIN',
    'FBFIF',
    'FEDERALINS',
    'FEKDIL',
    'FINEFOODS',
    'FIRSTFIN',
    'FIRSTSBANK',
    'FORTUNE',
    'FUWANGCER',
    'FUWANGFOOD',
    'GBBPOWER',
    'GEMINISEA',
    'GENEXIL',
    'GENNEXT',
    'GHAIL',
    'GHCL',
    'GLOBALINS',
    'GOLDENSON',
    'GP',
    'GPHISPAT',
    'GQBALLPEN',
    'GRAMEENS2',
    'GREENDELT',
    'GSPFINANCE',
    'HAKKANIPUL',
    'HEIDELBCEM',
    'HFL',
    'HRTEX',
    'HWAWELLTEX',
    'IBNSINA',
    'IBP',
    'ICB',
    'ICB3RDNRB',
    'ICBAGRANI1',
    'ICBAMCL2ND',
    'ICBIBANK',
    'ICBSONALI1',
    'IDLC',
    'IFADAUTOS',
    'IFIC',
    'ILFSL',
    'IMAMBUTTON',
    'INDEXAGRO',
    'INTECH',
    'INTRACO',
    'IPDC',
    'ISLAMIBANK',
    'ISLAMICFIN',
    'ISLAMIINS',
    'ISNLTD',
    'ITC',
    'JAMUNABANK',
    'JAMUNAOIL',
    'JANATAINS',
    'JHRML',
    'JMISMDL',
    'JUTESPINN',
    'KARNAPHULI',
    'KBPPWBIL',
    'KDSALTD',
    'KEYACOSMET',
    'KOHINOOR',
    'KPCL',
    'KPPL',
    'KTL',
    'LANKABAFIN',
    'LEGACYFOOT',
    'LHBL',
    'LIBRAINFU',
    'LINDEBD',
    'LOVELLO',
    'LRBDL',
    'MAKSONSPIN',
    'MALEKSPIN',
    'MARICO',
    'MATINSPINN',
    'MEGCONMILK',
    'MEGHNACEM',
    'MEGHNAINS',
    'MEGHNALIFE',
    'MEGHNAPET',
    'MERCANBANK',
    'MERCINS',
    'METROSPIN',
    'MHSML',
    'MIDASFIN',
    'MIRACLEIND',
    'MIRAKHTER',
    'MITHUNKNIT',
    'MJLBD',
    'MLDYEING',
    'MONNOAGML',
    'MONNOCERA',
    'MONNOFABR',
    'MONOSPOOL',
    'MPETROLEUM',
    'MTB',
    'NAHEEACP',
    'NATLIFEINS',
    'NAVANACNG',
    'NBL',
    'NCCBANK',
    'NEWLINE',
    'NFML',
    'NHFIL',
    'NITOLINS',
    'NORTHERN',
    'NORTHRNINS',
    'NPOLYMER',
    'NRBCBANK',
    'NTC',
    'NTLTUBES',
    'NURANI',
    'OAL',
    'OIMEX',
    'OLYMPIC',
    'ONEBANKLTD',
    'ORIONINFU',
    'ORIONPHARM',
    'PADMALIFE',
    'PADMAOIL',
    'PAPERPROC',
    'PARAMOUNT',
    'PDL',
    'PENINSULA',
    'PEOPLESINS',
    'PHARMAID',
    'PHENIXINS',
    'PHOENIXFIN',
    'PIONEERINS',
    'POPULARLIF',
    'POWERGRID',
    'PRAGATIINS',
    'PRAGATILIF',
    'PREMIERBAN',
    'PREMIERCEM',
    'PREMIERLEA',
    'PRIME1ICBA',
    'PRIMEBANK',
    'PRIMEFIN',
    'PRIMEINSUR',
    'PRIMELIFE',
    'PRIMETEX',
    'PROGRESLIF',
    'PROVATIINS',
    'PTL',
    'PUBALIBANK',
    'PURABIGEN',
    'QUASEMIND',
    'QUEENSOUTH',
    'RAHIMAFOOD',
    'RAHIMTEXT',
    'RAKCERAMIC',
    'RANFOUNDRY',
    'RDFOOD',
    'RECKITTBEN',
    'REGENTTEX',
    'RELIANCE1',
    'RELIANCINS',
    'RENATA',
    'RENWICKJA',
    'REPUBLIC',
    'RINGSHINE',
    'RNSPIN',
    'ROBI',
    'RSRMSTEEL',
    'RUNNERAUTO',
    'RUPALIBANK',
    'RUPALIINS',
    'RUPALILIFE',
    'SAFKOSPINN',
    'SAIFPOWER',
    'SAIHAMCOT',
    'SAIHAMTEX',
    'SALAMCRST',
    'SALVOCHEM',
    'SAMATALETH',
    'SAMORITA',
    'SANDHANINS',
    'SAPORTL',
    'SAVAREFR',
    'SBACBANK',
    'SEAPEARL',
    'SEMLFBSLGF',
    'SEMLIBBLSF',
    'SHAHJABANK',
    'SHASHADNIM',
    'SHEPHERD',
    'SHURWID',
    'SHYAMPSUG',
    'SIBL',
    'SILCOPHL',
    'SILVAPHL',
    'SIMTEX',
    'SINGERBD',
    'SINOBANGLA',
    'SKICL',
    'SKTRIMS',
    'SONALIANSH',
    'SONALILIFE',
    'SONALIPAPR',
    'SONARBAINS',
    'SONARGAON',
    'SOUTHEASTB',
    'SPCERAMICS',
    'SPCL',
    'SQUARETEXT',
    'SQURPHARMA',
    'SSSTEEL',
    'STANCERAM',
    'STANDARINS',
    'STANDBANKL',
    'STYLECRAFT',
    'SUMITPOWER',
    'SUNLIFEINS',
    'TAKAFULINS',
    'TALLUSPIN',
    'TAMIJTEX',
    'TITASGAS',
    'TOSRIFA',
    'TRUSTBANK',
    'TUNGHAI',
    'UCB',
    'UNILEVERCL',
    'UNIONBANK',
    'UNIONCAP',
    'UNIONINS',
    'UNIQUEHRL',
    'UNITEDFIN',
    'UNITEDINS',
    'UPGDCL',
    'USMANIAGL',
    'UTTARABANK',
    'UTTARAFIN',
    'VAMLRBBF',
    'VFSTDL',
    'WALTONHIL',
    'WATACHEM',
    'WMSHIPYARD',
    'YPL',
    'ZAHEENSPIN',
    'ZAHINTEX',
    'ZEALBANGLA'
]

def scrape_stock_data(
    driver,
    stock,
    testing=False
):
    stock_archive = (
          'https://dsebd.org/day_end_archive.php?'
        + 'startDate=2020-06-19'
        + '&endDate=2022-06-19'
        + '&inst=%s'
        + '&archive=data'
    ) % (
        stock 
    )
    
    page = driver.get(stock_archive)
    
    if not testing:
        print('Scraping data for stock %s' % stock)
        
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        
        table = soup.find(
            name='table',
            attrs={'class':'table table-bordered background-white shares-table fixedHeader'}
        )
        
        table_body = table.find('tbody')
        
        rows = table_body.find_all('tr')
        
        with open(stock + ".txt", 'w') as fp:
            fp.write('DATE TRADECODE LAST_TRADE_PRICE HIGH LOW OPEN CLOSE YDAY_CLOSE NUM_TRADES VALUE_IN_MN NUM_SHARES\n')
            
            for row in rows:
                cols = row.find_all('td')
                cols = [col.text.strip() for col in cols][1:]
                
                for col in cols:
                    fp.write(col.replace(',', '') + " ")
                
                fp.write('\n')

def start_driver():
    options = Options()
    options.add_argument('start-maximized')
    
    driver = webdriver.Edge(
        service=Service( EdgeChromiumDriverManager().install() ),
        options=options
    )
    
    return driver

def test_list_of_stocks(
    driver
):
    # testing by looping over all the stocks without scraping data
    for stock in stocks:
        try:
            scrape_stock_data(
                driver=driver,
                stock=stock,
                testing=True
            )
        except KeyboardInterrupt:
            sys.exit()
        except:
            print('Testing failed at stock %s' % stock)
            continue

def scrape_all_stock_data(
    driver
):
    for stock in stocks:
        try:
            scrape_stock_data(
                driver=driver,
                stock=stock
            )
        except KeyboardInterrupt:
            sys.exit()
        except:
            print('Failed to scrape data of stock %s' % stock)
            continue

def plot_data(
    x_data,
    y_data
):
    fig, ax = plt.subplots()
    
    ax.plot(
        x_data,
        y_data
    )
    
    plt.show()

def read_stock_data(
    stock
):
    #print('Reading data for stock %s' % stock)
    
    # flip dataframe horizontally to fix dates
    stock_data = pd.read_csv(
        filepath_or_buffer=(stock + '.txt'),
        delimiter=' ',
        index_col=False
    )[::-1]
    
    # removing rows with zero volume, assuming stock not traded that day
    stock_data = stock_data.iloc[ np.where(stock_data['NUM_SHARES'] != 0)[0] ]
    
    stock_data.reset_index(inplace=True)
    
    return stock_data
    
def read_all_stock_data():
    return {stock : read_stock_data(stock) for stock in stocks_to_trade}
    
def compute_relative_volume(
    stock_data,
    moving_average_window
):
    return (
        stock_data['VALUE_IN_MN']
        /
        stock_data['VALUE_IN_MN'].rolling(window=moving_average_window).mean()
    )
    
def add_relative_volume(
    stock,
    stock_data,
    all_stock_data,
    moving_average_window
):
    all_stock_data[stock]['REL_VOL'] = compute_relative_volume(
        stock_data=stock_data,
        moving_average_window=moving_average_window
    )
    
def add_all_relative_volumes(
    all_stock_data,
    moving_average_window
):
    for stock in stocks_to_trade:
        add_relative_volume(
            stock=stock,
            stock_data=all_stock_data[stock],
            all_stock_data=all_stock_data,
            moving_average_window=moving_average_window
        )

def compute_average_true_range(
    stock_data,
    moving_average_window
):
    high = stock_data['HIGH'].values
    low  = stock_data['LOW'].values
    ycp  = stock_data['YDAY_CLOSE'].values
    
    diff_high_low = np.abs(high - low)
    
    diff_ycp_high = np.array( [0, *np.abs( high[1:] - ycp[:-1] ) ] )
    diff_ycp_low  = np.array( [0, *np.abs( low[1:]  - ycp[:-1] ) ] )
    
    true_range = pd.Series(
        np.maximum.reduce(
            [
                diff_high_low,
                diff_ycp_high,
                diff_ycp_low
            ]
        )
    )
    
    return true_range.rolling(window=moving_average_window).mean()
    
def add_average_true_range(
    stock,
    stock_data,
    all_stock_data,
    moving_average_window
):
    all_stock_data[stock]['ATR'] = compute_average_true_range(
        stock_data=stock_data,
        moving_average_window=moving_average_window
    )
    
def add_all_average_true_ranges(
    all_stock_data,
    moving_average_window
):
    for stock in stocks_to_trade:
        add_average_true_range(
            stock=stock,
            stock_data=all_stock_data[stock],
            all_stock_data=all_stock_data,
            moving_average_window=moving_average_window
        )

def simulate_market():
    market_data = read_all_stock_data()
    
    add_all_relative_volumes(
        all_stock_data=market_data,
        moving_average_window=5
    )
    
    add_all_average_true_ranges(
        all_stock_data=market_data,
        moving_average_window=5
    )
    
    return market_data

class Position:
    def __init__(
        self,
        stock,
        open,
        abs_R,
        entry_commission,
        entry_slippage,
        price_noise,
        price_noise_scale_factor
    ):
        self.stock                    = stock
        self.abs_R                    = abs_R
        self.num_shares               = int( abs_R / (2 * price_noise_scale_factor * price_noise) )
        self.buy_price_per_share      = open * (1 + entry_slippage)
        self.buy_price                = self.buy_price_per_share * self.num_shares
        self.entry_price              = self.buy_price * (1 + entry_commission)
        self.stop_loss                = np.max( [ 0, self.buy_price_per_share - (price_noise_scale_factor * price_noise) ] )
        self.days_held                = 0
        
        
class Book:
    def __init__(
        self,
        name,
        starting_capital,
        R_per_position,
        price_noise_scale_factor
    ):
        self.name                     = name
        self.available_capital        = starting_capital
        self.invested_capital         = 0
        self.R_per_position           = R_per_position
        self.abs_R_per_position       = starting_capital * R_per_position
        self.price_noise_scale_factor = price_noise_scale_factor
        self.positions                = {}
        self.positions_exited         = 0
        self.PnL_data                 = {
            'Stock'                : [],
            'Days held'            : [],
            'Number of shares'     : [],
            'Buy price per share'  : [],
            'Sell price per share' : [],
            'Entry'                : [],
            'Exit'                 : [],
            'Profit'               : [],
            'R'                    : [],
            'Available capital'    : []
        }
        
    
    def write_PnL(
        self
    ):
        PnL_df = pd.DataFrame.from_dict(self.PnL_data)
        
        print( ('Total PnL of book %s: ' % self.name) + str( PnL_df['Profit'].sum() ) )
        
        PnL_df.to_csv('book-%s-PnL.csv' % self.name)
        
    def increment_days_held(
        self,
        stock
    ):
        if stock in self.positions:
            self.positions[stock].days_held += 1
    
    def enter_position(
        self,
        stock,
        open,
        entry_commission,
        entry_slippage,
        price_noise
    ):
        if price_noise == 0:
            print('Price noise is zero, cannot compute a position')
            return
        
        if open == 0:
            print('Open price is zero, hopefully because stock was not traded this day, not entering position')
            return
        
        if stock in self.positions:
            sys.exit('Exiting: tried to buy a stock that is already in the book (%s)' % stock)
        
        position = Position(
            stock=stock,
            open=open,
            abs_R=self.abs_R_per_position,
            entry_commission=entry_commission,
            entry_slippage=entry_slippage,
            price_noise=price_noise,
            price_noise_scale_factor=self.price_noise_scale_factor
        )
        
        enough_capital = ( (self.available_capital - position.entry_price) > 0 )
        enough_shares  = (position.num_shares > 0)
        
        if enough_capital and enough_shares:
            #print('Entering position in stock %s' % stock)
            
            self.available_capital -= position.entry_price
            
            self.positions[stock] = position
            
    def append_position_PnL(
        self,
        position,
        sell_price_per_share,
        exit_price
    ):
        profit   = exit_price - position.entry_price
        profit_R = profit / position.abs_R
        
        self.PnL_data['Stock'].append(position.stock)
        self.PnL_data['Days held'].append(position.days_held)
        self.PnL_data['Number of shares'].append(position.num_shares)
        self.PnL_data['Buy price per share'].append(position.buy_price_per_share)
        self.PnL_data['Sell price per share'].append(sell_price_per_share)
        self.PnL_data['Entry'].append(position.entry_price)
        self.PnL_data['Exit'].append(exit_price)
        self.PnL_data['Profit'].append(profit)
        self.PnL_data['R'].append(profit_R)
        self.PnL_data['Available capital'].append(self.available_capital)
    
    def exit_position(
        self,
        stock,
        open,
        exit_commission,
        exit_slippage
    ):
        if stock not in self.positions:
            sys.exit('Exiting: tried to sell a stock that is not in the book')
        
        if open == 0:
            print('Open price is zero, hopefully because stock was not traded this day, not exiting position')
            return
        
        #print('Exiting position in stock %s' % stock)
        
        sell_price_per_share = open * (1 - exit_slippage)
        sell_price           = sell_price_per_share * self.positions[stock].num_shares
        exit_price           = sell_price * (1 - exit_commission)
        
        self.available_capital += exit_price
        
        self.positions_exited += 1
        
        self.append_position_PnL(
            position=self.positions[stock],
            sell_price_per_share=sell_price_per_share,
            exit_price=exit_price
        )
        
        del self.positions[stock]
        
    def hold_position(
        self,
        stock,
        open,
        price_noise
    ):
        if stock not in self.positions:
            sys.exit('Exiting: tried to hold a stock that is not in the book')
        
        #print('Holding position in stock %s' % stock)
        
        sf        = self.price_noise_scale_factor
        days_held = self.positions[stock].days_held
        
        new_stop_loss = open - sf * price_noise
        
        new_stop_loss = np.max( [0, new_stop_loss] )
        
        if new_stop_loss > self.positions[stock].stop_loss:
            self.positions[stock].stop_loss = new_stop_loss
        
def compute_entry_signal(
    rel_vol,
    entry_rel_vol
):
    return rel_vol <= entry_rel_vol
    
def compute_exit_signal(
    open,
    stop_loss,
    days_held
):
    return (
        open < stop_loss
        and
        days_held > 2
    )

def manage_position(
    stock,
    stock_data,
    trading_date,
    book
):
    current_traded_day = np.where(stock_data['DATE'].values == trading_date)[0][0]
    yday_traded_day    = current_traded_day - 1
    
    # only consider stock if it's been traded for at least 5 days
    if current_traded_day <= 4:
        return
    
    open = stock_data['OPEN'].iloc[current_traded_day]
    
    should_exit = compute_exit_signal(
        open=open,
        stop_loss=book.positions[stock].stop_loss,
        days_held=book.positions[stock].days_held
    )
    
    if should_exit:
        book.exit_position(
            stock=stock,
            open=open,
            exit_commission=0.01,
            exit_slippage=0.01
        )
    else:
        yday_ATR = stock_data['ATR'].iloc[yday_traded_day]
        
        book.hold_position(
            stock=stock,
            open=open,
            price_noise=yday_ATR
        )

def check_stock_for_entry(
    stock,
    stock_data,
    trading_date,
    entry_rel_vol,
    candidate_stocks
):
    current_traded_day = np.where(stock_data['DATE'].values == trading_date)[0][0]
    yday_traded_day    = current_traded_day - 1
    
    # only consider stock if it's been traded for at least 5 days
    if current_traded_day <= 4:
        return
    
    yday_rel_vol = stock_data['REL_VOL'].iloc[yday_traded_day]
    
    should_enter = compute_entry_signal(
        rel_vol=yday_rel_vol,
        entry_rel_vol=entry_rel_vol
    )
    
    if should_enter:
        candidate_stocks[stock] = yday_rel_vol
        
def open_new_positions(
    market_data,
    trading_date,
    candidate_stocks,
    book
):
    # sort candidate_stocks from lowest yday_rel_vol
    # https://docs.python.org/3/howto/sorting.html#key-functions
    candidate_stocks_sorted = {
        stock : rel_vol
        for stock, rel_vol in sorted( candidate_stocks.items(), key=lambda stock_rel_vol_tuple : stock_rel_vol_tuple[1], reverse=True )
    }
    
    for stock in candidate_stocks_sorted:
        stock_data = market_data[stock]
        
        current_traded_day = np.where(stock_data['DATE'] == trading_date)[0][0]
        yday_traded_day    = current_traded_day - 1
        
        open     = stock_data['OPEN'].iloc[current_traded_day]
        yday_ATR = stock_data['ATR'].iloc[yday_traded_day]
        
        book.enter_position(
            stock=stock,
            open=open,
            entry_commission=0.01,
            entry_slippage=0.01,
            price_noise=yday_ATR
        )
        
        # enter at most one position per day
        # exit after first iteration of loop
        break

def trade(
    market_data,
    trading_dates,
    book,
    entry_rel_vol
):
    for day, trading_date in enumerate(trading_dates):
        print('Trading, day %s...' % trading_date)
        
        candidate_stocks = {}
        
        if day <= 4:
            continue
        
        for stock in stocks_to_trade:
            stock_data = market_data[stock]
            
            book.increment_days_held(stock)
            
            # skip if stock wasn't traded on this date
            if trading_date not in stock_data['DATE'].values:
                continue
            else:
                if stock in book.positions:
                    manage_position(
                        stock=stock,
                        stock_data=stock_data,
                        trading_date=trading_date,
                        book=book
                    )
                else:
                    check_stock_for_entry(
                        stock=stock,
                        stock_data=stock_data,
                        trading_date=trading_date,
                        entry_rel_vol=entry_rel_vol,
                        candidate_stocks=candidate_stocks
                    )
        
        open_new_positions(
            market_data=market_data,
            trading_date=trading_date,
            candidate_stocks=candidate_stocks,
            book=book
        )
    
def plot_relative_volume(
    stock_data
):
    plot_data(
        stock_data['REL_VOL'].index,
        stock_data['REL_VOL'].values
    )

def backtest():
    market_data = simulate_market()
    
    trading_dates = np.loadtxt(
        fname='BATBC.txt',
        skiprows=1,
        usecols=0,
        dtype='str'
    )[::-1]
    
    half_of_trading_dates = int(trading_dates.shape[0] / 2)
    
    book_train = Book(
        name='train',
        starting_capital=10000,
        R_per_position=0.01,
        price_noise_scale_factor=1.0
    )
    
    book_test = Book(
        name='test',
        starting_capital=10000,
        R_per_position=0.01,
        price_noise_scale_factor=1.0
    )
    
    trade(
        market_data=market_data,
        trading_dates=trading_dates[:half_of_trading_dates],
        book=book_train,
        entry_rel_vol=0.5
    )
    
    book_train.write_PnL()
    
    trade(
        market_data=market_data,
        trading_dates=trading_dates[half_of_trading_dates:],
        book=book_test,
        entry_rel_vol=0.5
    )
    
    book_test.write_PnL()
    
def main():
    backtest()
    
if __name__ == '__main__':
    main()