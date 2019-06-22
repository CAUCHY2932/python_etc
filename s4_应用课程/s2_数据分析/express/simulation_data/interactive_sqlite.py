# coding:utf-8

import sqlite3


def insert_sqlite(dbname, tablename,loglist):

    with sqlite3.connect('./{}'.format(dbname)) as conn:
        print('link to database successfully and is preparing to insert data!')
        cur = conn.cursor()
        for i in loglist:
            cur.execute("insert into {} (NAME, AGE, ADDRESS, SALARY)values(?, ?, ?, ?)" .format(tablename), i)
        conn.commit()
        print('insert to database successfully!')
        # cur.execute()


def create_table(dbname):
    with sqlite3.connect(dbname) as conn:
        cur = conn.cursor()
        print('link to database successfully!')
        cur.execute(
            '''CREATE TABLE COMPANY
                   (ID INTEGER PRIMARY KEY    AUTOINCREMENT NOT NULL,
                   NAME           TEXT    NOT NULL,
                   AGE            INT     NOT NULL,
                   ADDRESS        CHAR(50),
                   SALARY         REAL);'''
        )
        conn.commit()
        print('create database successfully!')

def select_data(dbname, tablename):
    with sqlite3.connect(dbname) as conn:
        cur = conn.cursor()



if __name__ == "__main__":
    create_table('5.db')
    loglist = [
        ('lee', '12', 'chengdu', '4500'),
        ('harry', '23', 'beijing', '4590'),
        ('sun', '23', 'chongqing', '5600'),
        ('zam', '45', 'shanghai', '3400'),
    ]
    insert_sqlite('5.db','COMPANY', loglist=loglist)
