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
	id_httpd timeuuid PRIMARY KEY,
	ip inet,
	userid varchar,
	not_available varchar,
	datetime timestamp,
	method varchar,
	resource varchar,
	protocol varchar,
	status_code varchar,
	size_object varchar,
	message text
);