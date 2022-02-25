#!/usr/bin/python2.7
C1 = '\033[1;36m'
G0 = '\033[0;32m'
W0 = '\033[0;37m'
R0 = '\033[0;31m'
import requests,sys,os
from bs4 import BeautifulSoup

from multiprocessing.pool import ThreadPool
def scan(site):
	
	try:
		aytac = requests.get(site)
		text = aytac.content
		if requests.get(site).status_code==200 and ('Shell' in text or 'WSO' in text or 'shell' in text  or 'File Manager' in text or 'file manager' in text):
			print '%s[ %sLIVE %s] %s'%(W0,G0,W0,site)
			open('liveshell.txt','a+').write(site+'\n')
		else:
			print '%s[ %sDIEE %s] %s'%(W0,R0,W0,site)
	except:
		print '%s[ %sUNK %s] %s'%(W0,R0,W0,site)
		pass

try:
	os.system('clear')
	print '''%s
 SHELL SCANNER -->> Author: AKalinci
 ( 'Shell' , 'WSO', 'C99', 'R57' ) You can edit your keywords
'''%(C1,W0,C1,W0,C1,W0,C1)
	ThreadPool(1000).map(scan,open(sys.argv[1]).read().splitlines())
	print '\n%s[ %sDONE %s] Saved in live_shell.txt'%(W0,G0,W0)
except requests.exceptions.ConnectionError:
	exit('%s[%s!%s] %sCheck internet'%(W0,R0,W0,W0))
except IndexError:
	exit('%s[%s!%s] Use : python2 %s target.txt \n%s[%s!%s] Fill in target.txt with http or https'%(W0,R0,W0,sys.argv[0],W0,R0,W0))
except IOError:
	exit('%s[%s!%s] %sFile does not exist'%(W0,R0,W0,W0))
except KeyboardInterrupt:
	exit('\n%s[%s!%s] %sExit'%(W0,R0,W0,W0))
