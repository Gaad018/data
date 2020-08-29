import psycopg2
import sys
sys.path.insert(0, '/task1/lib/')
from task1.lib import logging as log


def bd(dbnameArgument,
       userArgument,
       passwordArgument,
       hostArgument,
       id,
       responseRecognition,
       phone_number,
       duration_call,
       textAudio):

    con = psycopg2.connect(
        dbname  = dbnameArgument,
        user    = userArgument,
        password= passwordArgument,
        host    = hostArgument
    )

    cur = con.cursor()
    log.logging("Database opened successfully", 'info')

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


    # Отправляем данные в таблицу
    cur.execute(f'''INSERT INTO test (unique_id, result, phone_number, duration_call, result_recognition) 
                    VALUES ('{id}', {responseRecognition}, '{phone_number}', {duration_call}, '{textAudio}');''')

    log.logging('Success query', 'info')
    con.commit()
    con.close()