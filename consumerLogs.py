from kafka import KafkaConsumer
from sendCassandra import SaveLogs
import re

class TweetConsumer:
	def __init__(self,urlKafka,topic,urlCass):
		self.urlKafka = urlKafka
		self.topic = topic
		self.consumer = KafkaConsumer(self.topic,bootstrap_servers=[self.urlKafka])
		self.saveLogs = SaveLogs(urlCass)
	def receiveMessage(self):
		for message in self.consumer:
			mes = message.value.decode('utf8')
			meslist = mes.split()
			#print(meslist[0]=='::1' or re.match("^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}", meslist[0])!=None )
			if meslist[0]=='::1' or re.match("^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}", meslist[0])!=None :
				self.saveLogs.saveHTTPaccess(mes)
			else:
				self.saveLogs.saveMessages(mes)
			print(mes)

urlKafka = "localhost:9092"
topic = "syslogs3"
urlCass = "localhost"
consumer = TweetConsumer(urlKafka,topic,urlCass)
consumer.receiveMessage()