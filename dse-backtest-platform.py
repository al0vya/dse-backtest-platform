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
    
    # flip dataframe horizontally to dates
    return pd.read_csv(
        filepath_or_buffer=(stock + '.txt'),
        delimiter=' ',
        index_col=False
    )[::-1]
    
def read_all_stock_data():
    return {stock : read_stock_data(stock) for stock in stocks}
    
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
    for stock in stocks:
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
    for stock in stocks:
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

'''
class Position:
    def __init__(
        self,
        stock,
        open,
        abs_R,
        entry_commission,
        entry_slippage,
        price_noise
    ):
        self.stock               = stock
        self.buy_price_per_share = open * (1 + entry_slippage)
        self.num_shares          = abs_R / (4 * price_noise)
        self.buy_price           = buy_price_per_share * num_shares
        self.entry_price         = buy_price * (1 + entry_commission)
        self.stop_loss           = buy_price_per_share - (4 * price_noise)
        self.days_held           = 0
        self.traded_days_held    = 0
        
class Book:
    def __init__(
        self,
        starting_capital,
        R_per_position
    ):
        self.starting_capital   = starting_capital
        self.current_capital    = starting_capital
        self.R_per_position     = R_per_position
        self.abs_R_per_position = starting_capital * R_per_position
        
        self.positions = {}
        
    def enter_position(
        self,
        stock,
        open,
        entry_commission,
        entry_slippage,
        price_noise
    ):
        if stock in self.positions:
            sys.exit('Exiting: tried to buy a stock that's already in the book')
        
        position = Position(
            stock=stock,
            open=open,
            abs_R=self.abs_R_per_position,
            entry_commission=entry_commission,
            entry_slippage=entry_slippage,
            price_noise=price_noise
        )
        
        enough_capital = ( (self.current_capital - position.entry_price) > 0 )
        
        if enough_capital:
            self.current_capital -= position.entry_price
            
            self.positions[stock] = position
            
    def exit_position(
        self,
        stock,
        open,
        exit_commission,
        exit_slippage
    ):
        if stock not in self.positions:
            sys.exit('Exiting: tried to sell a stock that's not in the book')
        
        sell_price_per_share = open * (1 - exit_slippage)
        sell_price           = sell_price_per_share * self.positions[stock].num_shares
        exit_price           = sell_price * (1 - exit_commission)
        
        self.current_capital += exit_price
        
        del self.positions[stock]
        
    def hold_position(
        self,
        stock,
        open,
        price_noise
    ):
        if stock not in self.positions:
            sys.exit('Exiting: tried to hold a stock that's not in the book')
        
        new_stop_loss = open - (4 * price_noise)
        
        if new_stop_loss > self.positions[stock].stop_loss:
            self.positions[stock].stop_loss = new_stop_loss
        
'''

def backtest():
    market_data = simulate_market()
    
    dates = np.loadtxt(
        fname='BATBC.txt',
        skiprows=1,
        usecols=0,
        dtype='str'
    )
    
    for day, date in enumerate(dates):
        if day + 1 <= 5:
            continue
        
        for stock in stocks:
            stock_dates = market_data[stock]['DATE']
            
            '''
            # increment real working days held no matter what
            if stock in book.positions:
                book.positions[stock].days_held += 1
            '''
            
            # skip if stock wasn't traded on this date
            if date not in stock_dates:
                continue    
            '''
            else:
                need:
                open
                yday_close
                ATR_yday
                yday_rel_vol
                
                if stock in book.positions:
                    # increment number of traded days held because stock is traded on this date
                    book.positions[stock].traded_days_held += 1
                    
                    should_exit = (
                        open < book.positions[stock].stop_loss
                        and
                        book.positions[stock].days_held > 2
                    )
                    
                    if should_exit:
                        exit_slippage = 0.05 if ( (np.abs(open - yday_close) / yday_close) > 0.1 ) else 0.01
                        
                        book.exit_position(
                            stock=stock,
                            open=open,
                            exit_commission=0.01,
                            exit_slippage=exit_slippage
                        )
                    else:
                        book.hold_position(
                            stock=stock,
                            open=open,
                            price_noise=ATR_yday
                        )
                else: # stock not in book, so check for entry signal
                    if yday_rel_vol > 2.5:
                        stocks_to_buy.append(stock)
            '''
            
        '''
        for stock in stocks_to_buy:
            book.enter_position(
                stock=stock,
                open=open,
                entry_commission=0.01,
                entry_slippage=0.01,
                price_noise=ATR_yday
            )
        '''
            
def main():
    backtest()
    
if __name__ == '__main__':
    main()