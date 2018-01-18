"""
This python script drops all the databases related to the project and recreates them.
Following is the PostgreSQL code.

                                                    ['DROP DATABASE library_buddy;',
                                                    'CREATE DATABASE library_buddy;',
                                                    'CREATE USER op3ntrap WITH PASSWORD 'a';',
                                                    'ALTER ROLE op3ntrap SET client_encoding to 'utf8';',
                                                    'ALTER ROLE op3ntrap SET timezone TO 'UTC+5:30';',
                                                    'GRANT ALL PRIVILEGES ON DATABASE library_buddy TO op3ntrap;']

"""


import psycopg2
try:
    connn = psycopg2.connect(
        "dbname='library_buddy' user='op3ntrap' host=localhost password='a'")
except:
    print "script failed"
    exit()
conn = connn.cursor()

connn.set_isolation_level(0)
conn.execute("""DROP DATABASE library_buddy""")
conn.execute("""CREATE DATABASE library_buddy""")
conn.execute("""CREATE USER op3ntrap WITH PASSWORD 'a'""")
conn.execute("""ALTER ROLE op3ntrap SET client_encoding to 'utf8'""")
conn.execute("""ALTER ROLE op3ntrap SET timezone TO 'UTC+5:30'""")
conn.execute("""GRANT ALL PRIVILEGES ON DATABASE library_buddy TO op3ntrap""")
