import urllib.request
import json
import _thread
import threading
import time
import mysql.connector
from pyquery import PyQuery as pq
import db_base
def url_open(url):
    print(url)
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}  
    req = urllib.request.Request(url=url, headers=headers)
    for i in range(10):
        try:
            response = urllib.request.urlopen(url=req, timeout=5).read().decode('utf-8')
            return response
        except Exception as e:
            print("github except:"+str(e))

github_list = {
    "BTC":"https://github.com/bitcoin/bitcoin",
    "ETH":"https://github.com/ethereum/go-ethereum",
    "XRP":"https://github.com/ripple/rippled",
    "USDT":"https://github.com/OmniLayer/omnicore",
    "BCH":"https://github.com/Bitcoin-ABC/bitcoin-abc",
    "LTC":"https://github.com/litecoin-project/litecoin",
    "EOS":"https://github.com/EOSIO/eos",
    "BNB":"no",
    "BSV":"https://github.com/bitcoin-sv/bitcoin-sv",
    "XLM":"https://github.com/stellar/stellar-core",
    "TRX":"","ADA":"","XMR":"","LEO":"","LINK":"","NEO":"","XTZ":"","HT":"","OKB":"","MIOTA":"","ATOM":"","DASH":"","MKR":"","ETC":"","ONT":"","USDC":"","CRO":"","XEM":"","VSYS":"","VET":"","DOGE":"","BAT":"","ZEC":"","PAX":"","PZM":"","DCR":"","ZB":"","QTUM":"","ZRX":"","HOT":"","VDS":"","BTG":"","REP":"","OMG":"","NANO":"","RVN":"","ALGO":"","XIN":"","DAI":"","SEELE":"","LSK":"","GUSD":"","KMD":"","BTM":"","DGB":"","EKT":"","BCD":"","BTT":"","QNT":"","FTT":"","SC":"","ICX":"","WAVES":"","IOST":"","MCO":"","MONA":"","XVG":"","BTS":"","KBC":"","HC":"","THETA":"","NEXO":"","RLC":"","AE":"","MAID":"","ARDR":"","ENJ":"","FSN":"","ZIL":"","ILC":"","STEEM":"","CHZ":"","RIF":"","ELF":"","SNT":"","GNT":"","NEW":"","AOA":"","CRPT":"","ZEN":"","DGTX":"","NPXS":"","SOLVE":"","XZC":"","ETN":"","ETP":"","EURS":"","STRAT":"","PLC":"","REN":"","GXC":"","MATIC":"","KNC":"","WIN":"","TNT":"","MANA":"","PPT":"","IGNIS":"","LRC":"","BRD":"","ELA":"","CTXC":"","PAI":"","ENG":"","AION":"","LAMB":"","NULS":"","WAN":"","NAS":"","WICC":"","DGD":"","ODE":"","RCN":"","WAX":"","R":"","BTCD":"","ARK":"","FTM":"","QASH":"","XMX":"","WTC":"","STORJ":"","FUN":"","ATP":"","BNT":"","ABT":"","POWR":"","GRIN":"","LOOM":"","ORBS":"","TOMO":"","BIX":"","DENT":"","GRS":"","NXS":"","CMT":"","PIVX":"","GAS":"","CVC":"","SYS":"","UIP":"","MAN":"","MDA":"","TUSD":"","NXT":"","VTC":"","LBA":"","AGI":"","TRUE":"","REQ":"","CS":"","MTL":"","BOLT":"","DAG":"","EGT":"","EMC2":"","CELR":"","TTC":"","BFT":"","POLY":"","IQ":"","GTO":"","UTK":"","EDO":"","DATA":"","ONG":"","EDR":"","PAY":"","RDN":"","ITC":"","CFI":"","CDT":"","SMT":"","INE":"","STORM":"","QSP":"","TNB":"","RUFF":"","UUU":"","EVX":"","ACT":"","SKY":"","VIB":"","CWV":"","TCT":"","PPC":"","NCASH":"","GNX":"","MDT":"","INS":"","MFT":"","MITH":"","NKN":"","SALT":"","META":"","YCC":"","MET":"","MEXC":"","INO":"","CRO":"","MIN":"","INB":"","HEDG":"","CENNZ":"","SNX":"","WON":"","YOU":"","DACH":"","CNX":"","SCGC":"","KCS":"","SLV":"","SXP":"","GAP":"","HAV":"","BCN":"","BDX":"","MCO":"","QBIT":"","BXK":"","FXC":"","VITAE":"","DMSD":"","NRG":"","VERI":"","BF":"","KEY":"","VEST":"","MX":"","HCOIN":"","DTR":"","NEX":"","CRPT":"","LA":"","GBT":"","FCT":"","JCT":"","VEEN":"","DEFI":"","DRG":"","ICN":"","RDD":"","SEC":"","LTK":"","BHD":"","ANT":"","LEND":"","SAN":"","C20":"","BCOO":"","MOAC":"","DAPS":"","SAFE":"","BCZERO":"","1SG":"","GNO":"","BIKI":"","ROX":"","GBYTE":"","COCOS":"","TCH":"","EVN":"","VAS":"","MED":"","ZT":"","PPP":"","LINA":"","RPX":"","APL":"","BZ":"","LOKI":"","DBET":"","CND":"","WGR":"","NMR":"","PRS":"","TEL":"","WABI":"","UNO":"","XET":"","KAN":"","WIX":"","UTT":"","1ST":"","FT":"","PLR":"","B2B":"","NOAH":"","HYC":"","REPO":"","RCOIN":"","DEW":"","DCN":"","PART":"","CSC":"","DIVX":"","DRGN":"","PRL":"","MON":"","INT":"","ZRC":"","COSS":"","NEC":"","DROP":"","RHOC":"","XTO":"","CAS":"","CNNS":"","ECA":"","INCNT":"","TAAS":"","TKY":"","QRL":"","POLIS":"","SOC":"","CVT":"","MWAT":"","NMC":"","NEBL":"","SXDT":"","LRN":"","SBD":"","ONE":"","XPX":"","UTNP":"","NAV":"","ADX":"","AT":"","ECOREAL":"","CBT":"","POE":"","EVR":"","WSX":"","DMT":"","BURST":"","XAS":"","SNGLS":"","NPX":"","CPT":"","AURA":"","SNM":"","BITCNY":"","SLS":"","BAX":"","REREREET":"","BET":"","BLOCK":"","PRO":"","GVT":"","XSN":"","BH":"","CHSB":"","PGN":"","PMA":"","BLZ":"","KEY":"","KKC":"","FNB":"","COSM":"","PHX":"","VIBE":"","VITE":"","PAI":"","VIA":"","ELI":"","FTN":"","XCP":"","QUN":"","PEPECASH":"","SNET":"","BTCP":"","ETZ":"","MRPH":"","BLK":"","DOCK":"","NEU":"","FLO":"","JNT":"","MDS":"","DEC":"","XDN":"","LOC":"","TRIO":"","AMB":"","YOYOW":"","SWFTC":"","SRN":"","DGX":"","GAME":"","SXUT":"","VEE":"","GET":"","STACS":"","SHOW":"","XDCE":"","HPB":"","CONI":"","QLC":"","XAUR":"","GENE":"","GEN":"","EMC":"","KTC":"","RSTR":"","AUTO":"","DDD":"","TERN":"","DLT":"","XRL":"","OCN":"","AEON":"","KIN":"","BMC":"","LCC":"","AST":"","EXMR":"","DERO":"","UBQ":"","DAGT":"","DNT":"","MR":"","BOX":"","POA":"","BTX":"","MOBI":"","BITUSD":"","HOT":"","NLG":"","LXT":"","LKK":"","APPC":"","COCO":"","DEX":"","LYM":"","DADI":"","QAU":"","ZIP":"","AVA":"","OST":"","MLN":"","MOD":"","CAG":"","BMX":"","NCT":"","VITES":"","SMART":"","HLC":"","ARN":"","DICE":"","GCR":"","PLBT":"","ETHOS":"","RBLX":"","MOC":"","GTC":"","TRAC":"","TV":"","CLAM":"","MTH":"","FLASH":"","SENSE":"","BCPT":"","BOX":"","BZNT":"","PPY":"","JADE":"","RNT":"","QRK":"","1WO":"","ECOB":"","DTA":"","MINT":"","DOGZ":"","OMNI":"","FTC":"","ONION":"","TDX":"","GET":"","GET":"","SLT":"","EDR":"","LBC":"","TEN":"","ECC":"","OLT":"","BTO":"","LUN":"","REM":"","UCT":"","SENT":"","XUC":"","SNC":"","LGLGGSC":"","DBC":"","CSNO":"","ZEL":"","BTT":"","ABYSSAXST":"","AMO":"","MESH":"","NIX":"","LET":"","CPC":"","NSR":"","BOS":"","CLN":"","RFR":"","TFD":"","AU":"","MITX":"","XPM":"","ECOM":"","BBR":"","CREDO":"","ATN":"","GBC":"","ZCL":"","BTN":"","ALIS":"","WINGS":"","IQN":"","UKG":"","SWM":"","FUEL":"","INSTAR":"","BAAS":"","EOSDAC":"","BGG":"","BBK":"","OK":"","KCASH":"","SHIP":"","OTB":"","MTC":"","XHV":"","EQL":"","FAIR":"","SHE":"","BKBT":"","XSPEC":"","DPY":"","SUB":"","ZCN":"","OAX":"","AIDOC":"","IDH":"","GOT":"","ADT":"","MVP":"","OF":"","ADC":"","GCC":"","VIN":"","CHX":"","HTB":"","NTY":"","APIS":"","XYO":"","TPAY":"","YEE":"","AIR":"","CPX":"","PRA":"","RC":"","XBX":"","SDA":"","BSC":"","CPAY":"","SKM":"","SHIFT":"","INK":"","KK":"","CV":"","DACS":"","UBT":"","HYDRO":"","PNK":"","CLOAK":"","TRST":"","RADS":"","PST":"","FOOD":"","KKG":"","ABL":"","BIS":"","HBZ":"","GRID":"","TFL":"","HTML":"","BAY":"","TAU":"","SPASP":"","CPU":"","ALQO":"","CHAT":"","IHT":"","DCT":"","18T":"","XMY":"","LIKE":"","SWTH":"","NGC":"","COV":"","CTE":"","RRRRLND":"","ATL":"","FLUZ":"","IOC":"","EFX":"","EAC":"","GSE":"","BCO":"","NBC":"","POT":"","SEN":"","AVH":"","SSP":"","OPQ":"","PHR":"","ECTE":"","DOT":"","COIN":"","MT":"","FOR":"","EEEE":"","UNT":"","GRC":"","CBC":"","NTKNTGC":"","VTR":"","XES":"","DDD":"","AXP":"","TOL":"","DDDDCHP":"","SUSD":"","UBUBUVRC":"","PAC":"","DAT":"","TRC":"","ET":"","XHI":"","JRC":"","JRPS":"","DMD":"","HMQ":"","ATCC":"","PCL":"","PCLVE":"","TAC":"","SPC":"","LEDU":"","BLT":"","TUBE":"","RMC":"","GMT":"","ADST":"","VEX":"","XNG":"","LINDA":"","CIC":"","NSD":"","MYST":"","NBAI":"","PARETO":"","ART":"","XPD":"","DOLLAR":"","FAIRFATI":"","NIM":"","TIME":"","TIO":"","MGD":"","CPT":"","S4F":"","DIME":"","BUT":"","CACACRECACAX":"","IMT":"","PRG":"","WET":"","SUMO":"","ORS":"","ORSOS":"","MTN":"","ZCO":"","SPX":"","CRW":"","STA":"","CURECURAG":"","ZPT":"","TRXC":"","ACAT":"","MUE":"","COVAL":"","WCT":"","BITG":"","STK":"","CCCCCDGCCKCCCCC":"","ZOI":"","HOR":"","DIG":"","OPTC":"","BLOC":"","XCASH":"","FXT":"","SHORTY":"","ISR":"","SIC":"","EKEKQOS":"","BPT":"","ZPR":"","LEV":"","ENU":"","PINK":"","ACM":"","XCEL":"","CARD":"","QNTU":"","1337":"","MGO":"","BAMB":"","BBB":"","SSC":"","MLC":"","MSP":"","CXO":"","UDOO":"","ITNS":"","SLR":"","BCBCBIB":"","LNC":"","SKB":"","ION":"","USNBT":"","BEET":"","SINSIELSICH":"","MAS":"","XNN":"","GARD":"","42":"","BCDT":"","AAAAPLAAAAPOIN":"","TCH":"","UCASH":"","UQC":"","NVC":"","WISH":"","HAT":"","BITB":"","SS":"","BBC":"","GEO":"","RED":"","OCT":"","MRK":"","CLO":"","HIT":"","MOON":"","MVC":"","STX":"","PURA":"","TOP":"","ZER":"","PTT":"","SPRTS":"","KRL":"","NOKU":"","IVY":"","FTX":"","TRTL":"","XWC":"","NYC":"","ECOM":"","HOLD":"","THC":"","ZP":"","SPD":"","PBT":"","SEM":"","GLD":"","DIT":"","TNC":"","BKX":"","BCI":"","MTV":"","DRT":"","IPL":"","MTX":"","SPD":"","PING":"","BWT":"","HKN":"","THRT":"","X8X":"","YBCT":"","MTC":"","SWT":"","EBC":"","DEB":"","FACE":"","EXP":"","GOLOS":"","FBN":"","UP":"","IXC":"","AIT":"","DATX":"","BKBC":"","IETH":"","GOT":"","LEO":"","AOG":"","CAPP":"","SUM":"","INXT":"","MC":"","QBT":"","NOTE":"","XDAG":"","AAA":"","LUX":"","ZLA":"","PTOY":"","HEAT":"","XBC":"","HSC":"","RVT":"","PTC":"","PORTAL":"","DCY":"","VLD":"","ESP":"","FCN":"","TRTT":"","OBITS":"","WSD":"","TMT":"","LIFE":"","AMN":"","CAN":"","DP":"","GLA":"","DXT":"","AUR":"","CEN":"","FOTA":"","ERC20":"","AID":"","BLAS":"","ETBS":"","CNET":"","OWN":"","ROCK2":"","XRA":"","LOG":"","SENC":"","RMESH":"","ATM":"","UFR":"","KEK":"","CANN":"","AAC":"","FISH":"","MNTP":"","RTE":"","ELEC":"","BTB":"","AMLT":"","BANCA":"","TSL":"","MGC":"","VSC":"","EXCL":"","COFI":"","ERT":"","GAM":"","HORUS":"","CL":"","BDG":"","UFO":"","SMLY":"","ZSZSZFL":"","LYNX":"","PBL":"","BLUE":"","GEM":"","PKT":"","OBSR":"","TKS":"","FTT":"","BNTY":"","FLIXX":"","ZIPT":"","DOVU":"","NANJ":"","LOBS":"","RVR":"","OMX":"","GENE":"","HUSH":"","J8T":"","CPY":"","CROAT":"","ALC":"","BQ":"","TES":"","KRB":"","BBP":"","MER":"","MAO":"","QAC":"","BTM":"","TGT":"","STB":"","EXY":"","ARX":"","LION":"","SPHTX":"","TOA":"","IXT":"","RC":"","ZAP":"","FREE":"","LATX":"","DYN":"","AERM":"","RIC":"","GIO":"","VCT":"","FYP":"","GEC":"","PIRL":"","SSS":"","GAT":"","LCS":"","RISE":"","TIPS":"","KB3":"","KLN":"","OLXA":"","TCC":"","ADB":"","BRM":"","BBO":"","XSH":"","RLX":"","BASH":"","MNX":"","MUSIC":"","MSR":"","MOT":"","VRM":"","DSH":"","COT":"","ORME":"","CTX":"","DNR":"","XMCT":"","THX":"","ZMN":"","XLR":"","SETH":"","BTCZ":"","0XBTC":"","VIEW":"","ETK":"","SHARD":"","NXCT":"","TTV":"","PALPHQX":"","PLAY":"","TMC":"","HLM":"","TELOS":"","EVN":"","PIGX":"","GRFT":"","LMC":"","SEXC":"","IIC":"","SCT":"","XVC":"","REAL":"","AMP":"","PIPL":"","CMCT":"","BEZ":"","RPD":"","SXC":"","MEME":"","START":"","SCRL":"","LUC":"","EFYT":"","ONL":"","PYLNT":"","TROLL":"","XSD":"","PRIX":"","BFB":"","ORE":"","UNB":"","DTH":"","SPHR":"","LLL":"","STQ":"","BIGUP":"","MIB":"","FLDC":"","FOD":"","NYAN":"","CARBON":"","PASS":"","PHI":"","SUPER":"","DUO":"","ZET":"","XMG":"","ERO":"","DBIX":"","HIRE":"","ZJLT":"","ENRG":"","LALA":"","SHND":"","CBX":"","CMPCO":"","XSG":"","PYN":"","BETR":"","BPTN":"","ACE":"","FRST":"","ZENI":"","CRED":"","ZNY":"","ADI":"","FJC":"","BRX":"","MLM":"","NLC2":"","WTL":"","UIS":"","HPC":"","KORE":"","SUR":"","XBP":"","CUBE":"","BWK":"","RYO":"","RAIN":"","EQUAD":"","EBTC":"","QWARK":"","COB":"","CNK":"","YOC":"","ADC":"","KICK":"","DAY":"","DOPE":"","TBX":"","HB":"","METAL":"","BITX":"","HGT":"","BETHER":"","GCN":"","BWT":"","GTM":"","GTMB":"","ATX":"","MONK":"","UUUU":"","LTHN":"","BIR":"","HNC":"","LFT":"","ATMI":"","RCT":"","LDOGE":"","SHDW":"","BOLI":"","EDRC":"","IDXM":"","XBI":"","GMC":"","NEOS":"","CPC":"","PENG":"","POLL":"","GUP":"","IPSX":"","EVC":"","ETHETTRUST":"","BIO":"","TEAM":"","XUN":"","GOOC":"","SCL":"","ZEUS":"","ABX":"","TRF":"","OOT":"","BOXX":"","MFG":"","CDN":"","DIM":"","TRA":"","TTC":"","BCAC":"","MEC":"","ODN":"","ESN":"","BTCS":"","SEND":"","INV":"","FRC":"","CRC":"","BYC":"","UCN":"","TIX":"","WGO":"","BOUTS":"","NPXSXEM":"","BITEUR":"","DAN":"","KAT":"","TEK":"","BSTY":"","TRUMP":"","NIO":"","PXC":"","SEQ":"","ETT":"","TOLL":"","HYP":"","ZCR":"","SGR":"","DEAL":"","AIB":"","ERC":"","CST":"","HER":"","NETKO":"","PIX":"","BUZZ":"","WAND":"","VME":"","STAR":"","PHO":"","BRIT":"","FBT":"","BERRY":"","PKG":"","SRCOIN":"","MSG":"","GVE":"","SCR":"","ASAFE2":"","SMQ":"","UNI":"","FSBT":"","EGC":"","BBN":"","REF":"","MRT":"","BELA":"","REX":"","NOBS":"","BLU":"","MAG":"","XCN":"","CIT":"","DAV":"","EVE":"","ALX":"","S":"","ZEIT":"","BRK":"","AHT":"","UNIFY":"","UNX":"","ZXC":"","EST":"","DGC":"","OPTI":"","CLR":"","TNS":"","HODL":"","TGC":"","VOT":"","GIC":"","CMM":"","ETG":"","WIRE":"","ELLA":"","TZC":"","VRS":"","FGC":"","WIZ":"","ONG":"","JC":"","MNC":"","PWR":"","MORE":"","EQT":"","HUZU":"","AIW":"","ADL":"","FORK":"","BON":"","NPER":"","ING":"","TIC":"","NRVE":"","NBR":"","DAG":"","CBC":"","IOP":"","PCN":"","EBCH":"","UNIT":"","PND":"","OTX":"","WEB":"","JSE":"","BRO":"","DEV":"","PUT":"","EL":"","ACACAFT":"","DTRC":"","FREC":"","CREA":"","GBX":"","ANC":"","EGEM":"","SINS":"","IND":"","BLTG":"","DDF":"","POP":"","BTB":"","PNY":"","BLOC":"","ZCC":"","ENGT":"","BBS":"","SWING":"","TX":"","ARO":"","FND":"","INSN":"","BTR":"","GOSS":"","BOBOONE":"","ADH":"","ARC":"","BTCN":"","GXX":"","ELY":"","SNOV":"","MMO":"","AREPA":"","BRIA":"","GLT":"","ICOS":"","PRIV":"","IC":"","WRC":"","OPC":"","MXT":"","PUT":"","BBK":"","CCL":"","SCSC":"","SIGSIET":"","SYNX":"","METM":"","REBL":"","RUP":"","TLC":"","MYMYEUNO":"","HXX":"","KLKS":"","ADZ":"","WAB":"","PFR":"","CHESS":"","EPY":"","NXC":"","VIT":"","SAT":"","SPF":"","RPI":"","CDX":"","JEW":"","ZAG":"","XVP":"","TDP":"","MCAP":"","NAVI":"","KIND":"","AMM":"","BVT":"","TALK":"","FLFL":"","2GIVE":"","BLAST":"","BLA":"","ATB":"","BSD":"","PEDI":"","BDL":"","XRE":"","VOISE":"","RBT":"","ELIX":"","PAT":"","SKIN":"","SONIQ":"","FOR":"","LOCI":"","ICR":"","CAT":"","BIT":"","NCP":"","GIN":"","BTW":"","VIVID":"","WEB":"","CJT":"","REC":"","JOINT":"","SAGA":"","LCP":"","GTC":"","UHC":"","AAAAMVPT":"","EEET":"","ITI":"","JIN":"","STARS":"","ARAW":"","OPCX":"","CSTL":"","BM":"","ITT":"","TDS":"","BTBTBTOAR":"","TOKC":"","NTK":"","IFLT":"","DFT":"","VSL":"","SIGT":"","INN":"","DEM":"","BTK":"","WTN":"","BSB":"","SHL":"","UNIC":"","GSR":"","GB":"","IRD":"","IMX":"","ETA":"","SMS":"","WILD":"","ARB":"","STEEP":"","SMC":"","TYPE":"","NTTC":"","XGS":"","BMH":"","XMCC":"","SHPING":"","SHI":"","BEN":"","BANK":"","HPC":"","MOIN":"","TCH":"","ACED":"","ONX":"","IQ":"","WDC":"","TRDT":"","XPAT":"","LNK":"","NMT":"","ENTS":"","CSOUL":"","DMB":"","DIX":"","WIT":"","XP":"","TAG":"","HLD":"","PLURA":"","MIC":"","BSTN":"","SND":"","DTB":"","SCC":"","DRM":"","CASH":"","ARY":"","HAC":"","ALL":"","TOK":"","BTA":"","FNC":"","CRM":"","CNUT":"","BOAT":"","ELTCOIN":"","888":"","HONEY":"","CYFM":"","B2G":"","XSTC":"","MNE":"","ECT":"","BTXC":"","LNC":"","BTCRED":"","SPR":"","ZZC":"","PSC":"","DML":"","CHEESE":"","OXY":"","HAND":"","XDNA":"","MEDIC":"","BC":"","RBIES":"","MAY":"","ARCT":"","MBI":"","FOXT":"","B@":"","APR":"","APR":"","AMS":"","SDRN":"","ABS":"","XPTX":"","XLC":"","NTWK":"","BSM":"","IG":"","EBET":"","PTS":"","TRC":"","REE":"","TTT":"","W3C":"","W3ST":"","KBR":"","CARE":"","STAC":"","PAK":"","CFL":"","RPC":"","BZX":"","STU":"","ATOM":"","MANNA":"","ALI":"","RUPX":"","GRLC":"","ARION":"","DAR":"","DTC":"","LINX":"","MCS":"","AUC":"","XUEZ":"","CRB":"","CCO":"","ESC":"","BTRN":"","LDBC":"","SCRIV":"","VTA":"","RLT":"","BPC":"","ELE":"","STN":"","CYMT":"","DACH":"","QVT":"","OTN":"","BZL":"","SRC":"","J":"","MOJO":"","POST":"","WAGE":"","VULC":"","KZC":"","PROC":"","STAK":"","NRP":"","BTD":"","COUPE":"","JWL":"","FNTB":"","ACC":"","HELP":"","CEC":"","NDNDND":"","ENT":"","MMM":"","NOX":"","TOTO":"","UET":"","BWS":"","ZYD":"","MICRO":"","KNT":"","CYL":"","CWXT":"","NUKO":"","CCT":"","ATS":"","CDM":"","MDC":"","RNTB":"","KUN":"","CTL":"","SKC":"","AIX":"","VIKKY":"","GLS":"","ZBA":"","MSCN":"","ESCE":"","KWH":"","XGOX":"","FLIK":"","NDC":"","CATO":"","KNT":"","BTAD":"","NLX":"","XINDXILC":"","BSC":"","ITL":"","ZNT":"","YLC":"","RNS":"","FDX":"","GRIM":"","SDP":"","ARB":"","PONZI":"","DATP":"","BTQ":"","SHB":"","NZL":"","DSR":"","HAVY":"","DTEM":"","BXT":"","CRX":"","LUNA":"","OCC":"","VLT":"","PEX":"","YUP":"","BTPL":"","RKC":"","MASH":"","AKA":"","HST":"","BFB":"","GRE":"","SHP":"","FTXT":"","LBTC":"","PIAT":"","GUS":"","VIVO":"","SPK":"","COMP":"","PLNC":"","ATH":"","FUNC":"","URALS":"","LPC":"","IBANK":"","XCXT":"","PXI":"","PAWS":"","EAGLE":"","DIN":"","VIU":"","DELTA":"","EMPR":"","BAS":"","XCT":"","BTCONE":"","NYEX":"","ATX":"","CNNC":"","BIT":"","HBC":"","IBTC":"","P7C":"","PNX":"","ARG":"","BUNNY":"","APC":"","MFTU":"","RAGNA":"","ACP":"","ALT":"","NTO":"","ICE":"","GEERT":"","IMP":"","STR":"","OCL":"","OLMP":"","QUAN":"","FLM":"","ADCN":"","COAL":"","WIN":"","ALTCOM":"","QBIC":"","BRAT":"","QNO":"","BTX":"","XOV":"","SOCC":"","HWC":"","CTIC3":"","PRC":"","XCG":"","ARGUS":"","EOT":"","ABY":"","ABJ":"","TSTR":"","XRC":"","PHON":"","JIYO":"","VLTC":"","CRC":"","VOCO":"","PCOIN":"","DDX":"","CREVA":"","BLN":"","SIM":"","LRM":"","BITS":"","COXST":"","SHADE":"","CJS":"","VGO":"","FAB":"","IRIS":"","MOF":"","ABBC":"","BEAM":"","CXC":"","PLPLPDAM":"","TFB":"","SERO":"","DVP":"","DFT":"","OPNN":"","CKB":"","PLG":"","QKC":"","MEDX":"","CON":"","GT":"","FXFXFR":"","AERGO":"","YTA":"","OCEAN":"","COS":"","TRBC":"","VID":"","RATING":"","ULT":"","VIDY":"","LT":"","BCV":"","BUSD":"","FET":"","FIL":"","TOP":"","CET":"","EC":"","ADN":"","TT":"","BOLTT":"","BHPC":"","MIX":"","NOIZ":"","DT":"","ONE":"","ERD":"","UPP":"","KICKS":"","ZG":"","UGAS":"","WXT":"","WIN":"","FOIN":"","GSB":"","LBTC":"","IOTX":"","DX":"","QB":"","AXE":"","GAT":"","LEND":"","TERA":"","MEETONE":"","BU":"","DACC":"","ANKR":"","BRZ":"","WHC":"","ADK":"","DOT":"","YO":"","GO":"","IDT":"","TSHP":"","BCX":"","BDP":"","SEER":"","STC":"","AMIO":"","OGO":"","GTN":"","PVT":"","RCCC":"","MESG":"","MTN":"","HBAR":"","MGC":"","SPIKE":"","RRB":"","IMG":"","TCT":"","BBK":"","COVA":"","BRC":"","AKRO":"","KNOW":"","FAT":"","LUNA":"","INF":"","ARPA":"","MBL":"","B91":"","KAN":"","HPT":"","XBASEXBOPC":"","DREP":"","TFUEL":"","MUSK":"","BPRO":"","MCC":"","HYN":"","HYL":"","BHT":"","CVNT":"","PCX":"","BIA":"","ELAC":"","DAPPT":"","TMTG":"","TAS":"","BAND":"","RBRBLIRBOEC":"","BRC":"","MHC":"","HNB":"","CSM":"","VRA":"","HQT":"","UC":"","HSN":"","TRTR":"","MMM":"","SSSS":"","AAA":"","GOS":"","IPC":"","NYE":"","COTI":"","DUSK":"","WKC":"","RSR":"","WWWWUSE":"","HUSD":"","BNANA":"","BBB":"","BQQQ":"","TSR":"","MCC":"","FLP":"","BIG":"","CNN":"","CVCC":"","CLB":"","TKC":"","PCCPCEVPCCZR":"","EAI":"","DOS":"","BBB":"","BOK":"","HMC":"","PC":"","LIGHTLITMLIGHT":"","IDHUB":"","GMAT":"","FO":"","IOTW":"","IOT":"","IOTO":"","AT":"","DCCB":"","DCN":"","DAC":"","UBTC":"","WETH":"","FDS":"","CAM":"","SNL":"","GMB":"","NNB":"","IFOOD":"","STRSTM":"","PLY":"","EUM":"","SOUL":"","SOVE":"","DASC":"","CODY":"","WWB":"","DAC":"","TEMCO":"","BOA":"","SBTC":"","CCCCTOKO":"","MPAY":"","OVC":"","AEN":"","FTO":"","INSUR":"","QMC":"","BTNT":"","SNTR":"","EMRX":"","VNT":"","TOS":"","SPRKLSPRF":"","LEVL":"","SWC":"","PLTC":"","USDS":"","DWS":"","CIX100":"","TFC":"","MRS":"","DPT":"","UND":"","SNTVT":"","EGCC":"","IIIIILAIITOK":"","NEWS":"","FFFFZ":"","EGG":"","CRE":"","KICK":"","FKX":"","HHHHHHHHT":"","HHX":"","FDZ":"","ENQ":"","LTO":"","DDK":"","CXTC":"","PROM":"","VENA":"","YEED":"","BIZ":"","PTI":"","EM":"","MXC":"","XFC":"","XFMC":"","WIB":"","RBTC":"","ROM":"","M2O":"","BHT":"","MNC":"","IOEXIOEL":"","IMC":"","N8VN8VAT":"","ESS":"","TYT":"","BEC":"","NOVA":"","WAC":"","TAT":"","SWTC":"","ADE":"","NOS":"","EURS":"","MCT":"","CAR":"","VJC":"","MT":"","VDG":"","BQT":"","HERO":"","CREDIT":"","NCC":"","UNC":"","DDM":"","USDQ":"","EDS":"","PTN":"","INCX":"","EVED":"","DAPP":"","NOIA":"","LQD":"","MAG":"","AMTC":"","EXT":"","ZAT":"","CAF":"","XENO":"","MXM":"","HOTC":"","CT":"","TENA":"","AIF":"","VNX":"","EXO":"","MBN":"","CREX":"","FIII":"","FOAM":"","CARAT":"","MEX":"","SRK":"","DADI":"","FBTC":"","AGRS":"","FEX":"","CHEX":"","HELP":"","CDC":"","BORA":"","BOOM":"","TGAME":"","GARK":"","JAR":"","SPT":"","PBC":"","WBTC":"","MSD":"","GRN":"","UOS":"","QUIN":"","TDC":"","LOTO":"","EDU":"","RKT":"","BCDN":"","DKYC":"","CAJ":"","PLA":"","JMT":"","EMGO":"","ANBF":"","WEBN":"","RIA":"","ECHT":"","TAN":"","CENT":"","MEDIBIMEDOP":"","CEL":"","BOTX":"","ZPAY":"","VNS":"","MEK":"","SLT":"","GUSS":"","COU":"","VDX":"","STPT":"","B2X":"","MVL":"","ACU":"","VALOR":"","LME":"","RISK":"","CANDY":"","OC":"","HINT":"","GCT":"","EDT":"","FLC":"","CNUS":"","VASH":"","BDS":"","XRC":"","FZ":"","XIN":"","OSCH":"","NEWOS":"","CDY":"","EUBC":"","UNIC":"","GRAM":"","NEXT":"","BLN":"","ZAIF":"","SNPC":"","KXC":"","HERB":"","PLAT":"","FI":"","XPC":"","ITS":"","DEEP":"","LZL":"","PASC":"","TKN":"","SKCH":"","PXC":"","GCS":"","BMB":"","BITH":"","EULO":"","SANC":"","QWC":"","BTU":"","QUBE":"","PDATA":"","RAVEN":"","SDS":"","IDC":"","QUSD":"","HRC":"","VTC":"","IGG":"","SEAD":"","AFC":"","WINT":"","INX":"","OSA":"","SKT":"","HPY":"","DRINK":"","OCX":"","VGW":"","BCW":"","KZE":"","BIN":"","LEMO":"","BURN":"","EON":"","INDI":"","BUB":"","CAN":"","VCA":"","SRNT":"","PCS":"","EMTEMTC":"","EVOS":"","SCC":"","ICTA":"","ADD":"","BTCB":"","HALO":"","GBG":"","ABDT":"","DEEX":"","CKUSD":"","CSPN":"","TOSC":"","HUM":"","RPL":"","SHOP":"","WMGO":"","TCASH":"","F1C":"","FUC":"","GOLD":"","DYNMT":"","SWL":"","VBK":"","NBOT":"","OEX":"","MINX":"","PEOS":"","CEFS":"","PIB":"","AMPL":"","CNP":"","IPT":"","DIO":"","FGC":"","LPT":"","VECT":"","MERI":"","TTN":"","BAN":"","A":"","WLO":"","MESSE":"","VLU":"","HXRO":"","MAPR":"","XAC":"","UPX":"","KMC":"","TESLA":"","ATNL":"","LHC":"","BIZ":"","PRES":"","LKC":"","DOGET":"","WIC":"","AGLT":"","BIFI":"","CLUB":"","FAB":"","OPEN":"","LVTC":"","EPC":"","BTCF":"","ACO":"","ROCO":"","BTCL":"","HEC":"","URAC":"","XD":"","COBRA":"","BUBO":"","BDSG":"","BDK":"","ORS":"","WGP":"","3DC":"","CGC":"","BCZ":"","IDEX":"","DVT":"","XMC":"","EDUC":"","GARY":"","BOOL":"","WYS":"","CYBR":"","ZNZ":"","WBL":"","GRMD":"","INC":"","RBG":"","WC":"","RFOX":"","MRI":"","ARQ":"","YBY":"","WNL":"","ETHPLO":"","FACC":"","CLD":"","KTS":"","XNV":"","NPC":"","GOD":"","P2PX":"","BNK":"","TETETHAR":"","WPP":"","XOT":"","BITCF":"","DSCB":"","BOPS":"","XLA":"","MGE":"","SHX":"","X42":"","MCPC":"","DASHG":"","BDC":"","THS":"","PDX":"","DOGEC":"","MCR":"","KARMA":"","SUP":"","PCC":"","LHT":"","LEEK":"","NANOX":"","BIT":"","TCN":"","BMT":"","CPS":"","IMT":"","VSF":"","HERC":"","FSCC":"","ACDC":"","1UP":"","XTA":"","ETX":"","HIGHT":"","TOKEN":"","IFC":"","SZC":"","CMS":"","XYT":"","ET10":"","PLX":"","PIA":"","ALI":"","EXPO":"","ZGC":"","SIGMA":"","DOOH":"","CIV":"","ZUC":"","XCON":"","EES":"","MCASH":"","CPCPVEO":"","3DC":"","HHHH":"","RRRRRNCS":"","EVT":"","THM":"","BAR":"","TVNT":"","STEX":"","FTS":"","PPS":"","IOV":"","EQUA":"","GZE":"","WFX":"","FLETA":"","CBR":"","CLOUT":"","PLUS1":"","AXF":"","IDA":"","MRX":"","SFE":"","ATC":"","PLA":"","SMARTUP":"","DDN":"","SNO":"","SCC":"","IQT":"","NNT":"","XMO":"","ELET":"","APC":"","MCW":"","WINK":"","KAC":"","FRT":"","PMPMRRT":"","WXC":"","WEBD":"","B2N":"","ZB":"","EOST":"","CUST":"","XGTC":"","SPDR":"","DAXT":"","KUBO":"","NPLC":"","NAT":"","SGCC":"","NBX":"","ABAO":"","BTE":"","JBC":"","ENTRC":"","DREAM":"","IMPL":"","QBT":"","BUD":"","BTBc":"","WID":"","SKULL":"","LV":"","VIO":"","KCC":"","BHC":"","BTV":"","UNRC":"","TRAID":"","DHT":"","IDRT":"","PETS":"","SWACE":"","CPG":"","XQN":"","ASA":"","RUNE":"","GST":"","TUB":"","BCARD":"","XPASC":"","BGG":"","SPH":"","IMOS":"","JOT":"","BEAUTY":"","WASH":"","CVH":"","TBC":"","DMC":"","RPM":"","PUN":"","CICC":"","HSN":"","UNC":"","SKT":"","CBIX":"","TLE":"","OCUL":"","TRICK":"","CIF":"","LEVO":"","SPRK":"","VEIL":"","GRXGRBT":"","PITCH":"","ICHX":"","HALLO":"","ALV":"","RBMC":"","ADM":"","JLP":"","NOW":"","CIC":"","UBN":"","BLACBLASC":"","ANON":"","EAG":"","CSFT":"","QBTC":"","LDL":"","RUNNERS":"","BITC":"","DCON":"","BUL":"","UCC":"","ASN":"","RBX":"","CES":"","CNET":"","MERO":"","DBDBMRDB":"","KST":"","AKY":"","RBBT":"","NRC":"","ACN":"","III":"","ALT":"","RUBIT":"","BAIC":"","TBT":"","MRO":"","GERC":"","COTN":"","CEDEX":"","RICHX":"","NUG":"","GFR":"","HLX":"","DRE":"","PROUD":"","CTRCTRCR":"","DRPU":"","ETI":"","ZDC":"","DREM":"","BLCR":"","PSM":"","SICA":"","TRP":"","DFS":"","HNDC":"","DCTO":"","ETGP":"","BITE":"","QBX":"","ELLI":"","GBC":"","XID":"","BZKY":"","PAXEX":"","MMMMMGEN":"","AIA":"","SNIP":"","ZNN":"","RDC":"","XG":"","XG":"","":"","BTF":"","MART":"","CROP":"","JPYZ":"","SFC":"","PAC":"","CMP":"","CMS":"","CT":"","CCC":"","CPS":"","CCHCCHP":"","CHT":"","CNMC":"","CMIT":"","CIG":"","COO":"","CORG":"","CCCCCRN":"","COSS":"","CHEAP":"","CXC":"","CFC":"","CCC":"","COZ":"","CEN":"","CCM100":"","CRBC":"","LBA":"","LBA":"","CASINO":"","CME":"","CRV":"","CROWD":"","CRT":"","CASH":"","CHCHXCD":"","C2C":"","BX":"","OCEAN":"","BTSR":"","BTRCN":"","BTMC":"","CSD":"","BTCM":"","BCK":"","BT2":"","BT1":"","BBB":"","BRH":"","XCS":"","CPCT":"","CC":"","BOPO":"","CYB":"","BNS":"","CYC":"","CYDER":"","DAAC":"","DAB":"","BLINK":"","BTA":"","BLX":"","DARI":"","DISK":"","DKPC":"","BLAZR":"","BKK":"","BKK":"","DASHS":"","BYC":"","STASH":"","BSR":"","BTR":"","DTO":"","BTR":"","DAV":"","BITOK":"","BKB":"","BGX":"","FID":"","BTW":"","BTC2X":"","DUBI":"","BTCS":"","DCNT":"","BPP":"","BCM":"","BCMBCMT":"","DELIZ":"","DCRE":"","BFC":"","DXN":"","DFC":"","DFN":"","BTCB":"","BICC":"","DIBC":"","BCEO":"","BAC":"","BIRDBIFUDD":"","DB":"","BIRD":"","DCC":"","DXC":"","DIY":"","BHTX":"","BFF":"","BET":"","DON":"","BEST":"","DOT":"","DPAY":"","BVC":"","DRCT":"","BECN":"","BDK":"","BCAT":"","BYT":"","BAT":"","BSN":"","DUB":"","DUC":"","BAR":"","DUTCH":"","BC":"","AXIOM":"","AT":"","AV":"","AO":"","AWC":"","EAE":"","EEET":"","ATD":"","ECOIN":"","AFT":"","AFIN":"","ACG":"","ARLIZE":"","EGGEGGOLD":"","EJOY":"","EBKC":"","ARC":"","E2C":"","APW":"","LTE":"","ELM":"","APAPAESHIP":"","ANTX":"","RYZ":"","ANI":"","ELTELTELTELAEC":"","ALP":"","ABC":"","EMIRG":"","ALC":"","AUM":"","ETT":"","SDT":"","AISIAISRO":"","ENSA":"","ENENAEN":"","DNZ":"","EOSC":"","ACS":"","ACES":"","EOSRAM":"","ACC":"","AC20":"","EPLUS":"","ACAD":"","ESCO":"","ABTC":"","ABN":"","ETER":"","ABLX":"","EDOGE":"","ECH":"","ABC":"","ELITE":"","SW":"","10MT":"","EBEBDOW":"","ET":"","ETTEX":"","FXE":"","BITF":"","EUSD":"","SONG":"","MFIT":"","HMC":"","LVPS":"","EXC":"","EXCC":"","RMC":"","PRJ":"","AIAIADC":"","PIZZA":"","2GO":"","DGCS":"","FBL":"","FC":"","FFF":"","FFFC":"","FRCT":"","GMCN":"","FFFFFFFFE":"","FFART":"","KAYKAFTKAFRRN":"","FRM":"","TOR":"","CALC":"","ROCK":"","GRPH":"","CONXCOIMK":"","BNN":"","FFC":"","SANDG":"","CTIC2":"","ZNE":"","FLVR":"","FLVZ":"","VPRC":"","FMC":"","ACRE":"","RGS":"","FONZ":"","MGM":"","PRTX":"","FOX":"","RRRP":"","FRN":"","FRWC":"","LGS":"","CRBT":"","FRES":"","FRE":"","AAA":"","FFF":"","BIOB":"","FC2":"","OS76":"","WSP":"","FUTC":"","CXT":"","ETF":"","ETF":"","":"","":"","RY":"","GES":"","ULULULACO":"","GMC":"","DALC":"","GBT":"","ECO":"","GMCI":"","EMB":"","GML":"","ALTC":"","GAY":"","MND":"","GBC":"","VOLT":"","GMC":"","GMC":"","CHAN":"","STEPS":"","GER":"","LIR":"","GES":"","WBB":"","NIMFA":"","CRDNC":"","GBRC":"","GMCT":"","IMIMIBENJI":"","GOX":"","PULSE":"","GDW":"","CFUN":"","GGGGGINFX":"","GMX":"","XGR":"","GUC":"","XBTS":"","URO":"","PRPRWORM":"","SH":"","SLEVIN":"","VISIO":"","XRH":"","VEC2":"","ROOFS":"","GP":"","HCC":"","HCC":"","S":"","MT":"","HFC":"","EGO":"","HCC":"","BRAIN":"","BRY":"","ICON":"","KWATT":"","HN":"","AMMO":"","AMM":"","DBTC":"","DCAR":"","VUC":"","ANAI":"","ANA":"","HIGH":"","CAB":"","ORLY":"","BUMBA":"","HGO":"","HLHLHDLB":"","PIE":"","HYT":"","BNX":"","HMX":"","HOTTO":"","HTML5":"","HHHHL":"","XIOS":"","HNCHNRO":"","JS":"","HBB":"","XOC":"","HYB":"","MILO":"","HYPER":"","G3N":"","TAGR":"","HYTVHYHL":"","LTCU":"","EVOEVOE":"","IIIQ":"","ICST":"","VIP":"","FRK":"","IDEAL":"","STV":"","FLAX":"","IDOL":"","IFISH":"","DLC":"","EEEM":"","SLFI":"","KRONE":"","HVCO":"","XXX":"","INCO":"","INDIN":"","ACTP":"","POS":"","ICOB":"","XCRE":"","GOLF":"","IPY":"","CACH":"","MNM":"","IMS":"","INS":"","ARP":"","ICT":"","ICC":"","SOIL":"","SNR":"","IOG":"","ETCETCNTETAJ":"","IHF":"","IVZ":"","JOBS":"","CMCT":"","SCS":"","BSX":"","IPFS":"","ERY":"","ADN":"","MST":"","SCORE":"","ITGC":"","MAR":"","JNS":"","OFF":"","WARP":"","TKR":"","JINN":"","JLL":"","DFS":"","URC":"","CRTM":"","IRL":"","YEL":"","VC":"","DEUS":"","KASHH":"","ELS":"","KMC":"","KTC":"","SPACE":"","MAC":"","HUR":"","KDC":"","PLC":"","LTCR":"","KRI":"","KUSH":"","KUYC":"","IAB":"","LABH":"","EUC":"","LDCN":"","LTH":"","LATINO":"","LAZ":"","SPT":"","LEAF":"","TKA":"","SCRT":"","CNT":"","LST":"","HLB":"","LEPEN":"","GIM":"","GPKR":"","LEX":"","AMBER":"","BIP":"","LST":"","ACC":"","DLISDLISVA":"","RIDE":"","SOL":"","LTG":"","LTS":"","CYP":"","XBTC21":"","PKB":"","LVT":"","LIZUN":"","OBT":"","QURO":"","LNX":"","LOCUS":"","TIT":"","BTWTY":"","ACOIN":"","CPN":"","BUCKS":"","LCK":"","LOT":"","LSTR":"","EXN":"","CF":"","QBC":"","$$$":"","ORI":"","MAGN":"","BNC":"","SOJ":"","OUR":"","DRS":"","MARMAMASP":"","SOON":"","EZW":"","MAVRO":"","MAXI":"","GLC":"","PYX":"","ELC":"","MORPH":"","IFP":"","ZMC":"","MET":"","808":"","FUZZ":"","KNC":"","FRV":"","GPL":"","RED":"","DRXNE":"","LMM":"","CHC":"","ISL":"","SFC":"","BLC":"","KKKKKKKKKKB":"","MINEX":"","FLY":"","AGLC":"","MRQ":"","TRCT":"","MMXVI":"","C2":"","MBL":"","MOLK":"","BRZC":"","MTLMC3":"","ZUR":"","XMRG":"","LWF":"","XCO":"","XMV":"","MONETA":"","MONEY":"","TRIA":"","GUESS":"","NEWB":"","UNITS":"","MOX":"","611":"","MTV":"","INPAY":"","MZK":"","MVT":"","MZC":"","NAI":"","300":"","NAM":"","NAMO":"","NTC":"","DART":"","CFC":"","PUREX":"","ICOO":"","NBTK":"","NCXC":"","NEOG":"","NEOX":"","FUCK":"","EARTH":"","EREAL":"","NBIT":"","CNO":"","NLF":"","FANS":"","ARC":"","NMS":"","XCPO":"","NXY":"","NGOT":"","BERN":"","MBRS":"","NWC":"","NAST":"","SGP":"","NOR":"","NOIZ":"","8BIT":"","LOVC":"","ETHD":"","MCI":"","KNDC":"","CJ":"","NUMUS":"","NVST":"","OBTC":"","OBX":"","V":"","GCC":"","OCOW":"","ZSE":"","BITZ":"","OEC":"","QTL":"","WEUR":"","WUSD":"","OIOC":"","OLE":"","OMEN":"","OMC":"","ONTOP":"","BBT":"","ECASH":"","TSC":"","OP":"","OPES":"","VSX":"","ARI":"","XRA":"","DOR":"","OST":"","SZ":"","LEA":"","OX":"","SAKE":"","GRN":"","MCRN":"","ICN":"","PNDM":"","GPX":"","BITSILVER":"","BLZ":"","PDX":"","PX":"","PAYP":"","XPY":"","CAZ":"","WTT":"","PEC":"","PCO":"","EVIL":"","MEN":"","EZT":"","YAC":"","PFT":"","XBL":"","PMNT":"","PKC":"","PDG":"","VIDZ":"","KED":"","CON":"","EGX":"","MTNC":"","FIRE":"","CTO":"","ESA":"","PASL":"","PCASH":"","CAT":"","CFD":"","PXG":"","PGC":"","XAPC":"","GDC":"","DAXX":"","KOBO":"","POKE":"","HTH":"","HHHHMARS":"","NNNNHAL":"","TRI":"","PLAN":"","WECC":"","BCF":"","PRIMU":"","PRM":"","PDC":"","OPAL":"","DGS":"","LTB":"","PRN":"","BSTAR":"","PSY":"","CCN":"","MODX":"","PURE":"","PRPPRPMD":"","QEC":"","POSS":"","FUNK":"","QLC":"","QLB":"","HOLD":"","QORA":"","CAT":"","QTG":"","FST":"","LDC":"","ARCO":"","QAQ":"","ZINC":"","GNR":"","PGD":"","FYN":"","MMC":"","RAC":"","RHP":"","RALLRALLC":"","SDC":"","QCN":"","FMF":"","WAY":"","RCO":"","LANA":"","RCD":"","BITGOLD":"","RSS":"","MAGE":"","REGA":"","BND":"","RNDR":"","PURE":"","RTL":"","PHS":"","RHFC":"","RIO":"","LIVE":"","SNRG":"","RC2RC2RDN":"","XJO":"","PAG":"","BITBTC":"","ROYAL":"","XRY":"","RRC":"","EMD":"","HORSE":"","RUNE":"","HUBI":"","RRRX":"","GAP":"","RUSTBITS":"","SAC":"","SAC":"","SHA":"","FT":"","SFSFSJC":"","MORE":"","SNDSNDSR":"","RTB":"","BTI":"","PR":"","BGC":"","DGPT":"","SC2":"","RIYA":"","BBI":"","SLG":"","BITS":"","BOT":"","SFCP":"","HMP":"","SHA":"","HDG":"","SAK":"","SHELL":"","STF":"","SHVR":"","SHOP":"","PIGGY":"","SUBX":"","LCT":"","SGN":"","POSW":"","SWIFT":"","SISA":"","SJW":"","SKW":"","TRAK":"","SLING":"","SLOT":"","SLOTH":"","TRK":"","GEAR":"","WFEE":"","SNAKE":"","GOOD":"","WELL":"","SNLC":"","CESC":"","SLRM":"","SOOM":"","EIEC":"","SOPH":"","OPT":"","NET":"","BPL":"","BTG":"","X":"","XSM":"","NTRN":"","FID":"","XID":"","NKA":"","ZEST":"","SURE":"","SPORT":"","BNL":"","MAD":"","GZRO":"","ZCG":"","MAX":"","GUN":"","GRWI":"","EMV":"","STO":"","SJCX":"","SGC":"","FLT":"","STS":"","SBC":"","SHMN":"","WECF":"","I0C":"","BUN":"","SCEC":"","SDD":"","CV2":"","TIE":"","SUPM":"","SUC":"","SPEX":"","SWP":"","BTCA":"","XPS":"","SET":"","TCOIN":"","BEAT":"","IPX":"","ROBET":"","TGC":"","TAGZ":"","BOC":"","TALC":"","MTRC":"","ETPP":"","TCLB":"","BLOCKPAY":"","TEAM":"","Q2C":"","KFC":"","TTTT":"","RKC":"","MOZO":"","CRYPT":"","TERA":"","XPA":"","AKC":"","ECN":"","HBN":"","TF":"","AVINOC":"","SPN":"","XVE":"","TCR":"","DRP":"","NOBL":"","SEAL":"","NER":"","THPC":"","MOTO":"","STRC":"","TSE":"","TMC":"","RC":"","TALAO":"","TODAY":"","777":"","TKGN":"","YUAN":"","HTC":"","TOMO":"","YOO":"","KT":"","TOPAZ":"","VAL":"","TOP":"","SVD":"","TRANCE":"","ROC":"","FKX":"","FLAP":"","ESZ":"","CFT":"","BDT":"","SAL":"","WNL":"","GAIA":"","TDT":"","ATMS":"","ATMSTIG":"","TURBO":"","TWIST":"","TYCHO":"","KRM":"","UAHPAY":"","EGAS":"","HERO":"","UGT":"","GAIN":"","UBC":"","ULMT":"","APX":"","USC":"","USITUSUST":"","PCH":"","TKT":"","CRYP":"","VZT":"","UICUIC8":"","UNY":"","UNGT":"","CPLO":"","ORB":"","DTX":"","OIO":"","UR":"","XTL":"","USDE":"","USDK":"","LGD":"","RPM":"","UTA":"","UTS":"","UUNUUNCHIPS":"","VLC":"","MRJA":"","FRD":"","VKVKBZVKICO":"","BXC":"","CTR":"","TBARTBATRO":"","MOL":"","EDS":"","ZEPH":"","GPU":"","58B":"","VSTR":"","PLC":"","VIDT":"","CEEK":"","ONE":"","EXCEXCMT":"","VIT":"","AC":"","XFT":"","WDT":"","LYL":"","EET":"","DLB":"","SIFT":"","VOYA":"","VOYA":"","CTCCTCU":"","WA":"","WABI":"","CTC":"","STC":"","PWV":"","PGT":"","LKY":"","BBB":"","BWB":"","WKT":"","WTB":"","PASC":"","BUBUWT":"","BATT":"","NEAL":"","WIKI":"","3DB":"","SMART":"","WWW":"","LLLLUT":"","RTH":"","WNL":"","WOMEN":"","JEX":"","COINSCOISS":"","WITH":"","WIT":"","WMC":"","MYT":"","WOC":"","WLK":"","ADD":"","DALI":"","SPF":"","WOWOSIX":"","INVE":"","WT":"","WTBS":"","WJC":"","HADE":"","BIT":"","BCC":"","X12":"","X2":"","SAFEX":"","XAU":"","XBTC":"","XCT":"","XDE2":"","NNNH":"","XRT":"","XTC":"","XTD":"","XTX":"","XTRD":"","YAYA":"","ET":"","YES":"","NXX":"","YTC":"","TKN":"","YT":"","TIX":"","IPBC":"","YUKYUYKC":"","BWX":"","LML":"","UNITY":"","TEAC":"","EXB":"","SCT":"","TRIG":"","TRX":"","TRXX":"","TCB":"","ZBC":"","USDS":""
}

db_base.init_db()
while True:
    for github_item in github_list:
        if github_list[github_item] == "":
            
            continue
        elif github_list[github_item] == "no":
            param = {}
            param["coin_name"] = github_item
            param["time"] = int(time.time())
            param["commit_count"] = 0
            db_base.insert_into_github(param)
        else:
            response = url_open(github_list[github_item])
            doc = pq(response)
            commit_count = doc(".numbers-summary:first li:first .num").text().replace(",","")
            param = {}
            param["coin_name"] = github_item
            param["time"] = int(time.time())
            param["commit_count"] = int(commit_count)
            db_base.insert_into_github(param)
            print(github_item+"_"+str(commit_count))
            
    time.sleep(60*60)