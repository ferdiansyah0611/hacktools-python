import sys, os, time, socket, optparse
from colorama import init
from termcolor import colored
# init color print
init()

def logtime(withcolor = True):
	now = time.localtime(time.time())
	if withcolor:
		return colored("[{hours}:{minutes}]".format(hours = now.tm_hour, minutes = now.tm_min), 'green') + ':'
	else:
		return "[{hours}:{minutes}]".format(hours = now.tm_hour, minutes = now.tm_min) + ':'
# start app
class App:
	# attribute
	version = 1
	full = 60
	hostname = socket.gethostname()
	# init
	def __init__(self):
		if sys.version_info[0] != 3:
			sys.exit()
		else:
			if os.system('cls') == 0:
				os.system('cls')
			if os.system('clear') == 0:
				os.system('clear')
			print(logtime(), '#' * self.full)
			print(logtime(), '##!!                                                    !!##')
			print(logtime(), f'##!!             {colored("Hacking Tools Application", "white", "on_red", attrs=["bold"])}              !!##')
			print(logtime(), '##!!                                                    !!##')
			print(logtime(), '##!!                   $$$$$$$$$$$$$                    !!##')
			print(logtime(), '##!!                 $$$$$$$$$$$$$$$$$                  !!##')
			print(logtime(), '##!!                   |           |                    !!##')
			print(logtime(), '##!!                  {| [0]   [0] |}                   !!##')
			print(logtime(), '##!!                   |    ___    |                    !!##')
			print(logtime(), '##!!                   |    !!!    |                    !!##')
			print(logtime(), '##!!                   |___________|                    !!##')
			print(logtime(), '##!!                                                    !!##')
			print(logtime(), f'##!!               {colored("Dev by Ferdiansyah0611", "white", "on_red", attrs=["bold"])}               !!##')
			print(logtime(), '##!!                                                    !!##')
			print(logtime(), '#' * self.full)
			print(logtime(), 'checking python version...')
			time.sleep(0.4)
			print(logtime(), 'checking application version...')
			time.sleep(0.4)
			print(logtime(), 'checking url...')
			time.sleep(0.4)
			print(logtime(), 'checking ip address...')
			ip = socket.gethostbyname(self.hostname)
			time.sleep(0.4)
			print(logtime(), 'Enjoy Your Hacking')
			print(logtime(), f"IP Address: {ip}")
			time.sleep(0.4)

def Main(): 
	parser = optparse.OptionParser("usage: %prog [options] arg")
	parser.add_option('-e', action="store", default=False, type='string', dest='email', help='email target of bruteforce')
	parser.add_option('-P', action="store", default=False, type='float', dest='phone', help='phone target of bruteforce')
	parser.add_option('-c', action="store", default=False, type='float', dest='choose', help='choose type target of bruteforce')
	parser.add_option('-t', action="store", default=False, type='string', dest='type', help='choose type of bruteforce')
	parser.add_option('-v', action='store_false', default=False, dest='version', help='check version library')
	parser.add_option('-p', action='store', default=False, dest='password', help='if choose manual you must be fillable password')
	group = optparse.OptionGroup(parser, "Example", "python app.py -e admin@server.domain -c 1 -t a")
	parser.add_option_group(group)
	(options, args) = parser.parse_args()
	if options.version != False:
		print('Version ', options.version)
	elif options.email != False or options.phone != False and options.choose != False and options.type !=  False:
		# Facebook Bruteforce
		if options.choose == 1:
			# auto bruteforce
			if options.type == 'a':
				App()
				from src.facebook import Facebook
				if options.email != False:
					Facebook(options.email, 'auto')
				if options.phone != False:
					Facebook(options.phone, 'auto')
			# manual bruteforce
			if options.type == 'm':
				if options.password != False:
					App()
					from src.facebook import Facebook
					if options.email != False:
						Facebook(options.email, 'manual', options.password)
					if options.phone != False:
						Facebook(options.phone, 'manual', options.password)
		if options.choose > 1 and options.choose <= 7:
			print(colored("Message : Sorry This Feature Is Coming Soon", "white", "on_cyan", attrs=["bold"]))
	else:
		App()
		from src.commandline import commandline

		commandline()

if __name__ == '__main__': 
	Main() 
