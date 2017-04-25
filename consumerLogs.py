from kafka import KafkaConsumer

class TweetConsumer:
	def __init__(self,urlKafka,topic):
		self.urlKafka = urlKafka
		self.topic = topic
		self.consumer = KafkaConsumer(self.topic,bootstrap_servers=[self.urlKafka])
	def receiveMessage(self):
		for message in self.consumer:
			print(message.offset,message.key, message.value.decode('utf8'))


urlKafka = "localhost:9092"
topic = "syslogs"
consumer = TweetConsumer(urlKafka,topic)
consumer.receiveMessage()