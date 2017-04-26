from cassandra.cluster import Cluster
import parsedatetime
from time import mktime
from datetime import datetime

class SaveLogs:
	def __init__(self,url):
		self.cluster = Cluster([url])
		self.session = self.cluster.connect('logs')
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