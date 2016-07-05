import getpass
import urllib.parse
import urllib.request
import json
import const.Constants as CO

class Session:

	def __init__(self):
		self.usr = ""
		self.pss = ""
		self.hdr = ""
		self.SESS_ID = ""
		self.SESS_NA = ""
		self.LOGGED = False

	def prompt_login(self):
		logSuccess = False
		while (logSuccess == False):
			print(" == LOGIN == ")
			self.usr = input("Username: ")
			self.pss = getpass.getpass()
			logSuccess = self.do_login()

	def do_login(self):
		
		try:
			vals = '{"username" : "' + self.usr + '", "password" : "' + self.pss + '" }'
			params = vals.encode('utf_8')
			headers = {'Content-type' : 'application/json', 'User-Agent' : 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)' }

			req = urllib.request.Request(CO.AUTH_URL, params, headers)
			res = urllib.request.urlopen(req)

			jsr = json.loads(res.read().decode('utf_8'))

			self.SESS_ID = jsr['session']['value']
			self.SESS_NA = jsr['session']['name']
			self.LOGGED = True
			self.hdr = {'Content-type' : 'application/json', 'User-Agent' : 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)', 'cookie' : self.SESS_NA + '=' + self.SESS_ID }
			return True
		except:
			print("\nFailed to login!\n")
			return False

	def get_hdr(self):
		if self.LOGGED == True:
			return self.hdr
		else:
			return ""

	def set_creds(u, p):
		self.usr = u
		self.pss = p
