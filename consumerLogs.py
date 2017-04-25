from kafka import KafkaConsumer
import parsedatetime
class TweetConsumer:
	def __init__(self,urlKafka,topic):
		self.urlKafka = urlKafka
		self.topic = topic
		self.consumer = KafkaConsumer(self.topic,bootstrap_servers=[self.urlKafka])
	def receiveMessage(self):
		p = parsedatetime.Calendar()
		for message in self.consumer:
			mes = message.value.decode('utf8')
			print(message.offset,message.key, mes)
			#datetime.datetime.now().strftime("%b %d %H:%M:%S")
			p.parse(mes)




urlKafka = "localhost:9092"
topic = "syslogs"
consumer = TweetConsumer(urlKafka,topic)
consumer.receiveMessage()