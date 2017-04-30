# Logs

## Synopsis
Aplicacion que envia el contenido de los logs: var/log/messages y var/log/httpd/access_log
a un topic de kafka mediante flume, el topic es consumido por un consumer de python y enviado
a Cassandra

## Despliegue

### 1 Crear un entorno virtual
```virtualenv -p /usr/bin/python3.4 env ```

### 2 Activar el entorno
```source env/bin/activate```

### 3 Instalar las librerias
```pip install -r requirements.txt```

### 4 Correr el contenedor [spotify/kafka](https://hub.docker.com/r/spotify/kafka/)
```docker run -p 2181:2181 -p 9092:9092 --env ADVERTISED_HOST=localhost --env ADVERTISED_PORT=9092 spotify/kafka```

### 5 Correr el contenedor [cassandra](https://hub.docker.com/_/cassandra/)
```docker run --name cassandra1 -d  -p 9042:9042 cassandra```

### 6 Crear la base de datos
```bash
docker run -it --link cassandra1:cassandra --rm cassandra sh -c 'exec cqlsh "$CASSANDRA_PORT_9042_TCP_ADDR"'
source '<path-repositorie>/cassandraScheme.sql'
```
### 7 Correr Flume
```bash
cd <flume-path>
export LOG_DIR=<path-repositorie>
sudo bin/flume-ng agent --name source_agent --conf ./conf/ --conf-file $LOG_DIR/flume-multilog-kafka.conf -Dflume.root.logger=DEBUG,console
```
### 8 Ejecutar el [consumerLogs.py](https://github.com/OswaldoCuzSimon/logs/blob/master/consumerLogs.py)
```python consumerLogs.py```
