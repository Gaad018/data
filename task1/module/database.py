#.env
from dotenv import load_dotenv
load_dotenv()
load_dotenv(verbose=True)

import psycopg2
import sys
import os

sys.path.insert(0, '/task1/module/')
from task1.module import logging as log

def connectBd():
    con = psycopg2.connect(
        dbname = os.getenv("BDNAME"),
        user = os.getenv('USER'),
        password = os.getenv('PASSWORD'),
        host = os.getenv('HOST')
    )
    return con

def checkTabel(cur):
    # Создание таблицы, если она не существует
    cur.execute('''CREATE TABLE if not exists data
                        (
                            id SERIAL,
                            "date" date not null default CURRENT_DATE,
                            "time" time without time zone not null default CURRENT_TIME,
                            unique_id text,
                            result integer,
                            phone_number text,
                            duration_call numeric,
                            result_recognition text COLLATE pg_catalog."default",
                            CONSTRAINT data_pkey PRIMARY KEY (id)
                        );''')

def bd(listArgument):
    con = connectBd()
    cur = con.cursor()
    log.logging("Database opened successfully", 'info')

    checkTabel(cur)


    # Отправляем данные в таблицу
    cur.execute(f'''INSERT INTO data (unique_id, result, phone_number, duration_call, result_recognition) 
                    VALUES ('{listArgument[0]}', {listArgument[1]}, '{listArgument[2]}', {listArgument[3]}, '{listArgument[4]}');''')

    log.logging('Success query', 'info')
    con.commit()
    con.close()