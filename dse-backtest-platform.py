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
    'KAY&QUE',
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
            fp.write('# DATE TRADECODE LAST_TRADE_PRICE HIGH LOW OPEN CLOSE YDAY_CLOSE NUM_TRADES VALUE_IN_MN NUM_SHARES\n')
            
            for row in rows:
                cols = row.find_all('td')
                cols = [col.text.strip() for col in cols][1:]
                [fp.write(col + " ") for col in cols]
                fp.write('\n')

def start_driver():
    options = Options()
    options.add_argument('start-maximized')
    
    driver = webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()), options=options)
    
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
        except:
            print('Failed to scrape data of stock %s' % stock)
            continue

def plot_stock_close_prices(
    stock
):
    stock_data = pd.read_csv(filepath_or_buffer=(stock + '.txt'), delimiter=' ')
    
    # flip dataframe horizontally to fix dates
    stock_data = stock_data[::-1]  
    
    print(stock_data)   
    
    fig, ax = plt.subplots()
    
    ax.plot(
        stock_data['#'],
        stock_data['CLOSE']
    )
    
    ax.set_ylabel('BDT')
    ax.set_xlabel('Days')
    
    plt.show()

def main():
    #test_list_of_stocks( start_driver() )
    scrape_all_stock_data( start_driver() )
    
    #plot_stock_close_prices('LHBL')
    
if __name__ == '__main__':
    main()