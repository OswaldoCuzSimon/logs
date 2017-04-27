CREATE KEYSPACE logs WITH  replication = {'class':'SimpleStrategy','replication_factor':1};
use logs;
CREATE TABLE messages(
	id_messages timeuuid PRIMARY KEY,
	datetime timestamp,
	hostname varchar,
	service varchar,
	message text
);
CREATE TABLE httpd(
	id_httpd timeuuid,
	ip inet,
	userid varchar,
	not_available varchar,
	datetime timestamp,
	method varchar,
	resource varchar,
	protocol varchar,
	status_code varchar,
	size_object varchar,
	message text,
	PRIMARY KEY(id_httpd)
);
CREATE INDEX ON httpd( userid );
CREATE INDEX ON httpd( status_code );
CREATE INDEX ON httpd( ip );
CREATE INDEX ON httpd( method );
CREATE INDEX ON httpd( datetime );


CREATE INDEX ON messages( datetime );
CREATE INDEX ON messages( hostname );
CREATE INDEX ON messages( service );