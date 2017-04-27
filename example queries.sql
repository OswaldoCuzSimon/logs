SELECT id_httpd FROM httpd WHERE 
id_httpd = 43552230-2b6a-11e7-a974-f58bd8d3766a;

SELECT id_httpd,datetime FROM httpd
WHERE id_httpd > maxTimeuuid('2013-01-01 00:05+0000')
AND id_httpd < minTimeuuid('2013-01-01 00:05+0000')


SELECT DateOf(id_httpd),datetime from httpd;

SELECT * FROM httpd WHERE status_code ='403' allow filtering;


SELECT id_httpd,datetime FROM httpd 
WHERE datetime < '2017-04-27 13:02:25' allow filtering;

SELECT id_httpd,datetime FROM httpd 
WHERE datetime > '2017-04-27 12:00:00' 
AND datetime < '2017-04-27 13:00:0' allow filtering;





select id_httpd,ip,datetime from httpd where ip = '10.110.70.182' ;

select id_httpd,status_code,datetime from httpd where status_code = '404' ;

SELECT id_messages FROM httpd WHERE id_messages in (
	SELECT id_messages FROM messages
	WHERE datetime > '2017-04-27 13:00:00'
	AND datetime < '2017-04-27 13:05:00'
)ORDER BY id_messages;


SELECT dateOf(id_messages) FROM messages
WHERE id_messages > maxTimeuuid('2017-04-27 20:00+0000')
AND id_messages < minTimeuuid('2017-04-27 20:01+0000') allow filtering;


SELECT dateOf(id_messages) FROM messages
WHERE id_messages > maxTimeuuid('2017-04-27 20:00')
AND id_messages < minTimeuuid('2017-04-27 20:01') allow filtering;

SELECT * FROM messages
WHERE id_messages > minTimeuuid( dateOf(now()) ) allow filtering;

SELECT * FROM messages
WHERE id_messages > maxTimeuuid( dateOf(now()) ) allow filtering;