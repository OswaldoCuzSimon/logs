from cassandra.cluster import Cluster
import parsedatetime
from time import mktime
from datetime import datetime

class SaveLogs:
	def __init__(self,url):
		self.cluster = Cluster([url])
		self.session = self.cluster.connect('logs')
	def saveHTTPaccess(self, message):
		tokens = [_.strip('"[]()') for _ in message.split()[:10] ]
		extra = ' '.join(message.split()[10:])
		tokens.append(extra)

		p = parsedatetime.Calendar()
		dateMes = p.parse(tokens[3])
		tokens[3] = datetime.fromtimestamp(mktime(dateMes[0])).isoformat()
		values = (tokens[0],tokens[1],tokens[2],tokens[3],tokens[5],tokens[6],tokens[7],tokens[8],tokens[9],tokens[10])
		#::1 - - [27/Apr/2017:11:02:46 -0500] "GET /images/poweredby.png HTTP/1.1" 304 - "http://localhost/" "Mozilla/5.0 (X11; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0"
		self.session.execute("INSERT INTO httpd (id_httpd,ip,userid,not_available,datetime,method,resource,protocol,status_code,size_object,message)"
		"VALUES (now(),%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", values)
	def saveMessages(self,message):
		dateStr = message[:15]
		message = message[15:]
		host = message.split()[0]
		service = message.split()[1][:-1]
		message = message[message.find(':')+1:].strip()

		p = parsedatetime.Calendar()
		dateMes = p.parse(dateStr)
		dt = datetime.fromtimestamp(mktime(dateMes[0]))

		self.session.execute("INSERT INTO messages (id_messages,datetime,hostname,service,message)"
			"VALUES (now(),%s,%s,%s,%s)", (dt.isoformat(),host,service,message))  # right
		#insert timestamp toTimestamp(now())

