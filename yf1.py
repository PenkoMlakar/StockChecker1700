# Script extracting data from yahoo finances

# Requirements:
# - pip3 install yfinance
# - pip3 install yahoo_fin
# - pip3 install requests_html
# - pip3 install django


def ExtractStocksData():

    import yfinance as yf1
    from multiprocessing import Process, Manager
    # import yahoo_fin.stock_info as yf2

    # stockSymbols = yf2.tickers_nasdaq()  # Get all stocks (over 3000!)
    # print(f"Number of stocks: {len(stockSymbols)}")
    # print(f"Stocks: {stockSymbols}")
    # Etoro stocks (https://etoro-cdn.etorostatic.com/e-marketing/AUM/FulllistofavailableStocksoneToro.pdf)
    # stockSymbols = ['AAPL', 'GOOG', 'FB', 'MSFT', 'AMZN', 'AABA', 'ZNGA', 'AA',
    #                 'AXP', 'BA', 'BAC', 'CAT', 'CSCO', 'CVX', 'DD', 'DIS', 'GE',
    #                 'HD', 'HPQ', 'IBM', 'INTC', 'JNJ', 'JPM', 'KO', 'MCD', 'MMM',
    #                 'MRK', 'PFE', 'PG', 'T', 'TRV', 'UNH', 'UTX', 'VZ', 'WMT',
    #                 'XOM', 'C', 'HMC', 'HBC', 'MANU', 'MA', 'NKE', 'PEP', 'SNE',
    #                  'TM', 'V', 'VOD', 'TWX', 'DB', 'CL', 'EBAY', 'SI', 'YNDX',
    #                  'QIWI', 'CHL', 'RENN', 'TEO', 'TX', 'PBR', 'VALE', 'SAN',
    #                  'TEF', 'AMX', 'CX', 'DTV', 'TV', 'SNDK', 'TSLA', 'F',
    #                  'LVS', 'LNKD', 'NOK', 'POT', 'FSLR', 'BRK.B', 'WU', 'GPS',
    #                  'RL', 'HOG', 'TRIP', 'EA', 'URBN', 'ADBE', 'NFLX', 'MSI',
    #                  'WDC', 'MU', 'ANF', 'DEM', 'AGNC', 'ADSK', 'ORCL', 'LMT',
    #                  'NVDA', 'FDX', 'NBL', 'CAR', 'BIDU', 'SBUX', 'AMGN',
    #                  'ATVI', 'CHKP', 'MOS', 'PETM', 'KDP', 'STZ', 'TWTR',
    #                  'KING', 'BABA', 'SPOT', 'DBX', 'TCEHY', 'ETSY', 'WIX',
    #                  'RYAAY', 'DLPH', 'PCRFY', 'ACB', 'SMG', 'CARA', 'INSY',
    #                  'WP', 'ZYNE', 'CRBP', 'CRON', 'PEGI', 'CVA', 'EVA', 'NEP',
    #                  'ALB', 'ENS', 'APHA', 'XI', 'OSTK', 'TLRY', 'LYFT', 'PINS',
    #                  'LEVI', 'UBER', 'BYND', 'SIE', 'BAS', 'SAP', 'BAYN', 'ALV',
    #                  'EOAN', 'DAI', 'DTE', 'LNA', 'VOW3', 'BMW', 'MUV2', 'RWE',
    #                  'FME', 'ADS', 'DPW', 'FRE', 'HEN3', 'DB1', 'TKA', 'IFX',
    #                  'SDF', 'CBK', 'MRK', 'BEI', 'HEI', 'LHA', 'CON', 'LXSd',
    #                  'BOSSd', 'AC', 'ACA', 'AI', 'AIR', 'ALO', 'ALU', 'BN',
    #                  'BNP', 'CA', 'CAP', 'CS', 'DG', 'EDF', 'EL', 'EN', 'FP',
    #                  'FR', 'GLE', 'ENGI', 'KER', 'LG', 'LR', 'MC', 'ML', 'MTS',
    #                  'OR', 'ORA', 'PUB', 'RI', 'RNO', 'SAF', 'SAN', 'SGO',
    #                  'SOLB', 'SU', 'TEC', 'UG', 'UL', 'VIE', 'VIV', 'A2A',
    #                  'AGL', 'ATL', 'AZM', 'BMPS', 'BP', 'BPE', 'BZU', 'CNHI',
    #                  'CPR', 'EGPW', 'ENEL', 'ENI', 'EXO', 'FCA', 'LDO', 'GASI',
    #                  'ISP', 'LUX', 'MDBI', 'MED', 'MONC', 'MS', 'PC', 'PMI',
    #                  'PRY', 'SFER', 'SPM', 'SRG', 'STM', 'STS', 'TEN', 'TLIT',
    #                  'TOD', 'TRN', 'UBI', 'UCG', 'US', 'WDF', 'YNAP', 'ABE',
    #                  'ABG-P', 'ACS', 'AMS', 'ANA', 'BBVA', 'BKIA', 'BKT', 'BME',
    #                  'CABK', 'DIAm', 'ELE', 'ENG', 'FCC', 'FER', 'SGRE', 'NTGY',
    #                  'GRF', 'IBE', 'IDR', 'ITX', 'JAZ', 'MAP', 'OHL', 'POP',
    #                  'REE', 'REP', 'SAB', 'SCYR', 'TL5', 'TRE', 'OGZDL', 'KMGL',
    #                  'KCELL', 'LKODL', 'MGNTL', 'MFONL', 'MNODL', 'NVTKL',
    #                  'PHORL', 'ROSNL', 'SBERL', 'SVSTL', 'SGGDL', 'ATADL',
    #                  'URKAL', 'QIHU', 'JMEI', 'CYOU', 'QUNR', 'NTES', 'JD',
    #                  'CTRP', 'ATHM', 'JOBS', 'GSOL', 'MOMO', 'TTWO', 'NESN',
    #                  'NOVN', 'ROG', 'CSGN', 'ABB', 'ADEN', 'ATLN', 'BAER',
    #                  'CFR', 'GEBN', 'GIVN', 'LHN', 'SCMN', 'SGSN', 'SLHN',
    #                  'SREN', 'SYNN', 'UBSG', 'UHR', 'ZURN', 'ACN', 'AAL',
    #                  'ABBV', 'BIIB', 'CBS', 'CELG', 'CMCSA', 'COF', 'COST',
    #                  'CVS', 'EMC', 'FOX', 'GILD', 'GPRO', 'GS', 'HON', 'K',
    #                  'CPRI', 'LOW', 'M', 'MCK', 'MDT', 'MET', 'BKNG', 'PM',
    #                  'PSX', 'PYPL', 'QCOM', 'RDS.B', 'S', 'SHAK', 'TGT', 'TTM',
    #                  'UNP', 'UPS', 'WBA', 'WFC', 'WMB', 'VLO', 'ABC', 'FNMA',
    #                  'KR', 'GM', 'ESRX', 'MPC', 'CAH', 'ANTM', 'FMC', 'AIG',
    #                  'DOW', 'AET', 'COP', 'ET', 'HUM', 'EPD', 'SYY', 'IM',
    #                  'JCI', 'PAGP', 'INT', 'BBY', 'DAL', 'HCA', 'ANDV', 'UAL',
    #                  'TSN', 'DE', 'ALL', 'CI', 'MDLZ', 'INTL', 'HAL', 'SHLD',
    #                  'GD', 'TJX', 'TECD', 'AVT', 'EXC', 'IP', 'QRTEA', 'DUK',
    #                  'RAD', 'BHI', 'EMR', 'NOC', 'NOV', 'RTN', 'TWC', 'ARW',
    #                  'AFL', 'SPLS', 'ABT', 'CYH', 'FLR', 'FCX', 'USB', 'NUE',
    #                  'KMB', 'HES', 'CHK', 'XRX', 'MAN', 'DHR', 'WHR', 'PBF',
    #                  'HFC', 'LLY', 'DVN', 'PGR', 'CMI', 'IEP', 'KSS', 'PCAR',
    #                  'HIG', 'LUV', 'APC', 'SO', 'SVU', 'GT', 'EOG', 'CTL',
    #                  'MO', 'THC', 'GIS', 'CAG', 'LEA', 'X', 'PAG', 'AES',
    #                  'GLP', 'TMO', 'PCG', 'NEE', 'AEP', 'BAX', 'CNC', 'BK',
    #                  'JBL', 'PNC', 'KMI', 'ODP', 'BMY', 'NRG', 'MON', 'PPG',
    #                  'GPC', 'OMC', 'ITW', 'MUSA', 'WNR', 'FE', 'ARMK', 'DISH',
    #                  'L', 'ECL', 'WFM', 'CB', 'HNT', 'WM', 'APA', 'TXT', 'SNX',
    #                  'VIAB', 'LNC', 'JWN', 'CHRW', 'EIX', 'YUM', 'PH', 'DVA',
    #                  'KMX', 'TXN', 'WCG', 'MMC', 'ED', 'OKE', 'JEC', 'CSX',
    #                  'ETR', 'D', 'JEF', 'AMP', 'VFC', 'PX', 'JCP', 'ADP', 'LLL',
    #                  'CDW', 'XEL', 'NSC', 'PPL', 'RRD', 'HUN', 'BBBY', 'SWK',
    #                  'LB', 'SHW', 'BLK', 'VOYA', 'ROST', 'SRE', 'EL', 'RGA',
    #                  'PEG', 'CAM', 'NAV', 'CST', 'STT', 'UNM', 'HLT', 'PFG',
    #                  'RS', 'APD', 'AIZ', 'HSIC', 'CTSH', 'MGM', 'GWW', 'GPI',
    #                  'BBT', 'AAP', 'ALLY', 'AGCO', 'GLW', 'NGL', 'SYK', 'MOH',
    #                  'PCP', 'DFS', 'GNW', 'EMN', 'DF', 'AZO', 'OMI', 'HRL',
    #                  'GME', 'CNP', 'FNF', 'SAH', 'HDS', 'CHTR', 'CCK', 'AMAT',
    #                  'CBRE', 'AVP', 'RSG', 'UHS', 'DRI', 'STLD', 'STI', 'CZR',
    #                  'TRGP', 'DLTR', 'NWSA', 'BLL', 'MAS', 'BEN', 'RAI', 'BDX',
    #                  'BRCM', 'CPB', 'ACM', 'VC', 'DK', 'DOV', 'BWA', 'JAH',
    #                  'UGI', 'MUR', 'PVH', 'CORE', 'CPN', 'DHI', 'WY', 'KKR',
    #                  'FTI', 'SPTN', 'WCC', 'PWR', 'MHK', 'LEN', 'TA', 'SEE',
    #                  'ES', 'CCE', 'ASH', 'IPG', 'BX', 'DGX', 'NEM', 'ORLY',
    #                  'CASY', 'CMS', 'FL', 'WRB', 'CMC', 'A', 'HII', 'LYV',
    #                  'DKS', 'OSK', 'CE', 'SPR', 'UNFI', 'BTU', 'OI', 'DDS',
    #                  'LVLT', 'LKQ', 'SYMC', 'BPL', 'R', 'ROK', 'DAN', 'NCR',
    #                  'EXPD', 'AKS', 'FITB', 'SEB', 'NI', 'CVC', 'AXE', 'EME',
    #                  'FIS', 'BKS', 'KBR', 'AVY', 'NTAP', 'DISCA', 'SANM',
    #                  'JBHT', 'SCHW', 'AEE', 'MAT', 'LH', 'HOT', 'BGC', 'AMRI',
    #                  'SPB', 'MRC', 'SE', 'ABG', 'PKG', 'WIN', 'PHM', 'JBLU',
    #                  'NWL', 'CLMT', 'EXPE', 'AFG', 'URI', 'INGR', 'NAVI', 'STJ',
    #                  'SJM', 'CLX', 'UFS', 'KELYA', 'ORI', 'AMD', 'BAH', 'IQV',
    #                  'WYNN', 'JLL', 'RF', 'LAD', 'CRM', 'ALK', 'HST', 'HAR',
    #                  'APH', 'RLGY', 'ESND', 'HBI', 'KND', 'ARRS', 'NSIT',
    #                  'LPNT', 'PXD', 'WYND', 'OC', 'Y', 'SPGI', 'BIG', 'NTI',
    #                  'MKL', 'LDOS', 'COL', 'SRLP', 'YRCW', 'THG', 'FISV',
    #                  'ABM', 'SON', 'HRS', 'TDS', 'WEC', 'LINE', 'RJF', 'BERY',
    #                  'SCG', 'CINF', 'ATO', 'POM', 'FLS', 'SPG', 'QUAD', 'BURL',
    #                  'BMS', 'TPR', 'CLR', 'ASNA', 'Z', 'OA', 'FTR', 'SPW',
    #                  'CF', 'MIK', 'MTB', 'RUSHB', 'GMCR', 'SPN', 'WSM', 'RHI',
    #                  'FAF', 'MDU', 'JNPR', 'AJG', 'CFX', 'CLF', 'MTZ', 'LRCX',
    #                  'AXLL', 'ICE', 'CTAS', 'COTY', 'ANDE', 'VAL', 'NTRS',
    #                  'INTU', 'TPC', 'PII', 'RACE', 'NVR', 'FWONA', 'ENR',
    #                  'BLMN', 'WLK', 'H', 'MJN', 'EVHC', 'FBHS', 'RPM', 'VWR',
    #                  'LPLA', 'KEY', 'KNX', 'AGN', 'HAS', 'RFP', 'TIF', 'MKC',
    #                  'GPK', 'GEF', 'ATI', 'BEAV', 'TAP', 'CNO', 'AE', 'CMG',
    #                  'AMT', 'AFSI', 'BC', 'PDCO', 'SWN', 'AME', 'TROW', 'TMK',
    #                  'DAR', 'LEG', 'WSO', 'CEQP', 'XYL', 'SLGN', 'TOL', 'MTW',
    #                  'ARGO', 'ARG', 'GNC', 'MAR', 'SQ', 'MTCH', 'SEDG', 'FIT',
    #                  'NTDOY', 'REGN', 'SGMO', 'NTLA', 'EDIT', 'MS', 'CLLS',
    #                  'HRMS', 'SNAP', 'AAL', 'ABF', 'ADM', 'ADN', 'AGK', 'AHT',
    #                  'AMFW', 'ANTO', 'ARM', 'AV', 'AZN', 'BAl', 'BAB', 'BARC',
    #                  'BATS', 'BG', 'BLND', 'BHP', 'BNZL', 'BP', 'BRBY', 'SKY',
    #                  'BT', 'CCH', 'CCL', 'CNA', 'CPG', 'CPI', 'CRH', 'DGE',
    #                  'EXPN', 'EZJ', 'FRES', 'GFS', 'GKN', 'GLEN', 'GSK', 'HL',
    #                  'HMSO', 'HSBA', 'IAG', 'IHG', 'IMI', 'IMB', 'ITRK', 'ITV',
    #                  'JMAT', 'KGF', 'LAND', 'LGEN', 'LLOY', 'LSE', 'MGGT',
    #                  'MKS', 'MNDI', 'MRO', 'MRW', 'NG', 'NXT', 'OML', 'PFC',
    #                  'PRU', 'PSN', 'PSON', 'RB', 'RBS', 'RDSA', 'REL', 'REX',
    #                  'RIO', 'RMG', 'RR', 'RRS', 'RSA', 'RSL', 'SAB', 'SBRY',
    #                  'SDR', 'SGE', 'SHP', 'SLA', 'SMIN', 'SN', 'SPD', 'SSE',
    #                  'STAN', 'SVT', 'TATE', 'TLW', 'TPK', 'TSCO', 'TT', 'ULVR',
    #                  'UU', 'VOD', 'WEIR', 'WMH', 'FERG', 'WPP', 'WTB', 'DMGT',
    #                  'III', 'BPM', 'HZD', 'BDEV.L', 'CRDA.L', 'DCC.L', 'DLG.L',
    #                  'INF.L', 'MCRO.L', 'PPB.L', 'RTO.L', 'SGRO.L', 'SKG.L',
    #                  'SMT.L', 'TUI.L', 'TW.L', 'QLT.L', 'MDC.L', 'AML.L',
    #                  'FEVR.L', 'ASC.L', 'RDSB.L', 'RYA.L', 'AVST.L', 'VVO.L',
    #                  'SMSN.L', 'TLN.L', 'AKA', 'AKSO', 'BWLPG', 'DNB', 'DNO',
    #                  'FOE', 'GJF', 'GOGL', 'MHG', 'NHY', 'NAS', 'OTELLO', 'ORK',
    #                  'PGS', 'PRS', 'STB', 'SUBC', 'TEL', 'TGS', 'YAR', 'ERIC-A',
    #                  'TELIA', 'NDA_SE', 'VOLV-A', 'SEB-A', 'SAND', 'HM-B',
    #                  'SHB-A', 'SKF-A', 'SWED-A', 'ASSA-B', 'ATCO-A', 'BOL',
    #                  'SCA-B', 'ALFA', 'ELUX-B', 'SECU-B', 'SKA-B', 'INVE-A',
    #                  'LUPE', 'TREL-B', 'SWMA', 'HEXA-B', 'KINV-A', 'ICA',
    #                  'INDU-A', 'LUND-B', 'NOVO-B', 'DANSKE', 'ORSTED', 'VWS',
    #                  'NZYM-B', 'PNDORA', 'TRYG', 'DSV', 'WDH', 'ISS', 'LUN',
    #                  'GEN', 'COLO-B', 'CARL-B', 'CHR', 'OSSR', 'NDA1V',
    #                  'SSABAH', 'STEAV', 'FORTUM', 'UPM', 'NESTE', 'KNEBV',
    #                  'SAMPO', 'ELISA', 'NRE1V', 'WRT1V', 'ORNAV', '0939.HK']

    stockSymbols = [# Technology
                    "ATVI", "ADBE", "ADSK", "AMAT", "AMD", "ANSS", "CDNS",
                    "CSCO", "DBX", "DELL", "DLG.DE", "EA", "GOOG", "IBM",
                    "INTC", "LOGI", "MSFT", "NOK", "NVDA", "NXPI", "SNAP",
                    "PINS", "PYPL", "QCOM", "SOXX", "SPOT", "TWTR", "TXN",
                    "WDC", "ZM", "DOCU", "KPN.AS", "VPK.AS", "SYNA", "NET",
                    "CRM", "FSLR", "SHOP", "HPE", "HPQ", "ASML", "AVGO", "INTU",
                    # Entertainment
                    "DIS", "NFLX", "UBI.PA",
                    # Services
                    "0700.HK", "AAL", "AIR.PA", "AMZN", "BABA", "DAL",
                    "DISH", "EBAY", "ETSY", "FB", "FSLY", "FVRR", "JMIA",
                    "LYFT", "MELI", "PTON", "ROKU", "SQ", "TTD", "UAL", "UBER",
                    "WORK", "AMWL", "BYND", "RYA.L", "MCD", "SBUX", "CHTR",
                    "OKTA", "LYV", "MAR", "MNST", "OSTK", "SAVE", "SIX", "URBN",
                    "W",
                    # Consumer Goods
                    "AAPL", "ADS.DE", "ALXN", "AML.L", "APRN", "COST",
                    "NESN.SW", "NIO", "NIU", "NKE", "PAH3.DE", "PEP", "PG",
                    "PM", "SHAK", "SNE", "TPR", "TSLA", "1810.HK", # XI
                    "TDOC", "GFRD.L", "PDD", "U", "MRNA", "CHWY", "WBA", "RACE",
                    "CL", "RDSB.L", "AEO", "BILI", "BOSS.DE", "CDI.PA", "CHGG",
                    "IRBT", "RCL", "UA",
                    # Financial
                    "BAC", "BBD", "CIT", "ITUB", "JPM", "O", "SLV", "V",
                    "BRK.B", "MA", "BLK", "VTI", "AGNC", "BPY", "DB", "HSBA.L",
                    "MAIN", "OHI", "SPG", "STOR"
                    # Basic Materials
                    "GOLD", "NEM", "SLB", "XOM", "ENC.MC", "APD", "RDS.B",
                    "RIO", "SAOC", "VOLV-A.ST",
                    # Industrial Goods
                    "BA", "LMT", "NTDOY", "RTX", "SIE.DE", "UPS", "NTLA",
                    "ENPH", "DHI", "ROK", "CAT", "UNP",
                    # Healthcare
                    "GILD", "PFE", "SAN.PA", "MDT", "ILMN",
                    # Utilities
                    "NEE", "ATADL.L",
                    # Coglomerates
                    "MMM"
                    ]

    # stockSymbols = ["NFLX"]  # for testing

    def downloadData(data_3d, stockSymbols, current, i):
        # Get history data
        data_3d[i] = yf1.download(stockSymbols[i], period="3d")

        # Get current price
        ticker_yahoo = yf1.Ticker(stockSymbols[i])
        data = ticker_yahoo.history()
        current_ = (data.tail(1)['Close'].iloc[0])
        # print(f"Stock {stockSymbols[i]}: current {current_}")

        current[i] = current_

    # dummies
    data_3d = []
    current = []

    with Manager() as manager:
        # stockSymbols = [# Technology
        #                 "ATVI", "ADBE", "ADSK", "ANSS", "AMD", "CDNS", "CSCO"]
        a = manager.list(range(len(stockSymbols)))  # <-- can be shared between processes.
        b = manager.list(range(len(stockSymbols)))
        processes = [None] * len(stockSymbols)
        for i in range(len(stockSymbols)):
            p = Process(target=downloadData, args=(a, stockSymbols,
                                                   b, i))  # Passing the lists
            p.start()

            # Join processes at certain point, otherwise the RAM gets eaten
            # for huge lists
            step = 100
            if i % step == 0 and i != 0:
                p.join()
            elif i >= len(stockSymbols) - (step % len(stockSymbols)):
                print(len(stockSymbols))
                print(i)
                p.join()

        # print(a[0]["Open"][-1])
        p.close()
        data_3d = list(a)
        current = list(b)

    return stockSymbols, current, data_3d


def filterStocks():

    import numpy as np
    import yfinance as yf1
    from multiprocessing import Process, Manager

    # Filter stocks
    stockSymbols, current, data_3d = ExtractStocksData()

    def filterData(stockSymbols, current, data_3d, filteredSymbols,
                   filteredPrevCloses, filteredOpens, filteredCurrents,
                   filteredOpenVsPrevClose, filteredOpenVsCurrent, i):

        print("Stock: ", stockSymbols[i])
        # print("Open: ", data_3d[i]["Open"][-1])
        # print("Close: ", data_3d[i]["Close"][-2])

        # Check if the data is available
        if len(data_3d[i]["Close"]) > 2:
            premarket_up_percent = \
                (data_3d[i]["Open"][-1] / data_3d[i]["Close"][-2] - 1) * 100
            current_percent = (current[i] / data_3d[i]["Close"][-2] - 1) * 100
        else:
            premarket_up_percent = 0.0  # Dummy
            current_percent = 0.0  # Dummy

        # print("premarket_up_percent: ", premarket_up_percent)
        # print("current_percent: ", current_percent)

        # SMA - SIMPLE MOVING AVERAGE
        pandas_table = yf1.download(stockSymbols[i], period="180m", interval="1m")
        # Calculating the n-window simple moving average
        sma = pandas_table.rolling(window=50).mean()
        # print(f"Current: {current[i]}; SMA: {sma['Open'][-1]}")

        if (current_percent > premarket_up_percent) and \
           ((current_percent - premarket_up_percent) > 1.5) and \
           (sma["Open"][-1] < current[i]):
            filteredSymbols.append(stockSymbols[i])
            filteredPrevCloses.append(np.round(data_3d[i]["Close"][-2], 2))
            filteredOpens.append(np.round(data_3d[i]["Open"][-1], 2))
            filteredCurrents.append(np.round(current[i], 2))
            filteredOpenVsPrevClose.append(
                np.round((filteredOpens[-1] / filteredPrevCloses[-1] - 1) * 100, 2))
            filteredOpenVsCurrent.append(
                np.round((filteredCurrents[-1] / filteredPrevCloses[-1] - 1) * 100, 2))

    # Dummies
    filteredSymbols = []
    filteredPrevCloses = []
    filteredOpens = []
    filteredCurrents = []
    filteredOpenVsPrevClose = []
    filteredOpenVsCurrent = []

    with Manager() as manager:
        a = manager.list(range(len(stockSymbols)))  # <-- can be shared between processes.
        b = manager.list(range(len(stockSymbols)))
        c = manager.list(range(len(stockSymbols)))
        d = manager.list(range(len(stockSymbols)))
        e = manager.list(range(len(stockSymbols)))
        f = manager.list(range(len(stockSymbols)))
        processes = []
        for i in range(len(stockSymbols)):
            p = Process(target=filterData, args=(stockSymbols, current,
                                                 data_3d, a, b, c, d, e, f, i))  # Passing the lists
            p.start()

            # Join processes at certain point, otherwise the RAM gets eaten
            # for huge lists
            step = 100
            if i % step == 0 and i != 0:
                p.join()
            elif i >= len(stockSymbols) - (step % len(stockSymbols)):
                print(len(stockSymbols))
                print(i)
                p.join()

        # print(a[0]["Open"][-1])
        p.close()
        filteredSymbols = list(a)
        filteredPrevCloses = list(b)
        filteredOpens = list(c)
        filteredCurrents = list(d)
        filteredOpenVsPrevClose = list(e)
        filteredOpenVsCurrent = list(f)

    # Remove obsolete integers from list
    filteredSymbols = [x for x in filteredSymbols if not isinstance(x, int)]
    filteredPrevCloses = [x for x in filteredPrevCloses if not isinstance(x, int)]
    filteredOpens = [x for x in filteredOpens if not isinstance(x, int)]
    filteredCurrents = [x for x in filteredCurrents if not isinstance(x, int)]
    filteredOpenVsPrevClose = [x for x in filteredOpenVsPrevClose if not isinstance(x, int)]
    filteredOpenVsCurrent = [x for x in filteredOpenVsCurrent if not isinstance(x, int)]

    zipped = zip(filteredSymbols, filteredPrevCloses, filteredOpens,
                 filteredCurrents, filteredOpenVsPrevClose,
                 filteredOpenVsCurrent)

    return zipped


if __name__ == "__main__":
    # test
    # stockSymbols, current, data_3d = ExtractStocksData()
    # print(stockSymbols)
    zipped = filterStocks()
    # print(zipped)
