import psycopg2
import sys
import os

def connect_to_db():
	user = os.getlogin()
	conn_string = "host='localhost' dbname='tweets-db_development' user='%(user)s'" % locals()

	# get a connection, if a connect cannot be made an exception will be raised here
	conn = psycopg2.connect(conn_string)
	print "Connection succeeded to database\n	->%s\n" % (conn_string)

	# conn.cursor will return a cursor object, you can use this cursor to perform queries
	return conn.cursor()

def retrieve_tweets( cant ):
	cursor = connect_to_db()
	cursor.execute("SELECT tweet_id, data FROM tweets LIMIT (%s)", [cant])
	tweets = cursor.fetchall()

	return tweets
