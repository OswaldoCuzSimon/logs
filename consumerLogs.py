from kafka import KafkaConsumer
from sendCassandra import SaveLogs

class TweetConsumer:
	def __init__(self,urlKafka,topic,urlCass):
		self.urlKafka = urlKafka
		self.topic = topic
		self.consumer = KafkaConsumer(self.topic,bootstrap_servers=[self.urlKafka])
		self.saveLogs = SaveLogs(urlCass)
	def receiveMessage(self):
		for message in self.consumer:
			mes = message.value.decode('utf8')
			self.saveLogs.saveMessages(mes)
			print(mes)

urlKafka = "localhost:9092"
topic = "syslogs"
urlCass = "localhost"
consumer = TweetConsumer(urlKafka,topic,urlCass)
consumer.receiveMessage()