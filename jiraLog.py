import urllib.parse
import urllib.request
import json
import getpass
import pprint
import const.Constants as CO
import auth.Session

pp = pprint.PrettyPrinter(indent=2)

sess = auth.Session.Session()

sess.prompt_login()



issueNum = input("Issue Key: ")
req = urllib.request.Request("https://quality.hubwoo.com/rest/api/latest/issue/" + issueNum, headers = sess.get_hdr())
res = urllib.request.urlopen(req)
jsr = json.loads(res.read().decode('utf_8'))
pp.pprint(jsr)
