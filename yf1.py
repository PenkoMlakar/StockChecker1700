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
    # # All stocks obtianed by yahoo_fin (removed some of delisted ones)
    # stockSymbols = ['AACG', 'AACQ', 'AACQU', 'AACQW', 'AAL', 'AAME', 'AAOI',
    #                 'AAON', 'AAPL', 'AAWW', 'AAXJ', 'AAXN', 'ABCB', 'ABCM',
    #                 'ABEO', 'ABIO', 'ABMD', 'ABST', 'ABTX', 'ABUS', 'ACACU',
    #                 'ACAD', 'ACAM', 'ACAMU', 'ACAMW', 'ACBI', 'ACCD', 'ACER',
    #                 'ACET', 'ACEVU', 'ACEVW', 'ACGL', 'ACGLO', 'ACGLP', 'ACHC',
    #                 'ACHV', 'ACIA', 'ACIU', 'ACIW', 'ACLS', 'ACMR', 'ACNB',
    #                 'ACOR', 'ACRS', 'ACRX', 'ACST', 'ACTCU', 'ACTG', 'ACWI',
    #                 'ACWX', 'ADAP', 'ADBE', 'ADES', 'ADI', 'ADIL', 'ADMA',
    #                 'ADMP', 'ADMS', 'ADOCU', 'ADP', 'ADPT', 'ADRE',
    #                 'ADSK', 'ADTN', 'ADTX', 'ADUS', 'ADV', 'ADVM', 'ADVWW',
    #                 'ADXS', 'AEGN', 'AEHL', 'AEHR', 'AEIS', 'AEMD', 'AEP',
    #                 'AEPPL', 'AEPPZ', 'AERI', 'AESE', 'AEY', 'AEYE', 'AEZS',
    #                 'AFIB', 'AFIN', 'AFINP', 'AFMD', 'AFYA', 'AGBAR', 'AGBAW',
    #                 'AGCUU', 'AGEN', 'AGFS', 'AGIO', 'AGLE', 'AGMH', 'AGNC',
    #                 'AGNCM', 'AGNCN', 'AGNCO', 'AGNCP', 'AGRX', 'AGTC',
    #                 'AGYS', 'AGZD', 'AHACU', 'AHCO', 'AHPI', 'AIA', 'AIH',
    #                 'AIHS', 'AIKI', 'AIMC', 'AINV', 'AIQ', 'AIRG', 'AIRR',
    #                 'AIRT', 'AIRTP', 'AIRTW', 'AKAM', 'AKBA', 'AKER', 'AKRO',
    #                 'AKTS', 'AKTX', 'AKU', 'AKUS', 'ALAC', 'ALACR', 'ALACU',
    #                 'ALACW', 'ALBO', 'ALCO', 'ALDX', 'ALEC', 'ALGM', 'ALGN',
    #                 'ALGS', 'ALGT', 'ALIM', 'ALJJ', 'ALKS', 'ALLK', 'ALLO',
    #                 'ALLT', 'ALNA', 'ALNY', 'ALOT', 'ALPN', 'ALRM', 'ALRN',
    #                 'ALRS', 'ALSK', 'ALT', 'ALTA', 'ALTM', 'ALTR', 'ALTY',
    #                 'ALVR', 'ALXN', 'ALXO', 'ALYA', 'AMAG', 'AMAL', 'AMAT',
    #                 'AMBA', 'AMCA', 'AMCI', 'AMCIU', 'AMCIW', 'AMCX', 'AMD',
    #                 'AMED', 'AMEH', 'AMGN', 'AMHC', 'AMHCU', 'AMHCW', 'AMKR',
    #                 'AMNB', 'AMOT', 'AMPH', 'AMRB', 'AMRH', 'AMRHW', 'AMRK',
    #                 'AMRN', 'AMRS', 'AMSC', 'AMSF', 'AMST', 'AMSWA', 'AMTB',
    #                 'AMTBB', 'AMTI', 'AMTX', 'AMWD', 'AMYT', 'AMZN', 'ANAB',
    #                 'ANAT', 'ANCN', 'ANDA', 'ANDAR', 'ANDAU', 'ANDAW', 'ANDE',
    #                 'ANGI', 'ANGL', 'ANGO', 'ANIK', 'ANIP', 'ANIX', 'ANNX',
    #                 'ANPC', 'ANSS', 'ANTE', 'ANY', 'AOSL', 'AOUT', 'APA',
    #                 'APDN', 'APEI', 'APEN', 'APHA', 'API', 'APLS', 'APLT',
    #                 'APM', 'APOG', 'APOP', 'APOPW', 'APPF', 'APPN', 'APPS',
    #                 'APRE', 'APTO', 'APTX', 'APVO', 'APWC', 'APXT', 'APXTU',
    #                 'APXTW', 'APYX', 'AQB', 'AQMS', 'AQST', 'ARAV', 'ARAY',
    #                 'ARCB', 'ARCC', 'ARCE', 'ARCT', 'ARDS', 'ARDX', 'AREC',
    #                 'ARGX', 'ARKR', 'ARLP', 'ARNA', 'AROW', 'ARPO', 'ARQT',
    #                 'ARRY', 'ARTL', 'ARTLW', 'ARTNA', 'ARTW', 'ARVN', 'ARWR',
    #                 'ARYA', 'ASET', 'ASLN', 'ASMB', 'ASML', 'ASND', 'ASO',
    #                 'ASPS', 'ASPU', 'ASRT', 'ASRV', 'ASRVP', 'ASTC', 'ASTE',
    #                 'ASUR', 'ASYS', 'ATAX', 'ATCX', 'ATCXW', 'ATEC', 'ATEX',
    #                 'ATHA', 'ATHE', 'ATHX', 'ATIF', 'ATLC', 'ATLO', 'ATNF',
    #                 'ATNFW', 'ATNI', 'ATNX', 'ATOM', 'ATOS', 'ATRA', 'ATRC',
    #                 'ATRI', 'ATRO', 'ATRS', 'ATSG', 'ATVI', 'ATXI', 'AUB',
    #                 'AUBAP', 'AUBN', 'AUDC', 'AUPH', 'AUTL', 'AUTO', 'AUVI',
    #                 'AVAV', 'AVCO', 'AVCT', 'AVCTW', 'AVDL', 'AVEO', 'AVGO',
    #                 'AVGOP', 'AVGR', 'AVID', 'AVIR', 'AVNW', 'AVO', 'AVRO',
    #                 'AVT', 'AVXL', 'AWH', 'AWRE', 'AXAS', 'AXDX', 'AXGN',
    #                 'AXLA', 'AXNX', 'AXSM', 'AXTI', 'AY', 'AYLA', 'AYRO',
    #                 'AYTU', 'AZN', 'AZPN', 'AZRX', 'AZYO', 'BAND', 'BANF',
    #                 'BANFP', 'BANR', 'BANX', 'BASI', 'BATRA', 'BATRK', 'BBBY',
    #                 'BBCP', 'BBGI', 'BBH', 'BBI', 'BBIG', 'BBIO', 'BBQ',
    #                 'BBSI', 'BCBP', 'BCDA', 'BCEL', 'BCLI', 'BCML',
    #                 'BCOR', 'BCOV', 'BCOW', 'BCPC', 'BCRX', 'BCTG', 'BCYC',
    #                 'BDGE', 'BDSI', 'BDSX', 'BDTX', 'BEAM', 'BEAT', 'BECN',
    #                 'BEEM', 'BEEMW', 'BELFA', 'BELFB', 'BFC', 'BFIN', 'BFIT',
    #                 'BFRA', 'BFST', 'BGCP', 'BGFV', 'BGNE', 'BGRN', 'BHAT',
    #                 'BHF', 'BHFAL', 'BHFAO', 'BHFAP', 'BHSEU', 'BHTG', 'BIB',
    #                 'BICK', 'BIDU', 'BIGC', 'BIIB', 'BILI', 'BIMI', 'BIOC',
    #                 'BIOL', 'BIS', 'BIVI', 'BJK', 'BJRI', 'BKCC', 'BKEP',
    #                 'BKEPP', 'BKNG', 'BKSC', 'BKYI', 'BL', 'BLBD', 'BLCM',
    #                 'BLCN', 'BLCT', 'BLDP', 'BLDR', 'BLFS', 'BLI', 'BLIN',
    #                 'BLKB', 'BLMN', 'BLNK', 'BLNKW', 'BLPH', 'BLRX', 'BLSA',
    #                 'BLU', 'BLUE', 'BMCH', 'BMLP', 'BMRA', 'BMRC', 'BMRN',
    #                 'BMTC', 'BND', 'BNDW', 'BNDX', 'BNFT', 'BNGO', 'BNGOW',
    #                 'BNR', 'BNSO', 'BNTC', 'BNTX', 'BOCH', 'BOKF', 'BOKFL',
    #                 'BOMN', 'BOOM', 'BOSC', 'BOTJ', 'BOTZ', 'BOWX', 'BOWXU',
    #                 'BOWXW', 'BOXL', 'BPFH', 'BPMC', 'BPOP', 'BPOPM', 'BPOPN',
    #                 'BPRN', 'BPTH', 'BPY', 'BPYPN', 'BPYPO', 'BPYPP', 'BPYU',
    #                 'BPYUP', 'BRID', 'BRKL', 'BRKR', 'BRKS', 'BRLI', 'BRLIR',
    #                 'BRLIU', 'BRLIW', 'BROG', 'BRP', 'BRPA', 'BRPAR',
    #                 'BRPAU', 'BRPAW', 'BRQS', 'BRY', 'BSAE', 'BSBE', 'BSBK',
    #                 'BSCE', 'BSCK', 'BSCL', 'BSCM', 'BSCN', 'BSCO', 'BSCP',
    #                 'BSCQ', 'BSCR', 'BSCS', 'BSCT', 'BSCU', 'BSDE', 'BSET',
    #                 'BSGM', 'BSJK', 'BSJL', 'BSJM', 'BSJN', 'BSJO', 'BSJP',
    #                 'BSJQ', 'BSJR', 'BSJS', 'BSML', 'BSMM', 'BSMN', 'BSMO',
    #                 'BSMP', 'BSMQ', 'BSMR', 'BSMS', 'BSMT', 'BSMU', 'BSQR',
    #                 'BSRR', 'BSTC', 'BSVN', 'BSY', 'BTAI', 'BTAQ', 'BTAQU',
    #                 'BTAQW', 'BTBT', 'BTEC', 'BTWNU', 'BUG', 'BUSE', 'BVXV',
    #                 'BWACU', 'BWAY', 'BWB', 'BWEN', 'BWFG', 'BWMX', 'BXRX',
    #                 'BYFC', 'BYND', 'BYSI', 'BZUN', 'CAAS', 'CABA', 'CAC',
    #                 'CACC', 'CACG', 'CAKE', 'CALA', 'CALB', 'CALM', 'CALT',
    #                 'CAMP', 'CAMT', 'CAN', 'CAPA', 'CAPAU', 'CAPR',
    #                 'CAR', 'CARA', 'CARE', 'CARG', 'CARV', 'CARZ', 'CASA',
    #                 'CASH', 'CASI', 'CASS', 'CASY', 'CATB', 'CATC', 'CATH',
    #                 'CATM', 'CATY', 'CBAN', 'CBAT', 'CBAY', 'CBFV', 'CBIO',
    #                 'CBLI', 'CBMB', 'CBMG', 'CBNK', 'CBPO', 'CBRL', 'CBSH',
    #                 'CBTX', 'CCAP', 'CCB', 'CCBG', 'CCCC']
    # 'CCD', 'CCLP', 'CCMP', 'CCNC', 'CCNE', 'CCNEP', 'CCOI', 'CCRC', 'CCRN', 'CCXI', 'CD', 'CDAK', 'CDC', 'CDEV', 'CDK', 'CDL', 'CDLX', 'CDMO', 'CDMOP', 'CDNA', 'CDNS', 'CDTX', 'CDW', 'CDXC', 'CDXS', 'CDZI', 'CECE', 'CEFA', 'CELC', 'CELH', 'CEMI', 'CENT', 'CENTA', 'CENX', 'CERC', 'CERE', 'CEREW', 'CERN', 'CERS', 'CETX', 'CETXP', 'CETXW', 'CEVA', 'CEY', 'CEZ', 'CFA', 'CFACU', 'CFB', 'CFBI', 'CFBK', 'CFFA', 'CFFAU', 'CFFAW', 'CFFI', 'CFFN', 'CFII', 'CFIIU', 'CFIIW', 'CFMS', 'CFO', 'CFRX', 'CG', 'CGBD', 'CGEN', 'CGIX', 'CGNX', 'CGO', 'CGRO', 'CGROU', 'CGROW', 'CHB', 'CHCI', 'CHCO', 'CHDN', 'CHEF', 'CHEK', 'CHEKZ', 'CHFS', 'CHI', 'CHKP', 'CHMA', 'CHMG', 'CHNA', 'CHNG', 'CHNGU', 'CHNR', 'CHPM', 'CHPMU', 'CHPMW', 'CHRS', 'CHRW', 'CHSCL', 'CHSCM', 'CHSCN', 'CHSCO', 'CHSCP', 'CHTR', 'CHUY', 'CHW', 'CHY', 'CIBR', 'CID', 'CIDM', 'CIGI', 'CIH', 'CIIC', 'CIICU', 'CIICW', 'CIL', 'CINF', 'CIVB', 'CIZ', 'CIZN', 'CJJD', 'CKPT', 'CLAR', 'CLBK', 'CLBS', 'CLCT', 'CLDB', 'CLDX', 'CLEU', 'CLFD', 'CLGN', 'CLIR', 'CLLS', 'CLMT', 'CLNE', 'CLOU', 'CLPS', 'CLPT', 'CLRB', 'CLRBZ', 'CLRG', 'CLRO', 'CLSD', 'CLSK', 'CLSN', 'CLVS', 'CLWT', 'CLXT', 'CMBM', 'CMCO', 'CMCSA', 'CMCT', 'CMCTP', 'CME', 'CMFNL', 'CMLF', 'CMLFU', 'CMLFW', 'CMLS', 'CMPI', 'CMPR', 'CMPS', 'CMRX', 'CMTL', 'CNBKA', 'CNCE', 'CNCR', 'CNDT', 'CNET', 'CNFR', 'CNFRL', 'CNNB', 'CNOB', 'CNSL', 'CNSP', 'CNST', 'CNTG', 'CNTY', 'CNXN', 'COCP', 'CODA', 'CODX', 'COFS', 'COGT', 'COHR', 'COHU', 'COKE', 'COLB', 'COLL', 'COLM', 'COMM', 'COMT', 'CONE', 'CONN', 'CONXU', 'COOP', 'CORE', 'CORT', 'COST', 'COUP', 'COWN', 'COWNL', 'COWNZ', 'CPAH', 'CPHC', 'CPIX', 'CPLP', 'CPRT', 'CPRX', 'CPSH', 'CPSI', 'CPSS', 'CPST', 'CPTA', 'CPTAG', 'CPTAL', 'CPZ', 'CRAI', 'CRBP', 'CRDF', 'CREE', 'CREG', 'CRESY', 'CREX', 'CREXW', 'CRIS', 'CRMT', 'CRNC', 'CRNT', 'CRNX', 'CRON', 'CROX', 'CRSA', 'CRSAU', 'CRSAW', 'CRSP', 'CRSR', 'CRTD', 'CRTDW', 'CRTO', 'CRTX', 'CRUS', 'CRVL', 'CRVS', 'CRWD', 'CRWS', 'CSA', 'CSB', 'CSBR', 'CSCO', 'CSCW', 'CSF', 'CSGP', 'CSGS', 'CSII', 'CSIQ', 'CSML', 'CSOD', 'CSPI', 'CSQ', 'CSSE', 'CSSEN', 'CSSEP', 'CSTE', 'CSTL', 'CSTR', 'CSWC', 'CSWCL', 'CSWI', 'CSX', 'CTAS', 'CTBI', 'CTEC', 'CTG', 'CTHR', 'CTIB', 'CTIC', 'CTMX', 'CTRE', 'CTRM', 'CTRN', 'CTSH', 'CTSO', 'CTXR', 'CTXRW', 'CTXS', 'CUBA', 'CUE', 'CURI', 'CURIW', 'CUTR', 'CVAC', 'CVBF', 'CVCO', 'CVCY', 'CVET', 'CVGI', 'CVGW', 'CVLG', 'CVLT', 'CVLY', 'CVV', 'CWBC', 'CWBR', 'CWCO', 'CWST', 'CXDC', 'CXDO', 'CXSE', 'CYAD', 'CYAN', 'CYBE', 'CYBR', 'CYCC', 'CYCCP', 'CYCN', 'CYRN', 'CYRX', 'CYTK', 'CZNC', 'CZR', 'CZWI', 'DADA', 'DAIO', 'DAKT', 'DALI', 'DARE', 'DAX', 'DBDRU', 'DBVT', 'DBX', 'DCOM', 'DCOMP', 'DCPH', 'DCRBU', 'DCT', 'DCTH', 'DDIV', 'DDOG', 'DEMZ', 'DENN', 'DFFN', 'DFHT', 'DFHTU', 'DFHTW', 'DFNL', 'DFPH', 'DFPHU', 'DFPHW', 'DGICA', 'DGICB', 'DGII', 'DGLY', 'DGRE', 'DGRS', 'DGRW', 'DHC', 'DHCNI', 'DHCNL', 'DHIL', 'DINT', 'DIOD', 'DISCA', 'DISCB', 'DISCK', 'DISH', 'DJCO', 'DKNG', 'DLHC', 'DLPN', 'DLPNW', 'DLTH', 'DLTR', 'DMAC', 'DMLP', 'DMRC', 'DMTK', 'DMXF', 'DNKN', 'DNLI', 'DOCU', 'DOGZ', 'DOMO', 'DOOO', 'DORM', 'DOX', 'DOYU', 'DRAD', 'DRADP', 'DRIO', 'DRIOW', 'DRIV', 'DRNA', 'DRRX', 'DRTT', 'DSACU', 'DSGX', 'DSKE', 'DSKEW', 'DSPG', 'DSWL', 'DTEA', 'DTIL', 'DTSS', 'DUO', 'DUOT', 'DUSA', 'DVAX', 'DVLU', 'DVOL', 'DVY', 'DWAS', 'DWAT', 'DWAW', 'DWCR', 'DWEQ', 'DWFI', 'DWLD', 'DWMC', 'DWPP', 'DWSH', 'DWSN', 'DWUS', 'DXCM', 'DXGE', 'DXJS', 'DXLG', 'DXPE', 'DXYN', 'DYAI', 'DYN', 'DYNT', 'DZSI', 'EA', 'EAR', 'EARS', 'EAST', 'EBAY', 'EBAYL', 'EBC', 'EBIX', 'EBIZ', 'EBMT', 'EBON', 'EBSB', 'EBTC', 'ECHO', 'ECOL', 'ECOLW', 'ECOR', 'ECOW', 'ECPG', 'EDAP', 'EDIT', 'EDOC', 'EDRY', 'EDSA', 'EDTK', 'EDUC', 'EDUT', 'EEFT', 'EEMA', 'EFAS', 'EFOI', 'EFSC', 'EGAN', 'EGBN', 'EGLE', 'EGOV', 'EGRX', 'EH', 'EHTH', 'EIDX', 'EIGI', 'EIGR', 'EKSO', 'ELOX', 'ELSE', 'ELTK', 'ELYS', 'EMB', 'EMCB', 'EMCF', 'EMIF', 'EMKR', 'EML', 'EMXC', 'EMXF', 'ENDP', 'ENG', 'ENLV', 'ENOB', 'ENPH', 'ENSG', 'ENTA', 'ENTG', 'ENTX', 'ENTXW', 'ENZL', 'EOLS', 'EPAY', 'EPIX', 'EPSN', 'EPZM', 'EQ', 'EQBK', 'EQIX', 'EQOS', 'EQOSW', 'EQRR', 'ERES', 'ERESU', 'ERESW', 'ERIC', 'ERIE', 'ERII', 'ERYP', 'ESBK', 'ESCA', 'ESEA', 'ESGD', 'ESGE', 'ESGR', 'ESGRO', 'ESGRP', 'ESGU', 'ESLT', 'ESPO', 'ESPR', 'ESQ', 'ESSA', 'ESSC', 'ESSCR', 'ESSCU', 'ESSCW', 'ESTA', 'ESXB', 'ETAC', 'ETACU', 'ETACW', 'ETNB', 'ETON', 'ETSY', 'ETTX', 'EUCRU', 'EUFN', 'EVBG', 'EVER', 'EVFM', 'EVGBC', 'EVGN', 'EVK', 'EVLMC', 'EVLO', 'EVOK', 'EVOL', 'EVOP', 'EVSTC', 'EWBC', 'EWEB', 'EWJE', 'EWJV', 'EWZS', 'EXAS', 'EXC', 'EXEL', 'EXFO', 'EXLS', 'EXPC', 'EXPCU', 'EXPCW', 'EXPD', 'EXPE', 'EXPI', 'EXPO', 'EXTR', 'EYE', 'EYEG', 'EYEN', 'EYES', 'EYESW', 'EYPT', 'EZPW', 'FAAR', 'FAB', 'FAD', 'FALN', 'FAMI', 'FANG', 'FANH', 'FARM', 'FARO', 'FAST', 'FAT', 'FATBP', 'FATBW', 'FATE', 'FB', 'FBIO', 'FBIOP', 'FBIZ', 'FBMS', 'FBNC', 'FBRX', 'FBSS', 'FBZ', 'FCA', 'FCACU', 'FCAL', 'FCAP', 'FCBC', 'FCBP', 'FCCO', 'FCCY', 'FCEF', 'FCEL', 'FCFS', 'FCNCA', 'FCNCP', 'FCRD', 'FCVT', 'FDBC', 'FDIV', 'FDNI', 'FDT', 'FDTS', 'FDUS', 'FDUSG', 'FDUSL', 'FDUSZ', 'FEIM', 'FELE', 'FEM', 'FEMB', 'FEMS', 'FENC', 'FEP', 'FEUZ', 'FEX', 'FEYE', 'FFBC', 'FFBW', 'FFHL', 'FFIC', 'FFIN', 'FFIV', 'FFNW', 'FFWM', 'FGBI', 'FGEN', 'FGM', 'FHB', 'FHTX', 'FIBK', 'FID', 'FIII', 'FIIIU', 'FIIIW', 'FINX', 'FISI', 'FISV', 'FITB', 'FITBI', 'FITBO', 'FITBP', 'FIVE', 'FIVN', 'FIXD', 'FIXX', 'FIZZ', 'FJP', 'FKU', 'FLDM', 'FLEX', 'FLGT', 'FLIC', 'FLIR', 'FLL', 'FLMN', 'FLMNW', 'FLN', 'FLNT', 'FLUX', 'FLWS', 'FLXN', 'FLXS', 'FMAO', 'FMB', 'FMBH', 'FMBI', 'FMBIO', 'FMBIP', 'FMHI', 'FMK', 'FMNB', 'FMTX', 'FNCB', 'FNHC', 'FNK', 'FNKO', 'FNLC', 'FNWB', 'FNX', 'FNY', 'FOCS', 'FOLD', 'FONR', 'FORD', 'FORK', 'FORM', 'FORR', 'FORTY', 'FOSL', 'FOX', 'FOXA', 'FOXF', 'FPA', 'FPAY', 'FPRX', 'FPXE', 'FPXI', 'FRAF', 'FRAN', 'FRBA', 'FRBK', 'FREE', 'FREEW', 'FREQ', 'FRG', 'FRGAP', 'FRGI', 'FRHC', 'FRLN', 'FRME', 'FROG', 'FRPH', 'FRPT', 'FRSX', 'FRTA', 'FSBW', 'FSDC', 'FSEA', 'FSFG', 'FSLR', 'FSRV', 'FSRVU', 'FSRVW', 'FSTR', 'FSV', 'FSZ', 'FTA', 'FTAG', 'FTC', 'FTCS', 'FTDR', 'FTEK', 'FTFT', 'FTGC', 'FTHI', 'FTHM', 'FTIV', 'FTIVU', 'FTIVW', 'FTLB', 'FTNT', 'FTOC', 'FTOCU', 'FTOCW', 'FTRI', 'FTSL', 'FTSM', 'FTXD', 'FTXG', 'FTXH', 'FTXL', 'FTXN', 'FTXO', 'FTXR', 'FULC', 'FULT', 'FULTP', 'FUNC', 'FUND', 'FUSB', 'FUSN', 'FUTU', 'FUV', 'FV', 'FVAM', 'FVC', 'FVCB', 'FVE', 'FWONA', 'FWONK', 'FWP', 'FWRD', 'FXNC', 'FYC', 'FYT', 'FYX', 'GABC', 'GAIA', 'GAIN', 'GAINL', 'GAINM', 'GALT', 'GAN', 'GASS', 'GBCI', 'GBDC', 'GBIO', 'GBLI', 'GBLIL', 'GBT', 'GCBC', 'GDEN', 'GDRX', 'GDS', 'GDYN', 'GDYNW', 'GEC', 'GECC', 'GECCL', 'GECCM', 'GECCN', 'GENC', 'GENE', 'GENY', 'GEOS', 'GERN', 'GEVO', 'GFED', 'GFN', 'GFNCP', 'GFNSL', 'GFNSZ', 'GGAL', 'GH', 'GHIV', 'GHIVU', 'GHIVW', 'GHSI', 'GIFI', 'GIGE', 'GIGM', 'GIII', 'GILD', 'GILT', 'GLAD', 'GLADD', 'GLADL', 'GLBS', 'GLBZ', 'GLDD', 'GLDI', 'GLG', 'GLIBA', 'GLIBP', 'GLMD', 'GLNG', 'GLPG', 'GLPI', 'GLRE', 'GLSI', 'GLTO', 'GLUU', 'GLYC', 'GMAB', 'GMBL', 'GMBLW', 'GMDA', 'GMHI', 'GMHIU', 'GMHIW', 'GMLP', 'GMLPP', 'GNCA', 'GNFT', 'GNLN', 'GNMA', 'GNMK', 'GNOM', 'GNPX', 'GNRS', 'GNRSU', 'GNRSW', 'GNSS', 'GNTX', 'GNTY', 'GNUS', 'GO', 'GOCO', 'GOGL', 'GOGO', 'GOOD', 'GOODM', 'GOODN', 'GOOG', 'GOOGL', 'GOSS', 'GOVX', 'GOVXW', 'GP', 'GPOR', 'GPP', 'GPRE', 'GPRO', 'GRAY', 'GRBK', 'GRCY', 'GRCYU', 'GRCYW', 'GRFS', 'GRID', 'GRIF', 'GRIL', 'GRIN', 'GRMN', 'GRNQ', 'GRNV', 'GRNVR', 'GRNVU', 'GRNVW', 'GROW', 'GRPN', 'GRSV', 'GRSVU', 'GRSVW', 'GRTS', 'GRTX', 'GRVY', 'GRWG', 'GSBC', 'GSHD', 'GSIT', 'GSKY', 'GSM', 'GSMG', 'GSMGW', 'GSUM', 'GT', 'GTEC', 'GTH', 'GTHX', 'GTIM', 'GTLS', 'GTYH', 'GURE', 'GVP', 'GWACU', 'GWGH', 'GWPH', 'GWRS', 'GXGX', 'GXGXU', 'GXGXW', 'GXTG', 'GYRO', 'HA', 'HAACU', 'HAFC', 'HAIN', 'HALL', 'HALO', 'HAPP', 'HARP', 'HAS', 'HAYN', 'HBAN', 'HBANN', 'HBANO', 'HBCP', 'HBIO', 'HBMD', 'HBNC', 'HBP', 'HBT', 'HCAC', 'HCACU', 'HCACW', 'HCAP', 'HCAPZ', 'HCAT', 'HCCH', 'HCCHR', 'HCCHU', 'HCCHW', 'HCCI', 'HCDI', 'HCKT', 'HCM', 'HCSG', 'HDS', 'HDSN', 'HEAR', 'HEBT', 'HEC', 'HECCU', 'HECCW', 'HEES', 'HELE', 'HEPA', 'HERD', 'HERO', 'HEWG', 'HFBL', 'HFFG', 'HFWA', 'HGBL', 'HGEN', 'HGSH', 'HHR', 'HIBB', 'HIFS', 'HIHO', 'HIMX', 'HJLI', 'HJLIW', 'HLAL', 'HLG', 'HLIO', 'HLIT', 'HLNE', 'HLXA', 'HMHC', 'HMNF', 'HMST', 'HMSY', 'HMTV', 'HNDL', 'HNNA', 'HNRG', 'HOFT', 'HOFV', 'HOFVW', 'HOL', 'HOLI', 'HOLUU', 'HOLUW', 'HOLX', 'HOMB', 'HONE', 'HOOK', 'HOPE', 'HOTH', 'HOVNP', 'HPK', 'HPKEW', 'HQI', 'HQY', 'HRMY', 'HROW', 'HRTX', 'HRZN', 'HSAQ', 'HSDT', 'HSIC', 'HSII', 'HSKA', 'HSON', 'HST', 'HSTM', 'HSTO', 'HTBI', 'HTBK', 'HTBX', 'HTGM', 'HTHT', 'HTIA', 'HTLD', 'HTLF', 'HTLFP', 'HUBG', 'HUGE', 'HUIZ', 'HURC', 'HURN', 'HUSN', 'HVBC', 'HWBK', 'HWC', 'HWCC', 'HWCPL', 'HWCPZ', 'HWKN', 'HX', 'HYAC', 'HYACU', 'HYACW', 'HYLS', 'HYMC', 'HYMCW', 'HYMCZ', 'HYRE', 'HYXF', 'HYZD', 'HZNP', 'IAC', 'IART', 'IBB', 'IBBJ', 'IBCP', 'IBEX', 'IBKR', 'IBOC', 'IBTA', 'IBTB', 'IBTD', 'IBTE', 'IBTF', 'IBTG', 'IBTH', 'IBTI', 'IBTJ', 'IBTK', 'IBTX', 'ICAD', 'ICBK', 'ICCC', 'ICCH', 'ICFI', 'ICHR', 'ICLK', 'ICLN', 'ICLR', 'ICMB', 'ICON', 'ICPT', 'ICUI', 'IDCC', 'IDEX', 'IDLB', 'IDN', 'IDRA', 'IDXG', 'IDXX', 'IDYA', 'IEA', 'IEAWW', 'IEC', 'IEF', 'IEI', 'IEP', 'IESC', 'IEUS', 'IFGL', 'IFMK', 'IFRX', 'IFV', 'IGACU', 'IGF', 'IGIB', 'IGIC', 'IGICW', 'IGMS', 'IGOV', 'IGSB', 'IHRT', 'III', 'IIIN', 'IIIV', 'IIN', 'IIVI', 'IIVIP', 'IJT', 'IKNX', 'ILMN', 'ILPT', 'IMAB', 'IMAC', 'IMACW', 'IMBI', 'IMGN', 'IMKTA', 'IMMP', 'IMMR', 'IMNM', 'IMOS', 'IMRA', 'IMRN', 'IMRNW', 'IMTE', 'IMTX', 'IMTXW', 'IMUX', 'IMV', 'IMVT', 'IMXI', 'INAQ', 'INAQU', 'INAQW', 'INBK', 'INBKL', 'INBKZ', 'INBX', 'INCY', 'INDB', 'INDY', 'INFI', 'INFN', 'INFR', 'INGN', 'INM', 'INMB', 'INMD', 'INO', 'INOD', 'INOV', 'INPX', 'INSE', 'INSG', 'INSM', 'INTC', 'INTG', 'INTU', 'INTZ', 'INVA', 'INVE', 'INVO', 'INZY', 'IONS', 'IOSP', 'IOVA', 'IPAR', 'IPDN', 'IPGP', 'IPHA', 'IPHI', 'IPKW', 'IPLDP', 'IPWR', 'IQ', 'IRBT', 'IRCP', 'IRDM', 'IRIX', 'IRMD', 'IROQ', 'IRTC', 'IRWD', 'ISBC', 'ISDX', 'ISEE', 'ISEM', 'ISHG', 'ISIG', 'ISNS', 'ISRG', 'ISSC', 'ISTB', 'ISTR', 'ITAC', 'ITACU', 'ITACW', 'ITCI', 'ITI', 'ITIC', 'ITMR', 'ITOS', 'ITRI', 'ITRM', 'ITRN', 'IUS', 'IUSB', 'IUSG', 'IUSS', 'IUSV', 'IVA', 'IVAC', 'IXUS', 'IZEA', 'JACK', 'JAGX', 'JAKK', 'JAMF', 'JAN', 'JAZZ', 'JBHT', 'JBLU', 'JBSS', 'JCOM', 'JCS', 'JCTCF', 'JD', 'JFIN', 'JFU', 'JG', 'JJSF', 'JKHY', 'JKI', 'JMPNL', 'JMPNZ', 'JNCE', 'JOBS', 'JOUT', 'JRJC', 'JRSH', 'JRVR', 'JSM', 'JSMD', 'JSML', 'JUPW', 'JUPWW', 'JVA', 'JYNT', 'KALA', 'KALU', 'KALV', 'KBAL', 'KBNT', 'KBNTW', 'KBSF', 'KBWB', 'KBWD', 'KBWP', 'KBWR', 'KBWY', 'KC', 'KCAPL', 'KDMN', 'KDNY', 'KDP', 'KE', 'KELYA', 'KELYB', 'KEQU', 'KERN', 'KERNW', 'KFFB', 'KFRC', 'KHC', 'KIDS', 'KIN', 'KINS', 'KIRK', 'KLAC', 'KLDO', 'KLIC', 'KLXE', 'KMDA', 'KNDI', 'KNSA', 'KNSL', 'KOD', 'KOPN', 'KOR', 'KOSS', 'KPTI', 'KRBP', 'KRKR', 'KRMA', 'KRMD', 'KRNT', 'KRNY', 'KRON', 'KROS', 'KRTX', 'KRUS', 'KRYS', 'KSMT', 'KSMTU', 'KSMTW', 'KSPN', 'KTCC', 'KTOS', 'KTOV', 'KTOVW', 'KTRA', 'KURA', 'KVHI', 'KXIN', 'KYMR', 'KZIA', 'KZR', 'LACQ', 'LACQU', 'LACQW', 'LAKE', 'LAMR', 'LANC', 'LAND', 'LANDO', 'LANDP', 'LARK', 'LASR', 'LATN', 'LATNU', 'LATNW', 'LAUR', 'LAWS', 'LAZY', 'LBAI', 'LBC', 'LBRDA', 'LBRDK', 'LBTYA', 'LBTYB', 'LBTYK', 'LCA', 'LCAHU', 'LCAHW', 'LCAP', 'LCAPU', 'LCAPW', 'LCNB', 'LCUT', 'LCYAU', 'LDEM', 'LDSF', 'LE', 'LECO', 'LEDS', 'LEGH', 'LEGN', 'LEGR', 'LESL', 'LEVL', 'LEVLP', 'LFAC', 'LFACU', 'LFACW', 'LFTRU', 'LFUS', 'LFVN', 'LGHL', 'LGHLW', 'LGIH', 'LGND', 'LHCG', 'LI', 'LIFE', 'LILA', 'LILAK', 'LINC', 'LIND', 'LIQT', 'LITE', 'LIVE', 'LIVK', 'LIVKU', 'LIVKW', 'LIVN', 'LIVX', 'LIZI', 'LJPC', 'LKCO', 'LKFN', 'LKQ', 'LLIT', 'LLNW', 'LMAT', 'LMB', 'LMBS', 'LMFA', 'LMNL', 'LMNR', 'LMNX', 'LMPX', 'LMRK', 'LMRKN', 'LMRKO', 'LMRKP', 'LMST', 'LNDC', 'LNGR', 'LNSR', 'LNT', 'LNTH', 'LOAC', 'LOACR', 'LOACU', 'LOACW', 'LOAN', 'LOB', 'LOCO', 'LOGC', 'LOGI', 'LOOP', 'LOPE', 'LORL', 'LOVE', 'LPCN', 'LPLA', 'LPRO', 'LPSN', 'LPTH', 'LPTX', 'LQDA', 'LQDT', 'LRCX', 'LRGE', 'LRMR', 'LSAC', 'LSACU', 'LSACW', 'LSBK', 'LSCC', 'LSTR', 'LSXMA', 'LSXMB', 'LSXMK', 'LTBR', 'LTRN', 'LTRPA', 'LTRPB', 'LTRX', 'LULU', 'LUMO', 'LUNA', 'LUNG', 'LUXAU', 'LVHD', 'LWAY', 'LX', 'LXEH', 'LXRX', 'LYFT', 'LYL', 'LYRA', 'LYTS', 'MAACU', 'MACK', 'MACUU', 'MAGS', 'MANH', 'MANT', 'MAR', 'MARA', 'MARK', 'MARPS', 'MASI', 'MAT', 'MATW', 'MAXN', 'MAYS', 'MBB', 'MBCN', 'MBII', 'MBIN', 'MBINO', 'MBINP', 'MBIO', 'MBNKP', 'MBOT', 'MBRX', 'MBUU', 'MBWM', 'MCAC', 'MCACR', 'MCACU', 'MCBC', 'MCBS', 'MCEF', 'MCEP', 'MCFE', 'MCFT', 'MCHI', 'MCHP', 'MCHX', 'MCMJ', 'MCMJW', 'MCRB', 'MCRI', 'MDB', 'MDCA', 'MDGL', 'MDGS', 'MDGSW', 'MDIA', 'MDIV', 'MDJH', 'MDLZ', 'MDNA', 'MDRR', 'MDRRP', 'MDRX', 'MDWD', 'MDXG', 'MEDP', 'MEDS', 'MEIP', 'MELI', 'MEOH', 'MERC', 'MESA', 'MESO', 'METC', 'METX', 'METXW', 'MFH', 'MFIN', 'MFINL', 'MFNC', 'MGEE', 'MGEN', 'MGI', 'MGIC', 'MGLN', 'MGNI',
    # 'MGNX', 'MGPI', 'MGRC', 'MGTA', 'MGTX', 'MGYR', 'MHLD', 'MICT', 'MIDD', 'MIK', 'MILN', 'MIME', 'MIND', 'MINDP', 'MIRM', 'MIST', 'MITK', 'MITO', 'MKD', 'MKGI', 'MKSI', 'MKTX', 'MLAB', 'MLAC', 'MLACU', 'MLACW', 'MLCO', 'MLHR', 'MLND', 'MLVF', 'MMAC', 'MMLP', 'MMSI', 'MMYT', 'MNCL', 'MNCLU', 'MNCLW', 'MNDO', 'MNKD', 'MNOV', 'MNPR', 'MNRO', 'MNSB', 'MNSBP', 'MNST', 'MNTX', 'MOBL', 'MOFG', 'MOGO', 'MOHO', 'MOMO', 'MOR', 'MORF', 'MORN', 'MOSY', 'MOTNU', 'MOTS', 'MOXC', 'MPAA', 'MPB', 'MPWR', 'MRAM', 'MRBK', 'MRCC', 'MRCCL', 'MRCY', 'MREO', 'MRIN', 'MRKR', 'MRLN', 'MRNA', 'MRNS', 'MRSN', 'MRTN', 'MRTX', 'MRUS', 'MRVL', 'MSBI', 'MSEX', 'MSFT', 'MSON', 'MSTR', 'MSVB', 'MTBC', 'MTBCP', 'MTC', 'MTCH', 'MTCR', 'MTEM', 'MTEX', 'MTLS', 'MTP', 'MTRX', 'MTSC', 'MTSI', 'MTSL', 'MU', 'MVBF', 'MVIS', 'MWK', 'MXIM', 'MYFW', 'MYGN', 'MYL', 'MYOK', 'MYOS', 'MYRG', 'MYSZ', 'MYT', 'NAII', 'NAKD', 'NAOV', 'NARI', 'NATH', 'NATI', 'NATR', 'NAVI', 'NBAC', 'NBACR', 'NBACU', 'NBACW', 'NBEV', 'NBIX', 'NBLX', 'NBN', 'NBRV', 'NBSE', 'NBTB', 'NCBS', 'NCMI', 'NCNA', 'NCNO', 'NCSM', 'NCTY', 'NDAQ', 'NDLS', 'NDRA', 'NDRAW', 'NDSN', 'NEO', 'NEOG', 'NEON', 'NEOS', 'NEPH', 'NEPT', 'NERV', 'NESR', 'NESRW', 'NETE', 'NEWA', 'NEWT', 'NEWTI', 'NEWTL', 'NEXT', 'NFBK', 'NFE', 'NFLX', 'NFTY', 'NGACU', 'NGHC', 'NGHCN', 'NGHCO', 'NGHCP', 'NGHCZ', 'NGM', 'NH', 'NHIC', 'NHICU', 'NHICW', 'NHLD', 'NHLDW', 'NHTC', 'NICE', 'NICK', 'NIU', 'NK', 'NKLA', 'NKSH', 'NKTR', 'NKTX', 'NLOK', 'NLTX', 'NMCI', 'NMFC', 'NMFCL', 'NMIH', 'NMMC', 'NMMCU', 'NMMCW', 'NMRD', 'NMRK', 'NMTR', 'NNBR', 'NNDM', 'NNOX', 'NOACU', 'NODK', 'NOVN', 'NOVS', 'NOVSU', 'NOVSW', 'NOVT', 'NPA', 'NPAUU', 'NPAWW', 'NRBO', 'NRC', 'NRIM', 'NRIX', 'NSEC', 'NSIT', 'NSSC', 'NSTG', 'NSYS', 'NTAP', 'NTCT', 'NTEC', 'NTES', 'NTGR', 'NTIC', 'NTLA', 'NTNX', 'NTRA', 'NTRP', 'NTRS', 'NTRSO', 'NTUS', 'NTWK', 'NUAN', 'NURO', 'NUVA', 'NUZE', 'NVAX', 'NVCN', 'NVCR', 'NVDA', 'NVEC', 'NVEE', 'NVFY', 'NVIV', 'NVMI', 'NVUS', 'NWBI', 'NWE', 'NWFL', 'NWL', 'NWLI', 'NWPX', 'NWS', 'NWSA', 'NXGN', 'NXPI', 'NXST', 'NXTC', 'NXTD', 'NXTG', 'NYMT', 'NYMTM', 'NYMTN', 'NYMTO', 'NYMTP', 'NYMX', 'OBAS', 'OBCI', 'OBLN', 'OBNK', 'OBSV', 'OCC', 'OCCI', 'OCCIP', 'OCFC', 'OCFCP', 'OCGN', 'OCSI', 'OCSL', 'OCUL', 'OCUP', 'ODFL', 'ODP', 'ODT', 'OEG', 'OESX', 'OFED', 'OFIX', 'OFLX', 'OFS', 'OFSSG', 'OFSSI', 'OFSSL', 'OFSSZ', 'OGI', 'OIIM', 'OKTA', 'OLB', 'OLD', 'OLED', 'OLLI', 'OM', 'OMAB', 'OMCL', 'OMER', 'OMEX', 'OMP', 'ON', 'ONB', 'ONCR', 'ONCS', 'ONCT', 'ONCY', 'ONEM', 'ONEQ', 'ONEW', 'ONTX', 'ONTXW', 'ONVO', 'OPBK', 'OPCH', 'OPES', 'OPESU', 'OPESW', 'OPGN', 'OPHC', 'OPI', 'OPINI', 'OPINL', 'OPK', 'OPNT', 'OPOF', 'OPRA', 'OPRT', 'OPRX', 'OPT', 'OPTN', 'OPTT', 'ORBC', 'ORGO', 'ORGS', 'ORIC', 'ORLY', 'ORMP', 'ORPH', 'ORRF', 'ORSN', 'ORSNR', 'ORSNU', 'ORSNW', 'ORTX', 'OSBC', 'OSIS', 'OSMT', 'OSN', 'OSPN', 'OSS', 'OSTK', 'OSUR', 'OSW', 'OTEL', 'OTEX', 'OTIC', 'OTLK', 'OTLKW', 'OTRK', 'OTRKP', 'OTTR', 'OVBC', 'OVID', 'OVLY', 'OXBR', 'OXBRW', 'OXFD', 'OXLC', 'OXLCM', 'OXLCO', 'OXLCP', 'OXSQ', 'OXSQL', 'OXSQZ', 'OYST', 'OZK', 'PAAS', 'PACB', 'PACW', 'PAE', 'PAEWW', 'PAHC', 'PAICU', 'PAND', 'PANL', 'PASG', 'PATI', 'PATK', 'PAVM', 'PAVMW', 'PAVMZ', 'PAYA', 'PAYAW', 'PAYS', 'PAYX', 'PBCT', 'PBCTP', 'PBFS', 'PBHC', 'PBIP', 'PBPB', 'PBTS', 'PBYI', 'PCAR', 'PCB', 'PCH', 'PCOM', 'PCRX', 'PCSA', 'PCSB', 'PCTI', 'PCTY', 'PCVX', 'PCYG', 'PCYO', 'PDBC', 'PDCE', 'PDCO', 'PDD', 'PDEV', 'PDEX', 'PDFS', 'PDLB', 'PDLI', 'PDP', 'PDSB', 'PEBK', 'PEBO', 'PECK', 'PEGA', 'PEIX', 'PENN', 'PEP', 'PERI', 'PESI', 'PETQ', 'PETS', 'PETZ', 'PEY', 'PEZ', 'PFBC', 'PFBI', 'PFC', 'PFF', 'PFG', 'PFHD', 'PFI', 'PFIE', 'PFIN', 'PFIS', 'PFLT', 'PFM', 'PFMT', 'PFPT', 'PFSW', 'PGC', 'PGEN', 'PGJ', 'PGNY', 'PHAS', 'PHAT', 'PHCF', 'PHIO', 'PHIOW', 'PHO', 'PHUN', 'PHUNW', 'PI', 'PICO', 'PID', 'PIE', 'PIH', 'PIHPP', 'PINC', 'PIO', 'PIRS', 'PIXY', 'PIZ', 'PKBK', 'PKOH', 'PKW', 'PLAB', 'PLAY', 'PLBC', 'PLC', 'PLCE', 'PLIN', 'PLL', 'PLMR', 'PLPC', 'PLRX', 'PLSE', 'PLUG', 'PLUS', 'PLW', 'PLXP', 'PLXS', 'PLYA', 'PMBC', 'PMD', 'PME', 'PMVP', 'PNBK', 'PNFP', 'PNFPP', 'PNNT', 'PNNTG', 'PNQI', 'PNRG', 'PNTG', 'POAI', 'PODD', 'POLA', 'POOL', 'POTX', 'POWI', 'POWL', 'PPBI', 'PPC', 'PPD', 'PPH', 'PPIH', 'PPSI', 'PRAA', 'PRAH', 'PRAX', 'PRCP', 'PRDO', 'PRFT', 'PRFX', 'PRFZ', 'PRGS', 'PRGX', 'PRIM', 'PRLD', 'PRN', 'PROF', 'PROG', 'PROV', 'PRPH', 'PRPL', 'PRPLW', 'PRPO', 'PRQR', 'PRSC', 'PRTA', 'PRTH', 'PRTK', 'PRTS', 'PRVB', 'PRVL', 'PS', 'PSAC', 'PSACU', 'PSACW', 'PSC', 'PSCC', 'PSCD', 'PSCE', 'PSCF', 'PSCH', 'PSCI', 'PSCM', 'PSCT', 'PSCU', 'PSEC', 'PSET', 'PSHG', 'PSL', 'PSM', 'PSMT', 'PSNL', 'PSTI', 'PSTV', 'PSTX', 'PT', 'PTAC', 'PTACU', 'PTACW', 'PTC', 'PTCT', 'PTE', 'PTEN', 'PTF', 'PTGX', 'PTH', 'PTI', 'PTMN', 'PTNR', 'PTON', 'PTRS', 'PTSI', 'PTVCA', 'PTVCB', 'PTVE', 'PUI', 'PULM', 'PUYI', 'PVAC', 'PVBC', 'PWFL', 'PWOD', 'PXI', 'PXLW', 'PXS', 'PXSAP', 'PXSAW', 'PY', 'PYPD', 'PYPL', 'PYZ', 'PZZA', 'QABA', 'QADA', 'QADB', 'QAT', 'QCLN', 'QCOM', 'QCRH', 'QDEL', 'QELLU', 'QFIN', 'QH', 'QIWI', 'QK', 'QLGN', 'QLYS', 'QMCO', 'QNST', 'QQEW', 'QQQ', 'QQQJ', 'QQQM', 'QQQN', 'QQQX', 'QQXT', 'QRHC', 'QRTEA', 'QRTEB', 'QRTEP', 'QRVO', 'QTEC', 'QTNT', 'QTRX', 'QTT', 'QUIK', 'QUMU', 'QURE', 'QYLD', 'QYLG', 'RACA', 'RADA', 'RADI', 'RAIL', 'RAND', 'RAPT', 'RARE', 'RAVE', 'RAVN', 'RBB', 'RBBN', 'RBCAA', 'RBCN', 'RBKB', 'RBNC', 'RCEL', 'RCHGU', 'RCII', 'RCKT', 'RCKY', 'RCM', 'RCMT', 'RCON', 'RDCM', 'RDFN', 'RDHL', 'RDI', 'RDIB', 'RDNT', 'RDUS', 'RDVT', 'RDVY', 'RDWR', 'REAL', 'REDU', 'REED', 'REFR', 'REG', 'REGI', 'REGN', 'REKR', 'RELL', 'RELV', 'REPH', 'REPL', 'RESN', 'RETA', 'RETO', 'REYN', 'RFAP', 'RFDI', 'RFEM', 'RFEU', 'RFIL', 'RGCO', 'RGEN', 'RGLD', 'RGLS', 'RGNX', 'RGP', 'RIBT', 'RICK', 'RIDE', 'RIDEW', 'RIGL', 'RILY', 'RILYG', 'RILYH', 'RILYI', 'RILYL', 'RILYM', 'RILYN', 'RILYO', 'RILYP', 'RILYZ', 'RING', 'RIOT', 'RIVE', 'RKDA', 'RLAY', 'RLMD', 'RMBI', 'RMBL', 'RMBS', 'RMCF', 'RMNI', 'RMR', 'RMRM', 'RMTI', 'RNA', 'RNDB', 'RNDM', 'RNDV', 'RNEM', 'RNET', 'RNLC', 'RNLX', 'RNMC', 'RNSC', 'RNST', 'RNWK', 'ROAD', 'ROBT', 'ROCH', 'ROCHU', 'ROCHW', 'ROCK', 'ROIC', 'ROKU', 'ROLL', 'ROOT', 'ROST', 'RP', 'RPAY', 'RPD', 'RPRX', 'RPTX', 'RRBI', 'RRGB', 'RRR', 'RSSS', 'RTH', 'RTLR', 'RTRX', 'RUBY', 'RUHN', 'RUN', 'RUSHA', 'RUSHB', 'RUTH', 'RVMD', 'RVNC', 'RVSB', 'RWLK', 'RXT', 'RYAAY', 'RYTM', 'RZLT', 'SABR', 'SABRP', 'SAFM', 'SAFT', 'SAGE', 'SAIA', 'SAII', 'SAIIU', 'SAIIW', 'SAL', 'SALM', 'SAMA', 'SAMAU', 'SAMAW', 'SAMG', 'SANM', 'SANW', 'SASR', 'SATS', 'SAVA', 'SBAC', 'SBBP', 'SBCF', 'SBFG', 'SBGI', 'SBLK', 'SBLKZ', 'SBNY', 'SBPH', 'SBRA', 'SBSI', 'SBT', 'SBUX', 'SCHL', 'SCHN', 'SCKT', 'SCOR', 'SCPH', 'SCPL', 'SCSC', 'SCVL', 'SCWX', 'SCYX', 'SCZ', 'SDC', 'SDG', 'SDGR', 'SDVY', 'SEAC', 'SECO', 'SEDG', 'SEED', 'SEEL', 'SEIC', 'SELB', 'SELF', 'SENEA', 'SENEB', 'SESN', 'SFBC', 'SFBS', 'SFET', 'SFIX', 'SFM', 'SFNC', 'SFST', 'SFT', 'SFTTW', 'SG', 'SGA', 'SGBX', 'SGC', 'SGEN', 'SGH', 'SGLB', 'SGLBW', 'SGMA', 'SGMO', 'SGMS', 'SGOC', 'SGRP', 'SGRY', 'SHBI', 'SHEN', 'SHIP', 'SHIPW', 'SHIPZ', 'SHLD', 'SHOO', 'SHSP', 'SHV', 'SHY', 'SHYF', 'SIBN', 'SIC', 'SIEB', 'SIEN', 'SIFY', 'SIGA', 'SIGI', 'SILC', 'SILK', 'SIMO', 'SINA', 'SINO', 'SINT', 'SIOX', 'SIRI', 'SITM', 'SIVB', 'SIVBP', 'SJ', 'SKOR', 'SKYW', 'SKYY', 'SLAB', 'SLCT', 'SLDB', 'SLGG', 'SLGL', 'SLGN', 'SLM', 'SLMBP', 'SLN', 'SLNO', 'SLP', 'SLQD', 'SLRC', 'SLRX', 'SLS', 'SLVO', 'SMBC', 'SMBK', 'SMCI', 'SMCP', 'SMED', 'SMH', 'SMIT', 'SMMC', 'SMMCU', 'SMMCW',
    # 'SMMF', 'SMMT', 'SMPL', 'SMSI', 'SMTC', 'SMTI', 'SMTX', 'SNBP', 'SNBR', 'SNCA', 'SNCR', 'SND', 'SNDE', 'SNDL', 'SNDX', 'SNES', 'SNEX', 'SNFCA', 'SNGX', 'SNGXW', 'SNLN', 'SNOA', 'SNPS', 'SNSR', 'SNSS', 'SNUG', 'SNY', 'SOCL', 'SOHO', 'SOHOB', 'SOHON', 'SOHOO', 'SOHU', 'SOLO', 'SOLOW', 'SOLY', 'SONA', 'SONM', 'SONN', 'SONO', 'SOXX', 'SP', 'SPCB', 'SPFI', 'SPI', 'SPKE', 'SPKEP', 'SPLK', 'SPNE', 'SPNS', 'SPOK', 'SPPI', 'SPQQ', 'SPRB', 'SPRO', 'SPRT', 'SPSC', 'SPT', 'SPTN', 'SPWH', 'SPWR', 'SQBG', 'SQFT', 'SQLV', 'SQQQ', 'SRAC', 'SRACU', 'SRACW', 'SRAX', 'SRCE', 'SRCL', 'SRDX', 'SRET', 'SREV', 'SRGA', 'SRNE', 'SRPT', 'SRRA', 'SRRK', 'SRSAU', 'SRTS', 'SSB', 'SSBI', 'SSKN', 'SSNC', 'SSNT', 'SSP', 'SSPK', 'SSPKU', 'SSPKW', 'SSRM', 'SSSS', 'SSTI', 'SSYS', 'STAA', 'STAF', 'STAY', 'STBA', 'STCN', 'STEP', 'STFC', 'STIM', 'STKL', 'STKS', 'STLD', 'STMP', 'STND', 'STNE', 'STOK', 'STRA', 'STRL', 'STRM', 'STRO', 'STRS', 'STRT', 'STSA', 'STTK', 'STWO', 'STWOU', 'STWOW', 'STX', 'STXB', 'SUMO', 'SUMR', 'SUNS', 'SUNW', 'SUPN', 'SURF', 'SUSB', 'SUSC', 'SUSL', 'SVA', 'SVAC', 'SVACU', 'SVACW', 'SVBI', 'SVC', 'SVMK', 'SVRA', 'SVVC', 'SWAV', 'SWBI', 'SWIR', 'SWKH', 'SWKS', 'SWTX', 'SXTC', 'SY', 'SYBT', 'SYBX', 'SYKE', 'SYNA', 'SYNC', 'SYNH', 'SYNL', 'SYPR', 'SYRS', 'SYTA', 'SYTAW', 'TA', 'TACO', 'TACT', 'TAIT', 'TANH', 'TANNI', 'TANNL', 'TANNZ', 'TAOP', 'TARA', 'TARS', 'TAST', 'TATT', 'TAYD', 'TBBK', 'TBIO', 'TBK', 'TBKCP', 'TBLT', 'TBLTW', 'TBNK', 'TBPH', 'TC', 'TCBI', 'TCBIL', 'TCBIP', 'TCBK', 'TCCO', 'TCDA', 'TCF', 'TCFC', 'TCFCP', 'TCMD', 'TCOM', 'TCON', 'TCPC', 'TCRR', 'TCX', 'TDAC', 'TDACU', 'TDACW', 'TDIV', 'TEAM', 'TECH', 'TECTP', 'TEDU', 'TEKKU', 'TELA', 'TELL', 'TENB', 'TENX', 'TER', 'TESS', 'TFFP', 'TFSL', 'TGA', 'TGLS', 'TGTX', 'TH', 'THBR', 'THBRU', 'THBRW', 'THCA', 'THCAU', 'THCAW', 'THCB', 'THCBU', 'THCBW', 'THFF', 'THMO', 'THRM', 'THRY', 'THTX', 'THWWW', 'TIG', 'TIGO', 'TIGR', 'TILE', 'TIPT', 'TITN', 'TLC', 'TLGT', 'TLMD', 'TLMDW', 'TLND', 'TLRY', 'TLSA', 'TLT', 'TMDI', 'TMDX', 'TMPMU', 'TMTS', 'TMTSU', 'TMTSW', 'TMUS', 'TNAV', 'TNDM', 'TNXP', 'TOMZ', 'TOPS', 'TOTA', 'TOTAR', 'TOTAU', 'TOTAW', 'TOUR', 'TOWN', 'TPCO', 'TPIC', 'TPTX', 'TQQQ', 'TRCH', 'TREE', 'TRHC', 'TRIB', 'TRIL', 'TRIP', 'TRIT', 'TRITW', 'TRMB', 'TRMD', 'TRMK', 'TRMT', 'TRNS', 'TROW', 'TRS', 'TRST', 'TRUE', 'TRUP', 'TRVG', 'TRVI', 'TRVN', 'TSBK', 'TSC', 'TSCAP', 'TSCBP', 'TSCO', 'TSEM', 'TSHA', 'TSIAU', 'TSLA', 'TSRI', 'TTCF', 'TTCFW', 'TTD', 'TTEC', 'TTEK', 'TTGT', 'TTMI', 'TTNP', 'TTOO', 'TTTN', 'TTWO', 'TUR', 'TURN', 'TUSA', 'TUSK', 'TVTY', 'TW', 'TWCT', 'TWCTU', 'TWCTW', 'TWIN', 'TWNK', 'TWNKW', 'TWOU', 'TWST', 'TXG', 'TXMD', 'TXN', 'TXRH', 'TYHT', 'TYME', 'TZAC', 'TZACU', 'TZACW', 'TZOO', 'UAE', 'UAL', 'UBCP', 'UBFO', 'UBOH', 'UBSI', 'UBX', 'UCBI', 'UCBIO', 'UCL', 'UCTT', 'UEIC', 'UEPS', 'UFCS', 'UFO', 'UFPI', 'UFPT', 'UG', 'UHAL', 'UIHC', 'ULBI', 'ULH', 'ULTA', 'UMBF', 'UMPQ', 'UNAM', 'UNB', 'UNIT', 'UNTY', 'UONE', 'UONEK', 'UPLD', 'UPWK', 'URBN', 'URGN', 'UROV', 'USAK', 'USAP', 'USAU', 'USCR', 'USEG', 'USIG', 'USIO', 'USLB', 'USLM', 'USMC', 'USOI', 'USWS', 'USWSW', 'USXF', 'UTHR', 'UTMD', 'UTSI', 'UVSP', 'UXIN', 'VACQU', 'VALU', 'VBFC', 'VBIV', 'VBLT', 'VBTX', 'VC', 'VCEL', 'VCIT', 'VCLT', 'VCNX', 'VCSH', 'VCTR', 'VCYT', 'VECO', 'VEON', 'VERB', 'VERBW', 'VERI', 'VERO', 'VERU', 'VERX', 'VERY', 'VETS', 'VFF', 'VG', 'VGIT', 'VGLT', 'VGSH', 'VIAC', 'VIACA', 'VIAV', 'VICR', 'VIE', 'VIGI', 'VIH', 'VIHAU', 'VIHAW', 'VIOT', 'VIR', 'VIRC', 'VIRT', 'VISL', 'VITL', 'VIVE', 'VIVO', 'VJET', 'VKTX', 'VKTXW', 'VLDR', 'VLDRW', 'VLGEA', 'VLY', 'VLYPO', 'VLYPP', 'VMAC', 'VMACU', 'VMACW', 'VMBS', 'VMD', 'VNDA', 'VNET', 'VNOM', 'VNQI', 'VOD', 'VONE', 'VONG', 'VONV', 'VOXX', 'VPN', 'VRA', 'VRAY', 'VRCA', 'VREX', 'VRIG', 'VRM', 'VRME', 'VRMEW', 'VRNA', 'VRNS', 'VRNT', 'VRRM', 'VRSK', 'VRSN', 'VRTS', 'VRTU', 'VRTX', 'VSAT', 'VSDA', 'VSEC', 'VSMV', 'VSPRU', 'VSTA', 'VSTM', 'VTC', 'VTGN', 'VTHR', 'VTIP', 'VTNR', 'VTRN', 'VTRSV', 'VTRU', 'VTSI', 'VTVT', 'VTWG', 'VTWO', 'VTWV', 'VUZI', 'VVPR', 'VWOB', 'VXRT', 'VXUS', 'VYGR', 'VYMI', 'VYNE', 'WABC', 'WAFD', 'WAFU', 'WASH', 'WATT', 'WB', 'WBA', 'WBND', 'WCLD', 'WDAY', 'WDC', 'WDFC', 'WEN', 'WERN', 'WETF', 'WEYS', 'WHF', 'WHFBZ', 'WHLM', 'WHLR', 'WHLRD', 'WHLRP', 'WIFI', 'WILC', 'WIMI', 'WINA', 'WINC', 'WING', 'WINT', 'WIRE', 'WISA', 'WIX', 'WKEY', 'WKHS', 'WLDN', 'WLFC', 'WLTW', 'WMG', 'WNEB', 'WOOD', 'WORX', 'WPRT', 'WRLD', 'WRTC', 'WSBC', 'WSBCP', 'WSBF', 'WSC', 'WSFS', 'WSG', 'WSTG', 'WTBA', 'WTER', 'WTFC', 'WTFCM', 'WTFCP', 'WTRE', 'WTREP', 'WTRH', 'WVE', 'WVFC', 'WVVI', 'WVVIP', 'WW', 'WWD', 'WWR', 'WYNN', 'XAIR', 'XBIO', 'XBIOW', 'XBIT', 'XCUR', 'XEL', 'XELA', 'XELB', 'XENE', 'XENT', 'XERS', 'XFOR', 'XGN', 'XLNX', 'XLRN', 'XNCR', 'XNET', 'XOMA', 'XONE', 'XP', 'XPEL', 'XPER', 'XRAY', 'XSPA', 'XT', 'XTLB', 'YGMZ', 'YGYI', 'YGYIP', 'YI', 'YIN', 'YJ', 'YLCO', 'YLDE', 'YMAB', 'YNDX', 'YORW', 'YRCW', 'YSACU', 'YTEN', 'YTRA', 'YVR', 'YY', 'Z', 'ZAGG', 'ZAZZT', 'ZBRA', 'ZBZZT', 'ZCMD', 'ZCZZT', 'ZEAL', 'ZEUS', 'ZG', 'ZGNX', 'ZGYH', 'ZGYHR', 'ZGYHU', 'ZGYHW', 'ZI', 'ZION', 'ZIONL', 'ZIONN', 'ZIONO', 'ZIONP', 'ZIOP', 'ZIXI', 'ZJZZT', 'ZKIN', 'ZLAB', 'ZM', 'ZNGA', 'ZNTL', 'ZS', 'ZSAN', 'ZUMZ', 'ZVO', 'ZVZZC', 'ZVZZT', 'ZWZZT', 'ZXYZ.A', 'ZXZZT', 'ZYNE', 'ZYXI']
    stockSymbols = [# Technology
                    "ATVI", "ADBE", "ADSK", "AMAT", "AMD", "ANSS", "CDNS", "CSCO", "DBX",
                    "DELL", "DLG.DE", "EA", "GOOG", "IBM", "INTC", "LOGI", "MSFT", "NOK",
                    "NVDA", "NXPI", "SNAP", "PINS", "PYPL", "QCOM", "SOXX",
                    "SPOT", "TWTR", "TXN", "WDC", "ZM",
                    # Entertainment
                    "DIS", "NFLX", "UBI.PA",
                    # Services
                    "0700.HK", "AAL", "AIR.PA", "AMZN", "BABA", "DAL", "DISH", "EBAY", "ETSY", "FB", "FSLY",
                    "FVRR", "JMIA", "LYFT", "MELI", "PTON", "ROKU", "SQ", "TTD", "UAL", "UBER", "WORK",
                    # Consumer Goods
                    "AAPL", "ADS.DE", "ALXN", "AML.L", "APRN", "COST", "NESN.SW", "NIO",
                    "NIU", "NKE", "PAH3.DE", "PEP", "PG", "PM", "SHAK", "SNE", "TPR", "TSLA",
                    "1810.HK", # XI
                    # Financial
                    "BAC", "BBD", "CIT", "ITUB", "JPM", "O", "SLV", "V",
                    # Basic Materials
                    "GOLD", "NEM", "SLB", "XOM",
                    # Industrial Goods
                    "BA", "LMT", "NTDOY", "RTX", "SIE.DE", "UPS",
                    # Healthcare
                    "GILD", "PFE", "SAN.PA"
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
