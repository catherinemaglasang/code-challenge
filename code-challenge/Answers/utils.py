import csv 
import mysql.connector
from mysql.connector import Error
from config import *

# open and read file
def csv_parse(file_path):
	# open the file
	data = []
	with open(file_path , 'r') as csvfile:
		# create the object of csv.reader()
		csv_file_reader = csv.reader(csvfile,delimiter=',')
		for row in csv_file_reader:
			data.append(tuple(row))
	data.pop(0)
	return data

# connect to mysql server
def db_connect():
	try:
		db_connection = mysql.connector.connect(
		host = MYSQL_HOST,
		user = MYSQL_USERNAME,
		password = MYSQL_PASSWORD,
		port = MYSQL_PORT
		)
		return db_connection

	except Error as e:
		print(e)


# create mysql database schema
def db_create_schema():
	try:
		query_return = (open('db_schema.sql', 'r').read() % (MYSQL_DATABASE, MYSQL_DATABASE))
		
		db = db_connect()
		cursor = db.cursor()
		res = cursor.execute(query_return, multi=True)
		for cur in res:
			cur
		db.commit()

		print("\nDatabase Schema Created Successfully!")
		
	except Error as e:
		print(e)


# insert csv data into database tables
def db_insert(query, data):
	try:
		# connect to mysql server
		db = mysql.connector.connect(
			host = MYSQL_HOST,
			user = MYSQL_USERNAME,
			password = MYSQL_PASSWORD,
			port = MYSQL_PORT,
			database = MYSQL_DATABASE
			)
		cursor = db.cursor()
		cursor.executemany(query, data)
		
		db.commit()

		print("")

	except Error as e:
		print("ERROR: ", e)


# insert csv data into database tables
def db_send_query(query):
	try:
		# connect to mysql server
		db = mysql.connector.connect(
			host = MYSQL_HOST,
			user = MYSQL_USERNAME,
			password = MYSQL_PASSWORD,
			port = MYSQL_PORT,
			database = MYSQL_DATABASE
			)
		cursor = db.cursor()
		cursor.execute("SET SESSION sql_mode=(SELECT REPLACE(@@sql_mode,'ONLY_FULL_GROUP_BY',''));")
		cursor.execute(query)
		headers = [i[0] for i in cursor.description]
		result = cursor.fetchall()
		result.insert(0, headers)

		
		db.commit()

		return result

	except Error as e:
		print("ERROR: ", e)


def date_format(dt):
	dt = dt.split('/', 3)
	#changing the dateformat
	new_date = f'{dt[2]}/{dt[0]}/{dt[1]}'         

	return new_date
	