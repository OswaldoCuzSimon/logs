#Start flume
export LOG_DIR=/home/administradorcito/gitRepos/logs
sudo bin/flume-ng agent --name source_agent --conf ./conf/ --conf-file $LOG_DIR/flume-log-kafka.conf -Dflume.root.logger=DEBUG,console

start kafka
sudo docker run -p 2181:2181 -p 9092:9092 --env ADVERTISED_HOST=localhost --env ADVERTISED_PORT=9092 spotify/kafka

Consumer kafka
bin/kafka-console-consumer.sh --zookeeper localhost:2181 --topic syslogs

Start Cassandra
sudo docker run --name cassandra1 -d  -p 9042:9042 cassandra


Start Cqlsh
sudo docker run -it --link cassandra1:cassandra --rm cassandra sh -c 'exec cqlsh "$CASSANDRA_PORT_9042_TCP_ADDR"'