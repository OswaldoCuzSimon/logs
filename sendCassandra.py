from cassandra.cluster import Cluster

cluster = Cluster()
session = cluster.connect('pets')

rows = session.execute('SELECT * FROM students')
for row in rows:
	print(row.id, row.accounts, row.age)

