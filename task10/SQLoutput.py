import sqlite3
from datetime import datetime

class SQLoutput:
    def create_connection_wcount(db_file ,text):
        con = sqlite3.connect(":memory:", detect_types=sqlite3.PARSE_COLNAMES)
        cur = con.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS word_count (text VARCHAR(512), date datetime PRIMARY KEY);")
        date = (datetime.now())
        cur.execute("insert into word_count(text,date) values (?,?)", (text, date,))
        cur.execute('select * from word_count')
        print("with column names:", cur.fetchall())
        cur.execute('select distinct text,count(*) from word_count group by text having count(*)>1')
        print("with column names:", cur.fetchall())

        cur.close()
        con.close()
    def create_connection_letter_count(db_file,str):
        con = sqlite3.connect(":memory:", detect_types=sqlite3.PARSE_COLNAMES)
        cur = con.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS letter_count (letter VARCHAR(10), count VARCHAR(10), upper VARCHAR(10), percent VARCHAR(256) );")
        for k in str.split('\n'):
            cur.execute("insert into letter_count(letter,count,upper,percent) values (?,?,?,?)", k.split(','))
        cur.execute('select * from letter_count')
        print("with column names:", cur.fetchall())
        cur.execute('select distinct letter,count,upper,percent,count(*) from letter_count group by letter,count,upper,percent having count(*)>1')
        print("with column names:", cur.fetchall())

        cur.close()
        con.close()
