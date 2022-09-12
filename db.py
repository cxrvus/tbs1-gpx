import mysql.connector

DATABASE = mysql.connector.connect(
	host="localhost",
	user="mso",
	password="test123",
	database="gpx_itf20a"
)

CURSOR = DATABASE.cursor()

CREATION_COMMANDS = [
	"""CREATE TABLE fahrer
	( 
	fid INT NOT NULL AUTO_INCREMENT PRIMARY KEY, 
	name VARCHAR(100), 
	vorname VARCHAR(100) 
	); """,
	"""CREATE TABLE fahrzeug 
	( 
	fzid INT NOT NULL AUTO_INCREMENT PRIMARY KEY, 
	polkz VARCHAR(10) 
	);""",
	"""CREATE TABLE fahrt 
	( 
	ftid INT NOT NULL AUTO_INCREMENT PRIMARY KEY, 
	dateiname VARCHAR(255), 
	fid INT, 
	fzid INT, 
	FOREIGN KEY(fid) REFERENCES fahrer(fid), 
	FOREIGN KEY(fzid) REFERENCES fahrzeug(fzid) 
	);""",
	"""CREATE TABLE fahrtpunkt 
	( 
	pid INT NOT NULL AUTO_INCREMENT PRIMARY KEY, 
	lat FLOAT,
	lon FLOAT, 
	ele FLOAT, 
	zeitstempel DATETIME, 
	ftid INT, 
	FOREIGN KEY(ftid) REFERENCES fahrt(ftid) 
	);"""
]

def create_tables():
	for command in CREATION_COMMANDS:
		CURSOR.execute(command)

def create_record(table, value_dict):
	insertion_str = f"INSERT INTO {table} ({', '.join(value_dict.keys())}) VALUES ({', '.join(value_dict.values())}))"
	_commit_sql(insertion_str)

def update_record(table, id_attribute, value_dict):
	kvpairs = []
	for attribute, value in value_dict:
		kvpairs.append(f'{attribute} = {value}')
	update_str = f"UPDATE {table} SET {', '.join(kvpairs)} WHERE {id_attribute} = {value_dict[id]}"
	_commit_sql(update_str)

def read_record(table, attribute, value):
	read_str = f"SELECT * FROM {table} WHERE {attribute} = '{value}'"
	CURSOR.execute(read_str)
	result = CURSOR.fetchall()
	return result or None

def delete_record(table, attribute, value):
	pass

def amend_record(table, attribute, value):
	record = read_record(table, attribute, value)
	if not record:
		create_record(table, {attribute: value})


def _commit_sql(sql):
	CURSOR.execute(sql)
	DATABASE.commit()

def _show_tables():
	CURSOR.execute("SHOW TABLES")
	for table in CURSOR:
		print(table)
